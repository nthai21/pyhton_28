#Nhập vào số in ra từ 1-n
n=int(input("Nhập vào giá trị của n"))
for i in range(1,n+1):
    print(i)
#In ra các số từ n-0
n=int(input("Nhập vào giá trị của n "))
while n>=0:
    print(n)
    n-=1
#ktra các số chẵn từ 0-n
n=int(input("Mời nhập vào giá trị n:"))
for i in range(0,n):
    if i %2==0:
        print(i)
#ktra các số lẻ <=n
n=int(input("Nhập vào giá trị của n là :"))
for i in range(n,0):
    if i%2 !=0:
        print(i)
#in ra n chữ cái in thường đầu tiên
n=int(input("Nhập n :"))
for i in range(0,n):
    print(chr(97+i))
