from pytube import YouTube


def Get_URl(link):
    yt = YouTube(link)

    return yt.streams.all()[0].url

def download_video(link):
    yt = YouTube(link)
    yt.streams.first().download()



# print(Get_URl('https://www.youtube.com/watch?v=I2rFeL8aFrQ'))