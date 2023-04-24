FROM jenkins/jenkins_amd64_base:lts
COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
# tsinghua
# ENV JENKINS_UC "https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/"
# ENV JENKINS_UC_DOWNLOAD "https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/"

# ali
ENV JENKINS_UC "https://mirrors.aliyun.com/jenkins/updates/"
ENV JENKINS_UC_DOWNLOAD "https://mirrors.aliyun.com/jenkins/updates/"

RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt
USER root
RUN sed -i 's/deb.debian.org/mirrors.aliyun.com/g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends net-tools expect inetutils-ping && rm -rf /var/lib/apt/lists/* # buildkit
USER jenkins
