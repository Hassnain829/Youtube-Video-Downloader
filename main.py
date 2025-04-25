import yt_dlp

def list_and_download_video(url):
    try:
        # List formats
        ydl_opts_list = {
            'listformats': True,
            'quiet': True,
        }

        print("\nFetching available formats...\n")

        with yt_dlp.YoutubeDL(ydl_opts_list) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            filtered_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('acodec') != 'none']

            for i, fmt in enumerate(filtered_formats, start=1):
                size = fmt.get('filesize', 0)
                print(f"{i}. {fmt['format']} - {round(size / (1024 * 1024), 2) if size else 'Unknown'} MB")

        choice = int(input("\nEnter the number of the format to download: "))
        if choice < 1 or choice > len(filtered_formats):
            print("Invalid selection.")
            return

        selected_format_id = filtered_formats[choice - 1]['format_id']

        # Download
        ydl_opts_download = {
            'format': selected_format_id,
            'outtmpl': '%(title)s.%(ext)s',
        }

        print("\nDownloading...")
        with yt_dlp.YoutubeDL(ydl_opts_download) as ydl:
            ydl.download([url])

        print("\nDownload completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    list_and_download_video(video_url)
