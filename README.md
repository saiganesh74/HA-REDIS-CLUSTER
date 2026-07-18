# High Availability Redis Cluster with Redis Sentinel & HAProxy

A production-style Redis High Availability (HA) environment built using **Docker Compose**, featuring automatic failover with **Redis Sentinel** and client-side load balancing through **HAProxy**.

This project demonstrates how highly available Redis deployments are built in real-world environments where service continuity is critical.

---

# Architecture

```
                    +----------------------+
                    |      HAProxy         |
                    |   TCP Load Balancer  |
                    +----------+-----------+
                               |
                               |
                    +----------v-----------+
                    |    Redis Master      |
                    +----------+-----------+
                               |
          ---------------------+---------------------
          |                                         |
+---------v---------+                     +----------v---------+
|  Redis Replica 1  |                     |  Redis Replica 2   |
+---------+---------+                     +----------+---------+
          \                                      /
           \                                    /
            \                                  /
             +-------------+------------------+
                           |
                Redis Sentinel Cluster
             +---------+---------+---------+
             | Sentinel1| Sentinel2| Sentinel3|
             +---------+---------+---------+

```

---

# Features

- Redis Master
- Two Redis Replicas
- Three Redis Sentinel nodes
- Automatic failover
- HAProxy TCP load balancing
- Docker Compose deployment
- Persistent Redis volumes
- Production-inspired project structure

---

# Tech Stack

- Docker
- Docker Compose
- Redis 7
- Redis Sentinel
- HAProxy
- Linux

---

# Project Structure

```
ha-redis-cluster/
│
├── docker-compose.yml
├── README.md
│
├── haproxy/
│   └── haproxy.cfg
│
├── redis/
│   ├── master/
│   │   └── redis.conf
│   │
│   ├── replica1/
│   │   └── redis.conf
│   │
│   └── replica2/
│       └── redis.conf
│
├── sentinel/
│   ├── sentinel1.conf
│   ├── sentinel2.conf
│   └── sentinel3.conf
│
├── scripts/
│
└── docs/
```

---

# Prerequisites

Install:

- Docker
- Docker Compose

Verify installation

```bash
docker --version
docker compose version
```

---

# Getting Started

Clone the repository

```bash
git clone https://github.com/<your-username>/ha-redis-cluster.git
cd ha-redis-cluster
```

Start all services

```bash
docker compose up -d
```

Verify containers

```bash
docker compose ps
```

---

# Redis Topology

Current deployment consists of:

| Service | Port |
|----------|------|
| Redis Master | 6379 |
| Redis Replica 1 | 6380 |
| Redis Replica 2 | 6381 |
| Sentinel 1 | 26379 |
| Sentinel 2 | 26380 |
| Sentinel 3 | 26381 |
| HAProxy | 6378 |

---

# Verify Replication

Connect to the master

```bash
docker exec -it redis-master redis-cli
```

Store data

```redis
SET user Sai
GET user
```

Expected output

```
"OK"
"Sai"
```

---

Check replication

```redis
INFO replication
```

Expected

```
role:master
connected_slaves:2
```

---

Check a replica

```bash
docker exec -it redis-replica1 redis-cli
```

Run

```redis
GET user
```

Expected

```
"Sai"
```

---

# Redis Sentinel

Connect

```bash
docker exec -it redis-sentinel1 redis-cli -p 26379
```

View monitored master

```redis
SENTINEL masters
```

View replicas

```redis
SENTINEL replicas mymaster
```

View sentinels

```redis
SENTINEL sentinels mymaster
```

---

# Automatic Failover Test

Stop the master

```bash
docker stop redis-master
```

Watch Sentinel logs

```bash
docker logs -f redis-sentinel1
```

A replica should automatically become the new master.

Verify

```redis
SENTINEL masters
```

or

```redis
INFO replication
```

---

Restart the old master

```bash
docker start redis-master
```

It should automatically join the cluster as a replica.

---

# HAProxy

Connect through HAProxy

```bash
redis-cli -h localhost -p 6378
```

Run

```redis
PING
```

Expected

```
PONG
```

---


Remove everything

```bash
docker compose down -v
```

---

# Future Improvements

- Redis Authentication (ACL)
- TLS Encryption
- Prometheus Monitoring
- Grafana Dashboard
- Redis Exporter
- Docker Swarm deployment
- Kubernetes StatefulSet migration
- Persistent storage using volumes
- GitHub Actions CI/CD pipeline
- Terraform deployment on AWS

---

# Author

**Sai Ganesh**

GitHub: https://github.com/saiganesh74

---

# License

This project is licensed under the MIT License.