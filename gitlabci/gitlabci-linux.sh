#!/bin/bash
gitlab-runner register \
	--non-interactive \
	--executor "shell" \
	--url "http://10.228.11.11/" \
	--registration-token "siXuGkXkYFKcQxW_pyyn" \
	--description "linux-runner" \
	--tag-list "test,prod" \
	--run-untagged="true" \
	--locked="false" \
	--access-level="not_protected" 
