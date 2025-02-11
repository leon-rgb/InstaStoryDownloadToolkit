# InstaStoryDownloadToolkit

A Python-based tool that downloads Instagram stories from public accounts (with login support including two-factor authentication) and merges the story videos into a single file with a timestamped filename to avoid overwriting existing files.

> **Disclaimer:** Use this tool only for personal purposes and ensure you respect Instagram's terms of service.
> This tool is provided for educational and personal use only. The author is not responsible for any misuse.

## Features

- **Download Instagram Stories:**  
  Uses [Instaloader](https://instaloader.github.io/) to log in and fetch stories (handles 2FA if enabled).
  
- **Merge Videos:**  
  Combines multiple story video files into one using [ffmpeg](https://ffmpeg.org/). The output filename includes a timestamp to avoid file overwrites.

- **Session Management:**  
  Saves your Instagram session in a file (e.g., `session-<username>`) to prevent repeated logins.

- **Note regarding insta login:**
 It is necessary to login to an instagram account for this tool to work since instaloader package requires this for getting the stories of ANY account (even if the account is public)

## Prerequisites

- Python 3.x installed on your system.
- [Instaloader](https://instaloader.github.io/) Python package.
- [ffmpeg](https://ffmpeg.org/) installed on your system and its `bin` folder added to your system's PATH.
- (Optional but recommended) A virtual environment to manage dependencies.

## Installation

1. Clone the Repository:
2. Install python and needed packages (preferably in an virtual env)
3. Run `py main_script.py` in the console
