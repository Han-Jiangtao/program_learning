cmake_minimum_required(VERSION 3.16.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package (Python3 COMPONENTS Interpreter Development)
message("Python3 include dirs:${Python3_INCLUDE_DIRS}")
message("Python3 libraries:${Python3_LIBRARIES}")

add_subdirectory(
    ${CMAKE_CURRENT_SOURCE_DIR}/common/glog
)

add_executable(cpp_learning
    cpp_learning.cpp
    common/utils/env_util.cpp
)


target_include_directories(cpp_learning BEFORE
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}
    PUBLIC ${CMAKE_BINARY_DIR}
    PUBLIC ${Python3_INCLUDE_DIRS}
)

target_compile_definitions(cpp_learning PUBLIC
    -DCPP_LEARNING
)

target_compile_options(cpp_learning PUBLIC
    -g
)

target_link_libraries(cpp_learning
    glog::glog
    dynamic_learning
    protobuf_learning
    ${Python3_LIBRARIES}
)

######################## dynamic learning #####################
add_library(dynamic_learning
    dynamic_learning/dynamic.cpp
)

target_include_directories(dynamic_learning BEFORE
    PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/dynamic_learning
)

#target_compile_definitions(dynamic_learning PUBLIC
#    -fPIC
#)

target_compile_options(dynamic_learning PUBLIC
    -fPIC -g
)

message("CMAKE_CURRENT_BINARY_DIR2222222 ${CMAKE_CURRENT_BINARY_DIR}")

