import turtle
from turtle import*
p=Pen()
p.speed(100)
a=5
b=60
sum1=0
for i in range(a,b):
    sum1+=i
sum1+=a
p.write(sum1,align='center',font=('arial,90'))
