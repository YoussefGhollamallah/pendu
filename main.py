import pygame
from random import choice

pygame.init()

largeur, hauteur = 1000, 800
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Le Pendu")

bg = (25, 35, 55)
text_color = (255, 255, 255)

menu = False

police = pygame.font.SysFont("arialblack", 30)

def menu_pendu(text, font, text_col, x, y):
    message = font.render(text, True, text_col)
    screen.blit(message, (x, y))

def afficher_mot(mot, lettres_devinées):
    affichage = " ".join([lettre if lettre in lettres_devinées else "_" for lettre in mot])
    texte = police.render(affichage, 1, text_color)
    screen.blit(texte, (largeur // 4, hauteur // 2))

def rejouer():
    global menu
    global max_erreurs
    global mot_solution
    global lettres_devinées

    menu = False
    max_erreurs = 6
    lettres_devinées = set()
    mot_solution = choice(mots).upper()

with open("mots.txt", 'r') as fichier:
    mots = fichier.read().splitlines()

mot_solution = choice(mots).upper()
lettres_devinées = set()
max_erreurs = 6

def game():
    global menu
    global max_erreurs
    global mot_solution
    global lettres_devinées

    screen.fill(bg)

    if menu == False:
        menu_pendu("Appuyer sur Espace pour jouer", police, text_color, 240, 360)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = True 
    else:
        afficher_mot(mot_solution, lettres_devinées)

        lettres_texte = police.render(f"Lettres devinées: {' '.join(sorted(lettres_devinées))}", 1, text_color)
        screen.blit(lettres_texte, (largeur // 4, hauteur // 4))

            
        if max_erreurs < 6:
            pygame.draw.circle(screen, text_color, (3 * largeur // 4, hauteur // 4), 30, 2)
        if max_erreurs < 5:
            pygame.draw.line(screen, text_color, (3 * largeur // 4, hauteur // 4 + 30), (3 * largeur // 4, hauteur // 2), 2)  
        if max_erreurs < 4:
            pygame.draw.line(screen, text_color, (3 * largeur // 4, hauteur // 4 + 30), (3 * largeur // 4 - 20, hauteur // 2), 2)  
        if max_erreurs < 3:
            pygame.draw.line(screen, text_color, (3 * largeur // 4, hauteur // 4 + 30), (3 * largeur // 4 + 20, hauteur // 2), 2)
        if max_erreurs < 2:
            pygame.draw.line(screen, text_color, (3 * largeur // 4, hauteur // 2), (3 * largeur // 4 - 20, 3 * hauteur // 4), 2)  
        if max_erreurs < 1:
            pygame.draw.line(screen, text_color, (3 * largeur // 4, hauteur // 2), (3 * largeur // 4 + 20, 3 * hauteur // 4), 2)  


        if set(lettres_devinées) >= set(mot_solution):
            menu_pendu("Voulez vous rejouer (appuyez sur R)", police, text_color, 240, 360)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:  
                rejouer()

        elif max_erreurs == 0:
            menu_pendu("Voulez vous rejouer (appuyez sur R)", police, text_color, 240, 360)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                rejouer()

    pygame.display.flip()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                lettre = event.unicode.upper()
                if lettre not in lettres_devinées:
                    lettres_devinées.add(lettre)
                    if lettre not in mot_solution:
                        max_erreurs -= 1

    game()

pygame.quit()
