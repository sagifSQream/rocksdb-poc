#!/bin/bash

TAG=0.6


podman build -t writer-rocksdb:${TAG} -f Dockerfile-writer .

podman build -t reader-rocksdb:${TAG} -f Dockerfile-reader .

podman login -u sagifsqream -p "Qwerty)987" docker.io

podman tag writer-rocksdb:${TAG} docker.io/sagifsqream/writer-rocksdb:${TAG}
podman push docker.io/sagifsqream/writer-rocksdb:${TAG}

podman tag reader-rocksdb:${TAG} docker.io/sagifsqream/reader-rocksdb:${TAG}
podman push docker.io/sagifsqream/reader-rocksdb:${TAG}

