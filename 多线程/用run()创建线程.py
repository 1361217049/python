import time
import threading
class MyThread(threading.Thread):
    def __init__(self,args):
        super(MyThread, self).__init__()
        self.args=args
    def run(self):
        time.sleep(2)
        print("the arg for this class is {}".format(self.args))
for i in range(5):
    t=MyThread(i)
    t.start()
    t.join()
print("ending>>>>>")