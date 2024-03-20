<h1>Proxy server using Redis Cache</h1>

## Index

- [Project Structure](link)
- [Guide to run](link)
- [Demo](link)


# Project Structure

The project is organized into multiple directories and files to maintain modularity and separation of concerns. Below is an overview of the directory structure:


- `cache/`: This directory contains cache-related functionality for storing and managing cached responses.
  - `__init__.py`: Initialization file to treat the `cache` directory as a package.
  - `cache_manager.py`: Module containing functions and classes for cache management.

- `http_parser/`: This directory contains functionality for parsing HTTP requests.
  - `__init__.py`: Initialization file to treat the `http_parser` directory as a package.
  - `http_parser.py`: Module containing functions for parsing HTTP requests.

- `__init__.py`: Initialization file for the `proxy_server` package.

- `proxy_server.py`: Main module containing the implementation of the proxy server.

- `utils.py`: Utility module containing helper functions used across the project.

## Overview

This project implements a simple proxy server using C language with features like caching and handling HTTP requests. Proxy servers act as intermediaries between clients and servers, forwarding client requests to the appropriate server and returning the server's response to the client. This proxy server can cache responses from remote servers to improve performance and reduce network traffic.

## Components Used

### Operating System Components
- **Sockets**: Used for communication between the proxy server and clients, as well as between the proxy server and remote servers.
- **Threads**: Utilized to handle multiple client requests concurrently, improving the server's responsiveness.
- **File I/O**: Used for caching responses from remote servers to disk.

### External Libraries
- **pthread**: Used for multithreading support to handle concurrent client requests.
- **semaphore**: Utilized to control access to shared resources, such as limiting the number of concurrent client connections.

## Limitations

- **HTTP Only**: This proxy server only supports HTTP requests and does not handle other protocols like HTTPS.
- **Basic Caching**: The caching mechanism implemented is basic and may not be suitable for high-performance or production environments.
- **Single-threaded Cache Management**: Cache management operations (adding, removing elements) are performed within a single thread, potentially leading to performance bottlenecks in high-traffic scenarios.

## How to Use

1. Ensure you have Python installed on your system. You can download it from the official Python website: https://www.python.org/downloads/.
2. Implement the proxy server functionality in Python, following the provided code structure.
3. Run the Python script that contains the proxy server implementation, specifying the desired port number for the proxy server.
4. Configure your web browser or application to use the proxy server by setting the proxy settings to localhost and the chosen port number.
5. Access web content through the configured proxy server, which will handle the requests and cache responses when applicable.
6. Monitor the console output or log files (if implemented) to observe the proxy server's behavior, including handling requests and caching responses.

## Project Structure

The project is organized into several directories and files:
- `cache/`: Contains functionality related to caching, including cache management.
- `http_parser/`: Contains modules for parsing HTTP requests.
- `proxy_server.py`: Main module containing the implementation of the proxy server.
- `utils.py`: Utility module containing helper functions used across the project.

## Contributors

- [Yash Mishra](https://github.com/Geekboieyash)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

