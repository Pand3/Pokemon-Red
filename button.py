# import pygame 

# ## class button
# class Button():
#     def __init__(self,x,y,image,scale): #takes in the x-y coordinates of the image, another variable scale is added to adjust the size 
#         width = image.get_width() # returns the width of the image
#         height = image.get_height() # returns the height of the image 
#         self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))# multiple the width and height by the scale
#         self.rect = self.image.get_rect() #turning img into a rectangle to make it easier to position image and allow actions to occur 
#         self.rect.topleft = (x,y) # positioning image onto the screen
#         self.clicked = False #checks if the user has left clicked onto the button or not 
        
#     def draw(self,screen): # this function draws button onto the screen and allows an action to occur depending on if clicked
#         action = False #local variable created, value depends on if clicked or not 
        
#         pos = pygame.mouse.get_pos() #obtain mouse position 
        
#         if self.rect.collidepoint(pos): #checks if mouse is hovering over button or not
#             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #checks if button is clicked 
#                 self.clicked = True
#                 action = True
        
#         if pygame.mouse.get_pressed()[0] == 0:
#             self.clicked = False  #resets the clicked button
        
#         screen.blit(self.image,(self.rect.x,self.rect.y)) #draws the button onto the screen. 
        
#         return action #returns if action is true or not. 
    
##--------------------------------------------------------------
    # class button
import pygame 

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        

    def draw(self, screen):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
        else:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
