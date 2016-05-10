import graphics
from graphics import *
import re
import copy

vfile = open("freq", "r")
hasharr = [0]
srcs = []
dests = []

src_dots = []
src_texts = []
src_freq = []
src_cur = []
src_last = []

dest_dots = []
dest_texts = []
dest_freq = []
dest_cur = []
dest_last = []

circles = []
circles_old = []
freqs = []
pos = [(80, 250), (160, 250), (240, 250), (320, 250), (400, 250), (480, 250), (560, 250), (640, 250), (700, 250),
       (80, 500), (160, 500), (240, 500), (320, 500), (400, 500), (480, 500), (560, 500), (640, 500), (700, 500)]
pos_taken = [0] * 18

gap = 10

lines = []
line_last = []

hfile = open("arrout", "r")
hline = hfile.readline()
while(len(hline) != 0):
    if(hline not in hasharr):
        hasharr.append(hline)
    hline = hfile.readline()
hfile.close()

win = GraphWin("visual", 1400, 800, autoflush = False)

vline = vfile.readline()
while(len(vline) != 0):

    while("ROOT" not in vline and len(vline) != 0):
        vline = vfile.readline()
    vline = vfile.readline()

    src_freq = [0] * len(src_freq)
    dest_freq = [0] * len(dest_freq)
    src_last = copy.copy(src_cur)
    src_cur = []
    dest_last = copy.copy(dest_cur)
    dest_cur = []
    line_last = copy.copy(lines)
    lines = []

    while("===" not in vline and len(vline) != 0):
        i = int(vline.split(' ')[0])
        ip = hasharr[i]
        src = ip.split(' ')[0]
        dest = ip.split(' ')[1]
        dest = dest.split('\n')[0]
        
        m = re.search('\((.|.+?)\)', vline)
        print m.group(1)
        if(int(m.group(1)) > 5):
        
            if src in srcs:
                src_freq[srcs.index(src)] = int(m.group(1))
                src_dots[srcs.index(src)] = Circle(Point(250, ((srcs.index(src))+1)*gap), 0.8*src_freq[(srcs.index(src))])
  
            else:
                srcs.append(src)
                src_freq.append(int(m.group(1)))
                src_dots.append(Circle(Point(250, ((srcs.index(src))+1)*gap), 0.8*src_freq[(srcs.index(src))]))
                src_texts.append(Text(Point(150, (srcs.index(src)+1)*gap), src))
            src_cur.append(srcs.index(src))
            
            if dest in dests:
                dest_freq[dests.index(dest)] = int(m.group(1))
                dest_dots[dests.index(dest)] = Circle(Point(450, ((dests.index(dest))+1)*gap), 0.8*dest_freq[(dests.index(dest))])
            else:
                dests.append(dest)
                dest_freq.append(int(m.group(1)))
                dest_dots.append(Circle(Point(450, ((dests.index(dest))+1)*gap), 0.8*dest_freq[(dests.index(dest))]))
                dest_texts.append(Text(Point(550, (dests.index(dest)+1)*gap), dest))
            dest_cur.append(dests.index(dest))
                
            lines.append(Line(src_dots[srcs.index(src)].getCenter(), dest_dots[dests.index(dest)].getCenter()))

        vline = vfile.readline()


    #draw circles
    for c in circles_old:
        if c not in circles:
            c.undraw()
            center = c.getCenter()
            print center.getX()
            print center.getY()
            pos_taken[pos.index((center.getX(), center.getY()))] = 0
            
        
    for c in circles:
        c.setFill("blue3")
        c.setOutline("blue3")

    circles_old = copy.copy(circles)
    circles = []
    freqs_old = copy.copy(freqs)
    freqs = []

    for i in range(0, len(src_cur)):
        if i not in circles_old:
            center = pos[pos_taken.index(0)]
            print center
            circles.append(Circle(Point(center[0], center[1]), max(10, src_freq[src_cur[i]])));
            pos_taken[pos_taken.index(0)] = 1
            print pos_taken
            circles[i].setFill("blue")
            circles[i].setOutline("blue")
            circles[i].draw(win)

            freqs.append(Text(circles[i].getCenter(), str(src_freq[src_cur[i]] / 1000.0 * 100.0) + "%"))
            freqs[i].setFill("white")
            freqs[i].draw(win)

        
                       
    
    #draw
##    
##    i = 0
##    while i < len(src_dots):
##        c = src_dots[i]
##        if(src_freq[i] > 0):
##            c.setFill("red")
##            c.setOutline("red")
##        else:
##            c.setFill("white")
##            c.setOutline(color_rgb(245,245,245))
##        t = src_texts[i]
##        if(i in src_cur and (i not in src_last)):
##            t.setFill("black")
##            t.setStyle('bold')
##            try:
##                t.draw(win)
##                c.draw(win)
##                #break
##            except:
##                pass
##        elif(i not in src_cur and (i in src_last)):
##            
##            t.setStyle('normal')
##            t.setFill("grey")
##            try:
##                t.draw(win)
##                c.draw(win)
##                #break
##            except:
##                pass
##        elif(i not in src_cur and (i not in src_last)):
##            t.undraw()
##            c.undraw()
##
##        i = i + 1
##
##    i = 0
##    while i < len(dest_dots):
##        c = dest_dots[i]
##        if(dest_freq[i] > 0):
##            c.setFill("red")
##            c.setOutline("red")
##        else:
##            c.setFill("white")
##            c.setOutline(color_rgb(245,245,245))
##        t = dest_texts[i]
##        if(i in dest_cur and i not in dest_last):
##            t.setFill("black")
##            t.setStyle('bold')
##            try:
##                t.draw(win)
##                c.draw(win)
##                #break
##            except:
##                pass
##        elif(i not in dest_cur and i in dest_last):    
##            t.setStyle('normal')
##            t.setFill("grey")
##            try:
##                t.draw(win)
##                c.draw(win)
##                #break
##            except:
##                pass
##        elif(i not in dest_cur and i not in dest_last):
##            t.undraw()
##            c.undraw()
##        i = i + 1
##
##    for l in lines:
##        if l in line_last:
##            l.setFill("grey")
##            l.setArrow('last')
##            line_last.remove(l)
##        else:
##            l.draw(win)
##            l.setArrow('last')
##    for ll in line_last:
##        ll.undraw()

    update()
    time.sleep(1)
