from concurrent.futures import ThreadPoolExecutor
import time
import random


# 参数times用来模拟网络请求的时间
def get_html(times):
    print("task {} start".format(times))
    time.sleep(times)
    print("task {}s end".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
# 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))

tasks = {}
for i in range(2):
    r = random.randint(0, 9)
    print("random int: {}".format(r))
    task = executor.submit(get_html, (r))
    tasks[i] = task
    print("task {} submitted".format(i))

# done方法用于判定某个任务是否完成
print(task1.done())
# cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
print(task2.cancel())
time.sleep(4)
print(task1.done())
# result方法可以获取task的执行结果
print(task1.result())

# 执行结果
# False  # 表明task1未执行完成
# False  # 表明task2取消失败，因为已经放入了线程池中
# get page 2s finished
# get page 3s finished
# True  # 由于在get page 3s finished之后才打印，所以此时task1必然完成了
# 3     # 得到task1的任务返回值
