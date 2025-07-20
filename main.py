import yt_dlp

def baixar_live_com_audio_e_video(url, caminho_arquivo="live.mp4"):
    opcoes = {
        "outtmpl": caminho_arquivo,  # Nome do arquivo de saída
        "format": "bestvideo+bestaudio/best",  # Combina vídeo e áudio
        "merge_output_format": "mp4",  # Formato final
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])
        print(f"Download concluído: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao baixar a live: {e}")

# URL da live do YouTube
url_da_live = "https://youtu.be/LBpeLo7a4H4"
baixar_live_com_audio_e_video(url_da_live)

#
