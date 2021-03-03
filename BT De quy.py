# Bài toán tháp Hà Nội 
def THN(n, A, B, C):
    if n == 1:
        print("Di chuyển vòng 1 từ nguồn", A, "đến đích", B)
        return 
    THN(n-1, A, C, B)
    print("Di chuyển vòng", n, "từ nguồn", A, "đến đích", B)
    THN(n-1, A, B, C)

n = int(input("Số tầng của tháp: "))
THN(n, "A", "B", "C")   
