import pygame
import random
pygame.init()

screen_width = 900
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("firstGAME")
pygame.display.update()
clock = pygame.time.Clock() 
font= pygame.font.SysFont(None, 45)

# display score
def text_score(text, color,x,y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, (x,y))

def plot_snake(gameWindow,color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color, [x, y, snake_size, snake_size])    #snake drawing
def welcome_screen():
    exit_game = False
    while not exit_game:
        gameWindow.fill((255,255,255))
        text_score("WELCOME TO SNAKES",(0,0,0),260,250)
        text_score("Press SPACE to play",(0,0,0),260,270)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            pygame.display.update()
            clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    init_velocity = 2
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 10
    food_x = random.randint(20, screen_width/1.5)
    food_y = random.randint(20, screen_height/1.5)
    food_size = 10
    fps = 60
    score = 0
    snake_list = []
    snake_length = 1

    with open ("high_score.txt","r") as f:
        high_score = f.read()

    while not exit_game:
        if game_over:
            with open ("high_score.txt","w") as f:
                f.write(str(high_score))
            gameWindow.fill((0,0,0))
            text_score("GAME OVER! PRESS ENTER TO CONTINUE !!!", (255,0,0),100,300)
            for event in pygame.event.get():   #what mouse is doing, that event is handled
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():   #what mouse is doing, that event is handled
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            # cheatcode
            # if event.key == pygame.K_q:
            #     score += 10

            if abs(snake_x-food_x)<6 and abs(snake_y - food_y)<6:
                score += 10
                food_x = random.randint(20, screen_width/1.5)
                food_y = random.randint(20, screen_height/1.5)
                snake_length += 5
                if score>int(high_score):
                    high_score = score

            gameWindow.fill((0,255,0))
            pygame.draw.rect(gameWindow,(0,0,0), [food_x, food_y, food_size, food_size])    #food drawing
            text_score("Score: "+ str(score) + "   High-Score: "+ str(high_score),(98,56,58),5,5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:         #snake khudse nhi takrana chahiye
                game_over = True
            if snake_x <0 or snake_x > screen_width or snake_y<0 or snake_y> screen_height:   #snake screen se bahar nhi jana chahiye
                game_over = True

        plot_snake(gameWindow, (255,0,0),snake_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome_screen()
gameloop()