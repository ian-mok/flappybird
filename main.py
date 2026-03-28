import pygame
import random

pygame.init()

WIDTH, HEIGHT = 864,936
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flappy bird")

clock = pygame.time.Clock()
running = True
background_image = pygame.image.load('bg.png')
ground_image = pygame.image.load("ground.png")
pipe_img = pygame.image.load("pipe.png")
# Global score so show_score() can read it
restart_img = pygame.image.load("restart.png")
score = 0
ground_scroll = 0
scroll_speed = 4
gravity = 0.5
bird_velocity = 0
ground_y = 768
bird_frame_index = 0
animation_counter = 0
game_over = False

def restart_game():
    global score, game_over, pipe_pairs, bird_velocity
    score = 0
    game_over = False
    pipe_pairs.clear()
    bird_rect.center = (100, int (HEIGHT / 2))
    bird_velocity = 0


def show_game_over():
    font = pygame.font.SysFont('arial', 100)

    surface = font.render("YOU DIED :(", True, pygame.Color(255, 0, 0))
    rect = surface.get_rect()
    rect.midtop = (WIDTH // 2, HEIGHT // 3)
    screen.blit(surface, rect)
    screen.blit(restart_img, (350, 450))
    pygame.display.flip()





bird_frames=[]
for num in range(1,4):
    bird_frames.append(pygame.image.load(f"bird{num}.png").convert_alpha())
bird_rect = bird_frames[0].get_rect(center=(100, int(HEIGHT /2)))
pipe_pairs = {}
pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency


def show_score():
    # Use the global score variable
    font = pygame.font.SysFont('arial', 50)
    surface = font.render("score: " + str(score), True, pygame.Color(0, 0, 0))
    rect = surface.get_rect()
    rect.midtop = (100, 100)
    screen.blit(surface, rect)

def play_mp3_simple(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print("playing... Press Ctrl+C to stop")


while running:
  # Update display
    screen.blit(background_image,(0,0))
    screen.blit(ground_image,(ground_scroll,768))


    if game_over:
        show_game_over()


    else:
        ground_scroll -= scroll_speed
        if ground_scroll < -35:
            ground_scroll = 0
        bird_velocity += gravity
        bird_velocity = min(bird_velocity, 8)
        bird_rect.y += int(bird_velocity)
        animation_counter = animation_counter + 1
        if animation_counter > 10:
            animation_counter = 0
            bird_frame_index = bird_frame_index + 1
        if  bird_frame_index > 2:
            bird_frame_index = 0

        rotated_bird = pygame.transform.rotate(bird_frames[bird_frame_index],-bird_velocity * 2)
        screen.blit(rotated_bird,bird_rect)
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(200,400)
            btm_pipe = pipe_img.get_rect(midtop=(WIDTH, pipe_height + pipe_gap // 2))
            top_pipe = pipe_img.get_rect(midbottom=(WIDTH, pipe_height - pipe_gap // 2))
            pipe_pairs[time_now] = (btm_pipe,top_pipe,False)
            last_pipe = time_now

        for spawn_time in list(pipe_pairs.keys()):
            btm_pipe, top_pipe , scored = pipe_pairs[spawn_time]

            btm_pipe.x -= scroll_speed
            top_pipe.x -= scroll_speed
            screen.blit(pipe_img,btm_pipe)


            flipped_pipe = pygame.transform.flip(pipe_img,False,True)
            screen.blit(flipped_pipe, top_pipe)

            if not scored and btm_pipe.right < bird_rect.left:
                score += 1
                pipe_pairs[spawn_time] = (btm_pipe, top_pipe, True)
            if btm_pipe.right <0:
               del pipe_pairs[spawn_time]



        if bird_rect.y >= ground_y or bird_rect.y <= 0:
           game_over = True



        for pipe in pipe_pairs:
            btm_pipe, top_pipe, _= pipe_pairs[pipe]
            if bird_rect.colliderect(btm_pipe) or bird_rect.colliderect(top_pipe):

                game_over = True

                #Pipe collision
        show_score()






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if game_over:
                if 350 < (pos[0]) < 470 and 450 < (pos[1]) < 470:
                    restart_game()




        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_mp3_simple('jump.mp3')
                bird_velocity = -8

    pygame.display.update()
    # Limit FPS
    clock.tick(60)


