import random
# 生成一个 1 到 100 之间的随机整数（包含 1 和 100）
secret_number = random.randint(1, 100)
# 用于记录用户猜测的次数
attempts = 0
print("欢迎来到猜数字游戏！")
print("我已经想好了一个 1 到 100 之间的数字，你可以开始猜啦。")
while True:
    try:
        # 提示用户输入猜测的数字
        guess = int(input("请输入你猜测的数字: "))
        # 每进行一次猜测，猜测次数加 1
        attempts += 1
        if guess < secret_number:
            # 如果用户猜测的数字小于随机数，提示用户猜的数字太低了
            print("你猜的数字太低了，再试一次。")
        elif guess > secret_number:
            # 如果用户猜测的数字大于随机数，提示用户猜的数字太高了
            print("你猜的数字太高了，再试一次。")
        else:
            # 如果用户猜测的数字等于随机数，说明猜对了
            print(f"恭喜你，猜对了！你一共用了 {attempts} 次尝试。")
            break  # 猜对后跳出循环，结束游戏
    except ValueError:
        # 如果用户输入的不是有效的整数，提示用户重新输入
        print("输入无效，请输入一个有效的整数。")
print("游戏结束。")