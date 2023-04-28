import turtle

turtle.color('blue')

turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)
turtle.right(120)
turtle.forward(50)

turtle.color('white')
turtle.forward(50)

#changing the size and direction of the triangle
#using a variable to store the size of the trianlge side

tri_side = 100

#new triangle
turtle.color('red')
turtle.forward(tri_side)
turtle.left(120)
turtle.forward(tri_side)
turtle.left(120)
turtle.forward(tri_side)
turtle.left(120)
turtle.forward(100)


turtle.color('white')
turtle.right(90)
turtle.forward(20)
tri_side = 20
turtle.color('green')
turtle.forward(tri_side)
turtle.left(120)
turtle.forward(tri_side)
turtle.left(120)
turtle.forward(tri_side)
turtle.left(120)
