# import moviepy.editor as mp
import speech_recognition as sr
# import sys
from pydub import AudioSegment

# a variável path contem o nome do arquivo do seu vídeo
# path = “nome_do_arquivo.mp4” 

# converter de mp4 para mp3
# clip = mp.VideoFileClip(path).subclip()
# clip.audio.write_audiofile("./nome_para_audio.mp3")

src = (r".\avaliacao-cpsfij-2023-nicolau.mp3")

# converter de mp3 para wav
sound = AudioSegment.from_mp3(src)
sound.export(r".\avaliacao-cpsfij-2023-nicolau.wav", format="wav")
file_audio = sr.AudioFile(r".\avaliacao-cpsfij-2023-nicolau.wav")

# use the audio file as the audio source
r = sr.Recognizer()
with file_audio as source:
    audio_text = r.record(source)
    text = r.recognize_google(audio_text, language='pt-BR')

# cria arquivo e salva a transcrição
arq = open(r".\transcricao-avaliacao-cpsfij-2023-nicolau.txt", 'w')
arq.write(text)
arq.close()
print(text)
