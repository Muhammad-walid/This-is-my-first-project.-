from pytube import YouTube

def download_youtube_video(url, save_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video
        video_stream.download(output_path=save_path)

        print("Download complete!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
video_url = 'https://www.youtube.com/watch?v=UWP7YSo0Sbc'
download_youtube_video(video_url)
