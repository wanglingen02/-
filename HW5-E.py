n = int(input())

# 處理基礎邊界狀況 (0與1)
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    # 初始化前兩項：F(0) = 0, F(1) = 1
    a, b = 0, 1
    
    # 使用 for 迴圈逐步更新數值，重複 n-1 次
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    # 輸出第 n 項結果
    print(b)