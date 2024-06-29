# pong-py
A simple http echo server written in python


# how to run locally
run:
```bash

poetry shell

python pong_py/main.py

# you should see

 * Running on http://127.0.0.1:8080

```

from another console:
```bash
curl  http://127.0.0.1:8080/ping/111
{"pong":"111"}

```

# how to build docker image
```bash
$ docker build --no-cache -t pong-py:local .
```

# how to run docker image
```bash
$ docker run -d -name pong-py -p 9090:8080 -e PONG_LISTENING_ADDRESS=0.0.0.0:8080 pong-py:local

# note the port 9090 !

$ curl  http://127.0.0.1:9090/ping/1235   
{"pong":"1235"}

```
