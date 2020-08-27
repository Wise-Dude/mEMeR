import pygame
import time
import speech_recognition as sr
pygame.init()

WIDTH, HEIGHT = 720, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tAlK MemE")

WIN_IMAGE =  pygame.transform.scale(pygame.image.load(r"C:\Users\mehedee\Desktop\Python work\Img\mockingspongebobbb.jpg"), (WIDTH, HEIGHT))

r = sr.Recognizer()

def voice_rec():
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
        print("Done")

    text = r.recognize_google(audio)
    print(text)

def main():
    run = True
    FPS = 120
    clock = pygame.time.Clock()

    def draw_win():
        WIN.blit(WIN_IMAGE, (0,0))
        pygame.display.update()

        

    while run == True:
        clock.tick(FPS)
        draw_win()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

voice_rec()
main()
            