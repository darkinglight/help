#/bin/bash

docker run -d --name gitlab-runner --restart always \
	-v /var/run/docker.sock:/var/run/docker.sock \
	-v gitlab-runner-config:/etc/gitlab-runner \
	gitlab/gitlab-runner:latest
