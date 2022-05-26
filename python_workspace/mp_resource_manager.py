import time
import queue
import threading
import multiprocessing

import atexit
from multiprocessing.util import Finalize


class GlobalMgr(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mgr = multiprocessing.Manager()
        self.task_q = self.mgr.Queue()
        self.res_d = self.mgr.dict()
        self.resource_l = self.mgr.Lock()
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            try:
                key, func, args, kwargs = self.task_q.get(timeout=0.001)
                self.resource_l.acquire()
                self.res_d[key] = getattr(self, func)(*args, **kwargs)
                self.resource_l.release()
            except queue.Empty as e:
                continue

    def lock(self, *args, **kwargs):
        return self.mgr.Lock(*args, **kwargs)

    def event(self, *args, **kwargs):
        return self.mgr.Event(*args, *kwargs)

def get_resource_from_global_mgr(tools, func, *args, **kwargs):
    key = str(time.time())
    tools["task_q"].put((key, func, args, kwargs))
    res = None
    while res is None:
        tools["resource_l"].acquire()
        res = tools["res_d"].pop(key, None)
        tools["resource_l"].release()
        time.sleep(0.0001)
    return res

def test_resource(tools):
    event = get_resource_from_global_mgr(tools, "event")
    lock = get_resource_from_global_mgr(tools, "lock")
    print("hanjiangtao start!", event, lock, flush=True)
    cnt = 0
    while not event.is_set():
        lock.acquire()
        time.sleep(0.01)
        print(cnt, flush=True)
        cnt = cnt + 1
        lock.release()

def release(mgr, process):
    print("hanjiangtao register release")
    mgr.stop_event.set()
    mgr.join()
    process.terminate()
    process.join()


if __name__ == "__main__":
    mgr = GlobalMgr(daemon=True)
    mgr.start()
    tools = {
        "resource_l": mgr.resource_l,
        "res_d": mgr.res_d,
        "task_q": mgr.task_q
    }
    process = multiprocessing.Process(target=test_resource, args=(tools,), daemon=True)
    process.start()
    #Finalize(None, release, args=(mgr, process,), exitpriority=100)
    atexit.register(release, mgr, process)
    time.sleep(2)
