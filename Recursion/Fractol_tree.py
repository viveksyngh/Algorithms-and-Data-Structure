import turtle
import random 

def tree(branch_len, t) :
    if branch_len > 5 :
        t.pensize(branch_len/10)
        t.forward(branch_len)
        angle = random.randint(15, 45)
        minus_length = random.randint(5, 15)
        t.right(angle)
        tree(branch_len - minus_length, t)
        t.left(2*angle)
        tree(branch_len - minus_length, t)
        t.right(angle)
        t.backward(branch_len)

def main( ) :
    t= turtle.Turtle( )
    my_win = turtle.Screen( )
    t.left(90)
    t.up( )
    t.backward(100)
    t.down( )
    t.color("green")
    tree(90, t)
    my_win.exitonclick( )

main( )
