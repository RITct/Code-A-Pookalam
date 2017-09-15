def outc(x):
    for k in range(3):
      for j in range(12):
        for i in range(36):
          if(i%2==0):
            color("#D04801")
          else:
            color("#FAD9F4")
          circle(x,10)
        x=x-1
        lt(90)
        fd(1)
        rt(90)
        circle(x,1)
      circle(x,10)
def mid():
  lt(45)
  color("#92141F")
  begin_fill()
  for i in range(30):
    fd(1)
    lt(1)
  circle(10,270)
  rt(80)
  fd(20)
  lt(170)
  end_fill()
  pu()
  fd(30)
  pd()
  color("white")
  begin_fill()
  circle(3)
  end_fill()
  pu()
  rt(170)
  fd(30)
  lt(100)
def out():
  color("#344C29")
  begin_fill()
  rt(60)
  fd(30)
  rt(50)
  fd(45)
  rt(140)
  fd(45)
  rt(50)
  fd(30)
  rt(60)
  end_fill()
  pencolor("black")
def pattern():
  lt(90)
  circle(40,90)
  for i in range(3):
    lt(180)
    circle(40,90)
from turtle import *
speed(0)
rt(90)
pu()
fd(30)
lt(90)
pd()
color("#EE5F11")
begin_fill()
circle(210)
end_fill()
rt(90)
pu()
bk(30)
pd()
lt(90)
for i in range(16):
  circle(180,22.5)
  out()
color("#ECC92D")
begin_fill()
circle(178)
end_fill()
for i in range(13):
  mid()
  pu()
  circle(200,22.5)
  pd()
pu()
lt(90)
fd(41)
rt(90)
pd()
circle(135)
outc(135)
color("brown")
begin_fill()
circle(100)
end_fill()
for i in range(6):
  if(i%2==0):
    fillcolor("#F9D22F")
  else:
    fillcolor("#FC8D08")
  pu()
  circle(100,60)
  pd()
  begin_fill()
  pattern()
  lt(90)
  end_fill()
pu()
lt(90)
fd(68)
rt(90)
pd()
color("white")
for i in range(36):
  circle(30,10)
  circle(10)
  










