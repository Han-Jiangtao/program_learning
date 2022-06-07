<!--
https://github.com/python/cpython/issues/93563
-->
# Summary
<!--
如果一个子进程为了提供服务而创建，子进程的父进程如果创建一个线程去轮询对应服务，则当前的进程默认退出机制会先释放子进程，导致线程轮询服务的线程raise Error
-->
For a child process with daemon=False creates the multiprocessing.Manager object, if it creates a thread for polling SyncManager-created Lock/Event objects, the default recycling mechanism will first release the grandchild process corresponding to the created multiprocessing.Manager object, which can interrupt the polling thread and raise Error.
# Description
<!--
测试代码如下:
-->
The test code is as follows:
```python
import time
import queue
import threading
import multiprocessing

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

def subprocess():
    mgr = GlobalMgr(daemon=True)
    mgr.start()
    time.sleep(1)

if __name__ == "__main__":
    process = multiprocessing.Process(target=subprocess, daemon=False)
    process.start()
    process.join()
```
<!--
上述测试代码会抛出如下异常
-->
The above test code will throw the following exception:
```python
Traceback (most recent call last):
  File "/usr/lib/python3.10/threading.py", line 1009, in _bootstrap_inner
multiprocessing/process.py 318 source exit
    self.run()
  File "/home/hanjiangtao/workspace/program_learning/python_workspace/mp_resource_manager.py", line 18, in run
    self.task_q.get(timeout=0.001)
  File "<string>", line 2, in get
  File "/usr/lib/python3.10/multiprocessing/managers.py", line 833, in _callmethod
    raise convert_to_error(kind, result)
multiprocessing.managers.RemoteError: 
---------------------------------------------------------------------------
Traceback (most recent call last):
  File "/usr/lib/python3.10/multiprocessing/managers.py", line 260, in serve_client
    self.id_to_local_proxy_obj[ident]
KeyError: '7fcff61b4d00'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.10/multiprocessing/managers.py", line 262, in serve_client
    raise ke
  File "/usr/lib/python3.10/multiprocessing/managers.py", line 256, in serve_client
    obj, exposed, gettypeid = id_to_obj[ident]
KeyError: '7fcff61b4d00'
---------------------------------------------------------------------------
```
<!--
经过debug，发现上述异常抛出的根因是process子进程创建并start后,BaseProcess._bootstrap被调用，在程序资源释放也就是process对象退出时，走了BaseProcess._bootstrap中finally分支，导致提前调用util._exit_function，而util._exit_function方法会将BaseManger.start方法中注册的BaseManager._finalize_manager提前调用，导致thread还在运行时，SyncManager对象已经被释放，并抛出异常
-->
After debugging, it was found that the main cause of the above exception was the invocation of BaseProcess._bootstrap after the subprocess was created and started.While releasing the program resources, that is, when the process object try to exit, the finally brach in BaseProcess._bootstrap will be taken. Which leds to calling util._exit_function in advance. The util._exit_function method will futher call the BaseManager._finalize_manager registered in the BaseManger.start method in advance, and this will trigger the exception during the runtime of thread for the accidental release of SyncManager object.</br>

<!--
但是，multiprocessing.util模块在被import的时候，已经将util._exit_function注册至atexit模块中，所以本身在子进程退出的时候，util._exit_function已经会被被动调用，那么我们是否可以认为在BaseProcess._bootstrap的finally分支的主动调用是非必需的？
-->
However, the multiprocessing.util module registers util._exit_function in the atexit module automatically when it is imported, which means that util._exit_function will be called naturally while subprocess exits. Consequently, can we consider the active invocation of BaseProcess._bootstrap's finally branch as unnecessary?</br>

<!--
当然，通过学习multiprocessing.util模块的代码，我们可以通过如下方案进行规避：
-->
Of course, after learning the multiprocessing.util module, we can avoid the issue by the following:</br>
```python
import time
import queue
import threading
import multiprocessing


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
    # Actively registers destructors for high-priority _exit_function calls
    multiprocessing.util.Finalize(None, release, args=(mgr,), exitpriority=100)
    time.sleep(1)

if __name__ == "__main__":
    process = multiprocessing.Process(target=subprocess, daemon=False)
    process.start()
    process.join()
```
<!--
但是multiprocessing.util.Finalize方法不是模块外部可见方法，所以我认为这只算是个规避的方法。
-->
The multiprocessing.util.Finalize module is not an externally visible method, so it's only a hedge.'

# Environment
> Python 3.10.4</br>
> Ubuntu x86_64</br>
