import pygame
import os
import random
pygame.init()

#okno gry
window_width = 1000
window_heigh = 600
window = pygame.display.set_mode((window_width, window_heigh))

#tekst
def write(text, x , y, size):
    font = pygame.font.SysFont("Arial", size)
    rend = font.render(str(text), 1, (178,247,170))
    window.blit(rend, (x, y))

#wyswietlanie tekstu
def display_word(word, x, y, size):
    display_text = "".join(word)
    write(display_text, x, y, size)

#zmienne
what_shows_up = "menu"
user_word = []
entered_word = []
guess_letter = ""
guessed_letters = []
wrong_guessed_letters = []
wrong_guesses_count = 0
category = ""
random_word = False
displayed_entered_word = ""
hangman_phases_images = ["pics/pix_1.png", "pics/pix_2.png", "pics/pix_3.png", "pics/pix_4.png", "pics/pix_5.png", "pics/pix_6.png", "pics/pix_7.png", "pics/pix_8.png", "pics/pix_9.png", "pics/pix_10.png"]
categories = {"Zwierzeta": ["ocelot", "tygrys", "kangur", "panda", "chomik", "szynszyla", "slon", "kapucynka", "kaczka", "wilk", "kot", "krokodyl", "sowa", "pingwin", "niedzwiedz", "pancernik", "delfin", "papuga", "fratka", "pies"],
              "Gry komputerowe": ["minecraft", "fortnite", "overwatch", "unravel", "deceit", "moonlighter", "dishonored", "undertale", "spore", "fallout", "counter strike", "assassins creed", "fall guys", "among us", "payday", "dead by daylight", "the binding of isaac"],
              "Ksiezniczki Disneya": ["jasmina", "pocahontas", "mulan", "tiana", "merida", "arielka", "kopciuszek", "roszpunka", "vaiana", "bella", "aurora", "elsa", "anna"],
              "Filmy Disneya": ["lilo i stich", "bambi", "aladyn", "krol lew", "zwierzogrod", "kraina lodu", "coco", "zaplatani","raya i ostatni smok", "merida waleczna", "mala syrenka", "wielka szostka"],
              "Owoce i warzywa": ["marchewka", "brukselka", "malina", "trukawka", "seler", "kukurydza", "cebula", "arbuz", "borowka", "dynia", "papryka", "grejpfrut", "kiwi", "szparagi", "winogrona", "banan"],
              "Celebryci": ["paris hilton", "britney spears", "lady gaga", "angelina jolie", "emma stone", "julia roberts", "keanu reeves", "daniel radcliffe", "brad pitt", "johnny depp", "robert downey jr", "leonardo dicaprio", "tom cruise", "harrison ford"]}

#sprawdzanie eventow
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and what_shows_up == "menu":
                what_shows_up = "ask_player"

            #wybieranie slowa
            elif what_shows_up == "ask_player":
                if event.key == pygame.K_1:
                    what_shows_up = "enter_word"
                elif event.key == pygame.K_2:
                    category = random.choice(list(categories.keys()))
                    entered_word = random.choice(categories[category])
                    entered_word_as_string = "".join(entered_word)
                    for i, letter in enumerate(entered_word_as_string):
                        if letter == " ":
                            displayed_entered_word += "   "
                        else:
                            displayed_entered_word += "_ "
                    random_word = True
                    what_shows_up = "game_on"
                elif event.key == pygame.K_3:
                    what_shows_up = "choose_category"

            #zapisanie slowa i rozpoczecie gry
            elif event.key == pygame.K_RETURN and what_shows_up == "enter_word":    
                if len(user_word) > 0:
                    entered_word.append("".join(user_word))
                    user_word = []
                    entered_word_as_string = "".join(entered_word)

                    for i, letter in enumerate(entered_word_as_string):
                        if letter == " ":
                            displayed_entered_word += "   "
                        else:
                            displayed_entered_word += "_ "
                    what_shows_up = "game_on"
                    
            #wybor kategorii slowa
            elif what_shows_up == "choose_category":
                if event.key == pygame.K_1:
                    category = "Zwierzeta"
                elif event.key == pygame.K_2:
                    category = "Gry komputerowe"
                elif event.key == pygame.K_3:
                    category = "Ksiezniczki Disneya"
                elif event.key == pygame.K_4:
                    category = "Filmy Disneya"
                elif event.key == pygame.K_5:
                    category = "Owoce i warzywa"
                elif event.key == pygame.K_6:
                    category = "Celebryci"

                entered_word = random.choice(categories[category])
                entered_word_as_string = "".join(entered_word)
                for i, letter in enumerate(entered_word_as_string):
                    if letter == " ":
                        displayed_entered_word += "   "
                    else:
                        displayed_entered_word += "_ "
                random_word = True
                what_shows_up = "game_on"

        elif event.type == pygame.KEYUP and what_shows_up == "enter_word":
            if 97 <= event.key <= 122 or event.key == 32:  # Obsluga tylko liter od A do Z
                user_word.append(chr(event.key))    #dodawanie wpisanych liter

            elif event.key == pygame.K_BACKSPACE:
                if len(user_word) > 0:
                    user_word.pop() #usuwanie wpisanych liter

        elif event.type == pygame.KEYUP and what_shows_up == "game_on":
            if 97 <= event.key <= 122:  # Obsluga tylko liter od A do Z
                guess_letter = chr(event.key)   #dodanie zgadywanej literki
            elif event.key == pygame.K_BACKSPACE:
                if guess_letter != "":
                    guess_letter = ""

            #wyswietlanie hasla w oknie gry
            elif event.key == pygame.K_RETURN:
                if guess_letter != "":
                    if guess_letter in entered_word_as_string:
                        displayed_entered_word = ""
                        for letter in entered_word_as_string:
                            if letter == guess_letter:
                                displayed_entered_word+= guess_letter + " "
                                guessed_letters.append(guess_letter)
                            elif letter in guessed_letters:
                                displayed_entered_word += letter + " "
                            elif letter == " ":
                                displayed_entered_word += "   "
                            else:
                                displayed_entered_word += "_ "
                        guess_letter = ""

                    else:
                        if guess_letter not in wrong_guessed_letters:
                            wrong_guessed_letters.append(guess_letter)
                            wrong_guesses_count += 1
                        guess_letter = ""

                
    window.fill("black")
    keys = pygame.key.get_pressed()

    #odpowiednie tła i działanie gry
    if what_shows_up == "menu":
        write("Nacisnij spacje aby zaczac", 380, 400, 30)
        pic = pygame.image.load(os.path.join("pics", "game_logo.png"))
        window.blit(pic, (250, 180))#obraz na tych wspolrzednych

    elif what_shows_up == "ask_player":
        write("Wybierz w jaki sposob chcesz zagrac (kliknij odpowiedni przycisk): ",120, 200, 30)
        write("1 - chce wpisac wlasne haslo", 120, 300, 30 )
        write("2 - chce zagrac z losowym haslem", 120, 350, 30)
        write("3 - chce wybrac kategorie zgadywanego slowa", 120, 400, 30)
    
    elif what_shows_up == "choose_category":
        write("Wybierz kategorie: ",120, 200, 30)
        write("1 - Zwierzeta", 120, 250, 30 )
        write("2 - Gry komputerowe", 120, 290, 30)
        write("3 - Ksiezniczki Disneya", 120, 330, 30)
        write("4 - Filmy Disneya", 120, 370, 30 )
        write("5 - Owoce i warzywa", 120, 410, 30)
        write("6 - Celebryci", 120, 450, 30)

    elif what_shows_up == "enter_word":
        write("Wprowadz slowo: ", 400, 250, 30)
        write("".join(user_word), 440, 350, 30)
        

    elif what_shows_up == "game_on":
            write("Sprobuj zgadnac litere: ", 380, 400, 30)
            write(displayed_entered_word,360, 300, 30)
            #kiedy przegrana gra
            if wrong_guesses_count < 9:
                pic = pygame.image.load(hangman_phases_images[wrong_guesses_count])
            else:
                what_shows_up = "lost_game"

            window.blit(pic, (100, 140))
            #wyswietlanie zgadywanej litery w oknie gry
            write(str(guess_letter), 500, 450, 30)
            #wyswietlanie zle zgadnietych liter
            write(" ". join(wrong_guessed_letters), 440, 550, 20)
            #wyswietlanie kategorii
            if random_word == True:
                write(f"Wylosowana kategoria: {category}", 360,200,30)
            #kiedy wygrana gra
            if "_" not in displayed_entered_word:
                what_shows_up = "won_game"
        
    elif what_shows_up == "lost_game":
        write(displayed_entered_word, 360, 300, 30)
        pic = pygame.image.load(hangman_phases_images[wrong_guesses_count])
        window.blit(pic, (100, 140))

        write(" ". join(wrong_guessed_letters), 440, 550, 20)
        write("Przegrales! Powodzenia nastepnym razem!", 360, 200, 30)
        write(f"Haslo: {entered_word_as_string}", 360, 250, 30)
    

    elif what_shows_up == "won_game":
        write(displayed_entered_word, 360, 300, 30)
        pic = pygame.image.load(hangman_phases_images[wrong_guesses_count])
        window.blit(pic, (100, 140))

        write(" ". join(wrong_guessed_letters), 440, 550, 20)
        write("Wygrales! Zgadles prawidlowo haslo!", 360, 200, 30)
        write(f"Haslo: {entered_word_as_string}", 360, 250, 30)

    pygame.display.update()