import socket
import threading
from cache.cache_manager import Cache

class ProxyServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.cache = Cache()

    def handle_client_request(self, client_socket, client_address):
        request = client_socket.recv(4096).decode('utf-8')

        # Extract host and port from the request
        host = request.split()[1]
        port = 80

        if ':' in host:
            host, port = host.split(':')
            port = int(port)

        # Check if the requested data is in the cache
        cached_data = self.cache.get_cache_element(host)
        if cached_data:
            print("Cache hit! Sending cached data to client.")
            client_socket.send(cached_data)
            client_socket.close()
            return

        print("Cache miss! Forwarding request to remote server.")

        # Forward the request to the remote server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as remote_socket:
            remote_socket.connect((host, port))
            remote_socket.sendall(request.encode('utf-8'))
            response = remote_socket.recv(4096)

            # Cache the response
            self.cache.add_cache_element(host, response)

            # Send the response back to the client
            client_socket.sendall(response)

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_socket:
            proxy_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            proxy_socket.bind((self.host, self.port))
            proxy_socket.listen(5)
            print(f"Proxy server is listening on {self.host}:{self.port}")

            while True:
                client_socket, client_address = proxy_socket.accept()
                print(f"Accepted connection from {client_address}")
                threading.Thread(target=self.handle_client_request, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    proxy = ProxyServer('localhost', 8080)
    proxy.start()
