# 定義字典
words_dict = {
    "apple": "蘋果",
    "banana": "香蕉",
    "cat": "貓",
    "dog": "狗",
    "elephant": "大象",
    "flower": "花",
    "guitar": "吉他",
    "house": "房子",
    "ice": "冰",
    "jacket": "夾克"
}

# 使用者輸入英文單字


Q = input("請輸入英文單字：").lower()
if Q == 'quit':
    break
A=words_dict[Q]
print("答案:",A )
