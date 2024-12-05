from turtle import *
import math


# make binary tree
def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)
#end tree


#make a quadratic tree/dandelion 
def d(n,l, pen):
    # termination
    if n==0 or l<2:
        return
    #endif
    pen.forward(l)
    pen.left(90)
    d(n-1,l/2, pen)
    pen.right(60)
    d(n-1, l/2, pen)
    pen.right(60)
    d(n-1, l/2, pen)
    pen.right(60)
    d(n-1, l/2, pen)
    pen.left(90)
    pen.backward(l)
# end dandelion


#define Fern/f  
def f(n,l, pen):
    #termination
    if n ==0 or l<2:
        return
    #endif
    pen.forward(0.4*l)
    pen.right(50);f(n-1, l/2, pen);pen.left(50)
    pen.forward(0.6*l)
    pen.left(35);f(n-1, l/2, pen); pen.right(35)
    pen.forward(0.9*l)
    pen.right(15);f(n-1, 0.8*l, pen);pen.left(15)
    pen.backward(1.9*l)
#end fern


#define koch curve
def koch(n,l, pen):
    if n==0 or l<2:
         pen.forward(l)
         return

    #endif
    koch(n-1, l/3, pen)
    pen.left(60);koch(n-1, l/3, pen)
    pen.right(120);koch(n-1, l/3, pen)
    pen.left(60);koch(n-1, l/3, pen)
#end of koch

#define antiflake
def antiflake(n,l,pen):
    for i in range(3):
        koch(n,l, pen)
        pen.left(120)
    #endfor
#end antiflake


#define snowflake/flake       
def snowflake(n,l, pen):
    for i in range(3):
        koch(n,l, pen)
        pen.right(120)
    #endfor
#end flake

#Define gasket3, triangles 
def gasket3(n,l, pen):
    #termination
    if n==0 or l<2:
        for i in range(3):
            pen.forward(l)
            pen.left(120)
        #endfor
        return
    #endif
    gasket3(n-1,l/2, pen);pen.forward(l);pen.left(120)
    gasket3(n-1,l/2, pen);pen.forward(l);pen.left(120)
    gasket3(n-1,l/2, pen);pen.forward(l);pen.left(120)
#end of gasket3


#make fractal that looks like the Swiss flag 
def gasket4(n,l, pen):
    #termination
    if n==0 or l<2:
        for i in range(4):
            pen.forward(l)
            pen.left(90)
        #end for
        return
    #end if
    gasket4(n-1,l/3, pen);pen.forward(l);pen.left(90)
    gasket4(n-1,l/3, pen);pen.forward(l);pen.left(90)
    gasket4(n-1,l/3, pen);pen.forward(l);pen.left(90)
    gasket4(n-1,l/3, pen);pen.forward(l);pen.left(90)
#end of gasket4

#define sierpinskiCarpet                                                                                                                                                                                                                                                                                                                                           
def sierpinskiCarpet(n,l, pen):
    #termination
    if n==0 or l<2:
        for i in range (4):
            pen.forward(l)
            pen.left(90)
        #endfor       
        return
    #endif

    for i in range (4):
        sierpinskiCarpet(n-1, l/3, pen)
        pen.forward(l/3)
        sierpinskiCarpet(n-1, l/3, pen)
        pen.forward(l/3)
        pen.forward(l/3)
        pen.left(90)
#end sierpinski carpet 


#make circular fractal  
def circle(n,r, pen):
     #termination
     if n==0 or r<2:
          for i in range(3):
               pen.circle(r)
          #endfor       
          return
     #endif
     circle(n-1, r, pen)
     for i in range(2):
          circle(n-1, r/2, pen);pen.left(90); pen.penup()
          pen.forward(2*r);pen.left(90); pen.pendown()
#end of circle


#make circle3 fractal 
def circle3(n,r, pen):
     #termination
     if n==0 or r<2:
          for i in range(3):
               pen.circle(r)
          #endfor    
          return
     #endif
     circle3(n-1, r, pen)
     for i in range(3):
          circle3(n-1, r/2.154700538, pen)
          pen.penup();pen.left(90);pen.forward(r/2.154700538);pen.left(30)
          pen.forward(2*r/2.154700538)
          pen.left(30);pen.forward(r/2.154700538);pen.left(90);pen.pendown()
#end of circle3


#make circle4         
def circle4(n,r, pen):
     #termination
     if n==0 or r<2:
          for i in range(4):
               pen.circle(r)
          #endfor    
          return
     #endif
     circle4(n-1, r, pen)
     for i in range(4):
          circle4(n-1, r/2.41421356237, pen)
          pen.penup();pen.left(45);pen.forward(r/2.41421356237);pen.left(90)
          pen.forward(2.41421356237*r/2.41421356237)
          pen.forward(r/2.41421356237);pen.left(90);pen.forward(r/2.41421356237);pen.left(45);pen.pendown()
#end circle4


"""

Make 3 Personal Fractals:

1. honeycomb
2. bat
3. tetris 

"""


#define hexagon gasket with star in the middle
def honeycomb(n,l, pen):
     #termination
     if n==0 or l<2:
          for i in range(3):
               pen.forward(l)
               pen.left(60)
          #endfor
          return
     #endif
     honeycomb(n-1,l/3, pen);pen.forward(l);pen.left(60)
     honeycomb(n-1,l/3, pen);pen.forward(l);pen.left(60)
     honeycomb(n-1,l/3, pen);pen.forward(l);pen.left(60)
     honeycomb(n-1,l/3, pen);pen.forward(l);pen.left(60)
     honeycomb(n-1,l/3, pen);pen.forward(l);pen.left(60)
     honeycomb(n-1,l/3, pen);pen.forward(l);pen.left(60)
     pen.forward(l); 
#end honeycomb
               

def bat(n,l, pen):
     #termination
     if n==0 or l<2:
         return
     #endif
     bat(n-1,l/3, pen);pen.forward(l);pen.left(120)
     bat(n-1,l/3, pen);pen.forward(l);pen.left(120)
     bat(n-1,l/3, pen);pen.forward(l);pen.left(120)
     bat(n-1,l/3, pen);pen.backward(l);pen.right(120)
     bat(n-1,l/3, pen);pen.backward(l);pen.right(120)
     bat(n-1,l/3, pen);pen.backward(l);pen.right(120)
#end of bat


#define the tetris
def tetris(n,l, pen):
    #termination
    if n==0 or l<2:
        for i in range(3):
            pen.forward(l)
            pen.left(90)
        #endfor
        return
    #endif
    tetris(n-1,l/2, pen);pen.forward(l);pen.left(90)
    tetris(n-1,l/2, pen);pen.forward(l);pen.left(90)
    tetris(n-1,l/2, pen);pen.forward(l);pen.left(90)
    tetris(n-1,l/2, pen);pen.forward(l);pen.left(90)
#end tetris
     
