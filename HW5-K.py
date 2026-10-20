a, b = map(int, input().split())

# 使用 while 迴圈，當 b 不為 0 時持續執行輾轉相除
while b != 0:
    r = a % b   # 1. 計算餘數
    a = b       # 2. 將 a 更新為原來的 b
    b = r       # 3. 將 b 更新為餘數 r

# 當 b 為 0 時，當下的 a 就是最大公因數
print(a)