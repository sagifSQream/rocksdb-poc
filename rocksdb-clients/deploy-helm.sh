#!/bin/bash

export HTTPS_PROXY=localhost:8888
cd $(dirname "${BASH_SOURCE[0]}")/helm-charts/rocksdb-poc-clients
helm upgrade -i rocksdb-client .