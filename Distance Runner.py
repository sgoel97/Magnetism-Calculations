#Program -find the magnetic
#field on every point of a
#sphere of chosen radius

import math

r= float(input("Radius:"))
ri=int(r)
while r>ri:
    ri=ri+1
print ("Enter Point #1")
x= float(input("x-coordinate:"))
while x>r or x<-r:
    print ("x-coordinate cannot be larger than radius")
    x= float(input("x-coordinate:"))
y= float(input("y-coordinate:"))
while y>r or y<-r:
    print ("y-coordinate cannot be larger than radius")
    y= float(input("y-coordinate:"))
z= float(input("z-coordinate:"))
while z>r or z<-r:
    print ("z-coordinate cannot be larger than radius")
    z= float(input("z-coordinate:"))
rij=math.sqrt(((x)**2)+((y)**2)+((z)**2))
while rij>r:
    print ("point is outside the circle")
    x=float(input("x-coordinate:"))
    while x>r or x<-r:
        print ("x-coordinate cannot be larger than radius")
        x=float(input("x-coordinate:"))
    y=float(input("y-coordinate:"))
    while y>r or y<-r:
        print ("y-coordinate cannot be larger than radius")
        y=float(input("y-coordinate:"))
    z=float(input("z-coordinate:"))
    while z>r or z<-r:
        print ("z-coordinate cannot be larger than radius")
        z=float(input("z-coordinate:"))
    rij=math.sqrt(((x)**2)+((y)**2)+((z)**2))
print ("Enter Point #2")
xd= float(input("x-coordinate:"))
while xd>r or xd<-r:
    print ("x-coordinate cannot be larger than radius")
    xd= float(input("x-coordinate:"))
yd= float(input("y-coordinate:"))
while yd>r or yd<-r:
    print ("y-coordinate cannot be larger than radius")
    yd= float(input("y-coordinate:"))
zd= float(input("z-coordinate:"))
while zd>r or zd<-r:
    print ("z-coordinate cannot be larger than radius")
    zd= float(input("z-coordinate:"))
rijd=math.sqrt(((xd)**2)+((yd)**2)+((zd)**2))
while rijd>r:
    print ("point is outside the circle")
    xd=float(input("x-coordinate:"))
    while xd>r or xd<-r:
        print ("x-coordinate cannot be larger than radius")
        xd=float(input("x-coordinate:"))
    yd=float(input("y-coordinate:"))
    while y>r or y<-r:
        print ("y-coordinate cannot be larger than radius")
        yd=float(input("y-coordinate:"))
    zd=float(input("z-coordinate:"))
    while zd>r or zd<-r:
        print ("z-coordinate cannot be larger than radius")
        zd=float(input("z-coordinate:"))
    rijd=math.sqrt(((xd)**2)+((yd)**2)+((zd)**2))

print ('Point #1:(',x,',',y,',',z,')')
print ('Point #2:(',xd,',',yd,',',zd,')')

xint=xd-x
yint=yd-y
zint=zd-z

while x<0:
    x=x*(-1)
while y<0:
    y=y*(-1)
while z<0:
    z=z*(-1)
    
xone=ri-x
yone=ri-y
zone=ri-z
xtwo=(-1)*(x+ri)
ytwo=(-1)*(y+ri)
ztwo=(-1)*(z+ri)
totalx=0
totaly=0
totalz=0
counter=0
rijint=math.sqrt(((xint)**2)+((yint)**2)+((zint)**2))
rijdiv=int(rijint/(0.1))
xdis=(xint)/(rijdiv)
ydis=(yint)/(rijdiv)
zdis=(zint)/(rijdiv)
while rijint>0.05:
    while xone>=xtwo:
        while yone>=ytwo:
            while zone>=ztwo:
                if xone==0 and yone==0 and zone==0:
                    zone=zone-1
                else:
                    rij=math.sqrt(((xone)**2)+((yone)**2)+((zone)**2))
                    rijc=math.sqrt(((x+xone)**2)+((y+yone)**2)+((z+zone)**2))
                    if rijc>r:
                        zone=zone-1
                    else:
                        Hx=((3*xone*zone)/((rij)**5))
                        Hy=((3*yone*zone)/((rij)**5))
                        Hz=(((2*((zone)**2))-((xone)**2)-((yone)**2))/((rij)**5))
                        totalx=totalx+Hx
                        totaly=totaly+Hy
                        totalz=totalz+Hz
                        zone=zone-1
            yone=yone-1
            zone=ri-z+((zdis)*(counter))
        xone=xone-1
        yone=ri-y+((ydis)*(counter))
    print(totalx,totaly,totalz)
    H=math.sqrt(((totalx)**2)+((totaly)**2)+((totalz)**2))
    if H<(10**(-15)):
        print ("total H: 0.0")
    else:
        print ("total H:",H)
    totalx=0
    totaly=0
    totalz=0
    rijint=rijint-(0.1)
    counter=counter+1
    xone=ri-x+((xdis)*(counter))
    yone=ri-y+((ydis)*(counter))
    zone=ri-z+((zdis)*(counter))

x=xd
y=yd
z=zd
rij=math.sqrt(((xd)**2)+((yd)**2)+((zd)**2))

while xd<0:
    xd=xd*(-1)
while yd<0:
    yd=yd*(-1)
while zd<0:
    zd=zd*(-1)

xone=ri-xd
yone=ri-yd
zone=ri-zd
xtwo=(-1)*(xd+ri)
ytwo=(-1)*(yd+ri)
ztwo=(-1)*(zd+ri)
totalx=0
totaly=0
totalz=0

while xone>=xtwo:
    while yone>=ytwo:
        while zone>=ztwo:
            if xone==0 and yone==0 and zone==0:
                zone=zone-1
            else:
                rij=math.sqrt(((xone)**2)+((yone)**2)+((zone)**2))
                rijc=math.sqrt(((xd+xone)**2)+((yd+yone)**2)+((zd+zone)**2))
                if rijc>r:
                    zone=zone-1
                else:
                    Hx=((3*xone*zone)/((rij)**5))
                    Hy=((3*yone*zone)/((rij)**5))
                    Hz=(((2*((zone)**2))-((xone)**2)-((yone)**2))/((rij)**5))
                    totalx=totalx+Hx
                    totaly=totaly+Hy
                    totalz=totalz+Hz
                    zone=zone-1
        yone=yone-1
        zone=ri+zd
    xone=xone-1
    yone=ri+yd

H=math.sqrt(((totalx)**2)+((totaly)**2)+((totalz)**2))
if H<(10**(-15)):
    print ("total H: 0.0")
else:
    print ("total H:",H)

    



        
