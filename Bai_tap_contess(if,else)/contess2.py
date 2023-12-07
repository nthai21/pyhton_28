#Bài 6
from math import*
n=float(input())
print(ceil(n))
print(floor(n))
print(round(n))
#Bài 7:Lấy 1 số cuối hoặc lấy 2 số cuối
n=int(input())
print(n%10)#Lấy 1 chữ số hàng đơn vị 12345=>5
print(n%100)#Lất 2 chữ số hàng đơn vị 1235=>35
#Bài 8 
b,a=map(int,input().split())
print(a//b)
c=a/b
print("%.2f"%c)
#Bài 9
n=int(input())
print(n//1000)#Mất đi 3 chữ số cuối cùng 123456=>>123
#Bài 10
a,b=map(int,input().split())
print(a%b)
