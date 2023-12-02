'''bài tập: tạo menu trong python
khi chạy chương trình:
    
*************** CHƯƠNG TRÌNH NHỎ - ĐOẠN CODE DÀI **************
    1.tính tổng
    2.đo lường sức khỏe
    3.tìm số đảo ngược
    4.thoát
**************************************************************
Mời bạn nhập chức năng ( 1-4): 1
*********** TÍNH TỔNG ***************
mời bạn nhập số A:
mời bạn nhập số A:
tổng là :

***************CHƯƠNG TRÌNH NHỎ - ĐOẠN CODE DÀI **************
    1.tính tổng
    2.đo lường sức khỏe
    3.tìm số đảo ngược
    4.thoát
**************************************************************
HƯƠNG DẪN:
def tinhtong()
def BMI()
def soDaoNguoc()
def menu()
while dk:
    luachon = int(input())
    if luachon == 1:
        gọi hàm tính tổng
    if luachon == 2:
        gọi ham tính BMI
    '''
#khai boa các hàm
def tinhtong():
    print(" mình đang tính tổng chờ tí ....")
def menu():
    while True:
        print("*************** CHƯƠNG TRÌNH NHỎ - ĐOẠN CODE DÀI **************")
        print(" 1.tính tổng\n2.đo lường sức khỏe\n3.tìm số đảo ngược\n4.thoát")
        luachon = int(input("Nhập lựa chọn : "))
        if luachon == 1:
            # gọi hàm tính tổng 
            tinhtong()
        elif  luachon == 2:
            # gọi hàm BMI
            print("chức nang 2")
        elif luachon == 3:
            print("chức nang 3")
        elif luachon == 4:
            break
        else:
            print("vui long chon đúng ")
            
menu()
