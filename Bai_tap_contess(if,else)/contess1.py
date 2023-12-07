#Bài 1
x=int(input())
print("Hello world")
print("Xin chào nthai !") 
#Bài 2
x=int(input())
b=int(input())
c=input()
d=float(input())
f=float(input())
print(x)
print(b)
print(c)
print("%.2f" % d)#print('{:..2d}.fomat(d)')
print("%.9f"%f)#print('{:..9f}.fomat(f'))
#bài 3
x,y,z,t=map(int,input("Nhập vào 4 gtri x,y,z,t").split())
print(y,z,x,t,sep=",")
print(x+y+z+t)
print(x-y+z*t)
#Bài 4 hàm pow
x,y=map(int,input().split())
print(x**y)#Dùng hàm pow(x,y,)
#Bài 5
from math import*
n=int(input)
b=sqrt(n)
print("%.2f"%b)
c=pow(n,1/3)#Căn bậc 3 lên là mũ 1,3
print("%.3f"%c)
