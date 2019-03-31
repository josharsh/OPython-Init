import turtle
window=turtle.Screen()
window.bgcolor('Red')
brad=turtle.Turtle()
brad.shape("circle")
brad.speed(0.55)
brad.color('yellow')
def draw_square():
    iterationsforsquare=4
    count=0
    while(count<iterationsforsquare):
         brad.forward(100)
         brad.right(90)
         count+=1

draw_square()
iterationforcircle=10;
circlecount=0;
while(circlecount<iterationforcircle):
    brad.right(10)
    draw_square()
    
    
