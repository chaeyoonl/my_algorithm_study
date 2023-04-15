import queue

# 큐 모듈의 큐 클래스 객체 선언
data = queue.Queue()

data.put(2)
data.put(5)
data.put(6)

print(data.get())
print(data.get())
print(data.get())
