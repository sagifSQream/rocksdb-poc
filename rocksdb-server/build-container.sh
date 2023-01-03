#!/bin/bash

TAG=0.1

podman build -t rocsdb-server-poc:0.1 -f Dockerfile .
podman tag rocsdb-server-poc:${TAG} docker.io/sagifsqream/rocksdb-server-poc:${TAG}
podman logout
podman login -u sagifsqream -p "Qwerty)987" docker.io
podman push docker.io/sagifsqream/rocksdb-server-poc:${TAG}
