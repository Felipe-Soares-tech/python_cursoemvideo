import pygame
pergunta = str(input('voce é apaixonado por careless whisper? ')).strip().lower()
if pergunta == 'sim':
    print('\033[35;40m Você sim é um homem de valores meu amigo')
    pygame.init()
    pygame.mixer.music.load('ex021b.mp3')
    pygame.mixer.music.play()
    input()
    pygame.event.wait()
else:
    print('\033[36;40m MENTIRA!!! \033[4;37;45m voce é viado')