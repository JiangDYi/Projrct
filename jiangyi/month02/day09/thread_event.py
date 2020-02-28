
from threading import Event,Thread

s=None
e=Event()

def yzr():
    print("杨子荣来拜山头")
    global s
    s="你大爷"
    e.set()

t=Thread(target=yzr)
t.start()

print("说口令")
e.wait()
if s=="你大爷":
    print("大爷里面请")
else:
    print("滚犊子")

t.join()