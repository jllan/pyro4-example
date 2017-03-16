import Pyro4
import os
import subprocess

'''启动server之前，要先在终端执行 pyro4-ns'''
@Pyro4.expose
class GreetingMaker(object):
    def get_fortune(self, name):
        return "Hello, {0}, 您已连接成功！. \n".format(name)

    def show_file(self):
        return os.listdir('.')

    def cp_file(self, file_name, dir):
        print(file_name, dir)
        if not os.path.isdir(dir):
            os.mkdir(dir)
        try:
            subprocess.call(['cp', file_name, dir+'/'+file_name+'.copy'])
        except Exception as e:
            return None
        return True


# greeting_maker = GreetingMaker()
daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(GreetingMaker)
ns.register('localhost', uri)
print("Ready. Object uri =", uri)
daemon.requestLoop()