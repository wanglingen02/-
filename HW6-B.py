s = input()

# 1. 移除頭尾的半形空白
s = s.strip(' ')

# 2. 把英文字母轉成小寫
s = s.lower()

# 3. 將中間每一段連續半形空白改成一個底線
# 利用 split() 自動切除並凝聚連續空白，再用 '_'.join() 串接，完美符合不使用正規表示式的限制
if s == "":
    processed_s = ""
else:
    processed_s = '_'.join(s.split())

# 4. 進行合法帳號檢查
is_valid = True

# 檢查長度是否為 6 至 16
if not (6 <= len(processed_s) <= 16):
    is_valid = False

# 檢查開頭是否為數字或底線
if is_valid and len(processed_s) > 0:
    first_char = processed_s[0]
    if not (first_char.isdigit() or first_char == '_'):
        is_valid = False

# 檢查每個字元是否只能是 a-z、0-9 或底線
if is_valid:
    for char in processed_s:
        if not (char.islower() or char.isdigit() or char == '_'):
            is_valid = False
            break

# 5. 依序輸出兩行
print(processed_s)
if is_valid and processed_s != "": # 依題意，空字串長度為 0 亦屬不合法
    print("VALID")
else:
    print("INVALID")