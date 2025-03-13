# 🚀 Flappy Elon

A "Flappy Bird" style game with a SpaceX/Elon Musk twist, created in Python using Pygame.

![Flappy Elon Game Screenshot](https://krimdevnode.ovh/flappy_elon.png)

## 📖 Description

"Flappy Elon" is a fun parody of the popular Flappy Bird game, but with a space theme and Elon Musk elements. In this game, you control a flying cat that must navigate between SpaceX rockets to reach Mars. During your journey, you'll encounter Tesla cars and X/Twitter logos.

## 🎮 Features

- Unique graphics with a flying cat as the playable character
- SpaceX rocket-shaped obstacles
- Collectible items like Tesla cars and X/Twitter logos
- Thematic space background
- Sound effects and background music
- Progress bar to Mars
- Special victory screen when you reach Mars
- Customized game over screen

## 🛠️ Prérequis

- Python 3.x
- Pygame

## 📥 Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/votre-username/flappy-elon.git
cd flappy-elon
```

2. Installez Pygame si vous ne l'avez pas déjà :
```bash
pip install pygame
```

## 🎯 Comment jouer

1. Lancez le jeu :
```bash
python flappy_elon.py
```

2. Appuyez sur la barre d'espace pour faire voler le chat
3. Évitez les fusées et atteignez Mars (score de 10)
4. Si vous perdez, appuyez sur "R" pour recommencer

## 🎨 Ressources graphiques

Vous aurez besoin des fichiers images suivants dans le même dossier que le script :
- elon_head.png (image du chat volant)
- rocket.png
- space_background.png
- tesla_car.png
- x_logo.png
- twitter_logo.png
- krimdevnode_avatar.png (optionnel)
- mars.png (optionnel)
- mars_background.png (optionnel)

## 🔊 Sons

Les fichiers sonores suivants sont optionnels mais améliorent l'expérience :
- background_music.mp3
- win_sound.mp3
- lose_sound.mp3
- milestone_sound.mp3

## 🛠️ Personnalisation

Vous pouvez modifier plusieurs paramètres du jeu en changeant les constantes dans le code :
- `WINDOW_WIDTH` et `WINDOW_HEIGHT` : dimensions de la fenêtre
- `GRAVITY` : force de gravité appliquée
- `JUMP` : puissance du saut
- `pipe_speed` : vitesse des fusées
- `tesla_speed` : vitesse des voitures Tesla et des logos
- `TESLA_SPAWN_RATE` : fréquence d'apparition des éléments
- `max_score` : score nécessaire pour atteindre Mars

## 🙏 Crédits

Développé par [@KrimDevNode](https://github.com/KrimDevNode) avec l'aide de Grok.

## 📜 Licence

[MIT License](LICENSE)

---
*Note: Ce projet est uniquement à des fins éducatives et humoristiques. Toutes les images utilisées doivent respecter les droits d'auteur appropriés.*
