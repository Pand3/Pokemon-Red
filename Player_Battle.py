import pygame 
import random 
import time
import button 

pygame.init()


## constants 
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOX_X = 5
BOX_Y = 280
dmg_grad = 30
BATTLE_MODE = True
PLAYER_WIN = False
PLAYER_LOSE = False
PKMN_CAP = False
poke_font = pygame.font.Font('Assests/small assests/Pixeltype.ttf', 50)
back_text = poke_font.render('BACK',False,"Black") 




dmg_grad = 30
## these are all the moves that I have created alongside their damages 
fire_moves = {'Ember': random.randint(5, 8) / dmg_grad, 'Flame Thrower': random.randint(4, 7)/ dmg_grad}
water_moves = {'Water Gun':random.randint(6, 11) / dmg_grad, 'Bubble':random.randint(5, 10) / dmg_grad, 'HydroPump':random.randint(6, 8) / dmg_grad}
grass_moves = {'Vine Whip':random.randint(5, 6) / dmg_grad, 'Spore':random.randint(6, 7) / dmg_grad, 'Razor Leaf':random.randint(9, 13) / dmg_grad, 'Solar': random.randint(5, 7) / dmg_grad }
normal_moves = {'Quick Attack': random.randint(3,8) / dmg_grad,'Scratch': random.randint(4,6)/ dmg_grad,'Tackle': random.randint(4, 8)/ dmg_grad, 'Bite':random.randint(5,7) / dmg_grad,
                'Headbutt':random.randint(3,6) / dmg_grad, 'Peck':random.randint(3,5) / dmg_grad,'Silk':random.randint(3,5) / dmg_grad,'Claw':random.randint(4,8) / dmg_grad,
                'Sting':random.randint(3,6) / dmg_grad,'Harden':random.randint(3,5) / dmg_grad,'Iron Tail':random.randint(5,8) / dmg_grad,'Chew':random.randint(3,7) / dmg_grad,
                'Gust':random.randint(3,7) / dmg_grad,'Poison':random.randint(3,7) / dmg_grad }
electric_moves = {'Thunder Bolt': random.randint(7, 13) / dmg_grad}

all_moves = {**fire_moves, **water_moves, **grass_moves, **normal_moves, **electric_moves} ## this adds all the moves into one dictionary 


    
def back():
    back_text = poke_font.render('BACK',False,"Black") 
    back_text_but = button.Button(400,450,back_text,1) ##back button is made to allow player to go back to change name 
    return back_text_but.draw(screen)

# Example usage
# text_to_display = "Hello, world!"
# display_text_with_delay(text_to_display, 0.1)  # Display each character with a delay of 0.1 seconds



def speech(text, x, y, size): ##x and y will be the coordinates of the text
    font = pygame.font.Font('Assests/small assests/Pixeltype.ttf',size)
    comment = font.render(str(text),False,BLACK) ##saves text to a variable making it black as well
    comment_rect = comment.get_rect(center = (x,y)) #moves the center of the text to the chosen coordinates 
    screen.blit(comment,comment_rect) ##text is now shown on the screen using the blit function


def display_text_with_delay(x, y, text, delay_time,FONT_SIZE): ## function used to delay text
    font = pygame.font.Font('Assests/small assests/Pixeltype.ttf', FONT_SIZE)
    

    for char in text:
        text_surface = font.render(char, True, BLACK)
        screen.blit(text_surface, (x, y))
        pygame.display.flip()  # Update the display
        time.sleep(delay_time)  # Delay for the specified time
        x += FONT_SIZE / 2 # Move the next character position


#### POKEMON CLASS 
class Pokemon:
    def __init__(self, pokemon, pokemon_pic, name, type, moveset, lvl, HP, atk, defence, spec_atk, spec_defence, speed):
        self.pokemon = pokemon  ## what pokemon it is 
        self.pokemon_pic = pokemon_pic ## the image of the pokemon, file location
        self.name = name  ##name set to pokemon specie, changed if user wants to 
        self.type = type  ## e.g. fire type, water type etc.
        self.moveset = moveset 
        self.lvl = lvl ##what level the pokemon is 
        self.HP = HP ##its health points 
        self.MAX_HP = HP
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
        
    
### starter Pokemon -- level 15 and below 
squirtle = Pokemon('Squirtle','Assests/Character Sprite/Pokemon/Squirtle1.png','Squirtle','Water',['Quick Attack','Bubble','',''],10, 16, 12, 11, 12, 11, 11 )
charmander = Pokemon('Charmander','Assests/Character Sprite/Pokemon/Charmander1.png', 'Charmander','Fire',['Scratch','Ember','',''], 5, 16, 11, 12, 13, 12, 11)
bulbasaur = Pokemon('Bulbasaur','Assests/Character Sprite/Pokemon/Bulbasaur1.png','Bulbasaur','Grass',['Tackle','Vine Whip','',''],5, 16, 12, 12, 13, 12, 12 )

opp_level = random.randint(1, 50)  ## this will randomly generate the level for the pokemon in which the player will ecounter
## player CONSTANTS 
player_name = 'BOB'
player_pokemon = squirtle  ## this will be the current players pokemon

opp_level = random.randint(player_pokemon.lvl - 2, player_pokemon.lvl + 2)  ## this will randomly generate the level for the pokemon in which the player will ecounter


lvl_stats_increase = round(opp_level) ##this will boost pokemon stats proportional to their level 

## Stray Pokemon under level 16  s_means stray                                                                                                      lvl, HP, atk, defence, spec_atk, spec_defence, speed
s_squirtle = Pokemon('Squirtle','Assests/Character Sprite/Pokemon/Squirtle1.png','Squirtle','Water',['Quick Attack','Bubble','',''],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7)+ lvl_stats_increase, random.randrange(5,7)+ lvl_stats_increase, random.randrange(6,8)+ lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(5,7)+ lvl_stats_increase )
s_charmander = Pokemon('Charmander','Assests/Character Sprite/Pokemon/Charmander1.png', 'Charmander','Fire',['Scratch','Ember','',''], opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase)
s_bulbasaur = Pokemon('Bulbasaur','Assests/Character Sprite/Pokemon/Bulbasaur1.png','Bulbasaur','Grass',['Tackle','Vine Whip','Spore','Solar'],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) +lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase )
s_caterpie = Pokemon('caterpie','Assests/Character Sprite/Pokemon/caterpie1.png','Caterpie','Bug',['Silk','Headbutt','',''],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase)
s_pidgey = Pokemon('pidgey','Assests/Character Sprite/Pokemon/Pidgey1.png','Pidgey','Normal',['Tackle','Gust','',''],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) +lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase )
s_pikachu = Pokemon('pikachu','Assests/Character Sprite/Pokemon/pikachu1.png','Pikachu','Electric',['Thunder Bolt','Iron Tail','',''],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) +lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase )
s_rattat = Pokemon('rattat','Assests/Character Sprite/Pokemon/Rattat1.png','Rattat','Normal',['Bite','Quick Attack','',''],opp_level, random.randrange(13, 16)+ lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(7,9) +lvl_stats_increase )
s_weedle = Pokemon('weedle','Assests/Character Sprite/Pokemon/weedle1.png','Weedle','Bug',['Sting','Tackle','Silk','Poison'],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase,random.randrange(5,7) +lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase )


## Stray Pokemon level 16/ over and under level 36
s_squirtle2 = Pokemon('Wartortle','Assests/Character Sprite/Pokemon/Squirtle2.png','Wartortle','Water',['Quick Attack','Bubble','Water Gun',''],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7)+ lvl_stats_increase, random.randrange(5,7)+ lvl_stats_increase, random.randrange(6,8)+ lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(5,7)+ lvl_stats_increase )
s_charmander2 = Pokemon('Charmeleon','Assests/Character Sprite/Pokemon/Charmander2.png', 'Charmeleon','Fire',['Scratch','Ember','Flame Thrower',''], opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase)
s_bulbasaur2 = Pokemon('Ivysaur','Assests/Character Sprite/Pokemon/Bulbasaur2.png','Ivysaur','Grass',['Tackle','Vine Whip','Spore','Solar'], opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) +lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase )
s_caterpie2 = Pokemon('Metapod','Assests/Character Sprite/Pokemon/caterpie2.png','Metapod','Bug',['Silk','Headbutt','Harden',''],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase)
s_pidgey2 = Pokemon('Pidgeotto','Assests/Character Sprite/Pokemon/Pidgey2.png','Pidgeotto','Normal',['Tackle','Gust','Peck',''], opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) +lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase )
s_pikachu2 = Pokemon('Raichu','Assests/Character Sprite/Pokemon/pikachu2.png','Raichu','Electric',['Thunder Bolt','Iron Tail','Charge','Tackle'],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) +lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase )
s_rattat2 = Pokemon('Raticate','Assests/Character Sprite/Pokemon/Rattat2.png','Raticate','Normal',['Bite','Quick Attack','Scratch','Chew'],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(7,9) +lvl_stats_increase )
s_weedle2 = Pokemon('Kakuna','Assests/Character Sprite/Pokemon/caterpie2.png','Kakuna','Bug',['Sting','Tackle','Silk',''],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase,random.randrange(5,7) +lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase )

## Stray Pokemon level 36 and over 
s_squirtle3 = Pokemon('Blastoise','Assests/Character Sprite/Pokemon/Balbasaur3.png','Blastoise','Water',['Quick Attack','Bubble','Water Gun','HyrdoPump'],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7)+ lvl_stats_increase, random.randrange(5,7)+ lvl_stats_increase, random.randrange(6,8)+ lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(5,7)+ lvl_stats_increase )
s_charmander3 = Pokemon('Charizard','Assests/Character Sprite/Pokemon/Charmander3.png', 'Charizard','Fire',['Scratch','Ember','Flame Thrower','Bite'], opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(6,8) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase)
s_bulbasaur3 = Pokemon('Venusaur','Assests/Character Sprite/Pokemon/Balbasaur3.png','Venusaur','Grass',['Tackle','Vine Whip','Spore','Razor Leaf'], opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) +lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase )
s_caterpie3 = Pokemon('Butterfree','Assests/Character Sprite/Pokemon/caterpie3.png','Butterfree','Bug',['Silk','Headbutt','Spore','Gust'],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase)
s_pidgey3 = Pokemon('Pidgeot','Assests/Character Sprite/Pokemon/Pidgey3.png','Pidgeot','Normal',['Tackle','Gust','Peck','Claw'], opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(4,6) +lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase )
s_weedle3 = Pokemon('Beedrill','Assests/Character Sprite/Pokemon/caterpie3.png','Beedrill','Bug',['Sting','Tackle','Silk','Poison'],opp_level, random.randrange(13, 16) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase,random.randrange(5,7) +lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase, random.randrange(5,7) + lvl_stats_increase )


# this will help generate random instance of the pokemon class for the player to battle.
if opp_level < 16: ## if the pokemon is below level 16 then it will only generate pokemon which are meant to be lvl 161 and below
    random_NPC_Pokemon = [s_squirtle, s_charmander, s_bulbasaur, s_caterpie, s_pidgey, s_pikachu, s_rattat, s_weedle]
    opponent_pokemon = random_NPC_Pokemon[random.randint(0,len(random_NPC_Pokemon)-1)] 
    ## this will randomly pick from the list of pokemon from random_NPC_Pokemon for the player to battle 
    
if opp_level >= 16 and opp_level < 36:
    random_NPC_Pokemon = [s_squirtle2, s_charmander2, s_bulbasaur2, s_caterpie2, s_pidgey2, s_pikachu2, s_rattat2, s_weedle2]
    opponent_pokemon = random_NPC_Pokemon[random.randint(0,len(random_NPC_Pokemon)-1)]

if opp_level >= 36:
    random_NPC_Pokemon = [s_squirtle3, s_charmander3, s_bulbasaur3, s_caterpie3, s_pidgey3, s_pikachu2, s_rattat2, s_weedle3]
    opponent_pokemon = random_NPC_Pokemon[random.randint(0,len(random_NPC_Pokemon)-1)]
    



## player CONSTANTS 
player_name = 'BOB'
player_pokemon = squirtle  ## this will be the current players pokemon
pokemon_team = [squirtle, s_charmander, s_bulbasaur3, s_pidgey2] ## this will be the team to test the code 


### Battle options 
## this is the text for each button
fight_text = poke_font.render('FIGHT', False, BLACK) 
item_text = poke_font.render('ITEM',False, BLACK)
pkmn_text = poke_font.render('PKMN',False, BLACK)
run_text = poke_font.render('RUN',False, BLACK)

##Battle states
item_state = False
pkmn_state = False
run_state = False
fight_state = False
battle_mode_menu = True


## this will help generate random instance of the pokemon class for the player to battle.

    

### Players inventory 
poke_balls = 3
heals = 1

## these will allow this to become a turn based game
players_turn = False
NPCs_turn = False

## checks which pokemons speed stat is greater. this determines who goes first 
if player_pokemon.speed > opponent_pokemon.speed: ## if the players speed is greater than opponents
    players_turn = True ## the player gets to go first
elif player_pokemon.speed == opponent_pokemon.speed: ## if both player and opponent speed are equal
    players_turn = True ## player still get to go first 
    
else: ## if player speed is less then opp speed then opp goes first 
    NPCs_turn = True
    

def dmg_effects(move, player):
    
    dmg_change = 1
    ## move --> the move of the attacker
    ##player --> the one being attacked 
    ## dmg_change will be the mutiplier if the move used is effective against the opponent 
    ## FIRE -
    if move in fire_moves and player.type == 'Grass':
        dmg_change = 1.25
    elif move in fire_moves and player.type == 'Water':
        dmg_change = 0.75
    
    ## GRASS - 
    if move in grass_moves and player.type == 'Water':
        dmg_change = 1.25
    elif move in grass_moves and player.type == 'Fire':
        dmg_change = 0.75
        
    ## WATER - 
    if move in water_moves and player.type == 'Fire':
        dmg_change = 1.25
    elif move in water_moves and player.type == 'Grass':
        dmg_change = 0.75
    
    ## ELECTRIC - 
    if move in electric_moves and player.type == 'Water':
        dmg_change = 1.25

    return dmg_change ## returns the multiplier 


def attack(move):
    global opponent_pokemon
    global player_pokemon
    global NPCs_turn
    global players_turn
    global BATTLE_MODE
    global PLAYER_WIN
    global PLAYER_LOSE
    global PKMN_CAP
    
    ## this is due to the type of move e.g. fire attack strong against grass pokemon
    if players_turn == True and NPCs_turn == False: ## checks if it is the players turn or not 
        if player_pokemon.HP > 0:  ## this allows player to attack only when pokemon has HP, & prevents attack if HP = 0 <------------ HERE
            opponent_pokemon.HP -= round((all_moves[move] * dmg_effects(move, opponent_pokemon )) + player_pokemon.atk) ## opp HP falls 
            if opponent_pokemon.HP <= 0: ## checks if opponent health is 0 or not 
                opponent_pokemon.HP = 0 ## prevents the opponent health from going into the negatives 
                ### win  
                PLAYER_WIN = True ## as opponent health is 0, player wins 
                BATTLE_MODE = False ## battle mode set to False to stop the Battle 
        
        
        
    elif players_turn == False and NPCs_turn == True:## checks if it is the NPC turn or not 
        if opponent_pokemon.HP > 0:  ## stops opponent from attacking when pokemon faints 
            player_pokemon.HP -= round((all_moves[move] * dmg_effects(move, player_pokemon )) + opponent_pokemon.atk/2)## player HP Falls 
            if player_pokemon.HP <= 0: ## checks if players health is 0 or not 
                player_pokemon.HP = 0 ## prevents the players health from going into the negatives 
                ### loose 
                PLAYER_LOSE = True ## as player health is 0, player loses 
                BATTLE_MODE = False ##battle mode set to False to stop the Battle 
        
        
    
    




### function for battle 
def Battle():
    screen.fill(WHITE)
    global BATTLE_MODE 
    global PKMN_CAP
    global fight_state
    global item_state
    global pkmn_state
    global run_state
    global battle_mode_menu ## I set this varaible to True 
    ## made these global varibles so values dont stay the same
    global poke_balls  
    global heals
    global pokemon_captured
    global player_pokemon
    global players_turn
    global NPCs_turn
    global players_turn
    global NPCs_turn
    
    opponent_move = opponent_pokemon.moveset[random.randint(0,len(opponent_pokemon.moveset)-1)] ## randomly picks a move for the NPC
    while opponent_move == '': ## if move is not an actual move  then re-roll
        opponent_move = opponent_pokemon.moveset[random.randint(0,len(opponent_pokemon.moveset)-1)]
        
    if NPCs_turn: ## checks if it is NPC's turn 
        attack(opponent_move) ## attack is made onto the player 
        players_turn = True ## flips the coin so now it is the players turn 
        NPCs_turn = False 
    
    # Battle buttons - making these text into buttons, making them have a function 
    fight_button = button.Button(260, 360, fight_text,  1.05)
    pkmn_button = button.Button(370, 360, pkmn_text, 1.05)
    item_button = button.Button(260, 430, item_text, 1.05)
    run_button = button.Button(370, 430, run_text, 1.05)
    
   
   
   
   
    
    
    
    if BATTLE_MODE == True:
        
        player_pokemon.text_box(500, 200, 0, 300) ## big box
        player_pokemon.text_box(250, 200, 0, 300) ## small box
        
        ## this shows the player how much health his pokemon has left 
        health_text = f"HP: {player_pokemon.HP}/{player_pokemon.MAX_HP}"  ## made new MAX_HP variable in class 
        speech(health_text, 390, 300, 50) ## speech functions already renders text, no need to do it again 
        
        ## players pokemon level 
        level_text = f"LVL:{player_pokemon.lvl} "
        speech(level_text, 100, 300, 50)
        
        
        ## this shows the player which pokemon they are using right now 
        speech(player_pokemon.name, 120, 400, 50)
        
       
        opponent_pokemon.pokemon_img(3, 400, 100) ## displaying the opp pokemon onto the screen
        opponent_health = f"HP: {opponent_pokemon.HP}/{opponent_pokemon.MAX_HP}"  ## opponents HP
        opponent_level = f"LVL:{opponent_pokemon.lvl}" ## the opponents level 
        speech(opponent_level, 60, 50, 50)  ## displays opponents level 
        speech(opponent_pokemon.name, 220, 50, 50) ## displays the name of the Pokemon
        speech(opponent_health, 100, 100, 50) ## places the opponents health at the top right corner
        
        
        
         
        
        
        
        if battle_mode_menu:  ## checks if the user is on the battle options or not, if yes then displayed options 
            
            
            if fight_button.draw(screen): ## functions are not below as it only causes the image to flash and return to battle state
                    fight_state = True ## these here will help cause the functions to happen
                    battle_mode_menu = False  ## this here will remove all the buttons so that they cannot be clicked whilst
                                             ## in the fight state 
                
            if item_button.draw(screen):
                    item_state = True
                    battle_mode_menu = False
                
            if pkmn_button.draw(screen):
                    pkmn_state = True
                    battle_mode_menu = False
                
            if run_button.draw(screen):
                    run_state = True
                    battle_mode_menu = False
        
        
        ### screen for when FIGHT is clicked   ## fight, item, pkmn, run
        if fight_state == True:
            
            player_pokemon.text_box(510, 200, -10, 300) ## big box drawnt 
            
            ## rendering text for moveset poke_font.render(  , False, BLACK)
            button_1_text = poke_font.render(player_pokemon.moveset[0], False, BLACK)
            button_2_text = poke_font.render(player_pokemon.moveset[1], False, BLACK)
            button_3_text =  poke_font.render(player_pokemon.moveset[2], False, BLACK)
            button_4_text =  poke_font.render(player_pokemon.moveset[3], False, BLACK)
            
            
            ## fight buttons for the player to choose from
            button_1_atk = button.Button(50,360,button_1_text,1)
            button_2_atk = button.Button(250,360,button_2_text,1)
            button_3_atk = button.Button(50,410,button_3_text,1)
            button_4_atk = button.Button(250,410,button_4_text,1)
            
            ## result of atk moves 
            if button_1_atk.draw(screen):
                attack(player_pokemon.moveset[0]) ## attack is made on the opponent 
                NPCs_turn = True ## coin is flipped so now it is the opponents turn 
                players_turn = False
            
            if button_2_atk.draw(screen):
                attack(player_pokemon.moveset[1]) ## attack is made on the opponent 
                NPCs_turn = True ## coin is flipped so now it is the opponents turn 
                players_turn = False
                
            
            if button_3_atk.draw(screen):
                attack(player_pokemon.moveset[2]) ## attack is made on the opponent 
                NPCs_turn = True ## coin is flipped so now it is the opponents turn 
                players_turn = False

            
            if button_4_atk.draw(screen):
                attack(player_pokemon.moveset[3]) ## attack is made on the opponent 
                NPCs_turn = True ## coin is flipped so now it is the opponents turn 
                players_turn = False
 
            
            
            
            
            
            ## BACK Button -- allows user to go back and forth between options 
            back_text_but = button.Button(370,450,back_text,1) ##back button is made to allow player to go back to change name 
            if back_text_but.draw(screen):  #function of back button
                fight_state = False
                battle_mode_menu = True ## re-displays the menu. in the background it is removed, prob solved 
                
        ### screen for when ITEM is clicked
        if item_state == True:
            player_pokemon.text_box(510, 200, -10, 300) ## big box
            
            ## Rendering item itex -->( for when item button is clicked)
            poke_ball_text = poke_font.render(f'POKEBALLS   X{poke_balls}', False, BLACK)##text for pokeballs 
            heals_text = poke_font.render(f'HEALS   X{heals}',False, BLACK)## text for health
            
            ## initialising Item buttons for player to choose from 
            poke_balls_button = button.Button(50, 360, poke_ball_text, 1)
            heals_button = button.Button(50, 410, heals_text, 1)
            
            if poke_balls_button.draw(screen): 
                if poke_balls > 0:  ##checks if pokeballs are greater than 0 if yes 
                    poke_balls -= 1 ##pokeballs is reduced by 1 
                    
                ## this will give me the percentag of the opponents health which is left 
                    opponent_HP_percentage = ((opponent_pokemon.HP - opponent_pokemon.MAX_HP)/ opponent_pokemon.MAX_HP) * -100
                    if opponent_HP_percentage != 0: ## prevents zero division error 
                        if random.randint(1,150) <  opponent_HP_percentage: ## checks if probability of capturing is True
                            pokemon_team.append(opponent_pokemon) ##if it is adds to pokemon Team 
                            PKMN_CAP= True
                            BATTLE_MODE= False
                            
                            
                            
        
            if heals_button.draw(screen):
                if heals > 0:## checks if heals are greaters than 0
                    heals -= 1 ## if yes then removes one heal from inventory 
                    player_pokemon.HP += 10 ## heals cause players HP to increase by 1 
                    if player_pokemon.HP > player_pokemon.MAX_HP:
                        player_pokemon.HP = player_pokemon.MAX_HP
                
            ## BACK Button -- allows user to go back and forth between options 
            back_text_but = button.Button(370,450,back_text,1) ##back button is made to allow player to go back to change name 
            if back_text_but.draw(screen):  #function of back button
                item_state = False
                battle_mode_menu = True
                
                
                
        ### screen for when PKMN is clicked 
        if pkmn_state == True:
            player_pokemon.text_box(510, 200, -10, 300) ## big box
            
            ## renders text for each pokemon in the team 
            pokemon1_name = poke_font.render(pokemon_team[0].name, False, BLACK)
            pokemon2_name = poke_font.render(pokemon_team[1].name, False, BLACK)
            pokemon3_name = poke_font.render(pokemon_team[2].name, False, BLACK)
            pokemon4_name = poke_font.render(pokemon_team[3].name, False, BLACK)
            ## makes a button consisting the the pokemons name for the player to recognise which pokemon they want to use 
            pkmn1_button = button.Button(70, 350, pokemon1_name, 1 )
            pkmn2_button = button.Button(250, 350, pokemon2_name, 1 )
            pkmn3_button = button.Button(70, 420, pokemon3_name, 1 )
            pkmn4_button = button.Button(250, 420, pokemon4_name, 1 )
            
            
            if pkmn1_button.draw(screen): ## if player clicks on pokemon1 then players pokemon switches to pokemon 1
                if player_pokemon.name != pokemon_team[0].name: ##checks if players pokemon isn't already the one being used right now 
                    player_pokemon = pokemon_team[0] ## if not then switches to main player_pokemon
                
            elif pkmn2_button.draw(screen): ## if player clicks on pokemon2 then players pokemon switches to pokemon 2
                if player_pokemon.name != pokemon_team[1].name:
                    player_pokemon = pokemon_team[1]
                
            elif pkmn3_button.draw(screen): ## if player clicks on pokemon3 then players pokemon switches to pokemon 3
                if player_pokemon.name != pokemon_team[2].name:
                    player_pokemon = pokemon_team[2]
                    
            elif pkmn4_button.draw(screen): ## if player clicks on pokemon4 then players pokemon switches to pokemon 4
                if player_pokemon.name != pokemon_team[3].name:
                    player_pokemon = pokemon_team[3]
            
            
            # speech(pokemon_team[0].name, 150, 380, 50)
            # speech(pokemon_team[1].name, 330, 380, 50 )
            # speech(pokemon_team[2].name, 150, 420, 50)
            # speech(pokemon_team[3].name, 330, 420, 50)
            
            # if player_pokemon.name == pokemon_team[0].name:
            #     pygame.draw.rect(screen, BLACK, (90, 390, 120, 5))

            
            
            ## BACK Button -- allows user to go back and forth between options 
            back_text_but = button.Button(370,450,back_text,1) ##back button is made to allow player to go back to change name 
            if back_text_but.draw(screen):  #function of back button
                pkmn_state = False
                battle_mode_menu = True
                
        ### screen for when RUN is clicked 
        if run_state == True:
            player_pokemon.text_box(510, 200, -10, 300) ## big box
            speech('You ran away successfully', 250, 400, 50)
            
            
            # ## BACK Button -- allows user to go back and forth between options 
            # back_text_but = button.Button(370,450,back_text,1) ##back button is made to allow player to go back to change name 
            # if back_text_but.draw(screen):  #function of back button
            #     run_state = False
            #     battle_mode_menu = True
            
    ### END GAMES             
    if PKMN_CAP:  ## this is at the end of the BATTLE function, the alternate it BATTLE MODE = False 
        #once pokemon is captured battle is over 
        pokemon_captured_text = f'You have caught {opponent_pokemon.name}!' ## text for capture
        player_pokemon.text_box(500, 200, 0, 300) ## big box 
        speech(pokemon_captured_text, 250, 400, 50) ## text pasted onto screen
        
    elif PLAYER_WIN: 
        player_win_text = f"{opponent_pokemon.name} has fainted" ## text for fainted
        player_win_annouce = f"You Win" ## player announed win 
        player_pokemon.text_box(500, 200, 0, 300) ## big box
        speech(player_win_text, 250, 400, 50)
        speech(player_win_annouce, 250, 450, 50)
    
    elif PLAYER_LOSE:
        player_lose_text = f"{player_pokemon.name} has fainted" ## text for players pokemon fainting 
        player_lose_annouce = f"You lose" ## player annonced loss
        player_pokemon.text_box(500, 200, 0, 300) ## big box
        speech(player_lose_text, 250, 400, 50)
        speech(player_lose_annouce, 250, 450, 50)
        
        

       
        
        
        

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

        
        Battle()
        
        
    
    
            

    # Limit the frame rate
    clock.tick(FPS)
    pygame.display.update()
# Quit Pygame properly
pygame.quit()