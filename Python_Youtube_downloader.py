# First install the pytube and 
# import the file YouTube

from pytube import YouTube

#Used the def function 

def download_video(url, save_path="."):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        stream.download(save_path)
        print("Download complete!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ")
    save_location = input("Enter save path (or press Enter for current directory): ") or "."
    download_video(video_url, save_location)

