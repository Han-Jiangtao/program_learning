
find_package(Protobuf REQUIRED)

file(GLOB PROTOFILES "${CMAKE_CURRENT_SOURCE_DIR}/*.proto")

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

