import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
GRAVITY = 0.25
FLAP_HEIGHT = -8
PIPE_WIDTH = 100
PIPE_GAP = 200
FPS = 60  

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34,139,34)
RED = (200, 2, 2)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Load bird image
bird_img = pygame.Surface((50, 50))
bird_img.fill(WHITE)  # Replace with your own bird image

# Load pipe image
pipe_img = pygame.Surface((PIPE_WIDTH, SCREEN_HEIGHT))
pipe_img.fill(WHITE)  # Replace with your own pipe image

# Define Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.vel_y = 0

    def flap(self):
        self.vel_y = FLAP_HEIGHT

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 50, 50))  # Draw the bird

# Define Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x  
        self.height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)

    def move(self):
        self.x -= 2

    def off_screen(self):
        return self.x < -PIPE_WIDTH*1.2 

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, PIPE_WIDTH, self.height))  # Draw upper pipe
        pygame.draw.rect(screen, GREEN, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT))  # Draw lower pipe

class Base():
    def __init__(self):
        self.x = 0
        self.y = SCREEN_HEIGHT - 20  # Position the base at 90% of the screen height
        self.height = 20  # Height of the base

    def draw(self):
        pygame.draw.rect(screen, RED, (0, self.y, SCREEN_WIDTH, self.height))  # Draw the base
        pygame.draw.rect(screen, RED, (0, 0, SCREEN_WIDTH, self.height))  # Draw the top base

class Score():
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(None, 30)
    
    def increaseScore(self):
        self.score += 1
    
    def draw(self, screen):
        number_text = str(self.score)
        number_surface = self.font.render(number_text, True, BLACK)
        number_rect = number_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 10))
        
        # Draw the number on the screen
        screen.blit(number_surface, number_rect)



# Main game function
def main():
    score1 = Score()
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + i * 300) for i in range(2)]
    base = Base()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()

        bird.update()

        if pipes[-1].x < SCREEN_WIDTH - 300:
            pipes.append(Pipe(SCREEN_WIDTH))

        for pipe in pipes:
            pipe.move()
            if pipe.off_screen():
                pipes.remove(pipe)

        # Check for collisions
        for pipe in pipes:
            if (pipe.x < bird.x + 50 < pipe.x + PIPE_WIDTH) and (bird.y < pipe.height or bird.y + 50 > pipe.height + PIPE_GAP):
                print("Game Over!")  # Replace with game over logic
                pygame.quit()
                sys.exit()
            if (bird.y+50 > base.y or bird.y < base.height):
                print("Game Over!")  # Replace with game over logic
                pygame.quit()
                sys.exit()
            elif (pipe.x + PIPE_WIDTH == bird.x +50 ):
                score1.increaseScore()
        screen.fill(WHITE)
        bird.draw()
        base.draw()
        
        for pipe in pipes:
            pipe.draw()
        score1.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
 