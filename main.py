# Кривая Коха и снежинка Коха
# import turtle as tur

# width = 1200
# height = 600
# tur.setup(width, height, 0, 0)
#
#
# def draw_koch_segment(t, ln):
#     if ln>3:
#         ln3=ln//3
#         draw_koch_segment(t,ln3)
#         t.left(60)
#         draw_koch_segment(t, ln3)
#         t.right(120)
#         draw_koch_segment(t, ln3)
#         t.left(60)
#         draw_koch_segment(t, ln3)
#     else:
#         t.forward(ln)
#         t.left(60)
#         t.forward(ln)
#         t.right(120)
#         t.forward(ln)
#         t.left(60)
#         t.forward(ln)
#
# t = tur.Turtle()
# # t.hideturtle() #прячит черепашку
#
# t.speed(100)
# draw_koch_segment(t,100)
# t.right(120)
# draw_koch_segment(t,100)
# t.right(120)
# draw_koch_segment(t,100)
# # t.right(120)
# # draw_koch_segment(t,100)
# tur.done()

# https://www.youtube.com/watch?v=5duGAaHdoE0&ab_channel=foo52ru%D0%A2%D0%B5%D1%85%D0%BD%D0%BE%D0%A8%D0%B0%D0%BC%D0%B0%D0%BD
# import turtle
# turtle.shape('turtle')
# turtle.color("green")
# turtle.shapesize(2,2,2)
# turtle.pensize(2)
# turtle.speed(2)
# n=10
# for item in range(50):
#     turtle.forward(n)
#     turtle.left(80)
#     n+=10
# # turtle.done()
# turtle.mainloop()


# Простая L-система на плоскости

import turtle
#
# t= turtle.Turtle()
# t.screen.setup(900,900)
turtle.shape("turtle")
turtle.hideturtle() #прячит черепашку
turtle.color("blue")
turtle.speed(100)

turtle.penup()

turtle.setposition(-150, 150)
turtle.pendown()
turtle.pensize(2)
axiom = "F"
tempAx = ""
for i in range(4):
    ln = len(axiom)
    for item in range(ln):
        if axiom[item] == "+":
            tempAx = tempAx + "+"
            turtle.left(90)
        elif axiom[item] == "-":
            tempAx = tempAx + "-"
            turtle.right(90)
        elif axiom[item]=='F':  # F
            tempAx = tempAx + "F+F-F-F+F"
            turtle.forward(5)

    axiom = tempAx
    tempAx = ""
    print(axiom)

turtle.done()
