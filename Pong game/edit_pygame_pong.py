import pygame, sys
import random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    
    ball.x += ball_speed_x        
    ball.y += ball_speed_y        

    if ball.top <= 50 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    
    # player score    
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        score_time = pygame.time.get_ticks()
        player_score += 1
    
    # opponent score    
    if ball.right >= screen_width:  
        pygame.mixer.Sound.play(score_sound)
        score_time = pygame.time.get_ticks()
        opponent_score += 1

    if ball.colliderect(player) and ball_speed_x > 0  : 
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left)< 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1    
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        
    if ball.colliderect(opponent) and ball_speed_x < 0: 
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right)< 10:
            ball_speed_x *= -1  
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1          
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1      
        
def player_animation():
    player.y += player_speed     
    if player.top <= 50:
        player.top = 50  
    if player.bottom >= screen_height:
        player.bottom = screen_height         
        
'''def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0  
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height'''
        
def opponent_animation():  
    opponent.y += opponent_speed     
    if opponent.top <= 50:
        opponent.top = 50  
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height  
        
            
def ball_start():
    global ball_speed_x, ball_speed_y,score_time,number_three, number_two, number_one
    
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2, screen_height/2) 
    
    if current_time - score_time < 700:
        number_three = game_font.render("3",False,red)
        screen.blit(number_three, (screen_width/2 - 10, screen_height/2 + 20))
        
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2",False,red)
        screen.blit(number_two, (screen_width/2 - 10, screen_height/2 + 20))
        
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1",False,red)
        screen.blit(number_one, (screen_width/2 - 10, screen_height/2 + 20))
    
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
        
    else:      
        ball_speed_y = 7 * random.choice((1, -1))  
        ball_speed_x = 7 * random.choice((1, -1))  
        score_time = None
           

#General setup
pygame.mixer.pre_init(44100, -16,2,492)
pygame.init()
clock = pygame.time.Clock()

#Setting up the main window
screen_width = 1000
screen_height = 680
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('THE PONG GAME')

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15 , screen_height/2 - 15 ,30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height/2 - 70,10, 140)

red = (190,100,40)
bg_color = (50, 25, 50)
grey = (250, 250, 250)
light_grey = pygame.Color('grey12')

# Game Variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 0
ball_moving = False
score_time = True

# Score Text
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 36)

#Sound
pong_sound = pygame.mixer.Sound("pong.og.mp3") 
score_sound = pygame.mixer.Sound("score.og.mp3") 


# score Timer
score_time = True

while True:
    #Handlinng input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                opponent_speed += 7
            if event.key == pygame.K_w:
                opponent_speed -= 7
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                opponent_speed -= 7
            if event.key == pygame.K_w:
                opponent_speed += 7    
        
                  
    
    ball_animation() 
    player_animation()
    '''opponent_ai()'''
    opponent_animation()
                    
    #Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen,red, player)
    pygame.draw.rect(screen,red, opponent)
    pygame.draw.ellipse(screen,red, ball)
    pygame.draw.aaline(screen, red, (screen_width/2,0), (screen_width/2, screen_height))
    pygame.draw.line(screen, red, (0, 50),(screen_width, 50))

    
    if score_time:
        ball_start()
        
    player_text = game_font.render(f"{player_score}", False, grey)
    screen.blit(player_text,(750, 10))
    
    player_text = game_font.render("PLAYER  : ", True, grey)
    screen.blit(player_text,(540, 10))
    
    opponent_text = game_font.render(f"{opponent_score}", False, grey)
    screen.blit(opponent_text,(320,10))
    
    player_text = game_font.render("OPPONENT : ", True, grey)
    screen.blit(player_text,(50, 10))
    
    win_score = 10
    
    if player_score == win_score and opponent_score < win_score :
        screen.fill(light_grey)
        ball = pygame.Rect(screen_width/2 - 15 , screen_height/2 - 15 ,30,30)
        player_text = game_font.render("PLAYER WIN THE MATCH ", True, red)
        screen.blit(player_text,(250, 300))
        ball_speed = 0
        player_speed = False
        opponent_speed = False
        
        
    elif player_score < win_score and opponent_score == win_score :  
        screen.fill(light_grey)
        ball = pygame.Rect(screen_width/2 - 15 , screen_height/2 - 15 ,30,30)
        player_text = game_font.render("OPPONENT WIN THE MATCH ", True, red)
        screen.blit(player_text,(240, 300))
        ball_speed = 0
        opponent_speed = False
        player_speed = False
    

    # Updating the window   
    pygame.display.flip()     
    clock.tick(60)