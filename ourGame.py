import pygame

pygame.init()
win = pygame.display.set_mode((800, 600))
win.fill([255, 255, 255])
pygame.display.set_caption('Our Game')

ball = {
    "speed": 1,
    "y": 300,
    "x": 400,
    "width": 20,
    "color": (68, 208, 145)
}

plate = {
    "y": 550,
    "x": 350,
    "width": 100,
    "height": 10,
    "color": (112, 204, 225)
}

frameRate = 60
running = True

while running:
    pygame.draw.rect(win, [255, 255, 255], (0, 0, 800, 600))
    pygame.time.delay(16)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(win, (255, 255, 255), (plate["x"], plate["y"], plate["width"], plate["height"]))
            plate["x"] = event.pos[0]
    pygame.draw.rect(win, plate["color"], (plate["x"], plate["y"], plate["width"], plate["height"]))
    pygame.draw.circle(win, ball["color"], (ball["x"], ball["y"]), ball["width"])
    ball["y"] += 1
    pygame.display.update()
    if ball["y"] > plate["y"] - ball["width"] & ball["x"] > plate["x"] - ball["width"]:
        ball["y"] = 0
pygame.quit()