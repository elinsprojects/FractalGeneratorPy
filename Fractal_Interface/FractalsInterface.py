#import tkinter 

from tkinter import *
from tkinter.ttk import *
import turtlefigures 
from turtle import *
import tkinter as tk
import math
from random import randrange 



# set up the turtle 


#make the window
root = Tk()
root.title("Turtle Generator")
root.geometry("1000x800+100+100")
root.config(background = "#a4c3fc")



#make the interface
titleLabel = Label(root, text = "Welcome to my Fractal Generator Interface! Below is my Control Panel:")
titleLabel.grid(row=0, column=0, padx=(20), pady=20, sticky="NW")


#make the canvas
canvasFrame = LabelFrame(root, text = "Canvas")
canvasFrame.grid(row = 2, column = 5, sticky="NW")
canvas = Canvas(canvasFrame, width=500, height=500)
canvas.pack()


#link turtleScreen to canvas
screen = TurtleScreen(canvas)
w, h = screen.screensize()

#make a turtle pen and setup its features
pen = RawTurtle(screen)
pen.speed(0)
pen.width(3)


#make the control panel
controlFrame = LabelFrame(root, text = "Control Panel")
controlFrame.grid(row = 2, column = 0,  padx=20, sticky="NW, SE")


#make the label for choosing image
pensizeLabel = Label(controlFrame, text = "Choose Fractal")
pensizeLabel.grid(row=1, column=1, padx=10, pady=10)

#place optionmenu
figureNames = ["Binary Tree", "Dandelion", "Fern", "Koch", "Antiflake", "Snowflake", "Gasket 3", "Gasket 4", "Sierpinski Carpet", "Circle", "Circle 3", "Circle 4", "Honeycomb", "Bat", "Tetris"  ]
figureStr = StringVar()
figureList = OptionMenu(controlFrame, figureStr, figureNames[0], *figureNames)
figureList.grid(row=2, column=1, padx=10, pady=10)

#make the label for choosing Fractal
pensizeLabel = Label(controlFrame, text = "Choose Pen Colour")
pensizeLabel.grid(row=3, column=1, padx=10, pady=10)

#color panel
colorNames = ["Black", "Blue", "Light Blue", "Green", "Light Green", "Orange", "Red", "Pink", "Purple", "Yellow" ]
colorStr = StringVar()
colorList = OptionMenu(controlFrame, colorStr, colorNames[0], *colorNames)
colorList.grid(row=4, column=1, padx=10, pady=10)

#Define colorPicker function and link it to colorNames List 

def colorPicker(*args):
    colorIndex = colorNames.index(colorStr.get())
    
    if colorIndex == 0:
        pen.color("black")
    elif colorIndex== 1:
        pen.color("blue")
    elif colorIndex== 2:
        pen.color("light blue")
    elif colorIndex== 3:
        pen.color("green")        
    elif colorIndex== 4:
        pen.color("light green")        
    elif colorIndex== 5:
        pen.color("orange")
    elif colorIndex== 6:
        pen.color("red")        
    elif colorIndex== 7:
        pen.color("pink")
    elif colorIndex== 8:
        pen.color("purple")
    elif colorIndex== 9:
        pen.color("yellow")

colorStr.trace("w", colorPicker) 


#make label for Pen Size 
pensizeLabel = Label(controlFrame, text = "Pen Size")
pensizeLabel.grid(row=5, column=1,padx=10, pady=10)


#make funtion for scaler to stick(round up)to float values. 
def scaleF(val):
    scaleVal=float(penSize.get())
    if int(scaleVal) != scaleVal:
        penSize.set(round(float(val)))


#make scaler for Pen Size 
penSize= Scale(controlFrame, orient=HORIZONTAL, to=8, command=scaleF)
penSize.grid(row=7, column=1)


#make the label for choosing order and length
pensizeLabel = Label(controlFrame, text = "Set order and length")
pensizeLabel.grid(row=8, column=1, padx=10, pady=10)

#make order label
orderLabel = Label(controlFrame, text = "Order")
orderLabel.grid(row=9, column=0, padx=10)

#make order entry
orderStr = IntVar()
orderEntry = Entry(controlFrame, textvariable=orderStr)
orderEntry.grid (row=9, column=1, padx=10)

#make length label
lengthLabel = Label(controlFrame, text = "Length")
lengthLabel.grid(row=10, column=0, padx=10)

#make length entry 
lengthStr = IntVar()
lengthEntry = Entry(controlFrame, textvariable=lengthStr)
lengthEntry.grid (row=10, column=1, padx=10)



#defining draw function

def drawF():

    # get order and length values
    order = int(orderEntry.get())
    length = int(lengthEntry.get())

    #make pen width options work within draw function
    scaleVal = float(penSize.get())


    #type out if statements for pen sizes that links to the scaleVal
    if scaleVal == 0.0:
        pen.width(2)
    elif scaleVal== 1.0:
        pen.width(3)
    elif scaleVal== 2.0:
        pen.width(4)
    elif scaleVal== 3.0:
        pen.width(5)
    elif scaleVal== 4.0:
        pen.width(6)
    elif scaleVal== 5.0:
        pen.width(7)
    elif scaleVal== 6.0:
        pen.width(8)
    elif scaleVal== 7.0:
        pen.width(9)
    elif scaleVal== 8.0:
        pen.width(10)
        
    
    # get the selection of turtlefigures from option menu
    figureIndex = figureNames.index(figureStr.get())
    

    # use the figure index to call the selected turtle method within the drawF
    if figureIndex == 0: 
        pen.up();pen.backward(w/2); pen.down()
        turtlefigures.tree(order, length, pen)
    elif figureIndex == 1:
        pen.up();pen.backward(w/2); pen.down()
        turtlefigures.d(order, length, pen)
    elif figureIndex == 2:
        pen.up();pen.backward(w/2); pen.down()
        turtlefigures.f(order, length, pen)
    elif figureIndex == 3:
        pen.up();pen.backward(w/2); pen.down()
        turtlefigures.koch(order, length, pen)
    elif figureIndex == 4:
        turtlefigures.antiflake(order, length, pen)
    elif figureIndex == 5:
        turtlefigures.snowflake(order, length, pen)
    elif figureIndex == 6:
        turtlefigures.gasket3(order, length, pen)
    elif figureIndex == 7:
        turtlefigures.gasket4(order, length, pen)
    elif figureIndex == 8:
        turtlefigures.sierpinskiCarpet(order, length, pen)
    elif figureIndex == 9:
        turtlefigures.circle(order, length, pen)
    elif figureIndex == 10:
        turtlefigures.circle3(order, length, pen)
    elif figureIndex == 11:
        turtlefigures.circle4(order, length, pen)
    elif figureIndex == 12:
        turtlefigures.honeycomb(order, length, pen)
    elif figureIndex == 13:
        turtlefigures.bat(order, length, pen)
    elif figureIndex == 14:
        turtlefigures.tetris(order, length, pen)
      
#making the button
drawButton = Button(controlFrame, text = "Draw", command=drawF)
drawButton.grid(row=11, column=1, padx=10, pady=(10,0))


 
#defining clear function

def clearF():
    # clear the entries
    orderStr.set("")
    lengthStr.set("")
    #clear the canvas and set pen to starting point
    screen.clear()
    pen.clear()
    pen.penup()
    pen.setx(0)
    pen.sety(0)
    pen.pendown()

    
#making the button
clearButton = Button(controlFrame, text = "Clear", command=clearF)
clearButton.grid(row=12, column=1, padx=10, pady=(0,10))



#make label for Random Fractal Selection 
pensizeLabel = Label(controlFrame, text = "Can't decide? Pick Random Fractal!")
pensizeLabel.grid(row=13, column=1,padx=10, pady=10)


#define Draw Random function
def drawRandom():
    # get order and length values, pen color and width
    order = 3
    length = 100
    pen.color("#09edb4")
    pen.width(3)

    #type out list string from which random function calls from 
    figureNames = ["Binary Tree", "Dandelion", "Fern", "Koch", "Antiflake", "Snowflake", "Gasket 3", "Gasket 4", "Sierpinski Carpet", "Circle", "Circle 3", "Circle 4", "Honeycomb", "Bat", "Tetris"  ]
    figureStr = StringVar()
    figureIndex = randrange(14)
    

    #type out if statements for random from the list of turtle figures
    if figureIndex == 0: 
        pen.up();pen.backward(w/2); pen.down()
        turtlefigures.tree(order, length, pen)
    elif figureIndex == 1:
        pen.up();pen.backward(w/2); pen.down()
        turtlefigures.d(order, length, pen)
    elif figureIndex == 2:
        pen.up();pen.backward(w/2); pen.down()
        turtlefigures.f(order, length, pen)
    elif figureIndex == 3:
        pen.up();pen.backward(w/2); pen.down()
        turtlefigures.koch(order, length, pen)
    elif figureIndex == 4:
        turtlefigures.antiflake(order, length, pen)
    elif figureIndex == 5:
        turtlefigures.snowflake(order, length, pen)
    elif figureIndex == 6:
        turtlefigures.gasket3(order, length, pen)
    elif figureIndex == 7:
        turtlefigures.gasket4(order, length, pen)
    elif figureIndex == 8:
        turtlefigures.sierpinskiCarpet(order, length, pen)
    elif figureIndex == 9:
        turtlefigures.circle(order, length, pen)
    elif figureIndex == 10:
        turtlefigures.circle3(order, length, pen)
    elif figureIndex == 11:
        turtlefigures.circle4(order, length, pen)
    elif figureIndex == 12:
        turtlefigures.honeycomb(order, length, pen)
    elif figureIndex == 13:
        turtlefigures.bat(order, length, pen)
    elif figureIndex == 14:
        turtlefigures.tetris(order, length, pen)
    

    
#making the random button
randomButton = Button(controlFrame, text = "Random", command=drawRandom)
randomButton.grid(row=14, column=1, padx=10, pady=(10))


 
# Create text widget and specify size and ocation
textBox = Text(root, height = 10, width = 54, padx=20, pady=20)
textBox.grid(row=12, column=0, pady=20)

#insert text about fractals
textBox.insert(tk.END, """Information about my User Interface:

You choose your fractal shape, pen colour and size.
Order determines how many recursive shapes is drawn
(best results are between 3-5) and length determines
the ultimate size of the shape (50-150 is recommended)
Draw button start the drawing, and clear button clears
the canvas and entry points. Please allow the fractal
to finish before clearing. If you can't choose a
fractal, click Random, and a random fractal is chosen.""")

#disable the ability to edit the text on the UI
textBox.configure(state="disabled")


# Create another text widget and specify size and location
textBox2 = Text(root, height = 10, width = 66, padx=20, pady=20)
textBox2.grid(row=12, column=5, columnspan=1, padx=(0,20), pady=(20))

textBox2.insert(tk.END, """About My Fractals:

Please select fractal from my dropdown menu.""")
#disable the ability to edit the text on the UI
textBox2.configure(state="disabled")

#make function for textbox text to correlate to fractals in dropdown menu 

def fractalText(*args):
    

#get the selection of turtlefigures from option menu
    figureIndex = figureNames.index(figureStr.get())
    textBox2.configure(state="normal")
    textBox2.delete("1.0", tk.END)
    
    #use the figure index to call the selected turtle method and insert text for each fractal.
    if figureIndex == 0: 
        textBox2.insert(tk.END, """About My Fractal:

Binary Tree draws leaves onto itself, the higher the order,
the more leaves it generates.""")
        
    elif figureIndex == 1:
        textBox2.insert(tk.END, """About My Fractal:

Dandelion is a fractal that draws its leaves in 90 and 60 degree
angles, the more order value you put in, the more it starts to
resemble a dandelion seed head.""")
        
    elif figureIndex == 2:
         textBox2.insert(tk.END, """About My Fractal:

Fern is fractal that is asymmetric and the higher order you give
it, the more complex fern it becomes.""")
        
    elif figureIndex == 3:
        textBox2.insert(tk.END, """About My Fractal:

Koch Curve is a curve that divides itself to have a point
in the middle of the line. This curve is used to make antiflake
and snowflake. The higher value order you give it, the more
points within the points it makes.""")
        
    elif figureIndex == 4:
        textBox2.insert(tk.END, """About My Fractal:

Anti-flake uses the Koch curve to make a shape with 3 arms
coming out of the middle point by turning 120 degrees to the left.
The car brand Mitsubishi uses this shape for its logo in its
simplest form.""")
        
    elif figureIndex == 5:
        textBox2.insert(tk.END, """About My Fractal:

Snowflake uses the Koch curve to create a snowflake shape.
Instead of turning left, as in Anti-flake, it turns right 
120 degrees and thus a snowflake is created.""")
        
    elif figureIndex == 6:
        textBox2.insert(tk.END, """About My Fractal:

Gasket 3 is a fractal with triangles within triangles.
It leaves the middle triangle empty of each nest.""")
        
    elif figureIndex == 7:
        textBox2.insert(tk.END, """About My Fractal:

Gasket 4 is a Swiss flag lookalike. It’s a square fractal
that draws 4 squares inside by each corner (in its simplest form).
The length of the smaller squares are one-third of the full length
so that 4 recursive squares fit in the big square, creating a
cross in the middle.""")
        
    elif figureIndex == 8:
        textBox2.insert(tk.END, """About My Fractal:

Sierpinski Carpet is also a square fractal that draws many small
squares inside itself, but leaves the middle empty. This one takes
a long time to draw for turtle, so choosing smaller order
value(2-3) is recommended.""")
        
    elif figureIndex == 9:
        textBox2.insert(tk.END, """About My Fractal:

Circle fractal draws two smaller circles within itself(radius of
recursive cirlces are half the size of circle), and those circles
have 2 smaller circles inside them. This repeats as often as the
order value is set.""")
        
    elif figureIndex == 10:
        textBox2.insert(tk.END, """About My Fractal:

Circle 3 fractal draws three smaller circles within itself, and
those circles have 3 smaller circles inside them. This repeats
as often as the order value is set.""")
        
    elif figureIndex == 11:
        textBox2.insert(tk.END, """About My Fractal:

Circle 4 fractal draws four smaller circles within itself, and
those circles have 4 smaller circles inside them. This repeats
as often as the order value is set.""")
        
    elif figureIndex == 12:
        textBox2.insert(tk.END, """About My Fractal:

Honeycomb fractal is a hexagon gasket. Smaller hexagons are drawn
3 times (adjoining at the sides, resembling a flower), at the
corners of the hexagon. When you choose a higher order value,
a star shape is formed in the middle of the honeycomb shape.""")
        
    elif figureIndex == 13:
         textBox2.insert(tk.END, """About My Fractal:

Bat fractal draws triangles first on the right side of the canvas,
then on the left side of the canvas. The corners of the bigger
triangles have smaller triangles attached. At the end, the fractal
loosely resembles a bat.""")
         
    elif figureIndex == 14:
        textBox2.insert(tk.END, """About My Fractal:

Tetris fractal creates small squares inside itself and re-draws
itself in a cross pattern. A higher order number, makes the
fractal start resembling Tetris pieces. Recommended order value
is 3, to see the Tetris patterns.""")

    #disable the textbox state so it's not editable in the UI  
    textBox2.configure(state="disabled")


figureStr.trace("w", fractalText) 



#loop it
root.mainloop()
