import pygame
import random
import numpy as np

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

# Q-learning parameters
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EXPLORATION_RATE = 0.1
EPISODES = 10000

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.vel_y = 0
        self.is_alive = True

    def flap(self):
        self.vel_y = FLAP_HEIGHT

    def update(self):
        if self.is_alive:
            self.vel_y += GRAVITY
            self.y += self.vel_y

    def draw(self):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, 50, 50))  # Draw the bird

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

class QLearningAgent:
    def __init__(self):
        self.num_states = 20  # Number of states
        self.num_actions = 2  # Number of actions (0: no flap, 1: flap)
        self.q_table = np.zeros((self.num_states, self.num_actions))  # Q-table initialization
        
    def get_state(self, bird, pipes):
        vertical_distance = bird.y - min(pipes[0].height, pipes[1].height)
        distance_to_pipe = min(pipes[0].x, pipes[1].x) - bird.x
        vertical_bins = 4  # Adjust the number of bins
        distance_bins = 5  # Adjust the number of bins
        state_vertical = min(vertical_distance // (SCREEN_HEIGHT // vertical_bins), vertical_bins - 1)
        state_distance = min(distance_to_pipe // (SCREEN_WIDTH // distance_bins), distance_bins - 1)
        state_index = state_vertical * distance_bins + state_distance
        return state_index
    
    # Rest of the Q-learning agent class...

    
    def choose_action(self, state):
        print("State:", state)
        print("Q-table shape:", self.q_table.shape)
        return np.argmax(self.q_table[state])  # Exploit

    
    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + DISCOUNT_FACTOR * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += LEARNING_RATE * td_error

# Main game function
def main():
    bird = Bird()
    pipes = [Pipe(SCREEN_WIDTH + i * 300) for i in range(2)]
    base = Base()
    agent = QLearningAgent()

    for episode in range(EPISODES):
        bird = Bird()
        pipes = [Pipe(SCREEN_WIDTH + i * 300) for i in range(2)]
        score = 0
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bird.flap()

            bird.update()
            
            state = agent.get_state(bird, pipes)
            action = agent.choose_action(state)

            # Apply action
            if action == 1:
                bird.flap()
            
            # Move pipes
            for pipe in pipes:
                pipe.move()
                if pipe.off_screen():
                    pipes.remove(pipe)
                    pipes.append(Pipe(SCREEN_WIDTH))

            # Check for collisions
            for pipe in pipes:
                if (pipe.x < bird.x + 50 < pipe.x + PIPE_WIDTH) and (bird.y < pipe.height or bird.y + 50 > pipe.height + PIPE_GAP):
                    reward = -100  # Penalty for collision
                    agent.update_q_table(state, action, reward, state)
                    break
            else:
                reward = 1  # Reward for surviving
                agent.update_q_table(state, action, reward, state)

            if (bird.y+50 > base.y or bird.y < base.height):
                break

            score += 1
            
            screen.fill(WHITE)
            bird.draw()
            base.draw()
            for pipe in pipes:
                pipe.draw()
            pygame.display.flip()
            clock.tick(FPS)

if __name__ == "__main__":
    main()
