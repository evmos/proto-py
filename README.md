# Evmos proto

[![PyPI version](https://badge.fury.io/py/evmosproto.svg)](https://badge.fury.io/py/evmosproto) [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/hanchon-live/evmosproto/master.svg)](https://results.pre-commit.ci/latest/github/hanchon-live/evmosproto/master)

Compiled evmos' `protobuf` files ready to use with `python3.9+`.

## Installation

```sh
pip install evmosproto
```

## Usage

```python
import grpc
from evmosproto.cosmos.tx.v1beta1.service_pb2_grpc import ServiceStub
from evmosproto.cosmos.tx.v1beta1.service_pb2 import BroadcastTxRequest
channel = grpc.insecure_channel('127.0.0.1:9090')
stub = ServiceStub(channel)

msg = BroadcastTxRequest()

# Set your msg params...

send = stub.BroadcastTx(msg)
print(send)
```
