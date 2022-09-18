from pygame import init
from pygame import mixer

init()
musica = mixer.Sound("HWA Theme on Guitar.mp3")
musica.play()

print("--  Music Player em Python  --")
input(">> PRESIONE ENTER PARA ENCERRAR")

