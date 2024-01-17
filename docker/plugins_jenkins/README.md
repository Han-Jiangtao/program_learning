基本的jenkins amd64镜像
安装推荐插件
Jenkins.instance.pluginManager.plugins.each{
  plugin -> 
    println ("${plugin.getShortName()}: ${plugin.getVersion()}")
}
添加role-base用户管理插件
镜像没有expect指令，已添加

docker load -i image_file
docker run -d -u 0 --name xxx -p 9998:8080 -p 9999:50000 -v /usr/share/zoneinfo/Asia/Shanghai:/etc/timezone:ro -v my_dir:/var/jenkins_home jenkins/plugins_amd64:latest
