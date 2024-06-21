#/bin/bash
version=$1
if [ -z "$version" ]
then
    echo "The script need one param(version). comman:bash build.sh version"
    exit 127
fi

docker rmi jenkins/jenkins:jdk17
docker pull jenkins/jenkins:jdk17

image_name="jenkins/plugins_amd64:$version"
file_name="jenkins_plugins_amd64_$version.tar"
echo "We will build docker image:$image_name! Cost about 200s!"
docker buildx build --no-cache -t $image_name --platform linux/amd64 .
echo "Docker build[$?], shell command[docker images] can find image named $image_name!"
echo "Save image[$image_name] to file[$file_name]!"
docker save -o $file_name $image_name

docker rmi jenkins/jenkins:jdk17
echo "All step end!"

