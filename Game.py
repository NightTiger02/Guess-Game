import pygame
import random
import time
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pick The Object")
screen.fill((255,255,255))
pygame.draw.rect(screen, (0,0,0),(220,110,360,150))
pygame.draw.rect(screen, (255,255,255),(225,115,350,140))
text_font = pygame.font.SysFont("Arial.ttf", 105)
text_surface = text_font.render("Play", 1, (0,155,0))
screen.blit(text_surface, (325,150))
home=True
correct_sound = "resources/Correct.mp3"
wrong_sound = "resources/Wrong.mp3"
while home:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        x,y = pygame.mouse.get_pos()
        if (220<x<580) and (110<y<260):
            pygame.draw.rect(screen, (255,255,255),(225,115,350,140))
            screen.blit(pygame.font.SysFont("Arial.ttf", 105).render("Play", 1, (0,255,0)), (325,150))
        else:
            pygame.draw.rect(screen, (255,255,255),(225,115,350,140))
            screen.blit(pygame.font.SysFont("Arial.ttf", 105).render("Play", 1, (0,155,0)), (325,150))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (220<x<580) and (110<y<260):
                home = False
    pygame.display.update()
time.sleep(1)
screen.fill((255,255,255))
pygame.draw.rect(screen, (0,0,0),(650, 10, 120,60))
pygame.draw.rect(screen, (255,255,255),(655, 15, 110,50))
next_font = pygame.font.SysFont("Arial.ttf", 35)
text_surface = next_font.render("Next >", 1, (0,0,0))
screen.blit(text_surface, (675, 28))
Colors = ["Red", "Blue", "Grey", "Green", "Pink", "Purple"] #Append a color name to add it
Shapes = ["Square", "Circle", "Triangle", "Rectangle"] #Add to drawObject method to add a shape as well as here
class Position:
    def __init__(self, x):
        self.color = ""
        self.shape = ""
        self.x = x
        self.y = 100
    def setColor(self, newColor):
        self.color = newColor
    def setShape(self, newShape):
        self.shape = newShape
    def drawObject(self):
        if self.shape == "Square":
            pygame.draw.rect(screen, (0,0,0),(self.x + 50 , self.y + 50, 140,140))
            pygame.draw.rect(screen, self.color,(self.x + 55 , self.y + 55, 130,130))
        elif self.shape == "Rectangle":
            pygame.draw.rect(screen, (0,0,0),(self.x + 30 , self.y + 60, 190, 110))
            pygame.draw.rect(screen, self.color,(self.x + 35 , self.y + 65, 180, 100))
        elif self.shape == "Triangle":
            pygame.draw.polygon(screen, (0,0,0), [(self.x + 120,self.y + 25),(self.x + 60,self.y + 160),(self.x + 185,self.y + 160)], 0)
            pygame.draw.polygon(screen, self.color, [(self.x + 120,self.y + 35),(self.x + 65,self.y + 155),(self.x + 180,self.y + 155)], 0)
        elif self.shape == "Circle":
            pygame.draw.circle(screen, (0,0,0), (self.x + 130, self.y + 150), 90)
            pygame.draw.circle(screen, self.color, (self.x + 130, self.y + 150), 85)
        pygame.display.update()
def GenerateText(Colors, Shapes):
    pygame.draw.rect(screen, (255,255,255),(0, 110, 800,400))
    pygame.draw.line(screen, (0,0,0), (260,100), (260,400), 5)
    pygame.draw.line(screen, (0,0,0), (520,100), (520,400), 5)
    pygame.draw.line(screen, (0,0,0), (0,100), (800,100), 5)
    Object = [random.choice(Colors), random.choice(Shapes)]
    pygame.draw.rect(screen, (255,255,255),(249, 30, 360,60))
    text_font = pygame.font.SysFont("Arial.ttf", 55)
    text_surface = text_font.render(Object[0] + " " + Object[1], 1, (0,0,0))
    screen.blit(text_surface, (250, 35))
    pygame.display.update()
    return Object
def GenerateObjects(Colors, Shapes, Object):
    Win_Position = random.randint(0,2)
    Positions = []
    selected_colors = set()
    selected_colors.add(Object[0])
    for count in range(3):
        Positions.append(Position(260*count))
        new_color = random.choice(Colors)
        if count == Win_Position:
            Positions[Win_Position].setColor(Object[0])
            Positions[Win_Position].setShape(Object[1])
        else:
            Positions[count].setColor(new_color)
            while(Positions[count].color in selected_colors):
                print(selected_colors)
                new_color = random.choice(Colors)
                Positions[count].setColor(new_color)
            Positions[count].setShape(random.choice(Shapes))
            selected_colors.add(new_color)
        Positions[count].drawObject()
    return Win_Position
def WinningCondition(Win_Position, mouse_Position):
    XPosition_to_win = Win_Position*260
    Next = False
    if mouse_Position[1] > 100:
        if XPosition_to_win < mouse_Position[0] < XPosition_to_win + 260:
            tick_font = pygame.font.SysFont("Arial.ttf", 40)
            tick_surface = tick_font.render("Correct!", 1, (2,150,20))
            pygame.mixer.music.load(correct_sound)
            pygame.mixer.music.play()
            screen.blit(tick_surface, (XPosition_to_win+70, 350))
            pygame.display.update()
            time.sleep(3)
            return True
    elif (650 < mouse_Position[0] < 770) and (10 < mouse_Position[1] < 70):
        tick_font = pygame.font.SysFont("Arial.ttf", 40)
        tick_surface = tick_font.render("Answer^", 1, (180,0,0))
        screen.blit(tick_surface, (XPosition_to_win+70, 350))
        pygame.display.update()
        time.sleep(1)
        return True
running = True
Object = GenerateText(Colors, Shapes)
Win_Pos = GenerateObjects(Colors, Shapes, Object)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if WinningCondition(Win_Pos, pos):
                Object = GenerateText(Colors, Shapes)
                Win_Pos = GenerateObjects(Colors, Shapes, Object)
            elif pos[1] > 100:
                for count in range(3):
                    positionx = 260*count
                    if positionx < pos[0] < ((positionx)+260):
                        tick_font = pygame.font.SysFont("Arial.ttf", 40)
                        tick_surface = tick_font.render("Wrong", 1, (180,0,0))
                        pygame.mixer.music.load(wrong_sound)
                        pygame.mixer.music.play()
                        screen.blit(tick_surface, (positionx+70, 350))
                        break
    pygame.display.update()
