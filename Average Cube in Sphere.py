#Program - create a sphere of chosen radius
#and find the average magnetic field on every point
#of a cube with side lenght 1 using intervals of 0.1

import math

r= float(input("Radius:"))
ri=int(r)
while r>ri:
    ri=ri+1
x=0.5
y=0.5
z=0.5
totalxx=0
totalyy=0
totalzz=0

while x>=(-0.5):
    while y>=(-0.5):
        while z>=(-0.5):
            if x==0 and y==0 and z==0:
                z=z-(0.1)
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
                totalxx=totalxx+totalx
                totalyy=totalyy+totaly
                totalzz=totalzz+totalz
                totalx=0
                totaly=0
                totalz=0
                z=z-(0.1)
        y=y-(0.1)
        z=(0.5)
    x=x-(0.1)
    y=(0.5)

print(totalxx)
print(totalyy)
print(totalzz)
    


