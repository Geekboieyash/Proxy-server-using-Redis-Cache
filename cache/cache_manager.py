#try to implement the lru 

import threading
import time
import socket
import sys

MAX_BYTES = 4096
MAX_CLIENTS = 400
MAX_SIZE = 200 * (1 << 20)
MAX_ELEMENT_SIZE = 10 * (1 << 20)

class cacheElement:
    def __init__(self, data, url):
        self.data = data
        self.len = len(data)
        self.url = url
        self.lru_time_track = time.time()
        self.next = None

class ProxyServer:
    def __init__(self,  port_number = 8000):
        self.port_number = port_number
        self.porxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.proxy_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.porxy_socket.bind(('localhost', self.port_number))
        self.head = None
        self.cache_size = 0
        self.lock = threading.Lock()

        