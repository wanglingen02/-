# 讀取人數 n
n = int(input())

# 讀取 n 個成績並轉為整數列表
scores = list(map(int, input().split()))

total_sum = 0     # 紀錄總分
pass_count = 0    # 紀錄及格人數

# 使用 for 迴圈走訪成績列表
for score in scores:
    total_sum += score       # 逐筆累加總分
    if score >= 60:
        pass_count += 1      # 判斷並統計及格人數

# 計算平均分數
average = total_sum / n

# 輸出第 1 行：平均分數（保留小數點後 2 位）
print(f"{average:.2f}")

# 輸出第 2 行：及格人數
print(pass_count)