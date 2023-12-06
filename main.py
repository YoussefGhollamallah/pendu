import pygame
from random import choice

pygame.init()


largeur, hauteur = 800, 800
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Le Pendu")


noir = (25, 35, 55)
blanc = (255, 255, 255)


police = pygame.font.SysFont("arial", 30)

def afficher_mot(mot, lettres_devinées):
    affichage = " ".join([lettre if lettre in lettres_devinées else "_" for lettre in mot])
    texte = police.render(affichage, 1, blanc)
    screen.blit(texte, (largeur // 4, hauteur // 2))


with open("mots.txt", 'r') as fichier:
    mots = fichier.read().splitlines()


mot_solution = choice(mots).upper()

lettres_devinées = set()

max_erreurs = 6

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

    screen.fill(noir)

    afficher_mot(mot_solution, lettres_devinées)

    lettres_texte = police.render(f"Lettres devinées: {' '.join(sorted(lettres_devinées))}", 1, blanc)
    screen.blit(lettres_texte, (largeur // 4, hauteur // 4))

    
    if max_erreurs < 6:
        pygame.draw.circle(screen, blanc, (3 * largeur // 4, hauteur // 4), 30, 2)
    if max_erreurs < 5:
        pygame.draw.line(screen, blanc, (3 * largeur // 4, hauteur // 4 + 30), (3 * largeur // 4, hauteur // 2), 2)  
    if max_erreurs < 4:
        pygame.draw.line(screen, blanc, (3 * largeur // 4, hauteur // 4 + 30), (3 * largeur // 4 - 20, hauteur // 2), 2)  
    if max_erreurs < 3:
        pygame.draw.line(screen, blanc, (3 * largeur // 4, hauteur // 4 + 30), (3 * largeur // 4 + 20, hauteur // 2), 2)
    if max_erreurs < 2:
        pygame.draw.line(screen, blanc, (3 * largeur // 4, hauteur // 2), (3 * largeur // 4 - 20, 3 * hauteur // 4), 2)  
    if max_erreurs < 1:
        pygame.draw.line(screen, blanc, (3 * largeur // 4, hauteur // 2), (3 * largeur // 4 + 20, 3 * hauteur // 4), 2)  

   
    pygame.display.flip()

  
    if set(lettres_devinées) >= set(mot_solution):
        print("Félicitations ! Vous avez gagné !")
        running = False
    elif max_erreurs == 0:
        print(f"Dommage ! Vous avez perdu. Le mot était '{mot_solution}'.")
        running = False

pygame.quit()
