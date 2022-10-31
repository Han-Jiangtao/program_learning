基本的jenkins amd64镜像
安装推荐插件
Jenkins.instance.pluginManager.plugins.each{
  plugin -> 
    println ("${plugin.getShortName()}: ${plugin.getVersion()}")
}
添加role-base用户管理插件
镜像没有expect指令，已添加
