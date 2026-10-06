a, b = map(float, input().split())
c, d = map(float, input().split())

# 計算行列式 det
det = a * d - b * c

# 計算反矩陣的四個元素
inv_11 = d / det
inv_12 = (-b) / det
inv_21 = (-c) / det
inv_22 = a / det

# 輸出結果，保留小數點後 4 位
print(f"{inv_11:.4f} {inv_12:.4f}")
print(f"{inv_21:.4f} {inv_22:.4f}")