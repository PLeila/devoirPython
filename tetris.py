import random

# Dimensions du terrain de jeu
LARGEUR, HAUTEUR = 10, 20

# Codes des pièces Tetris
PIECES = {
    'O': [['OO',
           'OO']],
    'I': [['....',
           'IIII',
           '....',
           '....'],
          ['..I.',
           '..I.',
           '..I.',
           '..I.']],
    'S': [['....',
           '.SS.',
           'SS..',
           '....'],
          ['S...',
           'SS..',
           '.S..',
           '....']],
    'Z': [['....',
           'ZZ..',
           '.ZZ.',
           '....'],
          ['.Z..',
           'ZZ..',
           'S...',
           '....']],
    'L': [['....',
           '.L..',
           '.L..',
           '.LL.'],
          ['....',
           '..LL',
           '.L..',
           '....'],
          ['....',
           'LL..',
           '.L..',
           '....'],
          ['....',
           '.L..',
           '.L..',
           '.L..']],
    'J': [['....',
           '.J..',
           '.J..',
           'JJ..'],
          ['....',
           '.JJ.',
           '..J.',
           '....'],
          ['....',
           'JJ..',
           '.J..',
           '....'],
          ['....',
           '..J.',
           '..J.',
           '.JJ.']]
}

def creer_terrain():
    return [[' ' for _ in range(LARGEUR)] for _ in range(HAUTEUR)]

def afficher_terrain(terrain):
    for ligne in terrain:
        print(' '.join(ligne))

def piece_aleatoire():
    return random.choice(list(PIECES.keys()))

def tourner_piece(piece, rotation):
    return PIECES[piece][rotation % len(PIECES[piece])]

def peut_placer_piece(terrain, piece, x, y):
    forme = tourner_piece(piece, 0)
    for i, ligne in enumerate(forme):
        for j, case in enumerate(ligne):
            if case == '.':
                continue
            if x + j < 0 or x + j >= LARGEUR or y + i >= HAUTEUR:
                return False
            if terrain[y + i][x + j] != ' ':
                return False
    return True

def placer_piece(terrain, piece, x, y):
    forme = tourner_piece(piece, 0)
    for i, ligne in enumerate(forme):
        for j, case in enumerate(ligne):
            if case != '.':
                terrain[y + i][x + j] = piece

def effacer_lignes(terrain):
    lignes_effacees = 0
    lignes_non_effacees = []
    for ligne in terrain:
        if ' ' not in ligne:
            lignes_effacees += 1
        else:
            lignes_non_effacees.append(ligne)
    terrain.clear()
    terrain.extend([' '] * LARGEUR for _ in range(lignes_effacees))
    terrain.extend(lignes_non_effacees)
    return lignes_effacees

def jouer():
    terrain = creer_terrain()
    piece_courante = piece_aleatoire()
    x, y = LARGEUR // 2, 0
    rotation = 0
    score = 0

    while True:
        if peut_placer_piece(terrain, piece_courante, x, y + 1):
            y += 1
        else:
            placer_piece(terrain, piece_courante, x, y)
            lignes_effacees = effacer_lignes(terrain)
            score += lignes_effacees
            print("\nTerrain:")
            afficher_terrain(terrain)
            print(f"Score: {score}")
            piece_courante = piece_aleatoire()
            x, y = LARGEUR // 2, 0
            rotation = 0
            if not peut_placer_piece(terrain, piece_courante, x, y):
                print("Jeu terminé. Score final:", score)
                break

        print("\nTerrain:")
        afficher_terrain(terrain)
        print(f"Score: {score}")

if __name__ == "__main__":
    jouer()
