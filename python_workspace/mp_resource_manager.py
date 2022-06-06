import time
import queue
import threading
import multiprocessing

import atexit

class GlobalMgr(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mgr = multiprocessing.Manager()
        self.task_q = self.mgr.Queue()
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            try:
                self.task_q.get(timeout=0.001)
            except queue.Empty as e:
                continue

def release(mgr):
    mgr.stop_event.set()
    mgr.join()

def subprocess():
    mgr = GlobalMgr(daemon=True)
    mgr.start()
    # multiprocessing.util.Finalize(None, release, args=(mgr,), exitpriority=100)
    #atexit.register(release, mgr, process)
    time.sleep(1)

if __name__ == "__main__":
    process = multiprocessing.Process(target=subprocess, daemon=False)
    process.start()
    process.join()

