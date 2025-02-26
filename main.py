import yt_dlp

def download_music(video_links):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {
                'key': 'FFmpegMetadata',
            },
            {
                'key': 'EmbedThumbnail',
            },
        ],
        'writethumbnail': True,
        'writemetadata': True,
        'postprocessor_args': [
            '-id3v2_version', '3',
        ],
        'prefer_ffmpeg': True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for link in video_links:
            try:
                print(f"\nDownloading: {link}")
                ydl.download([link])
                print("Download completed with metadata!\n")
            except Exception as e:
                print(f"Failed to download {link}: {e}\n")

def main():
    print("=== YouTube Music Downloader ===")
    print("Enter YouTube video links (separate multiple links with commas):")
    links_input = input("Links: ")

    video_links = [link.strip() for link in links_input.split(',') if link.strip()]

    if video_links:
        download_music(video_links)
    else:
        print("No links provided. Program exiting.")

if __name__ == "__main__":
    main()