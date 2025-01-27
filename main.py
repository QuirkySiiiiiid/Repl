import yt_dlp
import os
import time

# Define the download directory
DOWNLOAD_DIR = "./downloads"

# Ensure the download directory exists
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Function to download videos from a playlist in MP4 format (720p or lower)
def download_video_from_playlist(playlist_url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4][height<=720]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',  # Ensure output is in .mp4
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),  # Output filename
        'noplaylist': False,  # Download all videos from playlist
        'quiet': False,  # Display verbose output
        'progress_hooks': [hook],  # Progress hook for feedback
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Starting download for playlist: {playlist_url}")
            ydl.download([playlist_url])  # Download the playlist
    except Exception as e:
        print(f"Error downloading playlist: {e}")

# Progress hook function
def hook(d):
    if d['status'] == 'finished':
        print(f"\nDownload complete: {d['filename']}")
        print(f"Elapsed time: {d['elapsed']} seconds")
        time.sleep(5)  # Delay between downloads

# Main function
if __name__ == "__main__":
    playlist_url = input("Enter the playlist URL: ")
    download_video_from_playlist(playlist_url)
