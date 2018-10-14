import queue
import threading
import time
class sheng(threading.Thread):
    def run(self):
        count=0
        global queue
        while True:
            if queue.qsize()<1000:
                for i in range(10):
                    count=count+1
                    msg="生产产品"+str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(1)
class xiao(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize()>300:
                for i in range(3):
                    msg=self.name+"消费了"+queue.get()
                    print(msg)
            time.sleep(1)
if __name__=="__main__":
    queue=queue.Queue()
    for i in range(10):
        print("初始产品"+str(i))
    s=sheng()
    s.start()
    x=xiao()
    x.start()

