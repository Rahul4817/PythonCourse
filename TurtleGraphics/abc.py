import  pygame
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
x=200
x=200
x_chnge=0
gd=pygame.display.set_mode((500,500))
pygame.display.update()

game_over=False
while game_over==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_chnge=+10
                elif event.key==pygame.K_RIGHT:
                    x_chnge=-10
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                x_chnge=0
    gd.fill(white)
    pygame.draw.rect(gd,red,[x,x,50,50])
    x=x-x_chnge
    pygame.display.update()
pygame.quit()
quit()

