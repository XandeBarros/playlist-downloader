from pytube import Playlist, YouTube
import os

path = os.path.dirname(os.path.abspath(__file__))
link_playlist = str(input('Link da Playlist: '))

playlist = Playlist(link_playlist)

playlist_title = playlist.title

number = 1

for video in playlist:
  video = YouTube(video)
  print(f'Downloading {video.title}')
  title = str(video.title)
  video = video.streams.get_audio_only()
  full_path = f'{path}\downloads\{playlist_title}'
  out_file = video.download(full_path)
  base, ext = os.path.splitext(out_file)
  name_music = base.split(f'{full_path}\\')
  name_music = f'{number} - {name_music[1]}'
  base = f'{full_path}\\{name_music}'
  new_file = base + '.mp3'
  os.rename(out_file, new_file)
  number += 1

print('Downloads concluídos ;)')