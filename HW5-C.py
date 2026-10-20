n = int(input())

# 初始化階乘變數為 1 (乘法的基底必須是 1)
factorial = 1

# 使用 for 迴圈從 1 乘到 n
for i in range(1, n + 1):
    factorial *= i

# 輸出最終階乘結果
print(factorial)