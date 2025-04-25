from pytube import YouTube

def download_youtube_video(url):
    try:
        # Create YouTube object
        yt = YouTube(url)

        # Display video title
        print(f"Title: {yt.title}")

        # List all available streams
        print("\nAvailable streams:")
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        for i, stream in enumerate(streams, start=1):
            print(f"{i}. {stream}")

        # Ask user to select a stream
        choice = int(input("\nEnter the number of the stream to download: "))
        selected_stream = streams[choice - 1]

        # Download the selected stream
        print("\nDownloading...")
        selected_stream.download()
        print("Download completed!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_video(video_url)