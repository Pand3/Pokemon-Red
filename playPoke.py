import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
FPS = 60
TILE_SIZE = 20  # Adjust the tile size to fit the screen better
BLACK = (0, 0, 0)
GREY = (155,155,155)
WHITE = (255, 255, 255)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon")
clock = pygame.time.Clock()

## make the building, tile no. 00, 12, 104, 116, 117, 129, 130, 142,143, 155, 156, 168


game_map = [
    [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 5, 3, 5, 5, 4, 4, 3, 3, 3, 4, 3, 5, 0],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 3, 3, 3, 5, 3, 5, 3, 3, 4, 3, 5, 5, 1],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 4, 3, 5, 4, 5, 3, 3, 3, 5, 5, 4, 4, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 3, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 5, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 3, 4, 5, 3, 3, 5, 4, 4, 5, 4, 4, 4, 0],
    [1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 3, 5, 3, 4, 5, 4, 3, 4, 5, 3, 4, 4, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 3, 3, 5, 4, 3, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 5, 4, 4, 5, 5, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 3, 3, 5, 5, 3, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 4, 3, 3, 4, 4, 0, 1, 0, 1],   
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 5, 3, 5, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 4, 4, 4, 3, 3, 5, 3, 0, 0, 0, 0, 5, 4, 3, 4, 3, 5, 3, 0, 0, 1],
    [1, 1, 1, 3, 3, 3, 3, 3, 4, 3, 4, 0, 0, 0, 0, 5, 5, 4, 3, 3, 5, 5, 0, 0, 1],
    [1, 1, 0, 5, 3, 4, 4, 3, 3, 3, 3, 0, 0, 0, 0, 3, 5, 5, 5, 4, 3, 5, 1, 0, 1],
    [1, 0, 0, 3, 4, 3, 3, 5, 5, 3, 3, 0, 0, 0, 0, 3, 4, 3, 3, 4, 5, 4, 0, 1, 1],
    [1, 0, 1, 3, 3, 5, 5, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0],
]
##################

# Calculate the size of the map based on screen size and tile size
MAP_WIDTH = len(game_map[0]) * TILE_SIZE
MAP_HEIGHT = len(game_map) * TILE_SIZE

# Function to load and resize images
def load_and_resize(image_path, size):
    image = pygame.image.load(image_path)
    return pygame.transform.scale_by(image, size)

tile_images = {
    0: load_and_resize('Assests/Tiles/Grass/BW grass/Floor 1.png',1),
    1: load_and_resize('Assests/Tiles/Grass/BW grass/Floor 2.png', 1),  ## floor tiles
    3: load_and_resize('Assests/Tiles/Grass/BW grass/Tall Grass 1.imp.png', 1),
    4: load_and_resize('Assests/Tiles/Grass/BW grass/Tall Grass 2.imp.png', 1), ## tall grass tiles 
    5: load_and_resize('Assests/Tiles/Grass/BW grass/Tall Grass 3.imp.png', 1),
}

## function for blitting a tile 
def tile_blit(tile_number): 
    for y, row in enumerate(game_map):  
        for x, tile in enumerate(row):
        
            if tile == tile_number:  # For example, 0 represents a floor tile
                tile_image = tile_images[tile] #iterates through dictinary of images 
                screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))
    

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = {
            "left": [   # I assign specific images for each movement 
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_leftStand.png', 2),
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_leftWalk.png', 2)
            ],
            "right": [
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_rightStand.png', 2),
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_rightWalk.png', 2)
            ],
            "up": [
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_backStand.png', 2),
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_backrightWalk.png', 2),
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_backStand.png', 2),  
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_backleftWalk.png', 2)  
            ],
            "down": [
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_frontStand.png', 2),
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_frontrightWalk.png', 2),
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_frontStand.png', 2),
                load_and_resize('Assests/Character Sprite/Characters/Main character animation/MC_frontleftWalk.png', 2),
            ]
        }
        self.direction = "down" #sprites initial set direction
        self.index = 0
        self.image = self.images[self.direction][self.index] #iterates through the values of direction
        self.rect = self.image.get_rect() #each animation gets rect as it goes through
        self.rect.center = (WIDTH // 2, HEIGHT // 2) #initial position in the middle 
        self.speed = 3
        self.animation_delay = 5 # To Adjust the delay, the higher the no. the slower the animation
        self.animation_count = 0 

    def check_for_battle(self):
        global game_map  ##take in the game_map to see what tile the player is on 
        global player ## so that the players postion can be checked

        player_tile_x = player.rect.x // TILE_SIZE ##this is x coordinates of the tile
        player_tile_y = player.rect.y // TILE_SIZE## this is the y coordinate
        current_tile = game_map[player_tile_y][player_tile_x] ##saves the current tile to be compared

        # Check if the player is on a grass tile
        if current_tile == 3 or current_tile == 4 or current_tile == 5:  #checks if player is on grass tile
            if random.random() < 0.005:  ## chance of battle occuring 
                 print("Battle Commenced!")
             
    
    
    def update(self, keys):
        # Update player position based on keys pressed
        if keys[pygame.K_LEFT]: 
            self.direction = "left"
            self.rect.x -= self.speed
            
        elif keys[pygame.K_RIGHT]:
            self.direction = "right"
            self.rect.x += self.speed
            
        elif keys[pygame.K_UP]:
            self.direction = "up"
            self.rect.y -= self.speed
            
        elif keys[pygame.K_DOWN]:
            self.direction = "down"
            self.rect.y += self.speed
        
        self.check_for_battle()
        
            

        # Ensure the player stays within the screen boundaries
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(HEIGHT - self.rect.height, self.rect.y))

        # Update walking animation
        if self.animation_count < self.animation_delay: #as self.animation = 0
            self.animation_count += 1 #this gives the delay as it takes time for count to reach delay
        else:
            self.animation_count = 0 #resets 
            self.index = (self.index + 1) % len(self.images[self.direction])#goes down the list of animation
            self.image = self.images[self.direction][self.index]#changes direction if player changes 
            
    
    
    
    
# Create player object
player = Player()

# Sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# building = pygame.image.load('Assests/Tiles/Building/Building_light.png')
# building_shrink = pygame.transform.scale_by(building, 0.65 )



# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update all sprites
    all_sprites.update(keys)

    # Fill the screen
    screen.fill(GREY)
    tile_blit(0)
    tile_blit(1)
    tile_blit(2)
    tile_blit(3)
    tile_blit(4)
    tile_blit(5)
    tile_blit(6)
    
    
    # for y, row in enumerate(game_map):
    #     for x, tile in enumerate(row):
            
    #         if tile == 0:  # For example, 0 represents a floow tile
    #             tile_image = tile_images[tile] #iterates through dictinary of images 
    #             screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))
                
    #         if tile == 1:  
    #             tile_image = tile_images[tile] 
    #             screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))
            
            
    #         if tile == 3:  
    #             tile_image = tile_images[tile] 
    #             screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))
            
    #         if tile == 4:  
    #             tile_image = tile_images[tile] 
    #             screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))
            
    #         if tile == 5:  
    #             tile_image = tile_images[tile] 
    #             screen.blit(tile_image, (x * TILE_SIZE, y * TILE_SIZE))
            
    
            
                    #####################
    
    # screen.blit(building_shrink,(0,0))
    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FPS)

# Quit Pygame properly
pygame.quit()
sys.exit()
