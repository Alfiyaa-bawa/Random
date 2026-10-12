
import turtle
import math

# Choose: 1 = Simple, 2 = Aesthetic, 3 = Detailed
STYLE = 1

screen = turtle.Screen()
screen.setup(700, 750)
screen.bgcolor("black")
screen.title("My Portrait")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

if STYLE == 1:
    line = "#ffb6c1"
    face = "#e6a078"
    scarf = "#382522"
elif STYLE == 2:
    line = "white"
    face = "#ffb6c1"
    scarf = "#382522"
else:
    line = "#e8b58d"
    face = "#d99570"
    scarf = "#382522"


def polygon(points, fill, outline=None):
    t.penup()
    t.goto(points[0])
    t.pencolor(outline or fill)
    t.fillcolor(fill)
    t.pendown()
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()
    t.penup()


def ellipse(cx, cy, rx, ry, fill, outline):
    points = []
    for i in range(121):
        a = 2 * math.pi * i / 120
        points.append((
            cx + rx * math.cos(a),
            cy + ry * math.sin(a)
        ))
    polygon(points, fill, outline)


def curve(points, color, width=2):
    t.pencolor(color)
    t.pensize(width)
    t.penup()
    t.goto(points[0])
    t.pendown()
    for p in points[1:]:
        t.goto(p)
    t.penup()


# Hijab silhouette
polygon([
    (-75, 225), (-120, 205), (-165, 150),
    (-180, 45), (-170, -90), (-220, -240),
    (-145, -285), (145, -285), (220, -240),
    (170, -90), (180, 45), (165, 150),
    (120, 205), (75, 225)
], scarf, line)

# Face
ellipse(0, 45, 92, 125, face, line)

# Hairline under the hijab
curve([
    (-75, 125), (-55, 160), (-25, 173),
    (0, 177), (25, 173), (55, 160), (75, 125)
], "#211714", 5)

# Eyebrows
curve([
    (-70, 85), (-50, 99), (-25, 100), (-12, 94)
], scarf, 4)

curve([
    (12, 94), (30, 100), (53, 98), (70, 85)
], scarf, 4)

# Eyes
for cx in [-38, 38]:
    ellipse(cx, 60, 25, 14, "white", line)
    ellipse(cx, 60, 10, 11, "#382522", "#382522")
    ellipse(cx, 63, 4, 5, "white", "white")

# Nose
curve([
    (0, 48), (-5, 25), (-10, 12),
    (0, 7), (12, 12)
], line, 2)

# Lips
curve([
    (-30, -20), (-17, -13), (-5, -17),
    (0, -19), (5, -17), (17, -13), (30, -20),
    (18, -35), (0, -40), (-18, -35), (-30, -20)
], "#b85c64", 2)

# Smile detail
curve([(-18, -30), (0, -33), (18, -30)], "#8d4248", 1)

# Earring
t.pencolor("#e7b85d")
t.pensize(3)
t.penup()
t.goto(-94, 15)
t.pendown()
t.circle(10)
t.penup()

# Neck
polygon([
    (-35, -75), (-35, -125),
    (35, -125), (35, -75)
], face, line)

# Clothing
polygon([
    (-35, -115), (-110, -145), (-230, -285),
    (230, -285), (110, -145), (35, -115)
], "#171717", line)

# Hijab folds
curve([(-130, 90), (-140, -50), (-115, -180),
       (-65, -250)], line, 2)
curve([(130, 90), (140, -50), (115, -180),
       (65, -250)], line, 2)

# Style 3: extra highlights and necklace
if STYLE == 3:
    t.pencolor("#e7b85d")
    t.pensize(2)
    t.penup()
    t.goto(-45, -145)
    t.pendown()
    t.goto(0, -180)
    t.goto(45, -145)
    t.penup()
    t.goto(0, -180)
    t.dot(7, "#e7b85d")

    t.pencolor("#ffccaa")
    curve([(-48, 70), (-35, 75), (-25, 70)], "#ffccaa", 1)
    curve([(25, 70), (35, 75), (48, 70)], "#ffccaa", 1)

turtle.done()

