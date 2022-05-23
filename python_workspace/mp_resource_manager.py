import time
import queue
import threading
import multiprocessing


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

def get_resource_from_global_mgr(tools, func, args, kwargs):
    key = str(time.time())
    tools["task_q"].put((key, func, args, kwargs))
    while True:
        tools["resource_l"].acquire()
        
        tools["resource_l"].release()
        time.sleep(0.0001)

def test_resource(tools):
    event = tools[]

