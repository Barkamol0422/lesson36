import pygame
pygame.init()
w,h=800,600
s=pygame.display.set_mode((w,h))
pygame.display.set_caption("Game")
c1 = (255,255,255)
c2 = (0,0,255)
c3 = (255,0,0)
r=pygame.Rect(100,100,50,50)
q=pygame.Rect(300,300,50,50)
v=5
f=pygame.time.Clock()
x=True
while x:
    s.fill(c1)
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            x=False
    k=pygame.key.get_pressed()
    if k[pygame.K_LEFT]:
        r.x-=v
    if k[pygame.K_RIGHT]:
        r.x+=v
    if k[pygame.K_UP]:
        r.y-=v
    if k[pygame.K_DOWN]:
        r.y+=v
    pygame.draw.rect(s,c2,r)
    pygame.draw.rect(s,c3,q)
    pygame.display.flip()
    f.tick(60)
pygame.quit()
