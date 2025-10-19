import turtle

t=turtle.Turtle()

t.pensize(5)
t.speed(0
        )

colorlist= ["red" ,"blue" ,"green" ,"yellow" ,"purple"]
a=0
for i in range (200):
    t.color(colorlist[i%5])
    t.forward(i*5)
    t.left(144)
    a+=1

    #if a>=100:
     #   break
#for i in range (5):
 #   t.forward(100)
  #  t.left(144)


#for i in range (4):
 #   t.forward(100)
  #  t.left(90)
   # t.forward(100)
    #t.left(90)
    #t.forward(100)
    #t.left(90)
    #t.forward(100)
    #t.left(90)

turtle.done()