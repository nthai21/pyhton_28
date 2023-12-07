#Bài 1 :Đổi năm-tháng-tuần-ngày
ngay=int(input("Nhập vào số ngày "))
nam =ngay//365#Chia nguyên cho 365 để xem có bn năm
du_ngay=ngay%365#Lấy số năm chia dư cho 365 để xem còn bn ngày
tuan=du_ngay//7#Còn lại bn ngày chia  nguyên cho 7 để xem bn tuần
ngay_con_lai=du_ngay%7#Lấy số ngày dư khi chia năm chia dư cho 7 để xem còn lại bn ngày
print(nam,tuan,ngay_con_lai)
#Bài 2:mua n lít nước vs chai 1 lít và 2 lít,nhưg giá chai 1 lit và 2 lít khác nhau.
# Làm thế nào mua đc n lít nước vs giá tiền rẻ nhất
#  n:Số lít
# a:giá chai 1l ; b:giá chai 2l
n,a,b=map(int,input().split())
if a<=b/2:
    print(n*a)
else:
    if n%2==0:
        print(n//2*b)
    else:
        print((n-1)//2*b+a)
#Bài 3:
