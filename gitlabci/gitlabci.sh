#!/bin/bash
echo "Start register gitlab ci runner !"

docker run --rm -v gitlab-runner-config:/etc/gitlab-runner gitlab/gitlab-runner:latest register \
	--non-interactive \
	--executor "docker" \
	--docker-image docker:20 \
	--url "http://10.228.11.11/" \
	--registration-token "siXuGkXkYFKcQxW_pyyn" \
	--description "docker-runner" \
	--tag-list "test,prod" \
	--run-untagged="true" \
	--locked="false" \
	--access-level="not_protected" 
