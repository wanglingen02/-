a, b = map(int, input().split())
c, d = map(int, input().split())

# 讀取矩陣 B 的第一列與第二列
e, f = map(int, input().split())
g, h = map(int, input().split())

# 計算矩陣 C 的四個元素
c11 = a * e + b * g
c12 = a * f + b * h
c21 = c * e + d * g
c22 = c * f + d * h

# 依序輸出矩陣 C 的兩列
print(f"{c11} {c12}")
print(f"{c21} {c22}")