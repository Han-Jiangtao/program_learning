/* cpp_learning.cpp
 * autor: hanjiangtao
 * all rights resverd
*/

#include "cpp_learning.h"

#include "common/log.h"
#include "common/utils/string_util.h"
#include "protobuf_learning.pb.h"

void proto_test()
{
    protobuf_learning::simple_data a;
    void *b = malloc(1024 * 1024 * 1024);
    memset(b, 1, 1024 * 1024 * 1024);
    a.set_data(b, 1024 * 1024 * 1024);
}

int MAIN(int argc, char* argv[]) {
    COMMON::LogUtil logUtil = COMMON::LogUtil(argv[0]);
    for (int argLoc = 0; argLoc < argc; argLoc++) {
        LOG(INFO) << UTILS::StrUtil::StrFormat("arg[%d]:%s", argLoc, argv[argLoc]);
    }
    for (int i = 0; i < 1000; i++) {
        LOG(INFO) << UTILS::StrUtil::StrFormat("proto_test[%d]", i);
        proto_test();
    }
}
