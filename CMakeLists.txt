cmake_minimum_required(VERSION 3.16.0)
project(program_learning VERSION 0.1.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(
    ${PROJECT_SOURCE_DIR}/cpp_workspace/
    ${PROJECT_SOURCE_DIR}/protobuf/
)
