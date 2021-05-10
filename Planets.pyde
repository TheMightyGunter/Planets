oList = [] #orbit size list
pList = [] #planet size list
cList = [] #planet color list
sPoint = [] #starting point list 1
rList = [] #rotation speed list 2

eSize = random(10,100)
sunSize = eSize
increm = 0


def setup():
    size(800,800)
    global oList,pList,cList,eSize,increm

    noFill()
    stroke('#FFFFFF')
    
    
    for i in range(int(random(1,10))):
        eSize += random(40,100) 
        oList.append(eSize)
    
        r = lambda: int(random(0,255)) #random colour gen
        c = '#%02X%02X%02X' % ( r(),r(),r() ) 
        cList.append(c)
        
        planetSize = (random(5,40))
        pList.append(planetSize)
        
        sPoint.append(random(0,TAU))
        rList.append(random(0.005,0.01))
        
def draw():
    background('#222222')
    translate(width/2, height/2)
    fill('#FF9900')
    ellipse(0, 0, sunSize,sunSize)
    global increm,rList, rot
    
    for o in oList:
        noFill()
        stroke('#FFFFFF')
        ellipse(0, 0, oList[increm],oList[increm])#drawing the orbit
        fill(cList[increm])
        
        pushMatrix();
        rotate(sPoint[increm]); sPoint[increm] += rList[increm] 
        noStroke()
        ellipse(oList[increm]/2,0, pList[increm],pList[increm]) #drawing the planet
        popMatrix();
        
        increm += 1
        if increm >= len(oList):
            increm = 0
        
    