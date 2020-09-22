#@author Alejandro_Dapena
from logic import *
import shutil

hashtag = input("Hashtag: ")
video_lenght = input("Estimated lenght of the video (in minutes): ")

downloadTikTok(hashtag,int(video_lenght)*2) #Download the wanted amount of Tik Toks from the given category. Every video is +- 30 sec
concatenateVideo() #Concatenates all the videos and makes the final Tik Tok compilation video
shutil.rmtree('downloads', ignore_errors=True) #Delete the folder where all diferent Tik Toks were saved before the concatenation