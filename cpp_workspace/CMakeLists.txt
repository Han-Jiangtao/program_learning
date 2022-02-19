cmake_minimum_required(VERSION 3.16.0)
project(cpp_learning VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(
    ${PROJECT_SOURCE_DIR}/common/glog
)

add_executable(cpp_learning
    cpp_learning.cpp
    common/utils/env_util.cpp
)


include_directories(
    ${PROJECT_SOURCE_DIR}
)

target_compile_definitions(cpp_learning PUBLIC
    -DCPP_LEARNING
)

target_compile_options(cpp_learning PUBLIC
    -g
)

target_link_libraries(cpp_learning
    glog::glog
)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})

