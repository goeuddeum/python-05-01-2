x1,x2=2,3
w1,w2=3,4
w3,w4=5,6
b1,b2=1,2
y1T,y2T=27,-30
lr=0.01
for epoch in range(200):
    y1=x1*w1+x2*w2+1*b1
    y2=x1*w3+x2*w4+1*b2
    E=((y1-y1T)**2+(y2-y2T)**2)/2
    y1E=y1-y1T
    y2E=y2-y2T
    w1E=y1E*x1
    w2E=y1E*x2
    b1E=y1E*1
    w3E=y2E*x1
    w4E=y2E*x2
    b2E=y2E*1
    w1=w1-lr*w1E
    w2=w2-lr*w2E
    b1=b1-lr*b1E
    w3=w3-lr*w3E
    w4=w4-lr*w4E
    b2=b2-lr*b2E
    print(f'epoch={epoch}')
    print(f'y1:{y1:3f}')
    print(f'y2:{y2:3f}')
    print(f'w1:{w1:3f}')
    print(f'w2:{w2:3f}')
    print(f'b1:{b1:3f}')
    print(f'w3:{w3:3f}')
    print(f'w4:{w4:3f}')
    print(f'b2:{b2:3f}')
    if E<0.0000001:
        break
    