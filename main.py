from pytubefix import YouTube
import os

def download_video(url, output_path='.'):
  try:
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download(output_path)
    print(f"Download completo: {yt.title}")
  except Exception as e:
    print(f"Incosistência detectada: {e}")

if __name__ == "__main__":
  video_url = input("URL do vídeo: ")
  current_path = os.getcwd()
  download_path = os.path.join(current_path, 'videos')

  if not os.path.exists(download_path):
    os.makedirs(download_path)
  download_video(video_url, download_path)