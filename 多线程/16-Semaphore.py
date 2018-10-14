import threading
import time
#semaphore跟lock的概念差不多
#都有acquire()和release()两个函数
#semaphore：参数定义最多几个线程同时使用资源
#以下定义最多三个线程同时访问使用资源
semaphore=threading.Semaphore(3)
def fun():
    if semaphore.acquire():
        print(threading.currentThread().getName()+"get semaphore")
        time.sleep(2)
        semaphore.release()
        print(threading.currentThread().getName() + "release semaphore")
if __name__=="__main__":
    for i in range(8):
        t=threading.Thread(target=fun)
        t.start()