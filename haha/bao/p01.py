class Student():
    def __init__(self,name):
        self.name=name
    def say(self):
        print("我的名字是{}".format(self.name))
def walk():
    print("walkking.........")
#下面这句话使得如果在当前目录下调试，调用下面这句话
#在其他的目录下不调用这句话
if "__name__"=="__main__":
    print("hahahahhahahaahahahh")