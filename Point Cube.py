import math

r= float(input("Radius:"))
ri=int(r)
while r>ri:
    ri=ri+1
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
while rij>((math.sqrt(3))*r):
    print ("point is outside the cube")
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
print ('Point:(',x,',',y,',',z,')')

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

while xone>=xtwo:
    while yone>=ytwo:
        while zone>=ztwo:
            if xone==0 and yone==0 and zone==0:
                zone=zone-1
            else:
                rij=math.sqrt(((xone)**2)+((yone)**2)+((zone)**2))
                rijc=math.sqrt(((x+xone)**2)+((y+yone)**2)+((z+zone)**2))
                if rijc>((math.sqrt(3))*r):
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
        zone=ri+z
    xone=xone-1
    yone=ri+y

H=math.sqrt(((totalx)**2)+((totaly)**2)+((totalz)**2))
if H<(10**(-10)):
    print ("total H: 0.0")
else:
    print ("total H:",H)

    


