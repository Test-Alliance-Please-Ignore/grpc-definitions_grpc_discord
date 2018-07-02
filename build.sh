#!/bin/bash

python -m grpc_tools.protoc -I proto --python_out=./ --python_grpc_out=./ proto/grpc_discord/*.proto
