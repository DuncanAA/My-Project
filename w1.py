import random
x=random.randint(1,3)
print(x)

#1
for x in range(1,10):
    for y in range(1,10):
        z=x*y
        print(f"{x}*{y}={z}")
#2
x=0
while x<=50:
    x=x+1
    print('你好')
    if x==50:
        print("我說完了啦")
        break
#3
y=eval(input("請輸入一個數值:"))
for x in range(1,y,2):
 print(x)

 #4
 import random
 L=[]
 x=eval(input('請輸入rows:'))
 y=eval(input('請輸入columns:'))
 for i in range(x):
     L.append([])
     for k in range(y):
      L[i].append(random.randint(1, 100))
 print(L)

#不一樣的做法
import numpy as np
x = eval(input('請輸入rows:'))
y = eval(input('請輸入columns:'))
L=np.random.randint(1,100,x*y).reshape(x,y)
print(L)
for a in range(x):
    z=L.sum(axis=1)
    print(f"第{a}列總合為:{z[a]}")
for b in range(y):
    s=L.sum(axis=0)
    print(f"第{b}行總合為:{s[b]}")
print(f"所有總合為:{L.sum()}")
print(L[0][0])


def doo(num):
   print('ll')

#函式
flag=True
balance=0
drinks=[{'name':'可樂','price':2000},{'name':'雪碧','price':3000},{'name':'茶理王','price':4000},
        {'name':'原翠','price':5000},{'name':'水','price':6000}]
print(len(drinks))
while flag:
    print('\n=========')
    select=eval(input('1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:'))

    if select ==1:
        if select==1:
            value=eval(input('儲值金額:'))
            while value<1:
                print('金額需大於零')
                value = eval(input('儲值金額:'))
            balance+=value
            print(f'儲值後餘額為{balance}元')
    elif select ==2:
        print('請選擇商品')
        for i in range(len(drinks)):
            print(f'{i+1}.{drinks[i]["name"]} {drinks[i]["price"]}元')
        choose=eval(input('請選擇:'))
        while choose <1 or choose>6:
            print('請輸入1-6之間')
            choose=eval(input('請選擇:'))
        buy_drink = drinks[choose-1]
        if balance <buy_drink['price']:
            print('餘額不足')
        else:
            print(f'已購買{buy_drink["name"]} {buy_drink["price"]}元')
            balance-=buy_drink["price"]
            print(f'購買後餘額為{balance}元')

    elif select ==3:
        print(f'目前餘額為{balance}元')
    elif select ==4:
        print('bye')
        flag=False
        break
    else:
        print('====請輸入1-4之間')
        continue


weight=100
weight1=80
def add_weight(w1,w2):
    result=w1+w2
    return result
print(add_weight(weight,weight1))

weight=100
weight2=80
def add_weight(w1,w2=90):
    result=w1+w2
    result2=w1*w2
    return result,result2
x1,x2=add_weight(weight,weight2)
print(x1,x2)
print(add_weight(weight))
y1,t2=add_weight(w2=weight,w1=weight2)


