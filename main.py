import pytube
from pytube import Playlist

#for downloading playlist
playlist = Playlist(input("enter the link to download: "))

lista = playlist.video_urls

for key,video_url in enumerate(lista):
    # print(video_url)
    video = pytube.YouTube(video_url)
    stream = video.streams.get_by_itag(22)
    print("Donwloading..." + str(video_url))
    stream.download(filename="lesson" + str(key))


print("all files donwloaded")



#for downlading only one video 
# url = input("enter the URL: ")

# video = pytube.YouTube(url)

# stream = video.streams.get_by_itag(22)
# print("Donwloading...")
# stream.download(filename="Types of Amplifiers")
# print("done")