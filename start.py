import pygame
import random


pygame.init()
pygame.mixer.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Elon 1.0")

ORANGE_FIRE = (255, 69, 0)

player_img = pygame.image.load("img/elon_head.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (100, 62))
pipe_img = pygame.image.load("img/rocket.png").convert_alpha()
pipe_img = pygame.transform.scale(pipe_img, (70, 150))
background_img = pygame.image.load("img/space_background.png").convert()
tesla_img = pygame.image.load("img/tesla_car.png").convert_alpha()
tesla_img = pygame.transform.scale(tesla_img, (50, 25))
x_logo_img = pygame.image.load("img/x_logo.png").convert_alpha()
x_logo_img = pygame.transform.scale(x_logo_img, (30, 30))
twitter_logo_img = pygame.image.load("img/twitter_logo.png").convert_alpha()
twitter_logo_img = pygame.transform.scale(twitter_logo_img, (30, 30))

try:
    avatar_img = pygame.image.load("img/krimdevnode_avatar.png").convert_alpha()
    avatar_img = pygame.transform.scale(avatar_img, (207, 87)) 
except Exception as e:
    avatar_img = None

try:
    mars_img = pygame.image.load("mars.png").convert_alpha()
    mars_img = pygame.transform.scale(mars_img, (30, 30))
except Exception as e:
    mars_img = None

try:
    mars_background_img = pygame.image.load("img/mars_background.png").convert()
    mars_background_img = pygame.transform.scale(mars_background_img, (WINDOW_WIDTH, WINDOW_HEIGHT))
except Exception as e:
    mars_background_img = None

try:
    background_music = pygame.mixer.Sound("mp3/background_music.mp3")
    win_sound = pygame.mixer.Sound("mp3/win_sound.mp3")
    lose_sound = pygame.mixer.Sound("mp3/lose_sound.mp3")
    milestone_sound = pygame.mixer.Sound("mp3/milestone_sound.mp3")
except Exception as e:
    background_music = win_sound = lose_sound = milestone_sound = None

font = pygame.font.Font(None, 36) 
small_font = pygame.font.Font(None, 24)

# Texte du crédit
credit_text = small_font.render("@KrimDevNode", True, (255, 255, 255))

def reset_game():
    """reset all variable"""
    global player_x, player_y, player_velocity, pipe_x, pipe_height, score, tesla_cars, logo_items, tesla_spawn_timer, background_x, milestone_played
    player_x = 100
    player_y = WINDOW_HEIGHT // 2
    player_velocity = 0
    pipe_x = WINDOW_WIDTH
    pipe_height = random.randint(100, 400)
    score = 0
    tesla_cars = []
    logo_items = []
    tesla_spawn_timer = 0
    background_x = 0
    milestone_played = False
    if background_music:
        background_music.set_volume(0.3)
        background_music.play(-1)

player_size = 30
GRAVITY = 0.4
JUMP = -7
pipe_width = 70
pipe_gap = 150
pipe_speed = 3
tesla_speed = 2
TESLA_SPAWN_RATE = 60
max_score = 10
background_speed = 1

clock = pygame.time.Clock()
game_active = True

while True:
    reset_game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_velocity = JUMP

        player_velocity += GRAVITY
        player_y += player_velocity

        pipe_x -= pipe_speed
        if pipe_x < -pipe_width:
            pipe_x = WINDOW_WIDTH
            pipe_height = random.randint(100, 400)
            score += 1
            if score == 3 and not milestone_played and milestone_sound:
                milestone_sound.play()
                milestone_played = True
            if score >= max_score:
                running = False
                victory = True
                if background_music:
                    background_music.stop()
                if win_sound:
                    win_sound.play()
            else:
                victory = False

        background_x -= background_speed
        if background_x <= -background_img.get_width():
            background_x = 0

        tesla_spawn_timer += 1
        if tesla_spawn_timer >= TESLA_SPAWN_RATE:
            y_pos = random.choice([random.randint(0, 50), random.randint(WINDOW_HEIGHT - 100, WINDOW_HEIGHT - 25)])
            if score < 5:
                choice = random.choice(['tesla', 'twitter_logo'])
                if choice == 'tesla':
                    tesla_cars.append([WINDOW_WIDTH, y_pos])
                elif choice == 'twitter_logo':
                    logo_items.append(['twitter', WINDOW_WIDTH, y_pos])
            else:
                choice = random.choice(['tesla', 'x_logo'])
                if choice == 'tesla':
                    tesla_cars.append([WINDOW_WIDTH, y_pos])
                elif choice == 'x_logo':
                    logo_items.append(['x', WINDOW_WIDTH, y_pos])
            tesla_spawn_timer = 0

        for tesla in tesla_cars[:]:
            tesla[0] -= tesla_speed
            if tesla[0] < -50:
                tesla_cars.remove(tesla)

        for logo in logo_items[:]:
            logo[1] -= tesla_speed
            if logo[1] < -30:
                logo_items.remove(logo)

        player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
        pipe_upper = pygame.Rect(pipe_x, 0, pipe_width, pipe_height)
        pipe_lower = pygame.Rect(pipe_x, pipe_height + pipe_gap, pipe_width, WINDOW_HEIGHT - pipe_height - pipe_gap)

        if player_rect.colliderect(pipe_upper) or player_rect.colliderect(pipe_lower) or player_y < 0 or player_y > WINDOW_HEIGHT:
            running = False
            victory = False
            if background_music:
                background_music.stop()
            if lose_sound:
                lose_sound.play()

        window.blit(background_img, (background_x, 0))
        window.blit(background_img, (background_x + background_img.get_width(), 0))

        progress_width = (score / max_score) * (WINDOW_WIDTH - 50)
        pygame.draw.rect(window, ORANGE_FIRE, (10, 10, progress_width, 20))
        pygame.draw.rect(window, (255, 255, 255), (10, 10, WINDOW_WIDTH - 50, 20), 2)
        if mars_img:
            window.blit(mars_img, (WINDOW_WIDTH - 40, 5))
        else:
            pygame.draw.circle(window, (255, 0, 0), (WINDOW_WIDTH - 25, 15), 15)

        window.blit(player_img, (player_x, player_y))
        window.blit(pipe_img, (pipe_x, pipe_height - pipe_img.get_height()))
        window.blit(pygame.transform.flip(pipe_img, False, True), (pipe_x, pipe_height + pipe_gap))

        for tesla in tesla_cars:
            window.blit(tesla_img, (tesla[0], tesla[1]))
        
        for logo in logo_items:
            if logo[0] == 'x':
                window.blit(x_logo_img, (logo[1], logo[2]))
            elif logo[0] == 'twitter':
                window.blit(twitter_logo_img, (logo[1], logo[2]))

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        window.blit(score_text, (10, 40))

        pygame.display.flip()
        clock.tick(60)

    while not running and game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = True

        if victory:
            if mars_background_img:
                window.blit(mars_background_img, (0, 0))
            else:
                window.fill((139, 69, 19))
            victory_text = font.render("You have reached Mars!", True, (255, 255, 255))
            restart_text = font.render("Press R to restart", True, (255, 255, 255))
            window.blit(victory_text, (WINDOW_WIDTH // 2 - 140, WINDOW_HEIGHT // 2 - 20))
            window.blit(restart_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 20))

            if avatar_img:
                avatar_rect = avatar_img.get_rect()
                avatar_x = WINDOW_WIDTH // 2 - avatar_rect.width // 2
                avatar_y = WINDOW_HEIGHT // 2 + 90
                window.blit(avatar_img, (avatar_x, avatar_y))
                credit_rect = credit_text.get_rect()
                credit_x = WINDOW_WIDTH // 2 - credit_rect.width // 2
                credit_y = avatar_y + avatar_rect.height + 10 
                window.blit(credit_text, (credit_x, credit_y))
        else:
            window.blit(background_img, (0, 0))
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            score_text = font.render(f"Score final: {score}", True, (255, 255, 255))
            restart_text = font.render("Press R to restart", True, (255, 255, 255))
            window.blit(game_over_text, (WINDOW_WIDTH // 2 - 70, WINDOW_HEIGHT // 2 - 50))
            window.blit(score_text, (WINDOW_WIDTH // 2 - 80, WINDOW_HEIGHT // 2))
            window.blit(restart_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 + 50))
            if avatar_img:
                avatar_rect = avatar_img.get_rect()
                avatar_x = WINDOW_WIDTH // 2 - avatar_rect.width // 2
                avatar_y = WINDOW_HEIGHT // 2 + 90
                window.blit(avatar_img, (avatar_x, avatar_y))
                credit_rect = credit_text.get_rect()
                credit_x = WINDOW_WIDTH // 2 - credit_rect.width // 2
                credit_y = avatar_y + avatar_rect.height + 10
                window.blit(credit_text, (credit_x, credit_y))

        pygame.display.flip()
        clock.tick(60)

    if not game_active:
        break

print(f"Game closed ! Last score : {score}")
pygame.quit()