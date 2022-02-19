/* string_util.h
 * autor: hanjiangtao
 * all rights resverd
*/

#ifndef __COMMON_UTILS_STRING_UTIL_H__
#define __COMMON_UTILS_STRING_UTIL_H__
#include "common/common.h"

namespace UTILS {

class StrUtil {
public:
    template<typename ... Args>
    static std::string StrFormat(const std::string &format, Args ... args)
    {
        auto sizeBuf = std::snprintf(nullptr, 0, format.c_str(), args ...) + 1; 
        std::unique_ptr<char[]> buf(new(std::nothrow) char[sizeBuf]);

        if (!buf)
            return std::string("");

        std::snprintf(buf.get(), sizeBuf, format.c_str(), args ...);
        return std::string(buf.get(), buf.get() + sizeBuf - 1); 
    }
};

} // namespace UTILS
#endif