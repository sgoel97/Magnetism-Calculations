import math

r= float(input("Radius:"))
ri=int(r)
while r>ri:
    ri=ri+1
x=ri
y=ri
z=ri
totalxx=[]
totalyy=[]
totalzz=[]
counter = 0
distance=math.sqrt(((x)**2)+((y)**2)+((z)**2))
while x>=(-ri):
    while y>=(-ri):
        while z>=(-ri):
            distance=math.sqrt(((x)**2)+((y)**2)+((z)**2))
            if x==0 and y==0 and z==0:
                z=z-1
                distance=math.sqrt(((x)**2)+((y)**2)+((z)**2))
            else:
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
                        zone=ri+z
                    xone=xone-1
                    yone=ri+y
                if distance > r:
                    counter = counter + 1
                elif distance <= r:
                    totalxx.append(totalx)
                    totalyy.append(totaly)
                    totalzz.append(totalz)
                    print(x, y, z)
                totalx=0
                totaly=0
                totalz=0
                z=z-1
                distance=math.sqrt(((x)**2)+((y)**2)+((z)**2))
        y=y-1
        z=ri
    x=x-1
    y=ri
subpoint = (ri**2)+1-counter
print(totalxx)
print(totalyy)
print(totalzz)
    


