import pygame,sys

#general setup
pygame.init()
Clock = pygame.time.Clock()


#Setting up main window
screen_width = 1280
screen_height = 960

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong_By_Akshit')

#Game Rectangles
Ball = pygame.Rect(screen_width/2 - 15,screen_height/2 - 15,30,30)
Player = pygame.Rect(screen_width - 20,screen_height/2 - 20,10,140)
Opponent = pygame.Rect(10,screen_height/2-70,10,140)

bg_color = pygame.Color('grey12')
pink = (255, 192, 203)

# Score and game state
player_score = 0
opponent_score = 0
player_lives = 3
game_state = "menu"  # "menu", "playing", "game_over"
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)


ball_speed_x = 7
ball_speed_y = 7

# Movement speeds
player_speed = 7
opponent_speed = 5

while True:
    for evt in pygame.event.get(): #checks all input from user , har click of key and touch by mouse ko check karta hai 
        if(evt.type==pygame.QUIT): # if user clicks on the cross button.
            pygame.quit()
            sys.exit()
        
        # Menu controls
        if (game_state == "menu" and evt.type == pygame.KEYDOWN):
            if (evt.key == pygame.K_SPACE):
                game_state = "playing"
                player_score = 0
                opponent_score = 0
                player_lives = 3
                Ball.center = (screen_width/2, screen_height/2)
        

        if(game_state == "game_over" and evt.type == pygame.KEYDOWN):
            if (evt.key == pygame.K_r):
                game_state = "menu"
    
    if (game_state == "playing"):

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] and Player.top > 0):
            Player.y -= player_speed
        if (keys[pygame.K_s] and Player.bottom < screen_height):
            Player.y += player_speed
        
        # Opponent ka movement

        if (Opponent.centery < Ball.centery and Opponent.bottom < screen_height):
            Opponent.y += opponent_speed
        elif (Opponent.centery > Ball.centery and Opponent.top > 0):
            Opponent.y -= opponent_speed
        
        Ball.x += ball_speed_x
        Ball.y += ball_speed_y
        
        if(Ball.top<=0 or Ball.bottom>=screen_height):
            ball_speed_y *= -1
        
        # Score when ball goes off screen
        if Ball.left <= 0:
            player_score += 1
            Ball.center = (screen_width/2, screen_height/2)
            ball_speed_x = abs(ball_speed_x)  # Ball goes right
        
        if Ball.right >= screen_width:
            opponent_score += 1
            player_lives -= 1
            Ball.center = (screen_width/2, screen_height/2)
            ball_speed_x = -abs(ball_speed_x)  # Ball goes left
            
            if player_lives <= 0:
                game_state = "game_over"
        
        if(Ball.colliderect(Player) or Ball.colliderect(Opponent)):
            ball_speed_x *= -1
    
    
    #Visuals
    screen.fill(bg_color)
    
    if game_state == "menu":
        # Menu screen of game 
        title_text = font.render("PONG BY AKSHIT", True, pink)
        play_text = small_font.render("Press SPACE to Play", True, pink)
        screen.blit(title_text, (screen_width/2 - title_text.get_width()/2, screen_height/2 - 100))
        screen.blit(play_text, (screen_width/2 - play_text.get_width()/2, screen_height/2))
    
    elif game_state == "playing":

        pygame.draw.rect(screen,pink,Player)
        pygame.draw.rect(screen,pink,Opponent)
        pygame.draw.ellipse(screen,pink,Ball)
        pygame.draw.aaline(screen,pink,(screen_width/2,0),(screen_width/2,screen_height))
        
        # Scores
        player_text = font.render(str(player_score), True, pink)
        opponent_text = font.render(str(opponent_score), True, pink)
        lives_text = small_font.render(f"Lives: {player_lives}", True, pink)
        
        screen.blit(player_text, (3*screen_width/4, 50))
        screen.blit(opponent_text, (screen_width/4, 50))
        screen.blit(lives_text, (50, 50))
    
    elif game_state == "game_over":

        game_over_text = font.render("GAME OVER!", True, pink)
        final_score = small_font.render(f"Final Score - You: {player_score}  Computer: {opponent_score}", True, pink)
        restart_text = small_font.render("Press R to restart", True, pink)
        
        screen.blit(game_over_text, (screen_width/2 - game_over_text.get_width()/2, screen_height/2 - 100))
        screen.blit(final_score, (screen_width/2 - final_score.get_width()/2, screen_height/2))
        screen.blit(restart_text, (screen_width/2 - restart_text.get_width()/2, screen_height/2 + 50))




    pygame.display.flip() #updating window ke liye
    Clock.tick(60)
