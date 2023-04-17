# Import the required module for text
# to speech conversion
from gtts import gTTS
import pygame
import time

# import os


def text_to_speech(text):

    # The text that you want to convert to audio
    mytext = text

    # Language in which you want to convert
    # language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    #myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    #myobj.save("welcome.mp3")
    if mytext=="Red":
        pygame.init()
        pygame.mixer.music.load("Red.mp3")
        pygame.mixer.music.play()
        time.sleep(0.1)
    elif mytext=="Blue":
        pygame.init()
        pygame.mixer.music.load("Blue.mp3")
        pygame.mixer.music.play()
        time.sleep(0.1)
    elif mytext=="Green":
        pygame.init()
        pygame.mixer.music.load("Green.mp3")
        pygame.mixer.music.play()
        time.sleep(0.1)
    elif mytext=="Eraser":
        pygame.init()
        pygame.mixer.music.load("Eraser.mp3")
        pygame.mixer.music.play()
        time.sleep(0.1)