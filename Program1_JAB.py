#Program1_JAB

import turtle

colors=['red', 'green', 'blue', 'orange', 'purple']

def triangle():
    for i in range(3):
        turtle.pencolor(colors[i%3])
        turtle.forward(50)
        turtle.right(360/3)


def square():
    for i in range(4):
        turtle.pencolor(colors[i%4])
        turtle.forward(50)
        turtle.right(360/4)

def pentagon():
    for i in range(5):
        turtle.pencolor(colors[i%5])
        turtle.forward(50)
        turtle.right(360/5)

turtle.shape('turtle')
answer = input('Choose a shape to draw... triangle, square or pentagon: ')

print(answer)

if answer ==('triangle'):
    triangle()

elif answer == ('square'):
    square()

elif answer == ('pentagon'):
    pentagon()

else:
    print ('Invalid input')
    
    
turtle.getscreen()._root.mainloop()
