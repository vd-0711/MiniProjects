from pytube import YouTube
import webbrowser

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

print("You will be directed to Youtube \nPlease select a video which you want to download and copy the url")
webbrowser.open('https://www.youtube.com/',  new=0)
link = input("Enter the YouTube video URL: ")
Download(link)