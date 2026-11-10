k = int(input())

# 讀取原始訊息 S（包含可能有的頭尾空白與連續空白）
s = input()

result = []

# 逐字元進行走訪與加密判斷
for char in s:
    if 'A' <= char <= 'Z':
        # 大寫字母加密：先減去 'A' 的編碼變成 0~25，位移 K 後 % 26 循環，最後加回 'A'
        new_code = (ord(char) - ord('A') + k) % 26 + ord('A')
        result.append(chr(new_code))
    elif 'a' <= char <= 'z':
        # 小寫字母加密：先減去 'a' 的編碼變成 0~25，位移 K 後 % 26 循環，最後加回 'a'
        new_code = (ord(char) - ord('a') + k) % 26 + ord('a')
        result.append(chr(new_code))
    else:
        # 非英文字母（數字、空白、標點符號）保持原樣
        result.append(char)

# 將字元列表結合成字串並輸出
print("".join(result))