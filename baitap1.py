from myModule import tim_kiem_phan_tu
# bước 1 : nhập n
n = int(input("Nhập n: "))
# b2: tao 1 danh sách rỗng
danhsach =[]

#bước 3: nhập các phần tử vào Ds
for i in range(n):
    phantu = int(input(f"nhâp phần tử thứ {i+1} "))
    danhsach.append(phantu)
#hiển thị DS
print(danhsach)

#nhập số cần tìm
k = int(input("Nhập số cần tìm : "))
# tìm keiesm tuần tự, kĩ thuật đặt lính canh
# kiểm tra, nếu số cần tìm == phần tử trong DS thì in ra màn hình đã tìm thấy
def tim_kiem_phan_tu(ds, so_can_tim):
    for i in range(len(ds)):
        if ds[i] == so_can_tim:
            return i # tôi đã tìm thấy
    return -1 # tôi không tìm thấy
ketqua = tim_kiem_phan_tu(danhsach,k)
if ketqua !=-1:
    print("đã tìm thấy ")
else:
    print("không tồn tại")
    

