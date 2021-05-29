import turtle

wn = turtle.Screen()
wn.bgcolor("dodger blue")
wn.title("GunFire by Sanket")
wn.setup(width=1200, height=600)
wn.tracer(0)

gun = turtle.Turtle()
gun.shape("square")
gun.shapesize(stretch_wid=1, stretch_len=3)
gun.penup()
gun.goto(550,0)

wall_one = turtle.Turtle()
wall_one.shape("square")
wall_one.shapesize(stretch_wid=2, stretch_len=2)
wall_one.penup()
wall_one.goto(200,250)
wall_one.dx = 0
wall_one.dy = -0.09

bullet = turtle.Turtle()
bullet.shape("square")
bullet.penup()

score = 0
bullet_count = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.write("Press the Space bar to fire a bullet", align="center", font=("Courier",24,"normal"))

def fire():
    bullet.goto(gun.xcor()-40, gun.ycor())
    global bullet_count
    bullet_count = bullet_count + 1
    pen.clear()
    pen.goto(350, -200)
    pen.write(f"Score: {score}, bullets used: {bullet_count}", align="center", font=("Courier",24,"normal"))

wn.listen()
wn.onkeypress(fire, "space")

while True:
    wn.update()
    wall_one.setx(wall_one.xcor() + wall_one.dx)
    wall_one.sety(wall_one.ycor() + wall_one.dy)
    if wall_one.ycor() < -250:
        wall_one.sety(-250)
        wall_one.dy = wall_one.dy*-1
    if wall_one.ycor() > 250:
        wall_one.sety(250)
        wall_one.dy = wall_one.dy*-1
    bullet.goto(bullet.xcor()-0.09,0)
    if (bullet.xcor() > 170 and bullet.xcor() < 230) and (wall_one.ycor() > -30 and wall_one.ycor() < 30) and wall_one.xcor() == 200:
        wall_one.goto(-100,250)
        score = score + 1
        pen.clear()
        pen.goto(350, -200)
        pen.write(f"Score: {score}, bullets used: {bullet_count}", align="center", font=("Courier",24,"normal"))
    if (bullet.xcor() > -130 and bullet.xcor() < -70) and (wall_one.ycor() > -30 and wall_one.ycor() < 30) and wall_one.xcor() == -100:
        wall_one.goto(-400,250)
        score = score + 1
        pen.clear()
        pen.write(f"Score: {score}, bullets used: {bullet_count}", align="center", font=("Courier",24,"normal"))
    if (bullet.xcor() > -430 and bullet.xcor() < -370) and (wall_one.ycor() > -30 and wall_one.ycor() < 30) and wall_one.xcor() == -400:
        wall_one.goto(200,250)
        score = score + 1
        pen.clear()
        pen.write(f"Score: {score}, bullets used: {bullet_count}", align="center", font=("Courier",24,"normal"))
