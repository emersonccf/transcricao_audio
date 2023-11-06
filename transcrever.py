import whisper

# tiny base small medium large
modelo = whisper.load_model("small")
resposta = modelo.transcribe(r".\avaliacao-cpsfij-2023-nicolau.m4a")

# cria arquivo e salva a transcrição
arq = open(r".\transcricao-avaliacao-cpsfij-2023-nicolau.txt", 'w')
texto = resposta["text"]
arq.write(texto)
arq.close()
print(texto)
