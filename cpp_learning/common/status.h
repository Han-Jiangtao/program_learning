/* status.h
 * autor: hanjiangtao
 * all rights resverd
*/

#ifndef __COMMON_STATUS_H__
#define __COMMON_STATUS_H__
#include <iostream>

namespace COMMON {
enum class Status : unsigned int {
    SUCCESS = 0,
    FAIL = 1
};
} // namespace COMMON
#endif