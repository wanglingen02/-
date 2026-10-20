n = int(input())

# 使用外層 for 迴圈控制列數 (i)
for i in range(1, n + 1):
    # 使用內層 for 迴圈控制欄數 (j)
    for j in range(1, n + 1):
        # 計算乘積
        val = i * j
        # 使用 f-string 的 :4d 語法讓欄寬固定為 4 且靠右對齊，結尾不加額外空白
        print(f"{val:4d}", end="")
    # 每行結尾（內層迴圈結束後）直接換行
    print()