# cú pháp khai báo HÀM
'''def tên hàm ([ tham số 1] ,[tham số 2]....):
    câu lệnh của hàm '''
def hello(): # đây là hàm không tham số
    print("say Hello friends ")
    
# muốn dùng dc hàm thì cần goi hàm- là cách viết lại tên của hàm,
#và truyền tham số nếu có

'''hello()'''
def tinh_tong(a,b):
    tong = a+b
    print("tổng là : ",tong)
    return tong
    
x = int(input("Nhập x = "))
y = int(input("Nhập y = "))
#def tên hàm ([ tham số 1] ,[tham số 2]....):
c = tinh_tong(x,y)
print(c)
