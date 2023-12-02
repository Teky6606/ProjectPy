def fibonacci(n):
    if n <= 0:
        return
    elif n == 1:
        print(0)
        return
    elif n == 2:
        print("0, 1")
        return

    a, b = 0, 1
    print("0, 1", end=", ")
    for i in range(2, n):
        next_number = a + b
        print(next_number, end="")
        if i != n - 1:
            print(",", end=" ")
        a, b = b, next_number

# Nhập số lượng số Fibonacci cần tìm
n = int(input("Nhập số lượng số Fibonacci cần tìm: "))

# Gọi hàm để in ra chuỗi Fibonacci
print("Chuỗi Fibonacci gồm", n, "số đầu tiên là:")
fibonacci(n)
