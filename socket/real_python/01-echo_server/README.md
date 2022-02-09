## Running The Two Given Python Scripts in Two Separate Terminals
- First, get the server up and running
  ```bash
  ~/.../socket/real_python/01-echo_server$ python echo_server.py
  Connected by ('127.0.0.1', 37294)
  ```
- Second, run the client. It will receive the echo from the server immediately.
  ```bash
  ~/.../socket/real_python/01-echo_server$ python echo_client.py
  Received: b'Hello, World!'
  ```
- Finally, the server side will print the connected client's info even before the above second step.
  ```bash
  ~/.../socket/real_python/01-echo_server$ python echo_server.py
  Connected by ('127.0.0.1', 37294)
  ```

## Interactively
- through `netstat` (`apt install net-tools`)
  ```bash
  ~/.../socket/real_python/01-echo_server$ netstat -an | sed -n '1,2p;/65432/p'
  Active Internet connections (servers and established)
  Proto Recv-Q Send-Q Local Address           Foreign Address         State
  tcp        0      0 127.0.0.1:65432         0.0.0.0:*               LISTEN
  ```
- through `lsof`
  ```bash
  ~/.../socket/real_python/01-echo_server$ lsof -i TCP:65432
  COMMAND  PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
  python  4314 phunc20    3u  IPv4 833205      0t0  TCP localhost:65432 (LISTEN)
  ```
- through `nc` (`apt install netcat`). Once `echo_server.py` gets running, type in another terminal `nc localhost 65432` (or equiv. `nc 127.0.0.1 65432`). You can then start typing anything you like, and, after pressing Enter, you'd get a response send to the stdout, echoing what you have just typed.
  ```bash
  ~/.../socket/real_python/01-echo_server$ nc localhost 65432
  30
  30
  Apfel
  Apfel
  ^C
  ```

## Errors
If you have not started the server in the first place, and instead you run the client first, then you will get
```bash
~/.../socket/real_python/01-echo_server$ python echo_client.py
Traceback (most recent call last):
  File "echo_client.py", line 7, in <module>
    s.connect((HOST, PORT))
ConnectionRefusedError: [Errno 111] Connection refused
~/.../socket/real_python/01-echo_server$ nc localhost 65432
localhost [127.0.0.1] 65432 (?) : Connection refused
```
