import threading
import redis
import time

class Cache:
    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
        self.lock = threading.Lock()
        self.MAX_SIZE = 1000000  # Max size of the cache
        self.MAX_ELEMENT_SIZE = 10000  # Max size of an individual cache element

    def remove_cache_element(self, key):
        with self.lock:
            print("Remove Cache Lock Acquired")
            self.redis_client.delete(key)
            print("Cache element removed")
            print("Remove Cache Lock Released")

    def add_cache_element(self, key, data):
        with self.lock:
            print("Add Cache Lock Acquired")
            self.redis_client.set(key, data)
            print("Cache element added")
            print("Add Cache Lock Released")

    def get_cache_element(self, key):
        with self.lock:
            print("Get Cache Lock Acquired")
            data = self.redis_client.get(key)
            print("Get Cache Lock Released")
            return data

if __name__ == "__main__":
    cache = Cache()
    cache.add_cache_element("www.example.com", "Some data")