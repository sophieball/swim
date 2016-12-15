import graphics
from graphics import *
import re

win = GraphWin("visual", 1400, 800, autoflush = False)
update()

circles = []
cir_text = []
freqs = [1,1,1,1,1]
srcs = [0,0,0,0,0]
src_text = []
dests = [0,0,0,0,0]
squares = []
dest_text = []
hasharr = [0]
cur_freq = []
lines = []

#preset position for shapes and text
circles.append(Circle(Point(700, 400), freqs[0]))
circles.append(Circle(Point(300, 400), freqs[1]))
circles.append(Circle(Point(900, 200), freqs[2]))
circles.append(Circle(Point(500, 200), freqs[3]))
circles.append(Circle(Point(500, 600), freqs[4]))

cir_text.append(Text(circles[0].getCenter(), 0))
cir_text.append(Text(circles[1].getCenter(), 0))
cir_text.append(Text(circles[2].getCenter(), 0))
cir_text.append(Text(circles[3].getCenter(), 0))
cir_text.append(Text(circles[4].getCenter(), 0))


#middle rigth
#src
squares.append(Rectangle(Point(850, 360),
                         Point(1000, 400)))
#dest      
squares.append(Rectangle(Point(800, 550),
                         Point(950, 590)))

#middle left
squares.append(Rectangle(Point(50, 360),
                         Point(200, 400)))
squares.append(Rectangle(Point(30, 520),
                         Point(180, 560)))



#upper right
squares.append(Rectangle(Point(800, 60),
                         Point(950, 100)))
squares.append(Rectangle(Point(1000, 140),
                         Point(1150, 180)))



#upper left
squares.append(Rectangle(Point(250, 30),
                         Point(400, 70)))
squares.append(Rectangle(Point(100, 180),
                         Point(250, 220)))


#bottom
squares.append(Rectangle(Point(140, 610),
                         Point(290, 650)))
squares.append(Rectangle(Point(310, 670),
                         Point(460, 710)))


src_text.append(Text(circles[0].getCenter(), 0))
src_text.append(Text(circles[1].getCenter(), 0))
src_text.append(Text(circles[2].getCenter(), 0))
src_text.append(Text(circles[3].getCenter(), 0))
src_text.append(Text(circles[4].getCenter(), 0))

dest_text.append(Text(circles[0].getCenter(), 0))
dest_text.append(Text(circles[1].getCenter(), 0))
dest_text.append(Text(circles[2].getCenter(), 0))
dest_text.append(Text(circles[3].getCenter(), 0))
dest_text.append(Text(circles[4].getCenter(), 0))

for i in range(1,5):
    cir_text[i].setFill("white")
    src_text[i].setFill("white")
    dest_text[i].setFill("white")



vfile = open("freq", "r")
hfile = open("arrout", "r")
hline = hfile.readline()
while(len(hline) != 0):
    if(hline not in hasharr):
        hasharr.append(hline)
    hline = hfile.readline()
hfile.close()

for i in squares:
    i.setFill("purple3")
    i.setOutline("purple3")
    i.draw(win)
    
for i in range(0,5):
    circles[i].draw(win)
    cir_text[i].draw(win)
update()

vline = vfile.readline()
while(len(vline) != 0):

    while("ROOT" not in vline and len(vline) != 0):
        vline = vfile.readline()
    vline = vfile.readline()#for the ROOT line
    if(len(vline) == 0): break

    cur_freq = []
    cur_src = []
    cur_dest = []

    #read the entire block
    while("===" not in vline and len(vline) != 0):
        print vline
        i = int(vline.split(' ')[0])
        ip = hasharr[i]
        src = ip.split(' ')[0]
        dest = ip.split(' ')[1]
        dest = dest.split('\n')[0]

        m = re.search('\((.|.+?)\)', vline)
        freq = int(m.group(1))
        cur_freq.append(freq)
        cur_src.append(src)
        cur_dest.append(dest)
        vline = vfile.readline()

    #find the top 5
    if(len(cur_freq) >= 5):
        for j in range(0,5):
            print(cur_freq)
            max_freq = max(cur_freq)
            max_index = cur_freq.index(max_freq)
            srcs[j] = cur_src[max_index]
            cur_src.pop(max_index)
            dests[j] = cur_dest[max_index]
            cur_dest.pop(max_index)
            freqs[j] = cur_freq[max_index]
            cur_freq.pop(max_index)
            circles[j] = Circle(circles[j].getCenter(), 2*freqs[j])
            circles[j].setFill("blue")
            circles[j].setOutline("blue")
            cir_text[j] = Text(circles[j].getCenter(), freqs[j])
            cir_text[j].setFill("white")
            src_text[j] = Text(squares[2*j].getCenter(), srcs[j])
            dest_text[j] = Text(squares[2*j+1].getCenter(), dests[j])
            src_text[j].setFill("white")
            dest_text[j].setFill("white")
            
        for i in range(0,5):
            circles[i].draw(win)
            cir_text[i].draw(win)
            src_text[i].draw(win)
            dest_text[i].draw(win)
        #create lines
        #0
        lines.append(Line(Point(squares[0].getCenter().getX()-75,
                                squares[0].getCenter().getY()),
                        Point(circles[0].getCenter().getX() + circles[0].getRadius(),
                              circles[0].getCenter().getY())))
        #dest, from circle to square
        lines.append(Line(Point(circles[0].getCenter().getX(),
                                circles[0].getCenter().getY() + circles[0].getRadius()),
                         Point(squares[1].getCenter().getX(),
                            squares[1].getCenter().getY()-20)))
        #1
        lines.append(Line(Point(squares[2].getCenter().getX()+75,
                                squares[2].getCenter().getY()),
                        Point(circles[1].getCenter().getX() - circles[1].getRadius(),
                              circles[1].getCenter().getY())))
        #dest, from circle to square
        lines.append(Line(Point(circles[1].getCenter().getX(),
                                circles[1].getCenter().getY() + circles[1].getRadius()),
                         Point(squares[3].getCenter().getX(),
                            squares[3].getCenter().getY()-20)))
        #2
        lines.append(Line(Point(squares[4].getCenter().getX(),
                                squares[4].getCenter().getY()+20),
                        Point(circles[2].getCenter().getX(),
                              circles[2].getCenter().getY() - circles[2].getRadius())))
        #dest, from circle to square
        lines.append(Line(Point(circles[2].getCenter().getX() + circles[2].getRadius(),
                                circles[2].getCenter().getY()),
                         Point(squares[5].getCenter().getX(),
                            squares[5].getCenter().getY()+20)))
        #3
        lines.append(Line(Point(squares[6].getCenter().getX()+75,
                                squares[6].getCenter().getY()),
                        Point(circles[3].getCenter().getX(),
                              circles[3].getCenter().getY() - circles[3].getRadius())))
        #dest, from circle to square
        lines.append(Line(Point(circles[3].getCenter().getX() - circles[3].getRadius(),
                                circles[3].getCenter().getY()),
                         Point(squares[7].getCenter().getX()+75,
                            squares[7].getCenter().getY())))
        #4
        lines.append(Line(Point(squares[8].getCenter().getX()+75,
                                squares[8].getCenter().getY()),
                        Point(circles[4].getCenter().getX() - circles[4].getRadius(),
                              circles[4].getCenter().getY())))
        #dest, from circle to square
        lines.append(Line(Point(circles[4].getCenter().getX(),
                                circles[4].getCenter().getY() + circles[4].getRadius()),
                         Point(squares[9].getCenter().getX()+75,
                            squares[9].getCenter().getY())))

        for i in lines:
            i.setArrow("last")
            i.draw(win)
        
        update()
        for i in range(0,5):
            circles[i].undraw()
            cir_text[i].undraw()
            src_text[i].undraw()
            dest_text[i].undraw()
        for i in lines:
            i.undraw()
        lines = []
        time.sleep(4)



