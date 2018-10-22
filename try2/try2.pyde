import math

#variables
c=-1200
z=-600
x=0 
b=0
g=0
r=0
a=100
sunh=600
t=0
n=4
s=100
l=247
m=222
h=85
rx=-100                                                                 
ry=900
ra=70
rb=20

def setup():
    size(1300, 1000)#dimensions
    
def draw():
#globals
    global x
    global z
    global r
    global g
    global b
    global a
    global sunh
    global t
    global n
    global l
    global m
    global h
    global s
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
    global stary
    global starx
    
    background(r, g, b)#sky
    if z < -500:#colour generator
        r1 = random(0,255)
        r2 = random(0,255)
        r3 = random(0,255)
    if c<-1000:
        r4 = random(0,255)
        r5 = random(0,255)
        r6 = random(0,255)
        
    if x>=width+width/2:#bus loop
        x=0
    if z>=width:#car loop
        z=-600
    
    if c>=1500:
        c=-1200
    x+=5 #speed of x
    z+=5 #speed of bus
    c+=8 #speed of car
    rx+=10#movement of rails and road lines 
    t+=1#time*28
    
    
    if t<=140:
        r=64 
        g=40 
        b=74
    
    elif a!= -440.125 and s!=-240.125:
        r-=.25#shade of bg(r)
        g-=.125#shade of bg(g)
        b-=.125#shade of bg(b)
        n+=.125#colour(suns)
        a-=.150#size of shadow(sun)
        s-=.125#size of sun 
    
    
    noStroke()
    fill(r,g,b)
    ellipse(width/2, 600, a*16, a*16)#outmost  
    
    fill(115-n,67-n,75-n)
    ellipse(width/2, 600, a*8, a*8)
    
    fill(179-n,77-n,37-n)
    ellipse(width/2, 600, a*4, a*4)
    
    fill(240-n,126-n,7-n)#inmost
    ellipse(width/2, 600, a*2, a*2)
    
    fill(l,m,h)
    ellipse(width/2, sunh, s, s)#actual sun
    
    noStroke()
    fill(60, 150, 255)#water
    rect(0, 600, 10000, 10000)
    
    fill(70)
    rect(0,800,5000,2000)#road
    
    if t>=900 and a>0:
        sunh+=+1.25
    elif s<-10 and sunh!=300:
        sunh-=.125
    
    if a<0:
        a=0
    if s<0:
        l=255
        m=255
        h=255
        
    if rx==100:
        rx=0
    
    for lline in range(0,1700, 100):
        fill(102, 51, 0)
        noStroke()
        rect(0,745,1500,30)
        stroke(10)
        rect(rx+lline,680, 30, 150)
        noStroke()
        fill(255)
        rect(rx+lline,ry,70,20)
    
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
#road rails>>
#fix car, >>
#make delta carbus random<<
#add stars<<
#add diff passangers<<
