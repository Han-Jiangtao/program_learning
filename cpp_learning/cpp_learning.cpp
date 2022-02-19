/* cpp_learning.cpp
 * autor: hanjiangtao
 * all rights resverd
*/

#include "cpp_learning.h"

#include "common/log.h"
#include "common/utils/string_util.h"

int MAIN(int argc, char* argv[]) {
    COMMON::LogUtil logUtil = COMMON::LogUtil(argv[0]);
    for (int argLoc = 0; argLoc < argc; argLoc++) {
        LOG(INFO) << UTILS::StrUtil::StrFormat("arg[%d]:%s", argLoc, argv[argLoc]);
    }
}
