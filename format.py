import yt_dlp

def listar_formatos(url):
    try:
        opcoes = {}
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            info = ydl.extract_info(url, download=False)
            formatos = info.get("formats", [])
            for formato in formatos:
                print(f"id: {formato['format_id']}, ext: {formato['ext']}, res: {formato.get('resolution', 'N/A')}, fps: {formato.get('fps', 'N/A')}")
    except Exception as e:
        print(f"Erro ao listar os formatos: {e}")

# URL do vídeo
url_da_live = "https://youtu.be/LBpeLo7a4H4"
listar_formatos(url_da_live)
