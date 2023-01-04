#!/bin/bash

TAG=0.1

podman build -t writer-rocksdb:${TAG} -f Dockerfile-writer .

# podman login -u sagifsqream -p "Qwerty)987"
# podman tag writer-rocksdb:${TAG} docker.io/sagifsqream/writer-rocksdb:${TAG}
# podman push docker.io/writer-rocksdb:${TAG}

