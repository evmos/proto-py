# Evmos proto

Compiled evmos' `protobuf` files ready to use with `python3.6+`.

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
