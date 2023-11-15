import turtle as T
from time import sleep
import keyboard as k

#설정
t = T.Pen()
t.hideturtle()
T.setup(300,300)
t.screen.title('Pithon')
t.screen.bgcolor("#444")
colors = ['#2b5b84','#ffd343']
#파이값 100만 자리까지 입력
f = open('pi','r')
pi = f.readline()
pi.replace('\n','')
f.close()

#main
end = 0
t.penup()
t.goto(0,-150)
t.pendown()
while (True):
    for i in range(0,944465,1):
        if k.is_pressed('esc'):
            end = 1
            break
        t.color(colors[i%2])
        t.write(pi[i],align="center",font=("나눔고딕",200,"bold"))
        sleep(0.2)
        t.clear()
    if(end==1):
        break

