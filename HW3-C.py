x1, x2, x3 = map(int, input().split())

# 計算平均數 m
m = (x1 + x2 + x3) / 3.0

# 計算母體變異數 v
v = ((x1 - m)**2 + (x2 - m)**2 + (x3 - m)**2) / 3.0

# 依序輸出，並保留小數點後 2 位
print(f"{m:.2f}")
print(f"{v:.2f}")