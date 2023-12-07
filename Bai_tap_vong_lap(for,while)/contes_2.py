#Tính tổng từ 1-n/ ct: =n*(n+1)//2
n=int(input())
tong = 0
for i in range(1,n+1):
    tong += i
print(tong)
#Tính tổng bình phương các số tự nhiên/ ct:n(n+1)(2n+1)//6
n=int(input())
tong = 0
for i in range(1,n+1):
    tong += i**2
print(tong)
#Tính tổng bội của 3
n=int(input())
tong = 0
for i in range(0,n+1,3):
    tong += i
print(tong)

#Xem số đó có bn ước và in ra các ước
n=int(input("Nhập vào n :"))
dem = 0
for i in range(1,n+1):
    if n%i==0:
        dem+=1#Đếm số lượng ước
        print(dem)
for i in range(1,n+1):
    if n%i==0:
        print(i)#In ra cá ước