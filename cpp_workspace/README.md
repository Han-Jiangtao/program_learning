# cpp_learning
cpp learning testcase

本仓添加依赖子仓google/glog</br>
如果有任何侵权行为烦请联系本人删除</br>
邮箱：hanjiangtao-pub@hotmail.com</br>

安装cmake\gcc\g++\python3

mkdir -p cmake_workspace # 创建临时工作目录</br>
cd cmake_workspace</br>
cmake .. # cmake生成makefile</br>
make -j # 编译</br>

then generate exec file: cpp_learning # 可执行文件 cpp_learning</br>

## LOG CONFIG
The cpp_learing app is using glog.</br>
I only get the way to print log to stderr by the glog.</br>
So, it means the following 'print to terminal' is stderr.

> export LOG_LEVEL=0 # config log level print to terminal</br>
> > 0:INFO</br>
> > 1:WARN</br>
> > 2:ERROR(default)</br>
> > 3:FATAL</br>
>
> export LOG_PATH="./log" # config log file save to the path</br>
