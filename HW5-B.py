a, b, k = map(int, input().split())

count = 0  # 紀錄個數
total_sum = 0  # 紀錄總和

# 使用 for 迴圈走訪區間 [a, b]
for i in range(a, b + 1):
    # 用餘數判斷是否為 k 的倍數
    if i % k == 0:
        count += 1
        total_sum += i

# 輸出個數與總和，以空白分隔
print(f"{count} {total_sum}")