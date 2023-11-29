# kiến thức: dữ liệu string trong python
'''str1 = "Hello Friends"
str2 =' Xin chao ,
toi la ICT,
rat vui duoc gap ban '
print(type(str1))
print(str2)
'''
'''text = 'Quang'
print(text[2])
num1 = 'ICT_'
num2 = input("Nhập mã sinh viên: ")
ketqua = num1 + num2
print(ketqua)'''
str1 = "Hello, World!"
print(str1)
'''str1 = "Hello World"
print(str1[-5:-2])
trả về một chuỗi bắt đầu từ vị trí 3 đến vị trí 5 từ cuối chuỗi'''
# Tính độ dài của chuỗi dùng ' len '
print(len(str1))
# hàm loại bỏ kí tự bất kì trong chuỗi - strip()
print("xóa khoảng trắng ở đầu và cuối:",str1.strip())
# hàm in thường chữ - lower()
print("in thường:",str1.lower())
# hàm viết chữ in HOA - upper()
print("in hoa toàn bộ: ",str1.upper())
# hàm thay thế nội dung
print(str1.replace('World','Ican Tech'))
# hàm tách chuỗi thành các chuỗi con - split()
print(str1.split(','))
# kiểm tra sự tồn tại trong chuỗi
str2 = " Học lập trình dễ như ăn kẹo"
x = "kẹo" not in str2
print(x)

