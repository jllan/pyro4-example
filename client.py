import Pyro4

uri = input("输入uri: ").strip()
name = input("输入用户名: ").strip()

greeting_maker = Pyro4.Proxy("PYRONAME:" + uri)         # get a Pyro proxy to the greeting object
print(greeting_maker.get_fortune(name))   # call method normally
print('''操作选项:
        1-查看当前目录下的文件
        2-拷贝文件
        3-退出''')

while True:
    flag = int(input('请输入要进行的操作(1 or 2 or 3):'))
    if flag == 1:
        print('文件列表: ', greeting_maker.show_file())
    elif flag == 2:
        file_name = input("输入需要下载的文件名: ").strip()
        dir = input("输入需要保存到的目录: ").strip()
        if file_name and dir:
            print('开始下载文件{}到{}'.format(file_name, dir))
            if greeting_maker.cp_file(file_name, dir):
                print('下载成功')
            else:
                print('下载失败')
    elif flag == 3:
        print('退出！')
        break
    else:
        print('输入有误，请重新输入')
        continue
