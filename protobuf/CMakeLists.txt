
find_package(Protobuf REQUIRED)

file(GLOB PROTOFILES "${CMAKE_CURRENT_SOURCE_DIR}/*.proto")

message("CMAKE_CURRENT_BINARY_DIR ${CMAKE_CURRENT_BINARY_DIR}")
set(CMAKE_CURRENT_BINARY_DIR ${CMAKE_BINARY_DIR})
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS ${PROTOFILES})
message("PROTOFILES ${PROTOFILES}")
message("PROTO_SRCS ${PROTO_SRCS}")
message("PROTO_HDRS ${PROTO_HDRS}")

add_library(protobuf_learning
    ${PROTO_SRCS}
    ${PROTO_HDRS}
)

target_compile_options(protobuf_learning PUBLIC
    -fPIC -g
)
target_link_libraries(protobuf_learning ${Protobuf_LIBRARIES})

