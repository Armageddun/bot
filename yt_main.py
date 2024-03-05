from pytube import YouTube


def Get_URl(link):
    yt = YouTube(link)

    return yt.streams.all()[0].url


yt = YouTube('https://www.youtube.com/watch?v=I2rFeL8aFrQ')
yt.streams.first().download()


# print(Get_URl('https://www.youtube.com/watch?v=I2rFeL8aFrQ'))