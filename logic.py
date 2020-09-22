from TikTokApi import TikTokApi
import os,os.path
from moviepy.editor import VideoFileClip, concatenate_videoclips
'''
Function: Downloads enough Tik Toks in order to accomplish the estimated lenght of the desired video
Parameters:
    -hashtag: Name of the hashtag we want to download the videos from
    -lenght: Estimated lenght of the video. 
'''
def downloadTikTok(hashtag,lenght):
    api = TikTokApi()
    #Get the Tik Tok Object
    lista = api.byHashtag(hashtag, count=lenght, language='en', proxy=None)
    #Create the folder
    os.mkdir("downloads")

    for i in range(len(lista)):
        data = api.get_Video_By_TikTok(lista[i])# bytes of the video
        with open("downloads/{}.mp4".format(str(i)), 'wb') as output:
            output.write(data)
            print("Downloaded "+ str(i+1)+"/"+str(len(lista))) #at the beggining, i==0
def getClipFilename(i):
    return 'downloads/' + str(i) + ".mp4"
'''
Function: Concatenates all videos from the download folder and saves the final video
'''
def concatenateVideo():
    path = "downloads/"

    cliparray = []

    for filename in os.listdir(path):
        cliparray.append(VideoFileClip(path + filename))

    final_clip = concatenate_videoclips(cliparray, method='compose')

    final_clip.write_videofile("tiktTokCompilation.mp4", codec="libx264")

