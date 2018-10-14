import threading
import time
#Timer在指定时间之后启动一个功能
def func():
    print("I am running.........")
    time.sleep(4)
    print("I am done......")



if __name__ == "__main__":
    #每隔六秒钟执行一次func函数
    t = threading.Timer(6, func)
    t.start()

    i = 0
    while True:
        print("{0}***************".format(i))
        time.sleep(3)
        i += 1