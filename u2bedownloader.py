from pytube import YouTube
import sys

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
  except:
    print("An error has occurred")
    print("Download is completed successfully")
  
  if __name__ == "__main__":
    if len(sys.argv) != 2:
      print("Please provide the YouTube video URL as a command-line argument.")
      print("Usage: python script_name.py <video_url>")
    else:
      link = sys.argv[1]
      Download(link)
