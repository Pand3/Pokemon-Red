

# game_map = [
#     [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
#     [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 5, 3, 5, 5, 4, 4, 3, 3, 3, 4, 3, 5, 0],
#     [1, 6, 6, 6, 1, 1, 1, 0, 1, 0, 1, 0, 3, 3, 3, 5, 3, 5, 3, 3, 4, 3, 5, 5, 1],
#     [0, 6, 6, 6, 1, 1, 1, 0, 1, 1, 0, 0, 4, 3, 5, 4, 5, 3, 3, 3, 5, 5, 4, 4, 0],
#     [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 5, 1],
#     [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 3, 4, 5, 3, 3, 5, 4, 4, 5, 4, 4, 4, 0],
#     [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 3, 5, 3, 4, 5, 4, 3, 4, 5, 3, 4, 4, 0],
#     [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
#     [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
#     [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
#     [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 3, 3, 5, 4, 3, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 5, 4, 4, 5, 5, 0, 0, 1, 1],
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 3, 3, 5, 5, 3, 1, 0, 0, 1],
#     [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 4, 3, 3, 4, 4, 0, 1, 0, 1],   
#     [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#     [1, 0, 0, 5, 3, 5, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 3, 4, 4, 4, 3, 3, 5, 3, 0, 0, 0, 0, 5, 4, 3, 4, 3, 5, 3, 0, 0, 1],
#     [1, 1, 1, 3, 3, 3, 3, 3, 4, 3, 4, 0, 0, 0, 0, 5, 5, 4, 3, 3, 5, 5, 0, 0, 1],
#     [1, 1, 0, 5, 3, 4, 4, 3, 3, 3, 3, 0, 0, 0, 0, 3, 5, 5, 5, 4, 3, 5, 1, 0, 1],
#     [1, 0, 0, 3, 4, 3, 3, 5, 5, 3, 3, 0, 0, 0, 0, 3, 4, 3, 3, 4, 5, 4, 0, 1, 1],
#     [1, 0, 1, 3, 3, 5, 5, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0],
# ]

# #allows me to make a serires of the same tile
# #without manually entering them
# def copy(item, number ): 
#     list = []
#     for i in range(number):#no. of times i want ot iterate
#         list.append(item) #value i want to repeat
#     print(list) #outputs list 



# def random_no(number): #prints a random series of no.
#     list = [0,1] #list change to output any no. i want 
#     random_list = [] #list to store random no.
    
    
#     for items in range(number): #no. of random values
#         random_list.append(list[random.randint(0,1)]) #randomly adds no. from list
    
#     print(random_list)
    

        

# def count(list): #counts how many value there are in a list 
#     no_of_items = 0 # placeholder for final value
    
#     for items in range(len(list)): #iterate depending on no. of values in list
#         no_of_items += 1 
#     return no_of_items 
## Assests/small assests/text-box.png


# --------------------------------------------------------------------------------

# import random

            
# class Pokemon:
#     def __init__(self, pokemon, pokemon_pic, pokemon_back_pic, name, type, moveset, lvl, HP, atk, defence, spec_atk, spec_defence, speed):
#         self.pokemon = pokemon  ## what pokemon it is 
#         self.pokemon_pic = pokemon_pic ## the image of the pokemon, file location
#         self.pokemon_back_pic = pokemon_back_pic
#         self.name = name  ##name set to pokemon specie, changed if user wants to 
#         self.type = type  ## e.g. fire type, water type etc.
#         self.moveset = moveset 
#         self.lvl = lvl ##what level the pokemon is 
#         self.HP = HP ##its health points 
#         self.MAX_HP = HP
#         self.atk = atk  ## its normal attack e.g. its elemental attacks 
#         self.defence = defence ## its normal defence 
#         self.spec_atk = spec_atk ## its speacial attack e.g. its elemental attacks 
#         self.spec_defence = spec_defence ## its special attack
#         self.speed = speed ## how fast the pokemon is, determine if first move or no 
        




### Random Pokemon -- level 15 and below 
# squirtle = Pokemon('Squirtle','Assests/Character Sprite/Squirtle1.png','Squirtle','Water',['Quick Attack','Bubble','',''],5, 22, 12, 11, 12, 11, 11 )
# charmander = Pokemon('Charmander','Assests/Character Sprite/Charmander1.png', 'Charmander','Fire',['Scratch','Ember','',''], 5, 23, 11, 12, 13, 12, 11)
# bulbasaur = Pokemon('Bulbasaur','Assests/Character Sprite/Bulbasaur1.png','Bulbasaur','Grass',['Tackle','Vine Whip','',''],5, 23, 12, 12, 13, 12, 12 )

# caterpie = Pokemon('caterpie','Assests/Character Sprite/Bulbasaur1.png','caterpie','Grass',['Tackle','Vine Whip','',''],5, 23, 12, 12, 13, 12, 12 )
# pidgey = Pokemon('pidgey','Assests/Character Sprite/Bulbasaur1.png','pidgey','Grass',['Tackle','Vine Whip','',''],5, 23, 12, 12, 13, 12, 12 )
# pikachu = Pokemon('pikachu','Assests/Character Sprite/Bulbasaur1.png','pikachu','Grass',['Tackle','Vine Whip','',''],5, 23, 12, 12, 13, 12, 12 )
# rattat = Pokemon('rattat','Assests/Character Sprite/Bulbasaur1.png','rattat','Grass',['Tackle','Vine Whip','',''],5, 23, 12, 12, 13, 12, 12 )
# weedle = Pokemon('weedle','Assests/Character Sprite/Bulbasaur1.png','weedle','Grass',['Tackle','Vine Whip','',''],5, 23, 12, 12, 13, 12, 12 )




# random_NPC_Pokemon = [ caterpie, pidgey, pikachu, rattat, weedle]
# opponent_pokemon = random_NPC_Pokemon[random.randint(0, len(random_NPC_Pokemon))]

# print(opponent_pokemon.name)



    






