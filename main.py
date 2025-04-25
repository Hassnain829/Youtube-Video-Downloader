from pytube import YouTube

def download_youtube_video(url):
    try:
        # Create YouTube object
        if not url.startswith("https://www.youtube.com/") and not url.startswith("https://youtu.be/"):
            raise ValueError("Invalid YouTube URL. Please provide a valid URL.")
        yt = YouTube(url)

        # Display video title
        print(f"Title: {yt.title}")

        # List all available streams
        print("\nAvailable streams:")
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        if not streams:
            print("No available streams found. Please try a different video.")
            return

        for i, stream in enumerate(streams, start=1):
            print(f"{i}. Resolution: {stream.resolution}, FPS: {stream.fps}, File Size: {round(stream.filesize / (1024 * 1024), 2)} MB")

        # Ask user to select a stream
        choice = int(input("\nEnter the number of the stream to download: "))
        if choice < 1 or choice > len(streams):
            print("Invalid choice. Please restart the program and select a valid stream.")
            return
        selected_stream = streams[choice - 1]

        # Download the selected stream
        print("\nDownloading...")   
        selected_stream.download()
        print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    try:
        download_youtube_video(video_url)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")