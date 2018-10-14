import  multiprocessing
import time
def clock(n):
    while True:
        print("now time is %s"%time.ctime())
        time.sleep(n)
if __name__=="__main__":
    p=multiprocessing.Process(target=clock,args=(3,))
    p.start()
    while True:
        print("sleeping........")
        time.sleep(1)