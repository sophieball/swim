import graphics
from graphics import *
import re
import copy

vfile = open("freq", "r")
hasharr = [0]
srcs = []
dests = []

src_sqs = []
src_sqs_old = []
src_texts = []
src_texts_old = src_texts = []
src_freq = []
src_cur = []
src_last = []

dest_sqs = []
dest_sqs_old = []
dest_texts = []
dest_texts_old = []
dest_freq = []
dest_cur = []
dest_last = []

circles = []
circles_old = []
freqs = []
pos = [(100, 250), (200, 250), (300, 250), (400, 250), (500, 250), (600, 250), (700, 250), (800, 250), (900, 250), (1000, 250), (1100, 250), (1200, 250), (1300, 250),
       (100, 500), (200, 500), (300, 500), (400, 500), (500, 500), (600, 500), (700, 500), (800, 500), (900, 500), (1000, 500), (1100, 500), (1200, 500), (1300, 500)]
pos_taken = [0] * 26

gap = 10

src_lines = []
src_lines_old = []
dest_lines = []
dest_lines_old = []

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


    while("===" not in vline and len(vline) != 0):
        i = int(vline.split(' ')[0])
        ip = hasharr[i]
        src = ip.split(' ')[0]
        dest = ip.split(' ')[1]
        dest = dest.split('\n')[0]
        
        m = re.search('\((.|.+?)\)', vline)
        print m.group(1)
        if(int(m.group(1)) > 2):
        
            if src in srcs:
                src_freq[srcs.index(src)] = int(m.group(1))
            else:
                srcs.append(src)
                src_freq.append(int(m.group(1)))
            src_cur.append(srcs.index(src))
            
            if dest in dests:
                dest_freq[dests.index(dest)] = int(m.group(1))
            else:
                dests.append(dest)
                dest_freq.append(int(m.group(1)))
            dest_cur.append(dests.index(dest))
                

        vline = vfile.readline()


    #draw circles
    for c in circles_old:
        if c not in circles:
            c.undraw()
            center = c.getCenter()
            pos_taken[pos.index((center.getX(), center.getY()))] = 0

    for s in src_sqs_old:
        if s not in src_sqs:
            s.undraw()
    for d in dest_sqs_old:
        if d not in dest_sqs:
            d.undraw()
    for l in src_lines_old:
        if l not in src_lines:
            l.undraw()
    for l in dest_lines_old:
        if l not in dest_lines:
            l.undraw()
              
        
    for c in circles:
        c.setFill("blue3")
        c.setOutline("blue3")
    for s in src_sqs:
        s.setFill("purple3")
        s.setOutline("purple3")
    for d in dest_sqs:
        d.setFill("purple3")
        d.setOutline("purple3")
    for l in src_lines:
        l.setFill("grey")
        l.setOutline("grey")
    for l in dest_lines:
        l.setFill("grey")
        l.setOutline("grey")

    circles_old = copy.copy(circles)
    circles = []
    src_sqs_old = copy.copy(src_sqs)
    src_sqs = []
    dest_sqs_old = copy.copy(dest_sqs)
    dest_sqs = []
    src_lines_old = src_lines
    src_lines = []
    dest_lines_old = dest_lines
    dest_lines = []
    freqs_old = copy.copy(freqs)
    freqs = []
    dest_texts_old = copy.copy(dest_texts)
    dest_texts = []
    src_texts_old = copy.copy(src_texts)
    src_texts = []

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
    
            src_sqs.append(Rectangle(Point(center[0]+40, center[1] -75), Point(center[0]-40, center[1] - 100)))
            src_sqs[i].setFill("purple")
            src_sqs[i].setOutline("purple")
            src_sqs[i].draw(win)

            dest_sqs.append(Rectangle(Point(center[0]+40, center[1] +75 ), Point(center[0]-40, center[1] +100)))
            dest_sqs[i].setFill("purple")
            dest_sqs[i].setOutline("purple")
            dest_sqs[i].draw(win)

            src_lines.append(Line(Point(src_sqs[i].getCenter().getX(), src_sqs[i].getCenter().getY()+15), Point(circles[i].getCenter().getX(), circles[i].getCenter().getY() - circles[i].getRadius())))
            src_lines[i].setArrow('last')
            src_lines[i].draw(win)

            dest_lines.append(Line(Point(dest_sqs[i].getCenter().getX(), dest_sqs[i].getCenter().getY()-15), Point(circles[i].getCenter().getX(), circles[i].getCenter().getY() + circles[i].getRadius())))
            dest_lines[i].setArrow('first')
            dest_lines[i].draw(win)

            src_texts.append(Text(src_sqs[i].getCenter(), str(srcs[src_cur[i]])))
            src_texts[i].setSize(8)
            src_texts[i].setFill("white")
            src_texts[i].draw(win)

            dest_texts.append(Text(dest_sqs[i].getCenter(), str(dests[dest_cur[i]])))
            dest_texts[i].setSize(8)
            dest_texts[i].setFill("white")
            dest_texts[i].draw(win)

            freqs.append(Text(circles[i].getCenter(), str(src_freq[src_cur[i]] / 1000.0 * 100.0) + "%"))
            freqs[i].setFill("white")
            freqs[i].draw(win)

    update()
    time.sleep(1)
