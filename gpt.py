import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Intersection Signal Simulation")

# Vehicle counts
current_count = 0
previous_count = random.randint(0, 10)

# Signal timers
signal_timers = [0, 0, 0, 0]  # Timer for each signal [north, south, east, west]

# Initialize signals
signals = [BLACK, BLACK, BLACK, BLACK]  # Color for each signal [north, south, east, west]
signals[0] = GREEN  # Set initial signal as green

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    # Draw signals
    signal_radius = 40
    pygame.draw.circle(screen, signals[0], (400, 100), signal_radius)
    pygame.draw.circle(screen, signals[1], (400, 500), signal_radius)
    pygame.draw.circle(screen, signals[2], (100, 300), signal_radius)
    pygame.draw.circle(screen, signals[3], (700, 300), signal_radius)

    # Update signal timers
    for i in range(4):
        if signal_timers[i] > 0:
            signal_timers[i] -= 1
        elif signals[i] == YELLOW:
            signals[i] = RED

    # Handle emergency scenario (ambulance)
    if current_count > 10:  # Adjust the condition based on your criteria for an ambulance arrival
        signals = [RED, RED, RED, RED]  # Turn all signals to red
        ambulance_direction = random.randint(0, 3)  # Randomly select the direction of the ambulance
        signals[ambulance_direction] = GREEN  # Turn the signal of the ambulance direction to green

    # Update vehicle counts
    previous_count = current_count
    current_count = random.randint(0, 10)  # Generate random vehicle count

    # Update signal timers based on vehicle counts
    for i in range(4):
        if signals[i] == GREEN and signal_timers[i] == 0:
            weighted_avg = round(0.8 * current_count + 0.2 * previous_count)
            default_red = 20 - ((weighted_avg / 20) * 20)
            default_red = round(default_red)
            if default_red < 20:
                default_red = default_red - 20
            signal_timers[i] = default_red

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
