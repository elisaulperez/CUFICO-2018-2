#import matplotlib.pyplot as plt
#import numpy as np

#se importan las librerias
from mpl_toolkits.mplot3d import axes3d
##import numpy as np
##import matplotlib.pyplot as plt
import matplotlib.animation as animation


import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from particle import Particle as particle

Carga1=1.0
Carga2=-1.0

p1=particle(0.0,0.0,0.0,0.0,0.0,1.0,10.0,Carga1)
p2=particle(1.0,0.0,0.0,0.0,0.0,-1.0,10.0,Carga2)

x2=[];y2=[];z2=[];vx2=[]; vy2=[]; vz2=[]

x=[];y=[];z=[];vx=[]; vy=[]; vz=[]

x1final=[]
y1final=[]
z1final=[]
x2final=[]
y2final=[]
z2final=[]

BX=0.0
BY=0.0
BZ=10
i=0

while i<50000:
    x.append(p1.X); y.append(p1.Y); z.append(p1.Z)
    vx.append(p1.VX); vy.append(p1.VY); vz.append(p1.VZ)
    x2.append(p2.X); y2.append(p2.Y); z2.append(p2.Z)
    vx2.append(p2.VX); vy2.append(p2.VY); vz2.append(p2.VZ)
    p1.fuerza(p2.X,p2.Y,p2.Z,p2.Carga,BX,BY,BZ)
    p2.fuerza(p1.X,p1.Y,p1.Z,p1.Carga,BX,BY,BZ)
    p1.time_evol(p1.fx,p1.fy,p1.fz,0.001)
    p2.time_evol(p2.fx,p2.fy,p2.fz,0.001)

    i+=1

for i in range(len(x)/100):
    x1final.append(x[int(100*i)])
    y1final.append(y[int(100*i)])
    z1final.append(z[int(100*i)])
    x2final.append(x2[int(100*i)])
    y2final.append(y2[int(100*i)])
    z2final.append(z2[int(100*i)])    


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.cla()
ax.set_xlim(0,1)
ax.set_ylim(0,-3)
ax.set_zlim(-0.5,0.5)
p1.trayectorias(x1final, y1final, z1final, x2final, y2final, z2final)

ani = animation.FuncAnimation(fig, p1.update, frames=xrange(len(x1final)), 
    fargs=(ax, fig), interval=100)
ani.save("videoanimacion.htm", fps = 30)


