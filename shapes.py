import turtle
import random
from datetime import datetime, timedelta

def drawshapes(choice):
    t = turtle.Turtle()
    t.shape("turtle")
    color = ["red", "darkred", "blue", "green", "violet", "orange", "purple", "cyan", "yellow", "light blue", "brown", "tomato", "DodgerBlue", "MediumSeaGreen", "pink"]
    turtle.bgcolor("white")
    t.pen(pensize=5, speed=7)
    if choice == 1:
        circle(t, color)
    elif choice == 2:
        triangle(t, color)
    elif choice == 3:
        square(t, color)
    elif choice == 4:
        rectangle(t, color)
    elif choice == 5:
        parallelogram(t, color)        
    elif choice == 6:
        trapezoid(t, color) 
    elif choice == 7:
        slinky(t, color)         
    elif choice == 8:
        spiral(t, color)   
    elif choice == 9:
        tancircles(t, color)
    elif choice == 10:        
        snowflakessquare(t, color)
    elif choice == 11:
        snowflakesparallel(t, color)
    elif choice == 12:
        snowflakescircle(t, color)
    elif choice == 13:
        snowflakes4(t, color)
    elif choice == 14:
        plus(t, color)
    elif choice == 15:
        star(t, color)
    elif choice == 16:
        sparklingstar(t, color)
    elif choice == 17:
        wheel(t, color)        
    elif choice == 18:
        fan(t, color) 
    elif choice == 19:
        decorcircle(t, color) 
    elif choice == 20:
        concentriccircles(t, color)        
    elif choice == 21:        
        spiralsquare(t, color)
    elif choice == 22:        
        spiralstar(t, color)
    elif choice == 23: 
        spiraltriangle(t, color)
    elif choice == 24: 
        spiralpentagon(t, color)
    elif choice == 25:        
        olympicslogo(t, color)
    elif choice == 26:        
        snowman(t, color)
    elif choice == 27:        
        car(t, color)
    elif choice == 28:        
        chessboard(t, color)
    elif choice == 29:        
        spiderweb(t, color)
    elif choice == 30:        
        heart(t, color)
    else:
        randomlines(t, color)
    t.hideturtle()     
    turtle.exitonclick()    
        
def circle(t, color):
    turtle.title("A Circle")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))
    t.begin_fill()
    for count in range(360):
        t.forward(1)
        t.right(1)
    t.end_fill()        
        
def triangle(t, color):
    turtle.title("A Triangle")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))
    t.begin_fill()
    for count in range(3):
        t.right(60)
        t.forward(100)
        t.right(60)
    t.end_fill()
    
def square(t, color):
    turtle.title("A Square")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))
    t.begin_fill()
    for count in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()
    
def rectangle(t,color):
    turtle.title("A Rectangle")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))
    t.begin_fill()
    for count in range(2):
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
    t.end_fill()
    
def parallelogram(t, color):
    turtle.title("A Parallelogram")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))
    t.begin_fill() 
    for count in range(2):    
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.right(120)
    t.end_fill()

def trapezoid(t, color):
    turtle.title("A Trapezoid")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))
    t.begin_fill()
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)
    t.forward(200)
    t.right(120)
    t.forward(100)
    t.right(60)
    t.end_fill()
   
    
def slinky(t, color):
    turtle.title("A Slinky")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    for count in range(10):
        for rounds in range(36):
            t.forward(10)
            t.right(10)
        t.forward(25)

def spiral(t, color):
    turtle.title("A Spiral")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    for count in range(100):
        t.forward(1+count)
        t.right(20)  
    
def tancircles(t, color):
    turtle.title("Tangent Circles")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    for count in range(10):
        for rounds in range(360):
            t.forward(count+1)
            t.right(1)
        t.forward(10)    
    
def snowflakessquare(t, color):
    turtle.title("Square Snowflakes")
    for count2 in range(10):
        for count1 in range(4):
            t.forward(100)
            t.right(90)
        t.right(36)
    t.right(120)     

def snowflakesparallel(t, color):
    turtle.title("Parallelogram Snowflakes")
    for count2 in range(10):
        for count1 in range(2):
            t.forward(100)
            t.right(60)
            t.forward(100)
            t.right(120)
        t.right(36)

def snowflakescircle(t, color):
    turtle.title("Circular Snowflakes")
    for count3 in range(5):
        for count2 in range(36):
            t.forward(5)
            t.right(10)
        for count1 in range(36):
            t.forward(10)
            t.right(10)
        t.right(72)
   
def snowflakes4(t, color):
    for count3 in range(8):
        t.penup()
        t.forward(90)
        t.left(45)
        t.pendown()
      
        for count2 in range(3):
            for count1 in range(3):
               t.forward(30)
               t.backward(30)
               t.right(45)
            t.left(90)
            t.backward(30)
            t.left(90)
        t.right(45)
        t.right(45) 

def plus(t, color):
    for count3 in range(4):
        t.forward(100)
        t.backward(100)
        t.right(90)   

def sparklingstar(t, color):
    turtle.title("A Sparkling Star")
    for count3 in range(10):
        t.forward(100)
        t.backward(100)
        t.right(36)  

def star(t, color):
    turtle.title("A Star")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    side = 200
    t.begin_fill()
    for count in range(5):
        t.forward(side)
        t.right(144)  
    t.end_fill()

def wheel(t, color):
    t.circle(100)
    t.penup()
    t.left(90)
    t.forward(100)
    t.pendown()
    t.begin_fill()
    for count3 in range(24):
        t.forward(100)
        t.backward(100)
        t.right(15)
    t.end_fill()    

def fan(t, color):
    for count3 in range(24):
        t.forward(100)
        t.backward(100)
        t.left(4)

def decorcircle(t, color):
    for count3 in range(90):
        t.forward(100)
        t.backward(100)
        t.right(4)    
        
def concentriccircles(t, color):
    turtle.title("Concentric Circles")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    for count in range(1,10):
        t.circle(10*count)
        t.penup()
        t.sety((10*count)*(-1))
        t.pendown() 

def spiralsquare(t, color):
    turtle.title("A Spiral Square")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    side = 200
    for count in range(40):
        t.forward(side)
        t.left(90)  
        side = side - 5   

def spiralstar(t, color):
    turtle.title("A Spiral Star")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    side = 200
    for count in range(20):
        t.forward(side)
        t.right(144)  
        side = side - 10

def spiraltriangle(t, color):
    turtle.title("A Spiral Triangle")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    side = 200
    for count in range(20):
        t.forward(side)
        t.left(120)  
        side = side - 10 
        
def spiralpentagon(t, color):
    turtle.title("A Spiral Triangle")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    side = 200
    for count in range(40):
        t.forward(side)
        t.left(72)  
        side = side - 5

def olympicslogo(t, color):
    t.pen(pensize=6)
    t.penup()   
    t.goto(-100, 0)
    turtle.title("Olympics Logo")
    colors1 = ['blue', 'black', 'red']
    colors2 = ['yellow', 'green']
    for color1 in colors1:
        t.penup()
        t.pencolor(color1)
        if color1 != "blue":
            t.forward(100)
        t.pendown()
        t.circle(50) 
    t.penup()        
    t.goto(-150,-50)  
    t.pendown()
    for color2 in colors2:
        t.penup()
        t.pencolor(color2)
        t.forward(100)
        t.pendown()
        t.circle(50) 

def draw_circle(t, color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
  
def snowman(t, color): 
    draw_circle(t, "#ffffff", 30, 0, 0)         
    draw_circle(t, "#ffffff", 40, 0, -60)         
    draw_circle(t, "#ffffff", 60, 0, -160)
    t.pen(pensize=2)    
    draw_circle(t, "#ffffff", 2, -10, 40) #Eyes
    draw_circle(t, "#ffffff", 2, 10, 40)  #Eyes
    draw_circle(t, "red", 3, 0, 25)       #Nose
    # Button
    draw_circle(t, "#ffffff", 2, 0, 5)
    draw_circle(t, "#ffffff", 2, 0, -15)
    draw_circle(t, "#ffffff", 2, 0, -35)
    # Hands
    t.penup()
    t.goto(-25,-5)
    t.pendown()
    # Left Hand
    t.pen(pensize=5)
    t.goto(-100, -20)
    # Right Hand
    t.penup()
    t.goto(25,-5)
    t.pendown()
    t.pen(pensize=5)
    t.goto(100, -20)
    # Hat
    t.penup()
    t.goto(-35, 55)
    t.color("black")
    t.pensize(6)
    t.pendown()
    t.goto(35, 55)
 
    t.goto(30, 55)
    t.fillcolor("black")
    t.begin_fill()
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(15)
    t.end_fill()    
    
def car(t, color):
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))
    #rectangular upper body    
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.begin_fill()
    t.forward(300)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(50)
    t.end_fill()
 
    #window and roof
    t.penup()
    t.goto(50, 50)
    t.pendown()
    t.setheading(45)
    t.forward(70)
    t.setheading(0)
    t.forward(100)
    t.setheading(-45)
    t.forward(70)
    t.setheading(90)
    t.penup()
    t.goto(200, 50)
    t.pendown()
    t.forward(49.50)
 
    #two tyres
    t.penup()
    t.goto(70, -10)
    t.pendown()
    t.color('#000000')
    t.fillcolor('#000000')
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.penup()
    t.goto(250, -10)
    t.pendown()
    t.color('#000000')
    t.fillcolor('#000000')
    t.begin_fill()
    t.circle(20)
    t.end_fill()

def chessboard(t, color):   
    t.speed(8)
    for i in range(4): #for loop will run 4 times
        t.forward(800) 
        t.right(90)
        a = 0
        b = 0
    for i in range(8): #for loop will run 8 times as there are 8 rows in the chessboard
        if(b == 0):
            a=1
        else:
            a=0
        for j in range(8): #for loop will run 8 times as there are 8 columns in the chessboard
            t.penup()
            t.goto(j*100, i*100*(-1))
            t.pendown()
            if(a==0):
                t.fillcolor('black')
                a=1
            else:
                t.fillcolor('white')
                a=0
            t.begin_fill()
            for k in range(4):
                t.forward(100)
                t.right(90)
            t.end_fill()
        if(b==0):
            b=1
        else:
            b=0 

def spiderweb(t, color):
#Code for building radical thread
    for i in range(6):
        t.forward(150)
        t.backward(150)
        t.right(60)
 
#Code for building spiral thread
    side = 150
    for i in range(15):
        t.penup()
        t.goto(0,0)
        t.pendown()
        t.setheading(0)
        t.forward(side)
        t.right(120)
        for j in range(6):
            t.forward(side)
            t.right(60)
        side = side - 10         


def curve(t):
    for i in range(200): 
        t.right(1) 
        t.forward(1) 
  
# Defining method to draw a full heart 
def heart(t, color):
    t.fillcolor('red') 
    t.pencolor('darkred') 
    t.begin_fill() 
    t.left(140) 
    t.forward(113) 
    # Draw the left curve 
    curve(t) 
    t.left(120) 
    # Draw the right curve 
    curve(t) 
    t.forward(112)  
    t.end_fill() 
         
    
def randomlines(t, color):
    turtle.title("I don't know what am I drawing !")
    t.pencolor(random.choice(color))
    t.fillcolor(random.choice(color))    
    end_time = datetime.now() + timedelta(seconds=10)
    while datetime.now() < end_time:
        t.forward(100)
        t.right(random.randint(1,360))    
        t.forward(50)
        t.left(random.randint(1,360))    
    
choice = int(input('Enter any random number between 1 and 30 and see what Turtle draws for you ! \nEnter your choice number here: '))
drawshapes(choice)
