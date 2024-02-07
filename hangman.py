import pygame
import os
pygame.init()

#okno gry
window_width = 1000
window_heigh = 600
window = pygame.display.set_mode((window_width, window_heigh))

#wypisywanie tekstow
def write(text, x , y, size):
    font = pygame.font.SysFont("Arial", size)
    rend = font.render(str(text), 1, (178,247,170))
    window.blit(rend, (x, y))

def display_word(word, x, y, size):
    display_text = "".join(word)
    write(display_text, x, y, size)

what_shows_up = "menu"
user_word = []
entered_word = []
guess_letter = ""

#sprawdzanie eventow
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                what_shows_up = "ask_player"
            elif event.key == pygame.K_1:
                what_shows_up = "enter_word"
            elif event.key == pygame.K_RETURN and what_shows_up == "enter_word":
                what_shows_up = "game_on"
                entered_word.append("".join(user_word))
                user_word = []

        elif event.type == pygame.KEYUP and what_shows_up == "enter_word":
            if 97 <= event.key <= 122:  # Obsługa tylko liter od A do Z
                user_word.append(chr(event.key))    #dodawanie wpisanych liter

            elif event.key == pygame.K_BACKSPACE:
                if len(user_word) > 0:
                    user_word.pop() #usuwanie wpisanych liter

        elif event.type == pygame.KEYUP and what_shows_up == "game_on":
            if 97 <= event.key <= 122:  # Obsługa tylko liter od A do Z
                guess_letter = chr(event.key)   #dodanie zgadywanej literki
            elif event.key == pygame.K_BACKSPACE:
                if guess_letter != "":
                    guess_letter = ""
            # elif event.key == pygame.K_RETURN:
                

    window.fill("black")
    keys = pygame.key.get_pressed()

    #odpowiednie tła i działanie gry
    if what_shows_up == "menu":
        write("Nacisnij spacje aby zaczac", 380, 400, 30)
        pic = pygame.image.load(os.path.join("game_logo.png"))
        window.blit(pic, (250, 180))

    elif what_shows_up == "ask_player":
        write("Chcesz wpisać słowo do zgadnięcia (kliknij 1) czy wylosować (kliknij 2) ?",120, 280, 30)
    
    elif what_shows_up == "enter_word":
        write("Wprowadz slowo: ", 400, 250, 30)
        write("".join(user_word), 440, 350, 30)
        

    elif what_shows_up == "game_on":
        if not entered_word:
            what_shows_up == "enter_word"
        else:
            write("Sprobuj zgadnac litere: ", 380, 400, 30)
            pic = pygame.image.load(os.path.join("pix_10.png"))
            window.blit(pic, (400, 140))

            write(str(guess_letter), 500, 450, 30)
            # if user_word in entered_word:

            # ##sprawdzenie czy slowo jest poprawnie zapisane
            # for i, word in enumerate(entered_word):
            #     write(f"Wprowadzone słowo: {word}", 100, 250 + i * 30, 20)

fdfsfsdfsdf
    pygame.display.update()
