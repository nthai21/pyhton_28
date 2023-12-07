X=int(input("Nhập vào giá trị của X:"))
Y=int(input("Nhập vào giá trị của Y:"))
if X==Y:
    print("Giới tính nữ")
elif X!=Y:
    print("Giới tính nam ")
else:
    print("Không phù hợp")
#......................................

n=int(input())
tong =0
while n!=0:
    r=n%10
    tong+=r
    n//=10
print(tong)