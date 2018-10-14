import multiprocessing
import time
class clockprocess(multiprocessing.Process):
    def __init__(self,n):
        super().__init__()
        self.n=n
    def run(self):
        while True:
            print("now time is %s"%time.ctime())
            time.sleep(self.n)
if __name__=="__main__":
    process=clockprocess(3)
    process.start()
    while True:
        print("sleeping.......")
        time.sleep(1)
