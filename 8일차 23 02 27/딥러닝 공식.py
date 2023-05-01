x=2
w=3
b=1
y=2*3+1*1
y
yT=10
E=(y-yT)**2/2
E
yE=y-yT
yE
wE=yE*x
bE=yE*1
(wE,bE)
lr=0.01
w=w-lr*wE
b=b-lr*bE
(w,b)
y=x*w+1*b
y
x=2
w=3
b=1
yT=10
lr=0.01
for epoch in range(2):
    y=x*w+1*b
    E=(y-yT)**2/2
    yE=y-yT
    wE=yE*x
    bE=yE*1
    w-=lr*wE
    b-=lr*bE
    print(f'epoch={epoch}')
    print(f'y:{y:3f}')
    print(f'w:{w:3f}')
    print(f'b:{b:3f}')
x=2
w=3
b=1
yT=10
lr=0.01
for epoch in range(200):
    y=x*w+1*b
    E=(y-yT)**2/2
    yE=y-yT
    wE=yE*x
    bE=yE*1
    w=w-lr*wE
    b=b-lr*bE
    print(f'epoch={epoch}')
    print(f'y:{y:3f}')
    print(f'w:{w:3f}')
    print(f'b:{b:3f}')
    if E<0.0000001:
        break
x1,x2=2,3
w1,w2=3,4
b=1
y=x1*w1+x2*w2+1*b
y
yT=27
E=(y-yT)**2/2
E

    


