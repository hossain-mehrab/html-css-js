# import math

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Cannot divide by zero!"

# def power(a, b):
#     return a ** b

# def square_root(a):
#     return math.sqrt(a)

# def logarithm(a, base):
#     return math.log(a, base)

# def factorial(a):
#     return math.factorial(a)

# print("Scientific Calculator")
# print("Operations:")
# print("1. Add")
# print("2. Subtract")
# print("3. Multiply")
# print("4. Divide")
# print("5. Power")
# print("6. Square Root")
# print("7. Logarithm")
# print("8. Factorial")

# choice = input("Enter operation number (1-8): ")

# if choice in ['1', '2', '3', '4', '5']:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))

#     if choice == '1':
#         result = add(num1, num2)
#         operation = "Addition"
#     elif choice == '2':
#         result = subtract(num1, num2)
#         operation = "Subtraction"
#     elif choice == '3':
#         result = multiply(num1, num2)
#         operation = "Multiplication"
#     elif choice == '4':
#         result = divide(num1, num2)
#         operation = "Division"
#     elif choice == '5':
#         result = power(num1, num2)
#         operation = "Power"

#     print(f"{operation} of {num1} and {num2} is: {result}")

# elif choice in ['6', '7', '8']:
#     num = float(input("Enter the number: "))

#     if choice == '6':
#         result = square_root(num)
#         operation = "Square Root"
#     elif choice == '7':
#         base = float(input("Enter the base: "))
#         result = logarithm(num, base)
#         operation = f"Logarithm (base {base})"
#     elif choice == '8':
#         result = factorial(num)
#         operation = "Factorial"

#     print(f"{operation} of {num} is: {result}")

# else:
#     print("Invalid choice. Please select a valid operation.")



import pygame
import time

# Initialize Pygame
pygame.init()

# Set the window dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Dog")

# Load the dog images
dog_images = [pygame.image.load("dog1.png"), pygame.image.load("dog2.png")]
current_image_index = 0

# Set the initial position of the dog
x = 50
y = 50

# Set the initial speed of the dog
speed = 5

# Set the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the dog horizontally
    x += speed

    # Reverse the direction if the dog reaches the window edges
    if x <= 0 or x >= WIDTH - dog_images[current_image_index].get_width():
        speed *= -1

    # Display the background color
    win.fill((255, 255, 255))

    # Display the dog image
    win.blit(dog_images[current_image_index], (x, y))

    # Update the current dog image index
    current_image_index = (current_image_index + 1) % len(dog_images)

    # Update the window display
    pygame.display.update()

    # Delay for smoother animation
    time.sleep(0.1)

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
