import pygame
import math
def main():
    time2 = 0
    pygame.init()
    # set up the screen
    screen = pygame.display.set_mode([800, 450])
    background = pygame.image.load('book.jpg')
    # top bar
    pygame.display.set_caption('Mr.Kayler vs. Mr.Lanahan')
    icon = pygame.image.load('globe.jpg')
    pygame.display.set_icon(icon)

    # player
    playerImg = pygame.image.load('kayler.jpg')
    playerx = 370
    playery = 350
    playerx_change = 0
    playery_change = 0

    # player2
    player2Img = pygame.image.load('lanahan.jpg')
    player2x = 570
    player2y = 350
    player2x__change = 0
    player2y_change = 0

    #bullet2
    bullet2Img = pygame.image.load('globe.jpg')
    bullet2x = 0
    bullet2y = 0
    bullet2x_change = -1
    bullet2y_change = 0
    bullet2_state = "ready"
    # bullet
    # ready - you can't see the bullet on the screen
    # fire - the bullet is currently moving
    bulletImg = pygame.image.load('book1.jpg')
    bulletx = 0
    bullety = 0
    bulletx_change = 1
    bullety_change = 0
    bullet_state = "ready"
    #game over text
    over_font = pygame.font.Font('elvish ring nfi.ttf' , 64)
    lives = 10
    lives2 = 10
    lives_font = pygame.font.Font('Triforce.ttf' , 18)
    lives2_font = pygame.font.Font('Triforce.ttf' , 18)
    # score
    font = pygame.font.Font('Triforce.ttf', 32)

    pygame.mixer.music.load('songofthesouth.mp3')
    pygame.mixer.music.play(-1)

    def game_over_text():
        over_text = over_font.render("GAME OVER", True, (0, 0,255))
        screen.blit(over_text, (200, 225))

    def lives_text(x,y):
        live_text = lives_font.render("lives: " + str(lives), True, (0,240,255))
        screen.blit(live_text, (x, y))
        
    def lives_text2(x,y):
        live2_text = lives2_font.render("lives: " + str(lives2), True, (0,240,255))
        screen.blit(live2_text, (x,y))
            
    def player(x, y):
        screen.blit(playerImg, (x, y))


    def player2(x, y,):
        screen.blit(player2Img, (x, y))

    def fire_bullet(x, y):
        global bullet_state
        bullet_state = "fire"
        screen.blit(bulletImg, (x + 20, y + 10))

    def fire_bullet2(x, y):
        global bullet2_state
        bullet2_state = "fire"
        screen.blit(bullet2Img, (x - 20, y - 10))


    def isCollision(player2x, player2y, bulletx, bullety): 
        distance = math.sqrt((math.pow(player2x - bulletx, 2)) + (math.pow(player2y - bullety, 2)))
        if distance < 50:
            return True
        else:
            return False

    run = True
    t0 = pygame.time.get_ticks()
    # game loop
    while run:
        # backgrounhd image
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # key pressed if statement
            if event.type == pygame.KEYDOWN and lives > 0 and lives2 > 0:
                
                #move kayler left
                if event.key == pygame.K_LEFT:
                    playerx_change = -0.5
                #move kayler right
                if event.key == pygame.K_RIGHT:
                    playerx_change = 0.5
                #throw book
                if event.key == pygame.K_SPACE:
                    if bullet_state is "ready":
                        # get the current x cordnate of player
                        bullety = playery
                        bulletx = playerx
                        bullet_state = "fire"
                #move kayler up
                if event.key == pygame.K_UP:
                    playery_change = -0.5
                # move kayler down
                if event.key == pygame.K_DOWN:
                    playery_change = 0.5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN:
                    playerx_change = 0
                    playery_change = 0
                 
            if event.type == pygame.KEYDOWN and lives > 0 and lives2 > 0:
            # lanahan left            
                if event.key == pygame.K_a:
                    player2x__change = -0.5
                #lanahan right
                if event.key == pygame.K_d:
                    player2x__change = 0.5
                if event.key == pygame.K_TAB:
                    if bullet2_state is "ready":
                        bullet2x = player2x
                        bullet2y = player2y
                        bullet2_state = "fire"
                    #lanahan up
                if event.key == pygame.K_w:
                    player2y_change = -0.5
                    # lananhan down
                if event.key == pygame.K_s:
                    player2y_change = 0.5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or pygame.K_w:
                    player2x__change = 0
                    player2y_change = 0
                    

                            
     # kayler movement
        playery += playery_change
        playerx += playerx_change
        if playerx <= 0:
            playerx = 0
        elif playerx >= 700:
            playerx = 700
        if playery <= 0:
            playery = 0
        elif playery >=350:
            playery = 350
    # lanahan movement
        player2y += player2y_change
        player2x += player2x__change
        
        if player2x <= 0:
            player2x = 0
        elif player2x >= 700:
            player2x = 700
        if player2y <= 0:
            player2y = 0
        elif player2y >=350:
            player2y = 350
            
        # bullet movement
        if bulletx <= 0 or bulletx >= 800:
            bullety = playery
            bulletx = playerx
            bullet_state = "ready"
        if bullety <= 0 or bullety >= 450:
            bullety = playery
            bulletx = playerx
            bullet_state = "ready"
        if bullet_state is "fire":
            fire_bullet(bulletx, bullety)
            if  player2x < playerx:
                bulletx -= bulletx_change
            elif player2x > playerx:
                bulletx += bulletx_change
            if player2y < playery:
                bullety -= 0.3
            elif player2y > playery:
                bullety += 0.3

        # bullet2 movement
        if bullet2x <= 0 or bullet2x >= 800:
            bullet2y = player2y
            bullet2x = player2x
            bullet2_state = "ready"
        if bullet2y <= 0 or bullet2y >= 450:
            bullet2y = player2y
            bullet2x = player2x
            bullet2_state = "ready"
        if bullet2_state is "fire":
            fire_bullet2(bullet2x, bullet2y)
            if  player2x > playerx:
                bullet2x += bullet2x_change
            elif player2x < playerx:
                bullet2x -= bullet2x_change
            if player2y > playery:
                bullet2y -= 0.3
            elif player2y < playery:
                bullet2y += 0.3

        # players collide
        collision4 = isCollision(player2x,player2y,playerx,playery)        
        if collision4:
            lives -= 1
            lives2 -= 1
            playerx = 370
            playery = 350
            player2x = 570
            player2y = 350
                
        # bullet hits player 2
        collision = isCollision(player2x, player2y, bulletx, bullety)
        if collision:
            bullety = -1
            bulletx = -1
            bullet_state = "ready"
            lives -= 1
            pass
            #bullet2 hits player 
        collision2 = isCollision(playerx, playery, bullet2x, bullet2y)
        if collision2:
            bullet2y = -1
            bullet2_state = "ready"
            lives2 -= 1
            
        collision3 = isCollision(bullet2x, bullet2y, bulletx, bullety)
        if collision3:
            bullet2_state = "ready"
            bullet_state = "ready"
            bullety = playery
            bulletx = playerx
            bullet2x = player2x
            bullet2y = player2y
            



            # keep players from moving when game over
            if event.type == pygame.KEYDOWN:
                player2x__change = 0
                player2y_change = 0
                playerx_change = 0
                playery_change = 0
        time2 = pygame.time.get_ticks()
        score = font.render("SCORE = " + str(time2-t0) , True, (0,0,255))
        screen.blit(score, (10, 10))
        
        # literal easter egg
        if time2 > 191000:
            egg = pygame.image.load('egg.jpg')
            screen.blit(egg, (400, 225))
        #game over
        if lives <= 0 or lives2 <= 0:
            pygame.mixer.music.stop()
            bullet_state = "stop"
            bullet2_state = "stop"
            pygame.mixer.music.load('borncountry.mp3')
            pygame.mixer.music.play(-1)        
            break
        
        #show score and lives on screen
        lives_text(500, 100)
        player(playerx, playery)
        player2(player2x, player2y)
        lives_text2(100, 100)
        pygame.display.update()

    restartimg = pygame.image.load('newgame.png')
    restartx = 10
    restarty = 10

    def restart(restartx, restarty):
        t0 = pygame.time.get_ticks()
        screen.blit(restartimg, (restartx, restarty))

    button_min_X = 700
    button_max_X = 800
    running = True

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if pygame.mouse.get_pressed() == (1,0,0) and pygame.mouse.get_pos()[0] >= button_min_X and pygame.mouse.get_pos()[0] <= button_max_X and pygame.mouse.get_pos()[1] <= 30 and pygame.mouse.get_pos()[1] >= 10:
                main()
            if event.type == pygame.QUIT:
                running = False
        if lives <= 0 or lives2 <=0:
            game_over_text()
            score = font.render("SCORE = " + str(time2-t0) , True, (255,255,255))
            screen.blit(score, (10, 10))
            restart(700, 10)                 
        else:
            break
        pygame.display.update()
main()
