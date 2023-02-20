#/bin/bash
docker buildx build -t jenkins/plugins_amd64:V1.000.004 --platform linux/amd64   .

