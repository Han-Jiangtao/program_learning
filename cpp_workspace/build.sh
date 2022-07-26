#!/bin/bash
if [ -d ./cmake_workspace ];
then
    echo "./cmake_workspace is exist! remove it now"
    rm -rf ./cmake_workspace
fi

mkdir -p ./cmake_workspace && cd ./cmake_workspace && cmake ../.. && make VERBOSE=1 -j
if [ $? != 0 ];
then
    echo "Build Failed, please check error"
    exit 127
fi
cp cpp_workspace/cpp_learning ../../bin
echo "copy cpp_learning to ../../bin"
cp cpp_workspace/libdynamic_learning* ../../lib
echo "copy libdynamic_learning ../../lib"
exit 0
