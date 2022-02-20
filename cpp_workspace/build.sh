#!/bin/bash
if [ -d ./cmake_workspace ];
then
    echo "./cmake_workspace is exist! remove it now"
    rm -rf ./cmake_workspace
fi

mkdir -p ./cmake_workspace && cd ./cmake_workspace && cmake .. && make VERBOSE=1 -j
if [ $? != 0 ];
then
    echo "Build Failed, please check error"
    exit 127
fi
exit 0
