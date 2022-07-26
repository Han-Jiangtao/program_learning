/* cpp_learning.cpp
 * autor: hanjiangtao
 * all rights resverd
*/

#include "cpp_learning.h"

#include "Python.h"
#include "common/log.h"
#include "common/utils/string_util.h"
#include "protobuf_learning.pb.h"

void proto_test()
{
    protobuf_learning::my_message a;
    void *b = malloc(1024 * 1024 * 1024);
    memset(b, 1, 1024 * 1024 * 1024);
    auto simple1 = a.add_simple();
    simple1->set_allocated_data((std::string *)new std::string((char *)b, 1024 * 1024 * 1024));
    free(b);
}

int MAIN(int argc, char* argv[]) {
    COMMON::LogUtil logUtil = COMMON::LogUtil(argv[0]);
    for (int argLoc = 0; argLoc < argc; argLoc++) {
        LOG(INFO) << UTILS::StrUtil::StrFormat("arg[%d]:%s", argLoc, argv[argLoc]);
    }
    Py_Initialize();
    LOG(INFO) << UTILS::StrUtil::StrFormat("Py_None ref:%d", Py_None->ob_refcnt);
    PyObject* testPy = PyImport_ImportModule("python_learning");
    LOG(INFO) << UTILS::StrUtil::StrFormat("Py_None 1 ref:%d", Py_None->ob_refcnt);
    PyObject* res = PyObject_CallMethod(testPy, "test_return_None", nullptr);
    LOG(INFO) << UTILS::StrUtil::StrFormat("Py_None 2 ref:%d", Py_None->ob_refcnt);
    PyObject* res1 = PyObject_CallMethod(testPy, "test_return_None", nullptr);
    LOG(INFO) << UTILS::StrUtil::StrFormat("Py_None 3 ref:%d", Py_None->ob_refcnt);
    Py_Finalize();
}
