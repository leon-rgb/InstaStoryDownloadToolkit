import os
import instaloader
import getpass
from datetime import datetime

def get_instaloader_instance(login_username):
    L = instaloader.Instaloader()

    # Try to load an existing session
    try:
        L.load_session_from_file(login_username)
        print("Loaded session from file.")
    except FileNotFoundError:
        # No session found; perform a login
        password = getpass.getpass(f"Enter the password for {login_username}: ")
        try:
            L.login(login_username, password)
        except instaloader.exceptions.TwoFactorAuthRequiredException:
            # If 2FA is enabled, prompt for the code and complete 2FA login
            two_factor_code = input("Two-factor authentication code required. Enter the 2FA code: ")
            L.two_factor_login(two_factor_code)
        # Save the session to avoid logging in again later
        L.save_session_to_file()
        print("Session saved.")
    return L

def download_stories(target_username, L):
    # Get the profile of the target user
    try:
        profile = instaloader.Profile.from_username(L.context, target_username)
    except instaloader.exceptions.ProfileNotExistsException:
        print("Error: Profile does not exist.")
        return

    if profile.is_private:
        print("This account is private. You might not be allowed to access its stories.")
        return

    os.makedirs("stories", exist_ok=True)
    story_found = False

    # Download stories for the target profile
    for story in L.get_stories(userids=[profile.userid]):
        for item in story.get_items():
            story_found = True
            L.download_storyitem(item, target="stories")

    if not story_found:
        print(f"No public stories available for {target_username}.")

def merge_videos():
    if not os.path.exists("stories"):
        print("Stories folder not found. Make sure stories are downloaded before merging.")
        return

    video_files = sorted([f for f in os.listdir("stories") if f.endswith(".mp4")])
    if not video_files:
        print("No videos found in 'stories' folder.")
        return
    
    with open("video_list.txt", "w") as f:
        for video in video_files:
            f.write(f"file 'stories/{video}'\n")
    

    # Create the output file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"merged_stories_{timestamp}.mp4"
    os.system(f"ffmpeg -f concat -safe 0 -i video_list.txt -c copy {output_file}")
    print(f"Merged video saved as {output_file}")

def main():
    print("To access Instagram stories, you must log in to your Instagram account.")
    login_username = input("Enter your Instagram username for login: ")
    L = get_instaloader_instance(login_username)
    
    target_username = input("Enter the Instagram username whose stories you want to download: ")
    download_stories(target_username, L)
    merge_videos()

if __name__ == "__main__":
    main()
