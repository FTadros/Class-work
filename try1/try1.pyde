
import random
c=-1200
z=-600
x=0 
b=0
g=0
r=0
a=100
sunh=600
moonh=1000
t=0
n=4
s=100
l=247
m=222
h=85
sunw=500
rx=-100                                                                 
ry=900
ra=70
rb=20


def setup():
    size(1500, 1000)
    
def draw():
    global x
    global z
    global r
    global g
    global b
    global a
    global sunh
    global moonh
    global t
    global n
    global l
    global m
    global h
    global s
    global sunw
    global rx
    global ry
    global ra
    global rb
    global r1
    global r2
    global r3
    global r4
    global r5
    global r6
    global c

    if z < -500:#colour generator
        r1 = random.randint(0,255)
        r2 = random.randint(0,255)
        r3 = random.randint(0,255)
    if c<-1000:
        r4 = random.randint(0,255)
        r5 = random.randint(0,255)
        r6 = random.randint(0,255)
        
    if x>=width+width/2:
        x=0
    if z>=width:
        z=-600
    
    if c>=1500:
        c=-1200
    x+=5 #speed of x
    z+=3 #speed of bus
    c+=7 #speed of car
   
    t+=1#time
    background(r, g, b)#sky
    
    if t<=140:
        r=64 
        g=40 
        b=74
    
    elif a!= -440.125 and s!=-240.125:
        r-=.25
        g-=.125
        b-=.125
        n+=.125#colour(suns)
        a-=.130#size of shadow(sun)
        s-=.125#size of sun 
#b=64
#g=40
#r=74
    
    noStroke()
    fill(r,g,b)
    ellipse(width/2, 600, a*16, a*16)
#115,67,75   
    fill(115-n,67-n,75-n)
    ellipse(width/2, 600, a*8, a*8)
    
    fill(179-n,77-n,37-n)
    ellipse(width/2, 600, a*4, a*4)
    
    fill(240-n,126-n,7-n)# sun2
    ellipse(width/2, 600, a*2, a*2)
    
    fill(l,m,h)
    ellipse(width/2, sunh, s, s)#sun
    rx+=10
    
    if rx==100:
        rx=0 
    
    noStroke()
    fill(60, 150, 255)#water
    rect(0, 600, 10000, 10000)
    
    if t>=900 and a>0:
        sunh+=+1.25
    elif s<0 and sunh!=300:
        sunh-=.125
    
    if a<0:
        a=0
    if t>=1008:
        l=255
        m=255
        h=255
        #star
        fill(l,m,h)
    
    fill(70)
    rect(0,800,5000,2000)#road
    
    fill(102, 51, 0)
    rect(rx,680, 30, 150)#railing
    rect(rx+100, 680,30,150)
    rect(rx+200, 680,30,150)
    rect(rx+300, 680,30,150)
    rect(rx+400, 680,30,150)
    rect(rx+500, 680,30,150)
    rect(rx+600, 680,30,150)
    rect(rx+700, 680,30,150)
    rect(rx+800, 680,30,150)
    rect(rx+900, 680,30,150)
    rect(rx+1000, 680,30,150)
    rect(rx+1100, 680,30,150)
    rect(rx+1200, 680,30,150)
    rect(rx+1300, 680,30,150)
    rect(rx+1400, 680,30,150)
    rect(0,745,1500,30)
    
    for x in range(100):
        print(rx+x,ry,70,20)
    
    fill(255)#lines
    rect(rx,ry,70,20)
    rect(rx+100,ry,ra,rb)
    rect(rx+200,ry,ra,rb)
    rect(rx+300,ry,ra,rb)
    rect(rx+400,ry,ra,rb)
    rect(rx+500,ry,ra,rb)
    rect(rx+600,ry,ra,rb)
    rect(rx+700,ry,ra,rb)
    rect(rx+800,ry,ra,rb)
    rect(rx+900,ry,ra,rb)
    rect(rx+1000,ry,ra,rb)
    rect(rx+1100,ry,ra,rb)
    rect(rx+1200,ry,ra,rb)
    rect(rx+1300,ry,ra,rb)
    rect(rx+1400,ry,ra,rb)
    rect(rx+1500,ry,ra,rb)
    rect(rx+1600,ry,ra,rb)
    
    
    fill(r1, r2, r3)
    rect(z,655,500,200,10)#bus body
    
    fill(1)
    rect(z,655,70,100,5)#bus front window
    
    
    fill(1)
    ellipse(z+100, 850, 95, 95,)#wheel front
    fill(255)
    ellipse(z+100,850, 50,50)
    
    fill(1)
    ellipse(z+400, 850, 95, 95,)#wheel back
    fill(255)
    ellipse(z+400,850, 50,50)
    
    fill(1)
    rect(z+100,675,50,80)#window 1
    
    fill(1)
    rect(z+200,675,50,80)#window 2
    
    fill(1)
    rect(z+300,675,50,80)#window 3
    
    fill(1)
    rect(z+400,675,50,80)#window 4

    fill(1)
    rect(z,655,70,100)#bus front window

    fill(r4,r5,r6)
    rect(c,800,257,150,50,250,0,0)#car
    
    fill(1)
    ellipse(c+40, 950, 95, 95,)#wheel front
    fill(255)
    ellipse(c+40,950, 50,50)
    
    fill(1)
    ellipse(c+220,950, 95, 95,)#wheel back
    fill(255)
    ellipse(c+220,950, 50,50)
    
    rect(c,800,40,80,500,0,0,0)


#make bus outline>>
#make line strips>>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
#make sunset>>
#make birds<<
#make the sun set into the night>>
#add diff cars>>
#add the random element into the colour of cars and buses>>
#road rails
#fix car, >>
#make delta carbus random
#add stars
#add diff passangers
