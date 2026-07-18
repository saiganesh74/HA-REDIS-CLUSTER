from redis.sentinel import Sentinel
import time

sentinels = [
    ("sentinel1", 26379),
    ("sentinel2", 26379),
    ("sentinel3", 26379),
]
sentinel = Sentinel(sentinels, socket_timeout=2)

print("Connected to Sentinel cluster.")

master = sentinel.discover_master("mymaster")

print(f"Current Master: {master}")