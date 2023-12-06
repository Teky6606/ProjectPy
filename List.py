'''info = [] # list rỗng có tên là " info "
students =['Khánh Ngọc','Bảo An','Trung Kiên','Vinh','Quốc Anh','Minh Huy',1995,9.5,True] # list đã khai báo phần tử

print(students[:]) # hiển thị  toàn bộ list

viết chương trình tính tổng các phần tủ lẻ trong List < sử dụng hàm >
num = [ 2,5,6,3,7,9,11,22,6,4,3,0]
tong= ?'''
def tinh_tong(list_num):
    tong  = 0
    for i in list_num:
        if i %2 != 0:
            tong = tong +i
    return tong
num = [2,5,6,3,7,9,11,22,6,4,3,0]

ket_qua = tinh_tong(num)
print("Tỏng lẻ = ",ket_qua)
#people: |||*||||||| @ $ #
name  = ['orinn','alex']
name1 =[]
# thêm thông tin vào vị trí cuối của list
name.append('Diamond')
name.append('Diamond')

# chèn thêm thông tin vào vị trí bất kì trong list
name.insert(2,'insert')
# coppy danh sách
name1 = name.copy()

# loại bỏ vị trí index
name.pop(4)
# xóa bỏ phần tử, nhưng thực giữ lại danh sách
name1.clear()
# xóa bỏ phần tử trong ds ( theo value)
name.remove('orinn')
print("Danh sách  :",name)
print("Danh sách coppy :",name1)

