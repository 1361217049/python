import time
import threading
def fun1():
    print("fun1 start:")
    time.sleep(2)
    print("fun1 end:")
def main():
    #守护线程,就是子线程和主线程一起结束
    #主线程一结束，子线程（守护线程）就结束
    print("start doing")
    t1=threading.Thread(target=fun1,args=())
    t1.setDaemon(True)
    #t1.daemon=True
    t1.start()
    time.sleep(1)
    print("end doing")
if __name__=="__main__":
    main()
