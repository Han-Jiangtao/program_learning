FROM jenkins/jenkins_amd64_base:lts_20221021
COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt
USER root
RUN apt-get update && apt-get install -y --no-install-recommends expect && rm -rf /var/lib/apt/lists/* # buildkit
USER jenkins
