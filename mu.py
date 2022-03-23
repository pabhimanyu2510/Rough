from pytube import YouTube

link = YouTube(str(input("Enter Video Link : ")))

stream = link.streams.get_highest_resolution()

video = stream.download()


