from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=2W0JzGYq1Kc")
stream = yt.streams.first()
stream.download()
