B, N, R, C = map(int, input().split())

# 1. 計算服務費（不足 1 元的部分捨去，直接用整數除法 // 100）
service_charge = (B * R) // 100

# 2. 計算應付總額（若小於 0，改為 0）
T = B + service_charge - C
if T < 0:
    T = 0

# 3. 計算分攤：q 為整數商，r 為餘數（代表有 r 個人要多付 1 元）
q = T // N
r = T % N

# 4. 根據題目定義：a 個人付 q 元，b 個人付 q + 1 元
# 總人數 N = a + b，而多付 1 元的人數就是餘數 r，所以 b = r, a = N - r
b = r
a = N - r

# 5. 依序輸出三行
print(T)
print(f"{a} {q}")
print(f"{b} {q + 1}")