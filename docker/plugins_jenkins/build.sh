#/bin/bash
version=$1
image_name="jenkins/plugins_amd64:$version"
file_name="jenkins_plugins_amd64_$version"
docker buildx build --no-cache -t $image_name --platform linux/amd64 .

