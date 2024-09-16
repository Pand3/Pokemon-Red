import pygame
import sys
import button 

# Initialize Pygame
pygame.init()

## game states 
name_state = True 
pokemon_state = False
pokemon_choice = None 

# Constants
WIDTH, HEIGHT = 500, 500
FONT_SIZE = 50
MAX_NAME_LENGTH = 8
CHARACTER_WIDTH = 40  # Width of each character box
CHARACTER_HEIGHT = 60  # Height of each character box
SPACE_BETWEEN_CHARACTERS = 10  # Space between characters
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOX_X = 5
BOX_Y = 280
# poke_font = pygame.font.Font('Assests/small assests/Pixeltype.ttf', 50)
player_pokemon = None

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon")
clock = pygame.time.Clock()

# Initialize font
poke_font = pygame.font.Font('Assests/small assests/Pixeltype.ttf', 50)
poke_font_sizedown = pygame.font.Font('Assests/small assests/Pixeltype.ttf', 30)
text = ""

pokemon_starter_bool = {'Charmander': False, 'Squirtle': False, 'Bulbasaur': False}
        




    
    

# def speech(text, x, y): ##x and y will be the coordinates of the text
#     comment = poke_font.render(text,False,BLACK) ##saves text to a variable making it black as well
#     comment_rect = comment.get_rect(center = (x,y)) #moves the center of the text to the chosen coordinates 
#     screen.blit(comment,comment_rect) ##text is now shown on the screen using the blit function
def speech(text, x, y, size): ##x and y will be the coordinates of the text
    font = pygame.font.Font('Assests/small assests/Pixeltype.ttf',size)
    comment = font.render(str(text),False,BLACK) ##saves text to a variable making it black as well
    comment_rect = comment.get_rect(center = (x,y)) #moves the center of the text to the chosen coordinates 
    screen.blit(comment,comment_rect) ##text is now shown on the screen using the blit function


def back():
    back_text = poke_font.render('BACK',False,"Black") 
    back_text_but = button.Button(400,450,back_text,1) ##back button is made to allow player to go back to change name 
    return back_text_but.draw(screen)

def load_and_resize(image_path, size):
    image = pygame.image.load(image_path)
    return pygame.transform.scale_by(image, size)

    
                        #name   #poke img  coordinates
def starter_pick_button(poke_name, poke_img, x, y, scale):
    global pokemon_state ## this is to change the value of pokemon state to false once player picks starter 
    global pokemon_starter_bool
    
    pokemon_image = pygame.image.load(poke_img) ## loads the image of the pokemon
    poke_button = button.Button(x,y,pokemon_image, scale) ##makes the image of the pokemon a button
    poke_text = poke_font.render(poke_name,False,BLACK) ##saves text to a variable making it black as well
    poke_text_rect = poke_text.get_rect(midbottom = (x + 10, y - 10)) #moves text ontop of the image  
    
    
    if pokemon_state and name_state == False: ## checks if in correct state 
        screen.blit(poke_text,poke_text_rect) ## paste the text onto the screen
        if poke_button.draw(screen): ## draws pokemon as well as returning a boolean value 
            pokemon_starter_bool[poke_name] = True
            pokemon_state = False
            
class Pokemon:
    def __init__(self, pokemon, pokemon_pic, name, type, lvl, HP, atk, defence, spec_atk, spec_defence, speed):
        self.pokemon = pokemon  ## what pokemon it is 
        self.pokemon_pic = pokemon_pic ## the image of the pokemon, file location
        self.name = name  ##name set to pokemon specie, changed if user wants to 
        self.type = type  ## e.g. fire type, water type etc. 
        self.lvl = lvl ##what level the pokemon is 
        self.HP = HP ##its health points 
        self.atk = atk  ## its normal attack e.g. its elemental attacks 
        self.defence = defence ## its normal defence 
        self.spec_atk = spec_atk ## its speacial attack e.g. its elemental attacks 
        self.spec_defence = spec_defence ## its special attack
        self.speed = speed ## how fast the pokemon is, determine if first move or no 
        
    def text_box(self, box_width, box_height, box_x, box_y):  ## function places down text boxes 
        ## text box 
        text_box = pygame.image.load('Assests/small assests/text-box.png') ##loads text box img from files
        text_box_resize = pygame.transform.scale(text_box, (box_width,box_height)) ##resizes to whatever I need it to be 
        text_box_rect = text_box_resize.get_rect(topleft = (box_x, box_y)) ## placing the img 
        screen.blit(text_box_resize,text_box_rect) ##pasting img onto the screen
        
    def pokemon_img(self, scale_by, x, y):
        pokemon_img = pygame.image.load(self.pokemon_pic)  ## loads img of the pokemon
        pokemon_img_resize = pygame.transform.scale_by(pokemon_img, scale_by) ## change size of pokemon
        pokemon_img_rect = pokemon_img_resize.get_rect(center = (x, y)) ## positions the pokemon 
        screen.blit(pokemon_img_resize, pokemon_img_rect) ## pasting img on the screen
        
    def stats(self):  ## lvl , type, HP, ATK, DEF, SPEC ATCK, SPEC DEF, SPEED, this will show the stats of the pokemon
        lvl_text = f"lVl:{self.lvl}" ###
        type_text = f'Type:{self.type}' 
        HP_text = f'HP:{self.HP}'
        ATK_text = f'ATK:{self.atk}'
        DEF_text = f'DEF:{self.defence}'
        SPEC_ATK_text = f'SPE ATK:{self.spec_atk}'
        SPEC_DEF_text = f'SPE DEF:{self.spec_defence}'
        speed_text = f'Speed:{self.speed}'
        TEXT_SIZE = 50
        
        ## I made these all into f strings to allow my variables to be displayed
        ## this is placing these stats down into the text box 
        speech(lvl_text, BOX_X + 70, BOX_Y + 10, TEXT_SIZE)
        speech(type_text, BOX_X + 200, BOX_Y + 10, TEXT_SIZE)
        speech(HP_text, BOX_X + 90,BOX_Y + 70, TEXT_SIZE)
        speech(speed_text, BOX_X + 110, BOX_Y +100, TEXT_SIZE )  ##
        speech(ATK_text, BOX_X + 205, BOX_Y + 70, TEXT_SIZE )
        speech(DEF_text, BOX_X + 300, BOX_Y + 100, TEXT_SIZE )
        speech(SPEC_ATK_text, BOX_X + 130, BOX_Y + 150, TEXT_SIZE )
        speech(SPEC_DEF_text, BOX_X + 330, BOX_Y + 150, TEXT_SIZE )
        
            
        
        
        
    
    
        
    
         


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if name_state:  ## this section of the event is assocaited with the name of the player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Process the entered name (for now, just print it)
                    if len(text) != 0:  #code is run only if player types something down
                        player_name = text  ## player name is now associated with the players name choice 
                        print("Entered Name:", player_name) ##test to see is player name has a value
                        pokemon_state = True #pokemon_state becomes True whilst name_state ends 
                        name_state = False
                    text = '' #text value goes back to having no characters
                    
                elif event.key == pygame.K_BACKSPACE:  ## if the user deletes a character, it gets deleted 
                    text = text[:-1] ##text varaible changed to removed one character
                elif len(text) < MAX_NAME_LENGTH and event.unicode.isalnum(): #len(text) <Max_name prevent characters exceeding limit 
                    text += event.unicode ## isalnum() method checks if the character is an alphanumeric character (either a letter or a number)
    
     # # Render the text
        # rendered_text = poke_font.render(text, True, BLACK)
        # text_rect = rendered_text.get_rect(center=(WIDTH // 2, HEIGHT // 2)) ##centers the text
                    
    if name_state:
        # Fill the screen
        screen.fill(WHITE)
        speech('What is your name Travaler', 250,250, FONT_SIZE) ##changed the function to be called speech

        for i, char in enumerate(text): # i is the index, char is the characters 
            rect_x = i * (CHARACTER_WIDTH + SPACE_BETWEEN_CHARACTERS) #x position of rectangle 
            pygame.draw.rect(screen, BLACK, (rect_x, 90, CHARACTER_WIDTH, 8)) #left,top,width,height 
            char_surface = poke_font.render(char, False, BLACK) #prints the characters out 
            char_rect = char_surface.get_rect(center=(rect_x + CHARACTER_WIDTH // 2, 80)) #rects the input 
            screen.blit(char_surface, char_rect) ##blits users text onto screen
            
    elif pokemon_state:
        screen.fill(WHITE)  ## refreshes the page 
        
        ## tell user to pick starter pokemon
        speech(player_name, 250, 30, FONT_SIZE)  ## prints player name 
        speech('Pick your starter!', 250,70, FONT_SIZE) ## tells player what to do 
        starter_pick_button('Squirtle','Assests/Character Sprite/Pokemon/Squirtle1.png',70,320, 3) ## shows squirtle onto the screen
        starter_pick_button('Charmander','Assests/Character Sprite/Pokemon/Charmander1.png', 190, 180, 2.5 )
        starter_pick_button('Bulbasaur','Assests/Character Sprite/Pokemon/Bulbasaur1.png', 360, 300, 2.9)
        
        
        
        #BACK button 
        back_text = poke_font.render('BACK',False,"Black") 
        back_text_but = button.Button(400,450,back_text,1) ##back button is made to allow player to go back to change name 
        if back_text_but.draw(screen):  #function of back button
            name_state = True #causes name_state to become True and Pokemon_state = False
            pokemon_state = False
    
    
    ## picking Charmander 
    elif pokemon_starter_bool['Charmander']:
        screen.fill(WHITE)
        charmander = Pokemon('Charmander','Assests/Character Sprite/Pokemon/Charmander1.png', 'Charmander','Fire', 5, 23, 11, 12, 13, 12, 11)
        charmander.text_box(500,230,BOX_X,BOX_Y) ## sets text box for charmander 
        charmander.pokemon_img(3, 250, 90) ## image size multiplied by 3
        charmander.stats() ## stats shown
        
        #BACK button 
        back_text = poke_font.render('BACK',False,"Black") 
        back_text_but = button.Button(350,450,back_text,1) ##back button is made to allow player to go back to change name 
        if back_text_but.draw(screen):  #function of back button
            pokemon_starter_bool['Charmander'] = False #makes charmander False causing playing to go back to selection
            pokemon_state = True  ## Pokemon state becomes True 
            
        #CHOOSE button
        choose_text = poke_font.render('CHOOSE',False,"Black") ## text of the choose button is made 
        choose_text_but = button.Button(210,170,choose_text,1) ##choose button is made to allow player to go back to change name 
        if choose_text_but.draw(screen):  #function of choose button
            pokemon_starter_bool['Charmander'] = False #causes name_state to become False and Pokemon_state = False
            pokemon_state = False
            name_state = False
            player_pokemon = charmander ## player pokemon is now set to this pokemon
            screen.fill(WHITE) ## refreshes the page 
        
    ## picking Squirtle  
    
    elif pokemon_starter_bool['Squirtle']:
        screen.fill(WHITE)
        squirtle = Pokemon('Squirtle','Assests/Character Sprite/Pokemon/Squirtle1.png','Squirtle','Water',5, 22, 12, 11, 12, 11, 11 )
        squirtle.text_box(500,230,BOX_X,BOX_Y) ##sets text box for Squirtle 
        squirtle.pokemon_img(4, 250, 90) ## img multiplied by 4
        squirtle.stats()  ## stats shown
        
        #BACK button 
        back_text = poke_font.render('BACK',False,"Black") 
        back_text_but = button.Button(350,450,back_text,1) ##back button is made to allow player to go back to change name 
        if back_text_but.draw(screen):  #function of back button
            pokemon_starter_bool['Squirtle'] = False #causes name_state to become True and Pokemon_state = False
            pokemon_state = True
            
        #CHOOSE button
        choose_text = poke_font.render('CHOOSE',False,"Black")  
        choose_text_but = button.Button(210,170,choose_text,1) ##back button is made to allow player to go back to change name 
        if choose_text_but.draw(screen):  #function of back button
            pokemon_starter_bool['Squirtle'] = False #causes name_state to become True and Pokemon_state = False
            pokemon_state = False
            name_state = False
            player_pokemon = squirtle
            screen.fill(WHITE)
    
    
    ## picking Bulbasaur 
    
    elif pokemon_starter_bool['Bulbasaur']:
        screen.fill(WHITE)
        bulbasaur = Pokemon('Bulbasaur','Assests/Character Sprite/Pokemon/Bulbasaur1.png','Bulbasaur','Grass',5, 23, 12, 12, 13, 12, 12 )
        bulbasaur.text_box(500,230,BOX_X,BOX_Y)  ## text box for player 
        bulbasaur.pokemon_img(4, 250, 90) ## img of bulbasaur multiplied by 4 
        bulbasaur.stats() ## stats shown 
        
        #BACK button 
        back_text = poke_font.render('BACK',False,"Black") 
        back_text_but = button.Button(350,450,back_text,1) ##back button is made to allow player to go back to change name 
        if back_text_but.draw(screen):  #function of back button
            pokemon_starter_bool['Bulbasaur'] = False #causes name_state to become True and Pokemon_state = False
            pokemon_state = True
            
        #CHOOSE button
        choose_text = poke_font.render('CHOOSE',False,"Black") 
        choose_text_but = button.Button(210,170,choose_text,1) ##back button is made to allow player to go back to change name 
        if choose_text_but.draw(screen):  #function of back button
            pokemon_starter_bool['Bulbasaur'] = False #causes name_state to become True and Pokemon_state = False
            pokemon_state = False
            name_state = False
            player_pokemon = bulbasaur
            screen.fill(WHITE)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(30)

# Quit Pygame properly
pygame.quit()
sys.exit()







