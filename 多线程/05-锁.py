import threading
sum=0
loopsum=1000
lock=threading.Lock()
def myadd():
    global sum,loopsum
    for i in range(1,loopsum):
        lock.acquire()
        sum+=i;
        lock.release()
def mydel():
    global sum,loopsum
    for i in range(1,loopsum):
        lock.acquire()
        sum-=i;
        lock.release()
if __name__=="__main__":
    print("starting    {}".format(sum))
    t1=threading.Thread(target=myadd,args=())
    t1.start()
    t1.join()

    t2 = threading.Thread(target=mydel, args=())
    t2.start()
    t2.join()
    print("starting    {}".format(sum))
