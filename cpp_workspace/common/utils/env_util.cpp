/* env_util.cpp
 * autor: hanjiangtao
 * all rights resverd
*/

#include "env_util.h"

#include <cstdlib>

namespace UTILS {

std::string EnvUtil::GetEnv(const char *env) {
    if (env == nullptr) {
        return "";
    }
    char *envValue = std::getenv(env);
    if (envValue == nullptr) {
        return "";
    }
    return envValue;
}
} // end namespace UTILS