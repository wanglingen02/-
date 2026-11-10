def is_prime(n):
    # 質數是大於 1 的正整數
    if n <= 1:
        return False
    
    # 試除法判定質數，除數的平方不大於 n
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
        
    return True

# 2. 讀取輸入區間 L 與 R
L, R = map(int, input().split())

prime_list = []
prime_sum = 0

# 3. 走訪區間內每個整數並呼叫函式
for num in range(L, R + 1):
    if is_prime(num):
        prime_list.append(num)
        prime_sum += num

# 4. 格式化輸出
if len(prime_list) > 0:
    # 第一行：依遞增順序輸出所有質數，以空白分隔
    print(" ".join(map(str, prime_list)))
    # 第二行：輸出個數與總和，以空白分隔
    print(f"{len(prime_list)} {prime_sum}")
else:
    # 沒有質數時的特殊輸出
    print("NONE")
    print("0 0")