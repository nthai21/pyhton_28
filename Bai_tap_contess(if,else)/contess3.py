#Bài 1
x=int(input("Nhập giá trị của x "))
print(x**3+3*x**2+x+1)
#Bài 2
a,b,c=map(int,input().spit())
S=a*(a+b)+b*(a+c)
print(S)
#Bài 3
from math import*
x1,y1,x2,y2=map(int(input().split()))
res=sqrt((x2-x1)**2+(y2-y1)**2)
#Bài 4
#Điều kiện N chia hế cho 2
n=int(input())
if n %2==0:
    print("Yes")
else :
    print("No")
#Điều kiện n chi hết cho cả 3 và 5
if (n % 3==0 and n%5==0) :
    print("Yes")
else:
    print("No")
#Điều kiện để n chia hết cho 3 nhưng ko chia hết cho 7
if n%3==0 and n%7!=0:
    print("yes")
else:
    print("No")
#Điều kiện để n lớn hơn bằng 30 và n chia hết cho 3,5,2
if n>=30 and (n%3==0 or n%2==0 or n%5==0):
    print("Yes")
else :
    print("No")
#Điều kiện để n có 2 chữ số và chữ số cuối là số nguyên tố
r =n%10
if n>10 and(n==2 or n==3 or n==7 or n==5):
    print("Yes")
else:
    print("No")
#Điều kiện để n ko thuộc khoảng (10,20)
if n<10 or n>20:
    print("yes")
else:
    print("No")
#Bài 5
#Cho2 số a,b.St1 lớn nhất <=a and %b==0; st2 số nhỏ nhất >=a and %b==0
a,b=map(int,input().split())
res1=a//b*b
print(res1)
res2=(a+b-1)//b*b
print(res2)
#Bài 6
a,b=map(int(input().split()))
print(a+b)
print(a-b)
print(a*b)
if b==0:
    print("Như cứt")
else:
    print(a/b)
#Bài 7:Bài năm nhuộn
n=int(input())
if n%400==0 or(n%4==0 and n%100!=0):
    print("năm nhuận")
else:
    print("Ko là năm nhuận")
#Bài 8
a,b,c=map(int(input().split()))
if (a,b,c>0)and((a+b)>c or (a+c)>b or (b+c)>a):
    print("Là một tam giác")
else:
    print("Ko là tam giac")
#Bài 9:Ktra xem tam giác có cân ,đều ,vg 
a,b,c=map(int,input().split())
if a>0 and b>0 and c>0 and ((a+b)>c and (a+c)>b and (b+c)>a):
    if a==b==c:
        print('Là tam giác đều ')
    if a**2+b**2==c**2 and b**2+c**2==a**2 and c**2+a**2==b**2:
        print('Tam giác đó là tam giác vg')
    if a**2+b**2==c**2 and b**2+c**2==a**2 and c**2+a**2==b**2 and(a==b or b==c or a==c):
        print("Tam giác đó là tam giác vg cân ")
#Bài 10 :Tháng năm
x=int(input("Nhập tháng "))
y=int(input("Nhập năm :"))
if (x>0 and x<12) and (y>0):
    if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
        print("Tháng có 31 ngày")
    elif x==2 or x==4 or x==6 or x==9 or x==11:
        print("Tháng có 30 ngày ")
    elif y%400==0 and (y%4==0 and y%100!=0):
        print("Năm đó là năm nhuận")
else:
    print("không tồn tại ")