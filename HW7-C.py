# 1. 定義字串標準化函式（允許使用迴圈）
def normalize(text):
    result = []
    for char in text:
        # 只保留英文字母與數字
        if char.isalnum():
            result.append(char.lower())
    return "".join(result)

# 2. 定義回文判定函式（嚴格限定遞迴，禁止迴圈與切片）
def is_palindrome(text, left, right):
    # 基礎條件（Base Case）：當左指標大於或等於右指標，代表比對完畢或為空字串、單字元
    if left >= right:
        return True
    
    # 兩端字元不相同，立即判定非回文
    if text[left] != text[right]:
        return False
    
    # 直接呼叫自身，縮小兩端範圍（遞迴步驟）
    return is_palindrome(text, left + 1, right - 1)

# 主程式
# 讀取一整行原始密碼
s = input()

# 呼叫標準化清洗字串
clean_s = normalize(s)

# 呼叫遞迴函式進行回文檢查
if is_palindrome(clean_s, 0, len(clean_s) - 1):
    print("YES")
else:
    print("NO")