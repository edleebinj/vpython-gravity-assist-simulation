from vpython import*

vearth = -30000.0
vshipy = -130000.0
vshipx = -100000.0
earthradius = 13710000.0*2
shipradius = 3000000.0*2
earthdensity = 135270.0*2
shipdensity = 1.0

energy=0

scene=canvas(height=500,width=1200,x=0,y=0,center=vector(0,0,0),range=300000000,ambient=color.gray(0.3))

bg=box(pos=vec(0,0,-20000000),width=1,height=2000000000,length=2000000000,texture={'file':"https://upload.wikimedia.org/wikipedia/commons/6/62/Starsinthesky.jpg",'turn':-1})
earth=sphere(pos=vector(250000000,-200000000,0),radius=earthradius,v=vector(vearth,0,0),a=vector(0,0,0),texture={'file':textures.earth,'place':['all']},emissive=True,axis=vec(0,0,1))
ship=sphere(pos=vector(537100000.0,103710000.0,0),radius=shipradius,v=vector(vshipx,vshipy,0),color=color.yellow,emissive=True)
#scene.lights=[]
attach_trail(ship,radius = 2000000,color = color.white)
#scene.camera.follow(earth)

M=4/3*3.14159*earth.radius*earth.radius*earth.radius*earthdensity
m=4/3*3.14159*ship.radius*ship.radius*ship.radius*shipdensity

gd=graph(title="v-t plot",width=300,height=300,xtitle="t",ytitle="v")
f1=gcurve(color=color.blue)

#f2=gcurve(color=color.red)


def gforce(M,m,r):
    r=mag(earth.pos-ship.pos)
    return (0.0000000000667*M*m/(r*r))*(earth.pos-ship.pos)/mag(earth.pos-ship.pos)

t=0.0
dt=0.01*3000
r=mag(earth.pos-ship.pos)

while True:
    rate(50)

    t+=dt

    r=mag(earth.pos-ship.pos)

    energy=-0.0000000000667*M*m/r+mag(ship.v)*mag(ship.v)*m/2+mag(earth.v)*mag(earth.v)*M/2

    earth.rotate(angle=0.01,axis=earth.axis)#0.0022

    earth.a=gforce(M,m,r)/M
    earth.v+=earth.a*dt
    earth.pos+=earth.v*dt
    #print(round(energy,-30))
    
    ship.a=gforce(M,m,r)/m
    ship.v+=ship.a*dt
    ship.pos+=ship.v*dt
    #print(mag(ship.v))
    
    f1.plot(pos=(t,mag(ship.v)))
    #f2.plot(pos=(t,-0.0000000000667*M*m/r))
