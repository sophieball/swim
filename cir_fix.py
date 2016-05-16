import graphics
from graphics import *
import re

win = GraphWin("visual", 1400, 800, autoflush = False)

circles=[]
cir_text=[]
freq=[1,1,1,1,1]
srcs=[0,0,0,0,0]
dests=[0,0,0,0,0]
hasharr = [0]


#save space for circles
circles.append(Circle(Point(700, 400), freq[0]))
circles.append(Circle(Point(300, 400), freq[1]))
circles.append(Circle(Point(900, 200), freq[2]))
circles.append(Circle(Point(500, 200), freq[3]))
circles.append(Circle(Point(400, 600), freq[4]))
cir_text.append(Text(circles[0].getCenter(), 0))
cir_text.append(Text(circles[1].getCenter(), 0))
cir_text.append(Text(circles[2].getCenter(), 0))
cir_text.append(Text(circles[3].getCenter(), 0))
cir_text.append(Text(circles[4].getCenter(), 0))
for i in range(1,5):
    cir_text[i].setFill("white")

for i in range(0,5):
    circles[i].draw(win)
    cir_text[i].draw(win)
update()


vfile = open("freq", "r")
hfile = open("arrout", "r")
hline = hfile.readline()
while(len(hline) != 0):
    if(hline not in hasharr):
        hasharr.append(hline)
    hline = hfile.readline()
hfile.close()

vline = vfile.readline()
while(len(vline) != 0):
    while("ROOT" not in vline and len(vline) != 0):
        vline = vfile.readline()
    vline = vfile.readline()#for the ROOT line
    if(len(vline) == 0): break
    for i in range(0,5):
        circles[i].undraw()
        cir_text[i].undraw()

    for j in range(0,5):
        print vline
        
        #if("===" in vline): break
        i = int(vline.split(' ')[0])
        ip = hasharr[i]
        src = ip.split(' ')[0]
        dest = ip.split(' ')[1]
        dest = dest.split('\n')[0]

        m = re.search('\((.|.+?)\)', vline)
        freq = int(m.group(1))
        if(freq):
        
            srcs[j] = src
            dests[j] = dest
            circles[j] = Circle(Point(circles[j].getCenter().getX(),
                                      circles[j].getCenter().getY()),
                                10*freq/100)
            circles[j].setFill("blue")
            circles[j].setOutline("blue")
            

        vline = vfile.readline()
    for i in range(0,5):
        circles[i].draw(win)
        cir_text[i].draw(win)
    update()
    time.sleep(1)


    #go to the next block
    while("===" not in vline and len(vline) != 0):
         vline = vfile.readline()


