import random

all_chs = ['石头', '剪刀', '布']
win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
prompt = '''(0) 石头
(1) 剪刀
(2) 布
Please input your choice(0/1/2): '''
pwin = 0
cwin = 0

while pwin < 2 and cwin < 2:  # 人和计算机都没有赢够2局
    computer = random.choice(all_chs)
    ind = int(input(prompt))   # 将用户输入的数字转换成列表的下标
    player = all_chs[ind]   # 从列表中取出字符串

    print("Your choice: %s, Computer's choice: %s" % (player, computer))
    if player == computer:
        print('\033[32;1m平局\033[0m')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1mYou WIN!!!\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou LOSE!!!\033[0m')
