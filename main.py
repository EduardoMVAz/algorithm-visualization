import pygame

class Main():
    
    # Screen Size
    WIDTH = 800
    HEIGHT = 450

    def __init__(self):
        
        # Pygame Setup
        pygame.display.set_mode(self.WIDTH, self.HEIGHT)
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        # Dict with program screens
        self.screens = {}

    def mainLoop(self):
        pass

    def quit(self):
        pygame.quit()

if __name__ == "main":
    main = Main()
    main.mainLoop()