import pygame 
import random 
from sys import exit 
import button
# My imports above
pygame.init()
#initialise all pygame module
starting_bool = True
menu_bool = False
option_bool = False


# 'option' variables 
text_speed = 2
battle_animation = 1
battle_style = 1


## this is the function which shows the starting screen for the user, it also is the bridge between the starting screen & the menu
def starting_screen():
    global starting_bool
    global menu_bool
    if starting_bool == True:
        # adding the images to the title screen 
        screen.fill('white')
        screen.blit(red_start_resize,red_start_rect)
        screen.blit(charmander_start_resize,charmander_start_rect)
        screen.blit(title_resize, title_rect)
        screen.blit(text_start, text_start_rect)
        
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            starting_bool = False
            menu_bool = True
    
## this is the function which shows the the menu for the game. it's the bridge between settings, continue, and newgame
def menu_screen():
    global menu_bool
    global option_bool
    # loading continue text 
    continue_text = poke_font.render('Continue',False,'Black')
    continue_text_but = button.Button(90,160,continue_text,1)
    # loading new game text
    newGame_text = poke_font.render('New Game',False,'Black')
    newGame_text_but = button.Button(90,210,newGame_text,1)
    
    # loading option text
    option_text = poke_font.render('Options',False,'Black')
    option_text_but = button.Button(90,260,option_text,1)
    
    # loading the text box for the user to see text
    text_box_resize = pygame.transform.scale(text_box,(400,250))
    text_box_rect = text_box_resize.get_rect(topleft = (50,100))
    ## loading arrows for menu
  
    # adding images to menu screen
    if menu_bool == True:
        screen.fill('white')
        
        screen.blit(text_box_resize,text_box_rect)
       #clicking continue
        if continue_text_but.draw(screen):
            print('continue')
        #clicking new game
        if newGame_text_but.draw(screen):
            print('new game')
            
        #clicking option
        if option_text_but.draw(screen):
            option_bool = True 
            menu_bool = False
        

def option_screen():
    global option_bool
    global menu_bool
    
    global text_speed
    global battle_animation
    global battle_style
    
    #text box for option screen
    text_box_resize = pygame.transform.scale(text_box,(400,150))
    text_box_rect_top = text_box_resize.get_rect(topleft = (50,10))
    text_box_rect_mid = text_box_resize.get_rect(topleft = (50,150))
    text_box_rect_bot = text_box_resize.get_rect(topleft = (50,300))
    
    #coordinates of preset options 
    box_one_x,box_one_y = 200,100
    box_two_x,box_two_y = 150,240
    box_three_x,box_three_y = 150,380
    ##underline when an option is clicked and set.
    # underline_box1 = pygame.draw.rect(screen,'Black',(box_one_x,box_one_y,100,100))
    # underline_box2 = pygame.draw.rect(screen,'Black',(box_two_x,box_two_y,100,100))
    # underline_box3 = pygame.draw.rect(screen,'Black',(box_three_x,box_three_y,100,100))
    
    
    #text for first box - 'Text Speed'
    head_text_speed = poke_font.render('Text Speed',False,'Black')
    head_text_speed_rect = head_text_speed.get_rect(center = (250,70))
                    #1st button - TS
    sub_fast_text = poke_font.render('FAST',False,"Black")
    sub_fast_text_but = button.Button(100,100,sub_fast_text,1)
                    #2nd button - TS
    sub_medium_text = poke_font.render('MEDIUM',False,"Black")
    sub_medium_text_but = button.Button(200,100,sub_medium_text,1)
                    #3rd button - TS
    sub_slow_text = poke_font.render('SLOW',False,"Black")
    sub_slow_text_but = button.Button(320,100,sub_slow_text,1)
    
    #text for second box - 'Battle animation'
    head_battle_animation = poke_font.render('Battle Animation',False,'Black')
    head_battle_animation_rect = head_battle_animation.get_rect(center = (250,210))
    
                    #1st button - BT
    sub_on_animation = poke_font.render('ON',False,"Black")
    sub_on_animation_but = button.Button(150,240,sub_on_animation,1)
                    #2nd button - BT
    sub_off_animation = poke_font.render('OFF',False,'Black')
    sub_off_animation_but = button.Button(300,240,sub_off_animation,1)
    
    
    #text for third box - 'Battle Style'shit
    head_battle_style = poke_font.render('Battle Style',False,'Black')
    head_battle_style_rect = head_battle_style.get_rect(center = (250,350))
    
    sub_shift_style = poke_font.render('SHIFT',False,'Black')
    sub_shift_style_but = button.Button(150,380,sub_shift_style,1)
    
    sub_set_style = poke_font.render('SET',False,'Black')
    sub_set_style_but = button.Button(300,380,sub_set_style,1)
    
    
    #Exit button 
    exit_text = poke_font.render('EXIT',False,"Black")
    exit_text_but = button.Button(400,450,exit_text,1)
    
    
    
    if option_bool == True:
        screen.fill('white')
        #drawing text boxes
        screen.blit(text_box_resize,text_box_rect_top)
        screen.blit(text_box_resize,text_box_rect_mid)
        screen.blit(text_box_resize,text_box_rect_bot)
        
        #drawing top text
        screen.blit(head_text_speed,head_text_speed_rect)
        if sub_fast_text_but.draw(screen):  ## when clicked causes text_speed to be fast
            text_speed = 1
            box_one_x,box_one_y = 100,100
            underline_box1 = pygame.draw.rect(screen,'Black',(box_one_x,box_one_y,100,100),width = 1)
            
        if sub_medium_text_but.draw(screen):## when clicked causes text_speed to be noarmal
            text_speed = 2
            box_one_x,box_one_y = 200,100
            underline_box1 = pygame.draw.rect(screen,'Black',(box_one_x,box_one_y,100,100),width = 1)
            
        if sub_slow_text_but.draw(screen):## when clicked causes text_speed to be slow
            text_speed = 3
            box_one_x,box_one_y = 320,100
            underline_box1 = pygame.draw.rect(screen,'Black',(box_one_x,box_one_y,100,100),width = 1)
            
        
        
        #drawing middle text
        screen.blit(head_battle_animation,head_battle_animation_rect)
        if sub_on_animation_but.draw(screen):## when clicked causes battle_animation to be on
            battle_animation = 1
        if sub_off_animation_but.draw(screen):## when clicked causes battle_animation to be off
            battle_animation = 2
        
        #drawing bottom text
        screen.blit(head_battle_style,head_battle_style_rect)
        if sub_shift_style_but.draw(screen):## when clicked causes battle_style to be set to shift
            battle_style = 1
        if sub_set_style_but.draw(screen):## when clicked causes battle_style to be set to 'set'
            battle_style = 2
        
    
        #drawing exit button
        if exit_text_but.draw(screen):
            menu_bool = True
            option_bool = False

WIDTH = 500
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH,HEIGHT))
# setting screen for the user 
pygame.display.set_caption('Pokemon')
# game name 
clock = pygame.time.Clock()
# setting the users FPS 
running = True
poke_font = pygame.font.Font('Assests/small assests/Pixeltype.ttf', 50)
# font for game 


# loading red front cover 
red_start = pygame.image.load('Assests/title screen/front character sprite.PNG')
red_start_resize= pygame.transform.scale_by(red_start, 0.25)
red_start_rect = red_start_resize.get_rect(center =  (200,300))

# loading text for front cover
text_start = poke_font.render('Press any key to start' ,False, 'Black')
text_start_rect = text_start.get_rect(center = (250,400))


# loading red front cover 
charmander_start = pygame.image.load('Assests/title screen/charmander title screen.png')
charmander_start_resize = pygame.transform.scale_by(charmander_start, 0.07)
charmander_start_rect = charmander_start_resize.get_rect(center =(300,320))

# loading title front cover 
title = pygame.image.load('Assests/title screen/chart.png')
title_resize = pygame.transform.scale_by(title, 0.3)
title_rect = title_resize.get_rect(center =(250,100))
# loading in characters for starting screen and recting them

## loading images for menu 
text_box = pygame.image.load('Assests/small assests/text-box.png')
## loading arrows for buttons 
arrow = pygame.image.load('Assests/small assests/arrow.png')


### the while loop ###
while running:
    # event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    starting_screen()
    
    menu_screen()
    
    option_screen()
        

        
        # screen.blit(title,title_rect)
    
    
                
            # closing the window
    clock.tick(60) # setting the FPS
    pygame.display.update() # updating the screen


