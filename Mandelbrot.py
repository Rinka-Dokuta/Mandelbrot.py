import pygame
import math
import cmath #This moduel handles complex numbers

pygame.init()
pygame.display.set_caption("mandelbrot") #window title
screen = pygame.display.set_mode((800, 800)) #game screen
screen.fill((0,0,0))

WIDTH = 800
HEIGHT = 800


#Mandelbrot Function
def Mandelbrot(c):
    z = 0
    counter = 0

    while abs(z) < 2 and counter < 80:
        z = z**2 + c
        counter += 1

    return counter

The Render Algorithm
i = 0
while i < WIDTH:
    i += 1
    j = 0
    while j < HEIGHT:
        #j += 1
        #screen.set_at((i, j), (255, 0, 0)) #Set pixel at (i, j) to red
        
    i += 1
    
#Updated Drawing Algorithm
    c = complex(i, j)#create a complex number from iterators
    num = Mandelbrot(c)#call the function
    #these if statements are just to differentiate the colors more, not needed if you want black & white image
    if num < 20:
        screen.set_at((int(i*200+400), int(j*200+400)), (num*8,num*6,num*12))
    elif num < 40:
        screen.set_at((int(i*200+400), int(j*200+400)), (num*2,num/2,num*6))
    elif num < 80:
        screen.set_at((int(i*200+400), int(j*200+400)), (255, 255, 255)) #white
    else:
        screen.set_at((int(i*200+400), int(j*200+400)), (num*3,num/2,num*2))   
    #print("num is ", num, "at", i*100+400, j*100+400)
    
    pygame.display.flip() #puts pixel on screen
    
i = -2 #lower bound for real axis
while i<2: #upper bound for real (horizontal) axis
    i+=1 #make this number smaller to increase picture resolution
    
    j = -2 #lower bound for imaginary axis
    while j<2: #upper bound for imaginary (vertical) axis
        j+=1 #make this number smaller to increase picture resolution
                      
    













pygame.time.wait(10000)#Payse to see the picture
pygame.quit()#quit pygame




