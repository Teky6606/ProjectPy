# Nhập số lượng phần tử từ người dùng
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Khởi tạo danh sách rỗng
danh_sach = []

# Nhập các phần tử của danh sách từ người dùng
for i in range(n):
    phan_tu = int(input(f"Nhập phần tử thứ {i+1}: "))
    danh_sach.append(phan_tu)

# In danh sách đã nhập
print("Danh sách của bạn là:", danh_sach)
