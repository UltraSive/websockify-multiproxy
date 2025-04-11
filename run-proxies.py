import os
import logging
import multiprocessing
from websockify import WebSocketProxy

# Logging config
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
)

# Get the value of PROXY_COUNT from the environment variable (default to 1 if not set)
proxy_count = int(os.getenv("PROXY_COUNT", 100))

# Configuration
target_host = "127.0.0.1"


def start_proxy(i):
    target_port = 5900 + i
    websocket_port = 30000 + i

    logging.info(
        f"Starting proxy {i}: WebSocket port {websocket_port} -> Target"
        f" {target_host}:{target_port}"
    )

    proxy = WebSocketProxy(
        listen_host="0.0.0.0",
        listen_port=websocket_port,
        target_host=target_host,
        target_port=target_port,
        run_once=False,
        daemon=False,
        record=None,
        ssl_target=False,
    )

    logging.info(
        f"Proxy {i} started and listening on 0.0.0.0:{websocket_port}"
    )
    proxy.start_server()


if __name__ == "__main__":
    # Launch each proxy in a separate process
    processes = []
    for i in range(proxy_count):
        p = multiprocessing.Process(target=start_proxy, args=(i,))
        p.start()
        processes.append(p)

    # Wait for all processes to complete (or handle termination signals)
    for p in processes:
        p.join()
