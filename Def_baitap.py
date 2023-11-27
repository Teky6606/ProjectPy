# ---------- menu bai tập ---------------
#1. Làm bài tập 1
#2. Làm bài tập 2
#3. Làm bài tập 3
# Mời bạn chọn chức năng:
#----------------------------------------
def baitap1():
    a = int(input("Nhập số A: "))
    b = int(input("Nhập số B: "))
    tong = a +b
    print("Tổng là : ",tong)

def baitap2():
    a = int(input("Nhập số A: "))
    b = int(input("Nhập số B: "))
    tong = a - b
    print("Hiệu là : ",tong)
def baitap3():
    a = int(input("Nhập số A: "))
    b = int(input("Nhập số B: "))
    tong = a * b
    print("Tích là : ",tong)

def hienthi_menu():
    print("-"*10,"MENU BÀI TẬP ","-"*10)
    print("1. Làm bài tập 1\n2. Làm bài tập 2 \n3. Làm bài tập 3\n 4.Thoát")
    
#cách 2: xử lý bằng cách dùng hàm có tham số
def xuly_menu(luachon):
    if luachon == 1:
        print(" Xử lý bài tập 1 ")
        baitap1()
    elif luachon == 2:
        print(" Xử lý bài tập 2 ")
        baitap2()
    elif luachon ==3:
        print(" Xử lý bài tập 3 ")
        baitap3()
    elif luachon == 4:
        print("Đã Thoát ")
    else:
        print(" Vui lòng nhập lựa chọn [ 1 - 4 ]")
    
status = False

while not status:
    hienthi_menu()


    luachon1 = int(input("Vui lòng nhập lựa chọn: "))

    #xử lý yêu cầu của ng dùng nhập
    xuly_menu(luachon1)

    if luachon1==4:
        status = True

    
    
