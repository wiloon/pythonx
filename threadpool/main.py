from concurrent.futures import ThreadPoolExecutor
import time
import random
import uuid


# 参数times用来模拟网络请求的时间
def get_html(times):
    u = uuid.uuid4()
    print("task: {} start".format(u))
    time.sleep(times)
    print("task: {} end, sleep: {}s".format(u, times))
    return times


executor = ThreadPoolExecutor(max_workers=2)

tasks = {}

for i in range(10):
    task = executor.submit(get_html, (random.randint(0, 9)))
    tasks[i] = task
    print("task {} submitted, queue size: {}".format(i, executor._work_queue.qsize()))

    time.sleep(1)

time.sleep(20)
