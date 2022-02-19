/* env_util.h
 * autor: hanjiangtao
 * all rights resverd
*/

#ifndef __COMMON_UTILS_ENV_UTIL_H__
#define __COMMON_UTILS_ENV_UTIL_H__
#include "common/common.h"

namespace UTILS {

class EnvUtil {
public:
    static std::string GetEnv(const char *env);
};

} // namespace COMMON
#endif