x1, y1 = map(int, input().split())

# 讀取點 Q 的座標 (x2, y2)
x2, y2 = map(int, input().split())

# 計算距離平方
distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2

# 輸出結果
print(distance_squared)