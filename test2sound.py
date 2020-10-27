from gtts import gTTS
import pyttsx3
from playsound import playsound
from sys import platform
import os

print("Multiple text to speech made by github.com/terremoth")

phrase = input("Write something so I can speak with some different voices: ")
lang_choosed = input("Now type the language (ex: en, pt-br, es): ")

# gTTS
print("Voice from gTTS (google text to speech - requires internet connection)")
tts = gTTS(phrase, lang=lang_choosed)
voice_file = '._temp_audio.mp3'
tts.save(voice_file)
playsound(voice_file)
os.remove(voice_file)

# Pyttsx
print("Voice from Pyttsx:")
engine = pyttsx3.init()
engine.say(phrase)
engine.runAndWait()

platform = platform.lower()
if platform == "darwin":
	print("Voice from MAC/iOS speech:")
	import speech
	speech.say(phrase, lang_choosed)

elif platform == "windows" or platform == "win32":
	print("Voice from Microsoft speech engine:")
	from win32com.client import Dispatch
	speak = Dispatch("SAPI.SpVoice")
	speak.Speak(phrase)

'''
# Watson

from tts_watson.TtsWatson import TtsWatson

ttsWatson = TtsWatson('YOUR WATSON USER', 'YOUR WATSON PASSWORD', f"{lang_choosed}_AllisonVoice") 
ttsWatson.play(phrase)

'''