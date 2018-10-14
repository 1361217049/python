import multiprocessing
import time

def consumer(q):
    print("starting consumering:",time.ctime())
    while True:
        item=q.get()
        if item==None:
            break
        print("pull",item," out of q")
    print("ending consumering:",time.ctime())
def producer(sequende,q):
    print("starting produceing:", time.ctime())
    for item in sequende:
        q.put(item)
    print("ending produceing:", time.ctime())
if __name__=="__main__":
    q=multiprocessing.JoinableQueue()
    process_1=multiprocessing.Process(target=consumer,args=(q,))
    process_1.start()

    process_2=multiprocessing.Process(target=consumer,args=(q,))
    process_2.start()

    sequence=[1,2,3,4,5,6]
    producer(sequence,q)

    q.put(None)
    q.put(None)
    process_1.join()
    process_2.join()