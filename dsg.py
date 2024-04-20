import pygame
import random

pygame.init()

# Set up the display
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Traffic Simulator")

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the background
background_image = pygame.image.load("Images/intersection4.png")
background_surface = pygame.Surface(screen.get_size())
background_surface.blit(background_image, (0, 0))

# Set up the vehicle sprites
vehicle_images = ["Images/up/ambulance.png", "Images/up/bike.png", "Images/up/car.png", "Images/up/truck.png"]
vehicle_sprites = []

for i in range(len(vehicle_images)):
    vehicle_sprites.append(pygame.image.load(vehicle_images[i]))

# Set up the signal timers
signalTimers = [0, 0, 0, 0]
vehicleCounts = [0, 0, 0, 0]
signalIntervals = [100, 100, 100, 100]

# Set up the prevJn timer and counts
prevJnInterval = 100
prevJnTimer = 0
prevJnCount = 0
prevJnTimer2 = 0
prevJnCount2 = 0
prevJnTimer3 = 0
prevJnCount3 = 0
prevJnTimer4 = 0
prevJnCount4 = 0

# Set up the emergency variables
emergency_right = False

while True:
    screen.blit(background_surface, (0, 0))

    # Draw the vehicles
    for i in range(len(vehicle_sprites)):
        screen.blit(vehicle_sprites[i], (100 + i * 150, 500))

    # Update the signal timers
    for i in range(len(signalTimers)):
        signalTimers[i] += 1

    # Check if the signal timers are greater than the interval
    for i in range(len(signalTimers)):
        if signalTimers[i] >= signalIntervals[i]:
            signalTimers[i] = 0
            vehicleCounts[i] += 1

    # Generate random integers for prevJn counts
    prevJnTimer += 1
    if prevJnTimer >= prevJnInterval:
        prevJnCount = random.randint(1, 20)  # Generate a random integer between 1 and 10
        prevJnTimer = 0

    prevJnTimer2 += 1
    if prevJnTimer2 >= prevJnInterval:
        prevJnCount2 = random.randint(1, 20)  # Generate a random integer between 1 and 10
        prevJnTimer2 = 0

    prevJnTimer3 += 1
    if prevJnTimer3 >= prevJnInterval:
        prevJnCount3 = random.randint(1, 20)  # Generate a random integer between 1 and 10
        prevJnTimer3 = 0

    prevJnTimer4 += 1
    if prevJnTimer4 >= prevJnInterval:
        prevJnCount4 = random.randint(1, 20)  # Generate a random integer between 1 and 10
        prevJnTimer4 = 0

    # Draw the prevJn counts
    count1Text = font.render("PrevJn: " + str(prevJnCount), True, white)
    screen.blit(background_surface, (71, 287))
    screen.blit(count1Text, (71, 287))

    count1Text = font.render("PrevJn" + str(prevJnCount2), True, white)
    screen.blit(background_surface, (841,53))
    screen.blit(count1Text, (841,53))

    count1Text = font.render("PrevJn" + str(prevJnCount3), True, white)
    screen.blit(background_surface, (1227,579))
    screen.blit(count1Text, (1227,579))

    count1Text = font.render("PrevJn" + str(prevJnCount4), True, white)
    screen.blit(background_surface, (449,737))
    screen.blit(count1Text, (449,737))

    # Check for emergency
    if emergency_right==True:
        count1Text = font.render('Emergency!!', True, white)
        screen.blit(background_surface, (1005,605))
        screen.blit(count1Text, (1005,605))

    pygame.display.update()
