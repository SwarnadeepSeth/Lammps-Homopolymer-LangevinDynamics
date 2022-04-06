from math import *
from random import *

ParticleN = 64
ID = 1 
fi = open ("poly1_"+str(ParticleN)+".input","w")

# Output in LAMMPS input format
print ("LAMMPS Description \n", file = fi)
# atom, bond, angle numbers
print (str(ParticleN) + " atoms", file = fi)
print (str(ParticleN-1) + " bonds", file = fi)
print (str(ParticleN-2) + " angles \n", file = fi)
# type details
print ("1" + " atom types", file = fi)
print ("1" + " bond types", file = fi)
print ("1" + " angle types \n", file = fi)
# Box boundary
Lx = 2000
Ly = 2000
Lz = 2000

print (str(-Lx) + " " +  str(Lx) + " xlo" + " xhi", file = fi) # X Box Limits
print (str(-Ly) + " " +  str(Ly) + " ylo" + " yhi", file = fi) # Y Box Limits
print (str(-Lz) + " " +  str(Lz) + " zlo" + " zhi \n", file = fi) # Z Box Limits
# column drescriptions
print ("Atoms # id mol type xu yu zu \n", file = fi)

spacex = 0.9

x=[]
y=[]
z=[]

x.append(0.1)
y.append(0.0)
z.append(0.0)

i = 1
while (i<ParticleN):
    count =0
    xi = uniform(0,0.1)
    yi = uniform(0,0.01)
    x.append (x[0]+spacex*i+xi)
    y.append (y[0]+yi)
    z.append (0.0)
    i=i+1

# Printing particles coordinates
for i in range (ParticleN):
    print (x[i],y[i],z[i])
    print (i+1, ID, ID, x[i],y[i],z[i], file=fi)

# Printing bond connections
print ("\nBonds \n", file = fi)

for i in range (ParticleN-1):
	print (i+1, ID, i+1, i+2, file=fi)

# Printing angle connections
print ("\nAngles \n", file = fi)

for i in range (ParticleN-2):
	print (i+1, ID, i+1, i+2, i+3, file=fi)

# Checking Overlap Crossings
for i in range (ParticleN):
    for j in range (ParticleN):
        if (i != j):
            r = sqrt((x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]))
            if (r < 0.8):
                print ("------------------------------------------------")
                print (i, j, r)
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
