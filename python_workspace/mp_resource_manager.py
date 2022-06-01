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
        self.q = self.mgr.Queue()
        self.res_d = self.mgr.dict()
        self.resource_l = self.mgr.Lock()
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            #time.sleep(0.001)
            #continue
            try:
                key, func, args, kwargs = self.task_q.get(timeout=0.001)
                self.resource_l.acquire()
                self.res_d[key] = getattr(self, func)(*args, **kwargs)
                self.resource_l.release()
            except queue.Empty as e:
                continue
    def __del__(self, *args, **kwargs):
        print("hanjiangtao __del__")

    def lock(self, *args, **kwargs):
        return self.mgr.Lock(*args, **kwargs)

    def event(self, *args, **kwargs):
        return self.mgr.Event(*args, *kwargs)


def test_resource(event, lock, q):
    print("hanjiangtao start!", event, lock, flush=True)
    cnt = 0
    while not event.is_set():
        try:
            a = q.get(timeout=0.001)
        except queue.Empty as e:
            continue
        lock.acquire()
        time.sleep(0.01)
        print(cnt, flush=True)
        cnt = cnt + 1
        lock.release()

def release(mgr, process):
    print("hanjiangtao register release", flush=True)
    mgr.stop_event.set()
    mgr.join()
    process.terminate()
    process.join()


def subprocess():
    mgr = GlobalMgr(daemon=True)
    mgr.start()
    process = multiprocessing.Process(target=test_resource,
        args=(mgr.stop_event, mgr.resource_l, mgr.q,), daemon=True)
    process.start()
    #Finalize(None, release, args=(mgr, process,), exitpriority=100)
    #atexit.register(release, mgr, process)
    time.sleep(1)

if __name__ == "__main__":
    process = multiprocessing.Process(target=subprocess, daemon=False)
    process.start()
    process.join()
