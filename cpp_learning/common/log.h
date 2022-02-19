/* log.h
 * autor: hanjiangtao
 * all rights resverd
*/

#ifndef __COMMON_LOG_H__
#define __COMMON_LOG_H__
#include "common/common.h"
#include "common/utils/env_util.h"
#include <set>

namespace COMMON {
const static char *LOG_LEVEL = "LOG_LEVEL";
const static char *LOG_PATH  = "LOG_PATH";
// GLOG_INFO = 0, GLOG_WARNING = 1, GLOG_ERROR = 2, GLOG_FATAL = 3
const static std::set<std::string> ENABLE_LEVEL = {"0", "1", "2", "3"};

class LogUtil {
public:
    LogUtil(std::string appName) {
        google::InitGoogleLogging(appName.c_str());
        std::string logLevel = UTILS::EnvUtil::GetEnv(LOG_LEVEL);
        std::string logPath = UTILS::EnvUtil::GetEnv(LOG_PATH);

        if (!logLevel.empty() && (ENABLE_LEVEL.find(logLevel) != ENABLE_LEVEL.end())) {
            google::SetStderrLogging(atoi(logLevel.c_str()));
        }

        if (!logPath.empty()) {
            logPath = logPath + "/cpp_learning_";
            for ( int i = 0; i < google::NUM_SEVERITIES; ++i ) {
                google::SetLogDestination(i, logPath.c_str());
            }
        }
    };

    ~LogUtil() {
        google::ShutdownGoogleLogging();
    }
};

} // namespace COMMON
#endif