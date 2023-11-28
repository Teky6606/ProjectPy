# Khởi tạo các biến đếm cho từng loại học sinh
hoc_sinh_gioi = 0
hoc_sinh_kha = 0
hoc_sinh_tb = 0

# Nhập số lượng học sinh cần nhập thông tin
so_luong_hoc_sinh = int(input("Nhập số lượng học sinh: "))

# Lặp để nhập thông tin cho từng học sinh và phân loại chúng
for i in range(so_luong_hoc_sinh):
    ho_ten = input("Nhập họ tên học sinh: ")
    diem_toan = float(input("Nhập điểm môn Toán: "))
    # tiếp tục tạo biến

    # Tính điểm trung bình
    diem_tb = # công thức tính điểm tb

    # Phân loại học sinh vào từng nhóm dựa trên điểm số và hạnh kiểm
    if diem_tb >= 8.0 and hanh_kiem == "Tốt" or hanh_kiem == "tốt:
        hoc_sinh_gioi += 1
    # code tiếp chức năng khác tại đây

# In ra số lượng học sinh theo từng loại
print("Số lượng học sinh giỏi:", hoc_sinh_gioi)
# tiếp tục hiển thị các học sinh khác
