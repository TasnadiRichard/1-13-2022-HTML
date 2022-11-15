import turtle

screen = turtle.Screen()
teknos = turtle.Turtle()
class Teknös:
    def Kiiras(hanyszor, fok):
        screen.clear()
        teknos = turtle.Turtle()
        for i in range(0, hanyszor):
            teknos.left(fok)
            teknos.forward(100)
            


Teknös.kiiras(3,120)
Teknös.kiiras(4,90)
Teknös.kiiras(6,60)
Teknös.kiiras(8,45)

screen.mainloop()