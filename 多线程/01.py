import time
import threading
def fun1(a):
    print("fun1 start",time.ctime())
    print("我是参数",a)
    time.sleep(2)
    print("fun1 end:",time.ctime())
def fun2(a,b):
    print("fun2 start", time.ctime())
    print("我是参数", a,"  ，我是参数",b)
    time.sleep(3)
    print("fun1 end:", time.ctime())
def main():
    print("start doing")
    t1=threading.Thread(target=fun1,args=("韩广阳",))
    t1.start()

    t2=threading.Thread(target=fun2,args=("吴亦凡","鹿晗"))
    t2.start()

    t1.join()
    t2.join()

    print("end doing")
if __name__=="__main__":
    main()
