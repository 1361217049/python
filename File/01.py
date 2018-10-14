import shelve
#打开文件,必须有关闭文件
she=shelve.open(r"she.gb")
#此时she相当于一个字典
try:
    print(she["one"])
    print(she["twoo"])
except:
    print("烦死了")
#必须有关闭文件
finally:
    she.close()
