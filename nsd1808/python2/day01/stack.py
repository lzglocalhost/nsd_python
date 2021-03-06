stack = []

def push_it():
    item = input('item to push: ').strip()
    if item:   # 如果字符串非空才追加到列表
        stack.append(item)

def pop_it():
    if stack:   # 列表非空为真
        print('from stack popped %s' % stack.pop())

def view_it():
    print(stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}  # 把函数存入字典
    prompt = """(0) push it
(1) pop it
(2) view it
(3) quit
Please input your choice(0/1/2/3): """
    while True:
        choice = input(prompt).strip()[0]   # 移除输入字符两边的空白，取第一个字符
        if choice not in '0123':   # 如果不是0123中的一项，重来
            print('Invalid input. Try again.')
            continue
        if choice == '3':   # 如果是3则退出
            print('Bye-bye')
            break

        cmds[choice]()   # 从字典中取出函数，并调用
        # if choice == '0':   # 如果是012则调用相关的函数
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # else:
        #     view_it()

if __name__ == '__main__':
    show_menu()
