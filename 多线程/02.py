import time
import threading
def fun1():
    print("fun1 start:")
    time.sleep(2)
    print("fun1 end:")
def main():
    #非守护线程
    print("start doing")
    t1=threading.Thread(target=fun1,args=())
    t1.start()
    time.sleep(1)
    print("end doing")
if __name__=="__main__":
    main()
