import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

screenWidth = 500
screenHeight = 500
x, y = 50, 440
width, height = 40, 60
vel = 5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(50)  # milisecond

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel

    if not (isJump):

        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount**2) * 0.5 * neg # y-=(jumpCount*abs(jumpCount))*0.5
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()