from pytube import YouTube
from pytube.cli import on_progress

def Download(link):
    youtubeObject = YouTube(link,on_progress_callback=on_progress)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download('videos/')
    except:
        print("Ocorreu um erro")

    print("Download concluído")


link = input("Insira um URL de vídeo do YouTube: ")
Download(link)