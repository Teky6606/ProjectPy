# khai bao ham
'''def tinhtong():
    a = int(input("Nhập a = :"))
    b = int(input("Nhập b = :"))
    tong = a  +b
    print("Tổng = ",tong)
    
def sayHello():
    # các công việc của hàm
    print("Hello Friend \n"*10)
    # goi hàm tính tổng
    tinhtong()
# gọi hàm - viết lại tên của hàm

sayHello()
'''
'''# hàm có tham số
def tinhtong(a,b):
    tong = a+b
    print(tong)
# gọi hàm - cần truyền tham số vòa trong hàm
a = int(input("Nhập a = :"))
b = int(input("Nhập b = :"))
tinhtong(a,b)
'''
def tim_max(a,b,c):
    max_number = a
    if b > max_number:
        max_number = b
    if c > max_number :
        max_number = c
    if max_number+16% 2 == 0 :
        print("ICanTech")
    else:
        print("error")
    return max_number;

ketQua = tim_max(1,2,4)

print("Max là số: ",ketQua)
