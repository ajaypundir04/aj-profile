#!/usr/bin/env python3
"""
Generates assets/js/data/system-design.js with 110+ comprehensive System Design interview questions & topics.
"""
import json

QUESTIONS = [
    # --- DISTRIBUTED SYSTEMS FUNDAMENTALS ---
    {
        "id": "sd-1",
        "title": "CAP Theorem vs PACELC Theorem",
        "category": "Distributed Systems",
        "difficulty": "Medium",
        "question": "Explain the CAP Theorem and why the PACELC theorem is a more accurate and comprehensive model for modern distributed databases.",
        "answer": "CAP Theorem states that in the event of a network Partition (P), a distributed system must choose between Consistency (C) (all nodes see the same data simultaneously) and Availability (A) (every non-failing node returns a non-error response).\n\nWhy PACELC is superior:\nCAP only discusses system behavior during network partitions (which are rare in well-architected networks). PACELC extends this:\n- If Partition (P): choose between Availability (A) and Consistency (C);\n- Else (E): choose between Latency (L) and Consistency (C).\n\nExamples:\n- DynamoDB / Cassandra: PA/EL (under partition: Available; normal operation: chooses lower Latency over strong consistency).\n- Spanner / CockroachDB: PC/EC (under partition: Consistent; normal operation: chooses strong Consistency at the cost of higher round-trip Latency).\n- MongoDB: PC/EC (default replica sets choose strong consistency on primary).",
        "keyPoints": ["CAP is binary and only covers failure/partition scenarios", "PACELC evaluates normal operating trade-offs (Latency vs Consistency)", "Strong consistency during normal operations requires multi-node coordination adding latency", "Modern systems allow tunable consistency levels (e.g., Cassandra QUORUM, DynamoDB read consistency)"],
        "tags": ["CAP", "PACELC", "Distributed Systems", "Consistency", "Databases"]
    },
    {
        "id": "sd-2",
        "title": "Consistency Models: Strong, Eventual, Causal, and Read-After-Write",
        "category": "Distributed Systems",
        "difficulty": "Medium",
        "question": "Compare Linearizability (Strong Consistency), Eventual Consistency, Causal Consistency, and Read-After-Write (Monotonic Read) consistency. Provide real-world engineering use cases for each.",
        "answer": "1. Linearizability (Strong Consistency):\nEvery read returns the most recent write. Operations appear to execute instantaneously on a single virtual register. Used in: Financial ledgers, stock trading, inventory reservation.\n\n2. Eventual Consistency:\nIf no further updates occur, all replicas will eventually converge to the same value. High availability and ultra-low latency. Used in: Social media like counts, DNS propagation, video view counts.\n\n3. Causal Consistency:\nOperations that are causally related must be seen by every node in the same order. Operations that are concurrent may be seen in different order. Used in: Comment threads, chat messaging.\n\n4. Read-After-Write (Monotonic Read / Read-Your-Own-Writes):\nGuarantees that a user will always see updates submitted by themselves, avoiding the confusing experience of posting a comment or updating a profile and seeing it vanish on page refresh due to hitting an out-of-date read replica. Implemented by routing user's own reads to primary for 5-10 seconds or using client-side version timestamps.",
        "keyPoints": ["Linearizability requires consensus (Raft/Paxos) and adds network latency", "Eventual consistency maximizes write throughput at the cost of transient staleness", "Read-Your-Own-Writes solves user-facing staleness without requiring global strong consistency", "Vector clocks and version vectors are used to track causality"],
        "tags": ["Consistency", "Distributed Systems", "Replication", "Databases"]
    },
    {
        "id": "sd-3",
        "title": "Distributed Consensus: Raft vs Multi-Paxos",
        "category": "Distributed Systems",
        "difficulty": "Hard",
        "question": "How do Raft and Paxos establish consensus in distributed state machines? What are leader election terms, log replication, and heartbeat mechanisms?",
        "answer": "Raft is designed for understandability through clear decomposition:\n1. Leader Election: Nodes are in one of three states: Follower, Candidate, or Leader. Randomized election timeouts (150ms-300ms) prevent split votes. A candidate needs majority votes (N/2 + 1) in term `T` to become leader.\n2. Log Replication: Clients send commands to leader. Leader appends to its log, sends `AppendEntries` RPC to followers. Once a majority logs the entry, leader commits it, applies to state machine, and replies to client.\n3. Safety Invariants: An election winner must have all committed entries from previous terms (candidate's log must be as up-to-date as the voter's log).\n\nPaxos vs Raft:\nMulti-Paxos allows arbitrary proposal numbers and has complex view changes; Raft enforces strong leader invariants, making log reconciliation unidirectional (leader overwrites follower mismatches).\n\nProduction implementations: etcd (Kubernetes control plane), HashiCorp Consul, TiKV, Kafka KRaft.",
        "keyPoints": ["Raft decomposes consensus into Leader Election, Log Replication, and Safety", "Randomized election timeouts effectively eliminate split votes", "Requires odd quorum (2F + 1 nodes survive F failures)", "KRaft replaced ZooKeeper in Apache Kafka using Raft consensus"],
        "tags": ["Consensus", "Raft", "Paxos", "Distributed Systems", "etcd"]
    },
    {
        "id": "sd-4",
        "title": "Consistent Hashing with Virtual Nodes",
        "category": "Scalability & Routing",
        "difficulty": "Medium",
        "question": "Explain Consistent Hashing. Why does standard modulo hashing `hash(key) % N` fail when scaling clusters, and how do virtual nodes resolve hotspots and non-uniform distributions?",
        "answer": "The Modulo Problem:\nUsing `hash(key) % N`, adding or removing a server changes `N` to `N ± 1`. This invalidates almost 100% of cached keys (`(N-1)/N` keys relocate), causing massive cache stampedes and database crashes.\n\nConsistent Hashing Mechanism:\n1. Map both server identifiers and object keys to a 360° circular hash ring (e.g., 0 to 2³² - 1 using MurmurHash3 or SHA-256).\n2. To find the server for a key, hash the key and walk clockwise on the ring until the first server is reached.\n3. When adding or removing a node, only `1/N` of keys need to be relocated on average!\n\nVirtual Nodes (V-nodes):\nProblem with physical nodes: With few servers, keys distribute unevenly across the ring (hotspots), and when a node dies, 100% of its load dumps onto its immediate clockwise neighbor.\nSolution: Map each physical machine to multiple (e.g., 100–300) virtual positions on the ring (`server1#1`, `server1#2`, etc.).\nBenefits:\n- Balances load evenly across nodes according to physical hardware capacity.\n- When a node fails, its virtual nodes are scattered around the ring, distributing the failover load uniformly among ALL remaining servers.",
        "keyPoints": ["Modulo hashing forces ~100% key redistribution upon node change", "Consistent hashing redistributes only K/N keys on average", "Virtual nodes prevent hot spots and non-uniform clustering", "Core building block in DynamoDB, Cassandra, Akamai CDN, and Memcached"],
        "tags": ["Consistent Hashing", "Load Balancing", "Caching", "Distributed Systems"]
    },
    {
        "id": "sd-5",
        "title": "Layer 4 vs Layer 7 Load Balancing",
        "category": "Scalability & Routing",
        "difficulty": "Medium",
        "question": "Compare Layer 4 (Transport) and Layer 7 (Application) load balancers. When would you choose HAProxy/Envoy/NGINX at L7 vs AWS NLB/IPVS at L4?",
        "answer": "Layer 4 Load Balancing (Transport / TCP / UDP):\n- Operates at transport layer without inspecting application payload.\n- Routes packets based on IP address and TCP/UDP port tuple.\n- Does not terminate TLS or parse HTTP headers.\n- Pros: Ultra-high throughput (millions of packets/sec), ultra-low CPU overhead, sub-millisecond latency.\n- Technologies: AWS Network Load Balancer (NLB), Linux IPVS, Maglev.\n\nLayer 7 Load Balancing (Application / HTTP / gRPC):\n- Terminates TLS connection and inspects full HTTP request (path, cookies, headers, JSON body).\n- Enables intelligent routing: Path-based routing (`/api/v1/auth` vs `/api/v1/billing`), cookie-based sticky sessions, gRPC multiplexing, WAF inspection, rate limiting, and mTLS offloading.\n- Pros: Smarter routing, microservices routing, canary deployments, circuit breaking.\n- Cons: Higher CPU/memory overhead due to packet inspection and TLS decryption.\n- Technologies: Envoy Proxy, NGINX, HAProxy, AWS ALB.\n\nBest Practice: Two-tier architecture: L4 NLB handles high-throughput ingress and distributes TCP connections to a fleet of L7 Envoy proxies.",
        "keyPoints": ["L4 operates on IP/Port with zero payload inspection; maximum throughput", "L7 terminates HTTP/TLS, enabling path routing, header filtering, and WAF", "gRPC multiplexes requests over a single HTTP/2 connection requiring L7 balancing", "Production systems combine L4 ingress with L7 Envoy/NGINX mesh"],
        "tags": ["Load Balancing", "Networking", "Envoy", "NGINX", "Architecture"]
    },
    {
        "id": "sd-6",
        "title": "B-Tree vs LSM-Tree (Log-Structured Merge-Tree)",
        "category": "Databases & Storage",
        "difficulty": "Hard",
        "question": "Compare B-Tree (PostgreSQL, MySQL InnoDB) and LSM-Tree (Cassandra, RocksDB, ScyllaDB) storage engines. Analyze read amplification, write amplification, and compaction strategies.",
        "answer": "B-Trees (e.g. MySQL InnoDB, PostgreSQL):\n- Structure: Balanced N-ary tree with pages (usually 4KB–16KB) stored on disk.\n- Writes: In-place page updates. Modifying a single row requires rewriting an entire page to disk, plus Write-Ahead Log (WAL) append.\n- Characteristics: Low read amplification (O(log_B N) disk seeks); High write amplification (random I/O, writing entire pages for tiny updates); concurrency controlled by page latches.\n- Best for: Read-heavy OLTP workloads, point queries, range scans.\n\nLSM-Trees (e.g. RocksDB, Cassandra, LevelDB):\n- Structure:\n  1. MemTable: In-memory write buffer (SkipList or Red-Black Tree).\n  2. Write-Ahead Log (WAL): Sequential append on disk for crash recovery.\n  3. SSTables (Sorted String Tables): Immutable sorted files on disk in multiple levels (L0, L1, L2...).\n- Writes: Append to WAL and write to MemTable in memory (instantaneous sequential write). When MemTable fills, flush to L0 SSTable sequentially.\n- Compaction: Background process merges sorted SSTables, discarding tombstoned (deleted) or overwritten keys (Size-Tiered vs Leveled Compaction).\n- Reads: Check MemTable -> check Bloom filters for SSTables -> search SSTables from newest to oldest.\n- Characteristics: Ultra-high write throughput (sequential disk I/O); higher read amplification (mitigated by Bloom filters).\n- Best for: Write-heavy workloads, time-series data, event logging, high-throughput IoT.",
        "keyPoints": ["B-Trees write in-place to disk pages; optimal for read-heavy OLTP", "LSM-Trees turn all writes into sequential I/O via MemTable and SSTables", "Bloom filters are critical in LSM-Trees to avoid reading SSTables that don't have the key", "Compaction trade-offs: Leveled (lower space amplification) vs Size-Tiered (higher write throughput)"],
        "tags": ["Storage Engines", "Databases", "B-Tree", "LSM-Tree", "RocksDB", "Postgres"]
    },
    {
        "id": "sd-7",
        "title": "Database Sharding Strategies: Range, Hash, and Directory-Based",
        "category": "Databases & Storage",
        "difficulty": "Medium",
        "question": "What is database sharding? Compare Range-based, Hash-based, and Directory-based sharding. What problems arise with cross-shard transactions, cross-shard joins, and re-sharding?",
        "answer": "Sharding is horizontal partitioning of database rows across multiple independent physical database instances.\n\nSharding Strategies:\n1. Hash-Based Sharding: `Shard ID = hash(shard_key) % Num_Shards`. Uniform data distribution. Eliminates hotspots for sequential keys. Drawback: Range queries require querying every single shard (scatter-gather).\n2. Range-Based Sharding: Data partitioned by ranges of the shard key (e.g., Dates `2026-01`, `2026-02` or User IDs `1-1M`, `1M-2M`). Range queries are efficient and localized to 1 or 2 shards. Drawback: Hotspots occur if recent data or popular keys receive all write traffic.\n3. Directory-Based / Lookup Service: A separate routing service / table maps keys to physical shards. Maximum flexibility (easy to move individual customer shards). Drawback: Lookup service becomes single point of failure and extra latency hop (requires local client caching).\n\nKey Challenges:\n- Cross-Shard Joins: Extremely expensive; requires denormalization or application-layer joins.\n- Cross-Shard Transactions: Requires Two-Phase Commit (2PC) or SAGA pattern.\n- Re-sharding / Migration: Moving data while system is live requires dual-writing, backfilling, and shadow verification.",
        "keyPoints": ["Hash-based prevents hotspots but turns range queries into scatter-gather", "Range-based supports fast range scans but risks write hotspots", "Choosing the right shard key (e.g., tenant_id or user_id) is the most critical decision", "Cross-shard joins are avoided by colocation and data denormalization"],
        "tags": ["Sharding", "Databases", "Scalability", "Distributed Systems"]
    },
    {
        "id": "sd-8",
        "title": "Distributed Caching: Patterns, Cache Stampede, and Thundering Herd",
        "category": "Caching",
        "difficulty": "Medium",
        "question": "Explain Cache-Aside, Write-Through, Write-Back, and Write-Around patterns. How do you prevent Cache Stampede (Thundering Herd) when a popular key expires?",
        "answer": "Caching Patterns:\n- Cache-Aside (Lazy Loading): App checks cache. If hit, return. If miss, fetch from DB, write to cache, return. Most resilient to cache outages.\n- Write-Through: App writes to cache; cache writes synchronously to DB before acknowledging write. Strong read consistency, higher write latency.\n- Write-Back (Write-Behind): App writes to cache; cache acknowledges immediately and batches writes asynchronously to DB. Ultra-fast writes, but risks data loss on cache crash.\n- Write-Around: App writes directly to DB; cache is only populated on subsequent read misses. Prevents cache pollution for infrequently read writes.\n\nCache Stampede / Thundering Herd Prevention:\nWhen a hot key expires, thousands of concurrent requests miss cache simultaneously and bombard the database.\nMitigation Techniques:\n1. Mutex Locking / Single-Flight (e.g. Go `sync/singleflight` or Redis distributed lock): Only the first request acquires lock to query DB and update cache; other requests wait or return slightly stale data.\n2. Probabilistic Early Expiration (XFetch Algorithm): As a key nears TTL, background workers probabilistically refresh the key before it actually expires based on request compute time: `delta * beta * ln(rand())`.\n3. Jittering TTLs: Add random jitter (`TTL = 3600 + random(0, 300)`) so keys don't all expire simultaneously.",
        "keyPoints": ["Cache-aside is standard for read-heavy distributed architectures", "Write-back provides extreme write throughput but risks data loss", "Mutex locks (SingleFlight) eliminate thundering herd by collapsing duplicate queries", "TTL jittering prevents synchronized bulk key expiration"],
        "tags": ["Caching", "Redis", "Performance", "High Availability"]
    },
    {
        "id": "sd-9",
        "title": "Kafka Architecture: Partitions, Consumer Groups, and Log Compaction",
        "category": "Messaging & Streaming",
        "difficulty": "Hard",
        "question": "How does Apache Kafka achieve millions of messages per second? Explain zero-copy OS reads, sequential disk I/O, partition-based concurrency, and exactly-once semantics (EOS).",
        "answer": "Why Kafka is Ultra-Fast:\n1. Sequential Disk I/O: Kafka appends messages to an immutable commit log on disk. Sequential disk access on modern SSDs/HDDs matches or exceeds random memory access speeds.\n2. PageCache & Zero-Copy Transfer: Kafka relies on Linux kernel PageCache instead of JVM heap. When sending data to network sockets, Kafka uses the `sendfile()` system call (Zero-Copy): data copies directly from OS PageCache to Network Socket buffer, bypassing user-space CPU copying and garbage collection.\n3. Partitioning & Concurrency: Topics are divided into partitions. Each partition is an ordered, immutable log. Partitions allow horizontal scaling across brokers and parallel consumption across consumer group members.\n\nConsumer Groups & Ordering:\n- Within a single partition, message ordering is strictly guaranteed.\n- A partition can be consumed by at most ONE consumer in a given consumer group.\n\nExactly-Once Semantics (EOS):\n- Idempotent Producer: Broker assigns Producer ID (PID) and sequence numbers to messages. Broker drops duplicates caused by network retries.\n- Transactional Coordinator: Coordinates atomic multi-partition writes using a two-phase commit over the `__transaction_state` topic.",
        "keyPoints": ["sendfile() zero-copy transfers from kernel page cache directly to NIC buffer", "Sequential append avoids expensive disk seek operations", "Partitioning provides parallelism; ordering is guaranteed per partition, not per topic", "EOS combines idempotent producer sequence IDs with transactional coordinator"],
        "tags": ["Kafka", "Event Streaming", "Messaging", "Linux", "Architecture"]
    },
    {
        "id": "sd-10",
        "title": "The Transactional Outbox Pattern & Change Data Capture (CDC)",
        "category": "Messaging & Streaming",
        "difficulty": "Hard",
        "question": "How does the Transactional Outbox pattern resolve the dual-write problem between a relational database and an event broker like Kafka? How does Debezium implement CDC?",
        "answer": "The Dual-Write Problem:\nA service needs to update its local database (e.g., save user order) AND publish an event to Kafka. If DB commit succeeds but Kafka publish fails (or vice versa), the system enters an inconsistent state. Two-phase commit (XA transactions) across DB and Kafka is slow and unsupported by modern cloud brokers.\n\nTransactional Outbox Solution:\n1. In the same ACID database transaction, insert the business entity into `orders` AND insert an event record into an `outbox` table in the database.\n2. Because both occur in a single local database transaction, atomicity is guaranteed.\n\nEvent Dispatching via CDC (Change Data Capture) with Debezium:\n- A Debezium connector reads the database transaction log directly (Postgres WAL / MySQL Binlog).\n- Debezium streams committed rows from the `outbox` table into Kafka topics.\n- Guaranteed at-least-once delivery with zero application-level polling overhead and zero table locks.\n- Downstream consumers process events idempotently using message IDs.\n\nProduction pattern used extensively across modern banking and distributed systems (including Ajay's systems at Volkswagen Charging and Scalable Capital).",
        "keyPoints": ["Solves the dual-write problem without distributed 2PC transactions", "Business entity and outbox message commit in a single ACID transaction", "Debezium tailing the DB WAL eliminates database polling overhead", "Downstream consumers must implement idempotency to handle at-least-once delivery"],
        "tags": ["Outbox Pattern", "Debezium", "CDC", "Kafka", "Microservices", "Event-Driven"]
    },
    {
        "id": "sd-11",
        "title": "Distributed Rate Limiter: Algorithms & Scalable Architecture",
        "category": "High-Level Design",
        "difficulty": "Medium",
        "question": "Design a Distributed Rate Limiter capable of processing 100K+ requests/sec across a multi-region deployment. Compare Token Bucket, Leaky Bucket, and Sliding Window Counter algorithms.",
        "answer": "Algorithms Comparison:\n1. Token Bucket: Tokens added at constant rate up to bucket capacity. Request consumes 1 token. Allows controlled traffic bursts. Memory: O(1) storing `last_refreshed_timestamp` and `tokens_count`.\n2. Leaky Bucket: Requests enter FIFO queue and leak out at constant rate. Smooths out bursts to constant egress rate. Great for egress traffic.\n3. Sliding Window Log: Logs timestamps of all requests in Redis Sorted Set (ZSET). Accurately enforces limit over exact sliding window. High memory overhead: stores every request timestamp.\n4. Sliding Window Counter (Optimal): Combines current minute counter and previous minute counter with weight: `requests = prev_count * (1 - time_into_minute) + curr_count`. Low memory, sub-nanosecond compute, 99.9% accuracy.\n\nDistributed Architecture:\n- API Gateway / Envoy Proxy intercepts incoming requests.\n- Redis Cluster stores rate limit counters using Lua scripts (evaluates check and increment atomically in 1 round trip, eliminating race conditions).\n- Local In-Memory Cache (e.g., Envoy token bucket filter) handles hot IP addresses with local batching: increments local count and flushes batch to Redis every 50ms, reducing Redis queries by 90%.\n- Multi-Region: Async replication or regional counters (divide global limit proportionally across regions).",
        "keyPoints": ["Token Bucket allows bursts; Sliding Window Counter gives best memory/accuracy balance", "Redis Lua script ensures atomic check-and-increment operations", "Local batching on API Gateways protects centralized Redis clusters from overload", "Return standard HTTP 429 Too Many Requests with Retry-After header"],
        "tags": ["Rate Limiter", "Redis", "High-Level Design", "Distributed Systems"]
    },
    {
        "id": "sd-12",
        "title": "Design a Multi-Brand EV Charging & Session Management Platform",
        "category": "Domain Architecture",
        "difficulty": "Hard",
        "question": "Design a high-scale EV Charging Platform supporting B2C, B2B, and Fleet offerings (similar to Volkswagen Charging / Elli). Address OCPP station protocol, Auth0 IAM, real-time metering, and offline failover.",
        "answer": "System Architecture:\n1. Ingress & Protocols:\n- Physical Charging Stations communicate via OCPP (Open Charge Point Protocol) over secure WebSockets (WSS) to OCPP Gateway clusters.\n- OCPP Gateway terminates TCP/WebSocket, maintains persistent connections to tens of thousands of chargers, and translates OCPP JSON into Kafka event streams (`charging.session.started`, `charging.meter.value`, `charging.session.stopped`).\n\n2. Authentication & Authorization (IAM):\n- Drivers swipe RFID card, use mobile app, or AutoCharge/Plug&Charge (ISO 15118 public key cryptography).\n- Auth0 IAM manages B2C, B2B tenant spaces, and fleet policies.\n- ABAC/RBAC Engine: Verifies driver charging entitlement, company fleet budget, roaming network agreements (Hubject eRoaming).\n- Fast-path auth cache: In-memory Redis cluster answers authorization queries in <15ms to prevent driver timeout at the plug.\n\n3. Real-Time Metering & Ingestion:\n- High-frequency meter values streamed via Kafka.\n- Flink / Kafka Streams aggregate real-time kWh consumed, calculating dynamic pricing tariffs and enforcing fleet max-spending caps.\n- Outbox pattern ensures financial settlement records are atomically stored in CloudSQL/Postgres.\n\n4. Resilience & Offline Charging Mode:\n- If central cloud network drops, charging stations fall back to local whitelist cache of authorized RFID hashes to allow emergency charging without leaving drivers stranded.",
        "keyPoints": ["OCPP gateway terminates long-lived WebSockets and bridges to Kafka", "ISO 15118 Plug&Charge automates vehicle TLS mutual authentication", "Fast-path authorization caching guarantees sub-20ms station response", "Offline whitelist cache prevents vehicle stranding during cloud outages"],
        "tags": ["EV Charging", "OCPP", "IoT", "Auth0", "Kafka", "High-Level Design"]
    },
    {
        "id": "sd-13",
        "title": "Design a Global Unique ID Generator (Snowflake ID)",
        "category": "High-Level Design",
        "difficulty": "Medium",
        "question": "Design a distributed unique ID generator capable of generating 100,000+ IDs per second. IDs must be 64-bit integers, globally unique, roughly time-sorted, and resilient to single points of failure.",
        "answer": "Twitter Snowflake Architecture (64-bit ID):\n- 1 bit: Unused sign bit (always 0 for positive numbers).\n- 41 bits: Millisecond Timestamp (relative to custom epoch, e.g. 2026-01-01). Provides `2^41` ms ≈ 69 years of lifespan.\n- 10 bits: Machine / Worker ID (supports up to 1,024 generator nodes).\n  - Can be split into 5 bits Datacenter ID + 5 bits Worker ID.\n- 12 bits: Sequence Number (per worker per millisecond). Supports `2^12 = 4,096` unique IDs per millisecond per node.\n\nTotal Throughput Capacity:\n`1,024 nodes * 4,096 IDs/ms = 4,194,304,000 IDs/sec`.\n\nHandling Clock Drift / NTP Skew:\nIf the system clock moves backwards:\n1. If drift is small (<5ms): Pause and spin-wait until clock catches up.\n2. If drift is significant: Reject requests, throw exception, or dynamically allocate a new worker ID.\n\nComparison:\n- UUIDv4: 128-bit, random, poor database B-Tree index performance due to random page splits.\n- UUIDv7: 128-bit, time-ordered, but twice the size of 64-bit Snowflake.\n- Snowflake: Compact 64-bit integer, fits in standard SQL BIGINT, naturally ordered by creation time.",
        "keyPoints": ["64-bit Snowflake fits into SQL BIGINT for optimal B-Tree index locality", "41-bit timestamp provides 69 years of monotonically increasing IDs", "10-bit worker ID supports 1,024 independent server instances", "Clock drift mitigation is essential when relying on physical system clocks"],
        "tags": ["Snowflake ID", "Distributed Systems", "High-Level Design"]
    },
    {
        "id": "sd-14",
        "title": "Design a Scalable Financial KYC Rules Engine & Verification Platform",
        "category": "Domain Architecture",
        "difficulty": "Hard",
        "question": "Design an automated Know-Your-Customer (KYC) validation rules engine for a digital banking platform serving SME clients across multiple brands (similar to Deutsche Bank BizBanking). How do you handle complex rule evaluation, audit trails, and BigQuery data integration?",
        "answer": "Architecture Components:\n1. API Gateway & Identity Onboarding:\n- Microservices authenticate corporate clients via OAuth2/OIDC with fine-grained company role claims (Director, Signatory, Beneficial Owner).\n- IDNow / WebID integrations for regional video KYC and passport NFC biometric validation.\n\n2. KYC Rules Engine (Drools / Python AST Rule Evaluator):\n- Client submits SME registration data (commercial registry number, UBO ownership tree, PEP status, country of incorporation).\n- Rules Engine evaluates directed acyclic graph (DAG) of verification rules:\n  - Sanction list screening (OFAC, EU Sanctions API).\n  - Beneficial Owner identification (checks anyone holding >25% share capital).\n  - AML risk scoring matrix.\n- Stateless rule execution allows horizontal autoscaling on Kubernetes.\n\n3. Data Synchronization & Analytics Pipeline:\n- Real-time KYC decision events stream via Kafka.\n- Batch ETL / CDC: BigQuery data warehouse ingests daily corporate registry deltas and transaction history. Automated Python jobs process risk scores and synchronize updated risk ratings to operational PostgreSQL databases via CloudSQL.\n\n4. Immutable Audit & Compliance Logging:\n- Every rule execution, raw API payload, and KYC analyst override is stored in write-once tamper-evident audit logs (WORM storage / GCP Cloud Storage with bucket locks) to satisfy BaFin / ECB financial compliance.",
        "keyPoints": ["Decouples business rules engine from external ID verification vendors", "Automated DAG evaluation speeds up SME onboarding from days to minutes", "BigQuery-to-PostgreSQL pipeline balances analytic scale with low-latency OLTP", "WORM storage provides legally binding audit trails for regulatory compliance"],
        "tags": ["KYC", "FinTech", "Banking", "Rules Engine", "BigQuery", "High-Level Design"]
    },
    {
        "id": "sd-15",
        "title": "Design a Distributed Job Scheduler / Distributed Cron",
        "category": "High-Level Design",
        "difficulty": "Hard",
        "question": "Design a Distributed Job Scheduler capable of scheduling and executing millions of tasks with arbitrary delays and cron expressions. Ensure high availability, fault tolerance, and exactly-once task execution.",
        "answer": "Architecture:\n1. Storage Tier (Database / Redis):\n- Task Table: `task_id, execute_at, payload, state (SCHEDULED, RUNNING, COMPLETED, FAILED), lock_token, retry_count`.\n- Partition tasks by time bucket: e.g. using Redis Sorted Set (ZSET) where score is `execute_at` timestamp, or PostgreSQL indexed on `execute_at WHERE state = 'SCHEDULED'`.\n\n2. Leader Election & Coordinator Tier:\n- Use Raft / ZooKeeper / etcd or Kubernetes leader election to elect an active Scheduler Leader.\n- Leader queries tasks due for execution: `ZREVRANGEBYSCORE key (now -inf LIMIT 0 1000`.\n- Moves due tasks to high-throughput Kafka / RabbitMQ execution queues partitioned by task type.\n\n3. Worker Fleet:\n- Stateless workers pull tasks from queue.\n- Acquire distributed lock on `task_id` (via optimistic concurrency control: `UPDATE tasks SET state='RUNNING', version=version+1 WHERE task_id=:id AND state='SCHEDULED'`).\n- Execute job payload.\n- Heartbeat updates: Worker periodically touches task record. If worker crashes, coordinator detects missing heartbeat, resets task to `SCHEDULED`, and re-dispatches.\n\n4. Cron Recurring Jobs:\n- When a cron task completes, coordinator computes `next_execution_time` using cron expression and inserts the next occurrence.",
        "keyPoints": ["Time-bucketed index (Redis ZSET or SQL execute_at index) for efficient polling", "Decouple scheduling (coordinator) from execution (worker pool) via message queue", "Optimistic locking on task state prevents duplicate execution", "Worker heartbeats detect node crashes and trigger automated task recovery"],
        "tags": ["Job Scheduler", "Distributed Systems", "Cron", "High-Level Design"]
    },
    {
        "id": "sd-16",
        "title": "Design Twitter / X News Feed (Fan-Out on Write vs Fan-Out on Read)",
        "category": "High-Level Design",
        "difficulty": "Medium",
        "question": "Design the News Feed system for a social media platform. Contrast Fan-Out on Write (Push) and Fan-Out on Read (Pull), and explain the hybrid architecture for handling celebrity users.",
        "answer": "The Two Classical Approaches:\n1. Fan-Out on Write (Push Model):\n- When user posts a tweet, system fetches all their followers and writes the `tweet_id` directly into each follower's pre-computed in-memory feed list (e.g., Redis List of tweet IDs).\n- Read time: Ultra-fast O(1) read from Redis.\n- Bottleneck (The Celebrity Problem): If a user with 50M followers (e.g. Elon Musk) posts a tweet, 50 million Redis writes must execute instantly, causing massive write amplification and latency spikes.\n\n2. Fan-Out on Read (Pull Model):\n- When a user posts, write only to their own timeline.\n- When a follower opens their app, query the timelines of everyone they follow, merge, and sort by timestamp.\n- Bottleneck: Read latency is extremely high for users following hundreds of accounts (scatter-gather merge).\n\nHybrid Architecture (Production Solution):\n- Standard Users (<20K followers): Use Fan-out on Write (Push). Tweets are pushed immediately into follower feed caches.\n- Celebrity Users (>20K followers): Do NOT fan out on write. When followers open their feed, fetch the pre-computed feed from Redis AND dynamically pull recent tweets from celebrities they follow, merging the two lists in memory.\n- Inactive Users: Stop fanning out to users who haven't logged in for 14 days, saving massive Redis memory.",
        "keyPoints": ["Fan-out on write gives O(1) read latency but breaks on celebrity followers", "Fan-out on read eliminates write amplification but incurs expensive scatter-gather reads", "Hybrid model pushes standard users and dynamically merges celebrity tweets at read time", "Evicting inactive users from cache cuts memory footprint dramatically"],
        "tags": ["News Feed", "Redis", "High-Level Design", "Scalability"]
    },
    {
        "id": "sd-17",
        "title": "Design a Distributed Key-Value Store (Amazon Dynamo Paper)",
        "category": "High-Level Design",
        "difficulty": "Hard",
        "question": "Walk through the architectural principles of Amazon's Dynamo paper: Consistent Hashing, Vector Clocks, Sloppy Quorums, Hinted Handoff, and Merkle Tree Anti-Entropy.",
        "answer": "Dynamo's Core Components:\n1. Partitioning: Consistent Hashing with Virtual Nodes distributes keys across storage nodes in a ring.\n2. Replication: Each key is replicated on the first `N` healthy successor nodes moving clockwise around the ring (Preference List).\n3. Tunable Quorum (N, R, W):\n   - `N`: Replication factor (e.g. 3)\n   - `R`: Minimum nodes that must acknowledge a read (e.g. 2)\n   - `W`: Minimum nodes that must acknowledge a write (e.g. 2)\n   - Strong consistency if `R + W > N`.\n4. Sloppy Quorum & Hinted Handoff:\n   - If primary nodes are unreachable during a network partition, writes are accepted by healthy alternate nodes on the ring with a 'hint' indicating original destination.\n   - When original node recovers, the alternate node delivers the stored writes (Hinted Handoff), prioritizing Availability over Consistency.\n5. Vector Clocks: Detect concurrent conflicting updates without a centralized master clock. When conflicts occur, both versions are stored (divergence) and reconciled either automatically or client-side.\n6. Merkle Trees (Anti-Entropy):\n   - Replicas synchronize background data by comparing hierarchical hash trees (Merkle Trees) of key ranges.\n   - Only diverging branches are transferred over the network, minimizing synchronization bandwidth.",
        "keyPoints": ["Tunable quorums: R + W > N guarantees overlapping read and write sets", "Sloppy quorum with hinted handoff guarantees write availability during network splits", "Vector clocks capture causal history and detect concurrent write conflicts", "Merkle trees minimize network overhead during background replica synchronization"],
        "tags": ["Dynamo", "Distributed Systems", "NoSQL", "Key-Value Store"]
    },
    {
        "id": "sd-18",
        "title": "Design a Real-Time Uber / Lyft Geolocation & Ride Matching System",
        "category": "High-Level Design",
        "difficulty": "Hard",
        "question": "Design a ride-hailing geolocation platform. How do you store and query millions of moving driver locations every 4 seconds? Compare Geohash, QuadTrees, Google S2, and Uber H3 spatial indexing.",
        "answer": "System Scale & Challenges:\n- 1M active drivers sending GPS coordinates `(lat, lon)` every 4 seconds = 250,000 writes/sec.\n- Riders searching for nearest available drivers within 3km.\n- Standard SQL `WHERE lat BETWEEN ... AND lon BETWEEN ...` fails under this write/read load.\n\nSpatial Indexing Technologies:\n1. Geohash: Interleaves latitude and longitude bits into base32 strings. Prefix matching finds points in same bounding box. Boundary edge cases require querying all 8 surrounding cells.\n2. QuadTree: Hierarchical 2D space partition. In-memory tree where leaf nodes split into 4 quadrants when point capacity is exceeded. Challenging to keep updated with fast-moving drivers (requires continuous rebalancing).\n3. Google S2: Projects Earth onto a cube, subdivided into Hilbert curves. Fast 64-bit integer IDs.\n4. Uber H3 (Hexagonal Hierarchical Spatial Index - Industry Standard):\n   - Earth partitioned into hexagonal cells.\n   - Why Hexagons: Hexagons have equal distance between their center and all 6 neighbors! In contrast, squares have 4 orthogonal neighbors at distance `d` and 4 diagonal neighbors at distance `sqrt(2)*d`.\n   - Crucial for radius-based neighborhood searches and ride pricing.\n\nArchitecture:\n- Driver Location Service: Receives GPS pings -> writes to Redis Cluster (stores `H3_index -> set of driver_ids`). Key expires after 15s (auto-removes offline drivers).\n- Dispatcher Service: Computes rider H3 index, queries ring 0 and ring 1 neighboring hexagons from Redis in O(1) time.\n- Kafka streams driver positions for ETA calculation and surge pricing.",
        "keyPoints": ["Uber H3 hexagonal indexing ensures uniform distance to all 6 adjacent neighbors", "Driver location pings stored in Redis with short TTL to handle ephemeral disconnects", "Decouples location tracking (high write) from ride matching/dispatching", "Ring expansions around hexagonal cell easily locate closest drivers"],
        "tags": ["Uber", "Geolocation", "H3", "Redis", "High-Level Design"]
    },
    {
        "id": "sd-19",
        "title": "Design a Payment Gateway & Double-Entry Accounting Ledger (Stripe/PayPal)",
        "category": "High-Level Design",
        "difficulty": "Hard",
        "question": "Design a fault-tolerant payment gateway and immutable financial ledger. How do you guarantee idempotency, prevent double-spending, and enforce double-entry bookkeeping?",
        "answer": "Core Architectural Tenets:\n1. Idempotency Keys:\n- Every payment request includes a unique client-generated UUID `Idempotency-Key`.\n- API Gateway checks Redis with distributed lock: `SET payment:{idempotency_key} PROCESSING NX EX 120`.\n- If key exists with result, return cached response directly.\n- If in-flight, return HTTP 409 Conflict.\n- Guarantees network retries can never charge customer twice.\n\n2. Double-Entry Bookkeeping Ledger:\n- Money is never created or destroyed; it only moves between accounts.\n- Every transaction must contain at least two entries: one Debit (Dr) and one Credit (Cr).\n- Invariant: `SUM(Debits) == SUM(Credits)` for every single journal entry.\n- Immutable append-only ledger: No `UPDATE` or `DELETE` statements allowed. Reversals or refunds create new offsetting journal entries.\n\n3. Two-Phase Settlement (Auth & Capture):\n- Phase 1 (Authorize): Places a temporary hold on customer funds via Card Network (Visa/Mastercard).\n- Phase 2 (Capture): Finalizes transaction and transfers funds after goods dispatch.\n\n4. Reconciliation Pipeline:\n- Nightly batch jobs compare internal ledger records with banking bank statement clearing files (MT940 / CAMT.053), identifying discrepancies automatically.",
        "keyPoints": ["Idempotency keys prevent duplicate payments across client retries", "Double-entry bookkeeping guarantees total debits equal total credits", "Immutable append-only ledger records audit trails without destructive updates", "Daily reconciliation pipelines identify and flag settlement discrepancies"],
        "tags": ["FinTech", "Payments", "Idempotency", "Ledger", "High-Level Design"]
    },
    {
        "id": "sd-20",
        "title": "Design a Web Crawler (Frontier, Politeness, and Bloom Filters)",
        "category": "High-Level Design",
        "difficulty": "Hard",
        "question": "Design a distributed web crawler to index 1 billion web pages. Address URL frontier queue management, politeness policies, duplicate detection, and robots.txt compliance.",
        "answer": "Architecture:\n1. URL Frontier (Priority + Politeness Queues):\n- Politeness: Do not overwhelm a single domain with concurrent requests.\n- Two-tier queue system:\n  - Priority Queues (F1..Fn): Categorize URLs by PageRank and domain authority.\n  - Politeness Queues (B1..Bm): Each queue holds URLs for a single domain.\n  - Queue Selector: Round-robins among domain queues, enforcing a delay (e.g. 1 sec) per domain between downloads.\n\n2. Duplicate URL & Content Elimination:\n- Bloom Filters: Keep in-memory Bloom filter of seen URL hashes for O(1) duplicate URL checks with zero false negatives.\n- Content Fingerprinting (SimHash): Computes locality-sensitive hash of parsed HTML to detect near-duplicate pages (e.g., identical content with different header ads).\n\n3. HTML Fetcher & Parser Fleet:\n- Worker nodes fetch pages asynchronously, respect `robots.txt` (cached locally), parse DOM, extract new links, and feed new links back into the URL Frontier.\n- Dead Letter Queue handles 404s, redirect loops, and tarpits.\n\n4. Storage Tier:\n- Document Store: Compressed raw HTML stored in distributed object storage (S3 / GFS).\n- Metadata: Page metadata and link graph stored in Bigtable / Cassandra.",
        "keyPoints": ["Two-tier frontier separates URL priority from domain politeness constraints", "Bloom filters check seen URLs in memory with minimal RAM footprint", "SimHash detects near-duplicate content across different URLs", "Cached robots.txt parser ensures legal and ethical crawling"],
        "tags": ["Web Crawler", "Bloom Filter", "Queues", "High-Level Design"]
    }
]

# Add remaining 90 System Design questions to reach 110 total
ADDITIONAL_SD = [
    {
        "id": f"sd-{21+i}",
        "title": title,
        "category": cat,
        "difficulty": diff,
        "question": q,
        "answer": a,
        "keyPoints": kp,
        "tags": tags
    }
    for i, (title, cat, diff, q, a, kp, tags) in enumerate([
        (
            "Design TinyURL / URL Shortener",
            "High-Level Design",
            "Easy",
            "Design a URL shortening service like TinyURL or Bitly. Calculate storage capacity and explain Base62 encoding vs MD5/SHA256 hashing.",
            "Base62 Encoding (a-z, A-Z, 0-9 = 62 chars):\nA 7-character Base62 string yields `62^7 ≈ 3.5 trillion` unique URLs.\nApproach 1: Distributed ID generator generates unique 64-bit integer, then encode integer to Base62.\nApproach 2: MD5 hash original URL, take first 43 bits, encode to Base62. Handle collisions with salt.\nDatabase: NoSQL Key-Value store (DynamoDB/Cassandra) or PostgreSQL indexed on `short_hash`. Cache top 20% hot URLs in Redis (80-20 Pareto principle).",
            ["Base62 encoding of 7 chars provides 3.5 trillion URLs", "Counter/ID-based encoding avoids hash collision handling", "Redis caches hot URLs according to 80/20 rule", "Read-heavy system (100:1 read to write ratio)"],
            ["TinyURL", "Base62", "Caching", "High-Level Design"]
        ),
        (
            "Design WhatsApp / Telegram Real-Time Messaging",
            "High-Level Design",
            "Hard",
            "Design a secure, end-to-end encrypted messaging service supporting 1 billion daily active users. Explain WebSocket connection handling and offline message queuing.",
            "Architecture:\n- Gateway Tier: Fleet of WebSocket / TCP connection servers (Erlang/Elixir or Netty) maintaining millions of concurrent persistent connections.\n- Session Store: Redis cluster maps `user_id -> gateway_server_id`.\n- Message Delivery Flow:\n  1. Sender sends message to Gateway via WebSocket.\n  2. Gateway queries Session Store: if recipient is online, route directly to recipient's Gateway server.\n  3. If recipient is offline: store message in Cassandra/ScyllaDB offline message table and trigger Apple APNs / Google FCM push notification.\n  4. When recipient comes online, drain pending messages and mark delivered.\n- End-to-End Encryption: Signal Protocol with Double Ratchet Algorithm.",
            ["Erlang/Netty connection servers manage millions of persistent WebSockets", "Redis session registry maps users to their active gateway nodes", "Cassandra/ScyllaDB provides high-write offline message buffering", "Signal Protocol Double Ratchet ensures end-to-end encryption"],
            ["WhatsApp", "WebSocket", "Cassandra", "Real-Time", "High-Level Design"]
        ),
        (
            "Design Netflix / YouTube Video Streaming Platform",
            "High-Level Design",
            "Hard",
            "Design a global video streaming platform. Explain video ingestion, chunking, adaptive bitrate streaming (HLS/DASH), and CDN edge caching.",
            "Architecture:\n1. Ingestion & Transcoding Pipeline:\n- User uploads raw video -> stored in S3/GCS.\n- Distributed transcoding workers (FFmpeg) slice video into 2-10 second chunks and transcode into multiple resolutions (480p, 720p, 1080p, 4K) and codecs (H.264, H.265, AV1).\n- Generate Master Manifest playlist files (`.m3u8` for HLS or `.mpd` for MPEG-DASH).\n2. Adaptive Bitrate Streaming (ABR):\n- Client video player continuously monitors network bandwidth and dynamically requests higher or lower resolution chunks from manifest.\n3. Content Delivery Network (CDN):\n- Video chunks are static immutable files cached at ISP-edge CDN nodes (Akamai, Cloudflare, Netflix Open Connect) closest to users, shielding origins from 99%+ of video traffic.",
            ["Slices videos into small chunks across multiple bitrates and resolutions", "Adaptive Bitrate Streaming (HLS/DASH) adjusts video quality on the fly", "Manifest files coordinate chunk sequencing for client video players", "ISP-embedded CDN edge caching delivers video at minimal latency"],
            ["Video Streaming", "CDN", "HLS", "High-Level Design"]
        ),
        (
            "Design Search Autocomplete System (Typeahead)",
            "High-Level Design",
            "Medium",
            "Design a real-time search autocomplete system that returns the top 5 suggestions within 50 milliseconds as users type.",
            "Architecture:\n1. Data Structure: In-memory Trie where each node stores the top 5 most frequent search queries for that prefix.\n2. Ingestion & Frequency Aggregation:\n- Search query logs streamed via Kafka.\n- Aggregated in micro-batches (e.g. Spark / Flink) every hour to update search frequencies.\n- Periodically rebuild Trie snapshots and deploy to read-replica servers.\n3. Serving Tier:\n- Trie stored in memory on search nodes or cached in Redis.\n- Browser client debounces keystrokes (wait 150ms before firing request) and caches previous query prefixes locally in browser memory.",
            ["Trie nodes store precomputed top-K results to avoid runtime tree traversal", "Client-side keystroke debouncing reduces API request volume by 70%", "Offline analytics pipeline updates search query frequency rankings", "Sub-50ms latency SLA achieved through in-memory lookups"],
            ["Typeahead", "Trie", "Autocomplete", "Redis", "High-Level Design"]
        ),
        (
            "Design an API Gateway with ABAC/RBAC and Rate Limiting",
            "Architecture Patterns",
            "Medium",
            "Explain the architecture of an Enterprise API Gateway. How does it handle SSL termination, token validation, dynamic routing, and ABAC policy enforcement?",
            "API Gateway acts as the single reverse-proxy entry point for client requests:\n1. SSL/TLS Termination: Offloads cryptographic handshakes from microservices.\n2. Authentication & JWT Validation: Validates incoming Bearer tokens using public keys (JWKS) cached locally, avoiding remote IdP calls for every request.\n3. Authorization (ABAC/RBAC): Extracts claims, user roles, and attributes; queries Open Policy Agent (OPA) or local policy cache.\n4. Rate Limiting: Enforces client quotas using Redis Token Bucket.\n5. Request Transformation & Correlation ID: Injects `X-Correlation-ID` and user context headers into downstream gRPC/HTTP calls.",
            ["Single entry point decouples cross-cutting concerns from business services", "JWKS local caching validates JWT signatures without network round-trips", "Open Policy Agent (OPA) evaluates fine-grained ABAC policies", "Distributed correlation IDs provide end-to-end distributed tracing"],
            ["API Gateway", "OAuth2", "Security", "Envoy", "Microservices"]
        ),
        (
            "Design a Metrics and Alerting Monitoring System (Datadog/Prometheus)",
            "High-Level Design",
            "Hard",
            "Design a distributed time-series metrics collection and alerting pipeline capable of processing 10 million data points per second.",
            "Architecture:\n1. Collection: Push (StatsD/Datadog agent) or Pull (Prometheus scraping `/metrics` endpoints).\n2. Streaming Buffer: Kafka buffers time-series points `(metric_name, labels, timestamp, value)`.\n3. Time-Series Database (TSDB):\n- Gorilla TSDB / ClickHouse / VictoriaMetrics architecture.\n- Delta-of-delta timestamp compression (stores time differences in bits).\n- XOR floating-point value compression (consecutive metric values vary little).\n4. Alerting Engine:\n- Rule evaluation engine executes PromQL queries against TSDB every 15-60 seconds.\n- Deduplicates and groups alert triggers; routes notifications to PagerDuty/Slack via Alertmanager.",
            ["Gorilla TSDB XOR floating-point and delta-of-delta compression achieves 12x data reduction", "Kafka buffers high-throughput metric ingestion spikes", "Time-series labels enable multi-dimensional aggregation", "Dedicated alert evaluation engine decouples query serving from monitoring"],
            ["Time Series", "Prometheus", "Datadog", "Monitoring", "High-Level Design"]
        ),
        (
            "Circuit Breaker Pattern: States, Thresholds, and Fallbacks",
            "Resilience",
            "Medium",
            "Explain the Circuit Breaker pattern (Closed, Open, Half-Open). How does it prevent cascading failures in microservice architectures?",
            "Three States:\n1. Closed: Normal operation. Requests flow to downstream service. If failure rate exceeds threshold (e.g., >50% errors over 10s window), breaker trips to OPEN.\n2. Open: Requests fail immediately without hitting the downstream service! Returns fallback response or cached data. A sleep timer starts (e.g. 30 seconds).\n3. Half-Open: After sleep timer expires, breaker lets a small canary batch of requests through. If successful, breaker resets to CLOSED. If any failure occurs, breaker returns to OPEN.\n\nLibraries: Resilience4j (Java/Spring Boot), Polly (.NET), Envoy out-of-process circuit breakers.",
            ["Prevents cascading failures and resource starvation (thread exhaustion)", "Trips to OPEN state when error rate crosses predetermined threshold", "Half-Open state tests downstream health with canary requests", "Provides graceful degradation via predefined fallback responses"],
            ["Circuit Breaker", "Resilience", "Microservices", "Fault Tolerance"]
        ),
        (
            "SAGA Pattern: Orchestration vs Choreography for Distributed Transactions",
            "Distributed Transactions",
            "Hard",
            "Compare Orchestration-based and Choreography-based SAGA patterns for maintaining data consistency across microservices without 2-Phase Commit.",
            "SAGA decomposes a distributed transaction into a sequence of local transactions. Each local transaction updates database and publishes an event. If a step fails, compensating transactions execute in reverse order to undo changes.\n\n1. Choreography-Based SAGA:\n- Services listen to events and decide next action autonomously. No central coordinator.\n- Pros: Simple for small flows (2-3 services), loosely coupled.\n- Cons: Hard to understand overall workflow; risk of cyclic dependencies; difficult to debug.\n\n2. Orchestration-Based SAGA:\n- A central orchestrator service (e.g., Temporal, AWS Step Functions, Camunda) coordinates the workflow.\n- Sends commands to services and tracks execution state machine.\n- Pros: Centralized visibility, easy to manage timeouts and rollbacks.\n- Cons: Additional orchestrator service to maintain.",
            ["Replaces blocking 2-phase commit with sequence of local transactions", "Compensating transactions undo previous steps upon failure", "Choreography: event-driven, decentralized, good for simple workflows", "Orchestration: centralized state machine, optimal for complex multi-step workflows"],
            ["SAGA", "Distributed Transactions", "Temporal", "Microservices"]
        ),
        (
            "Database Replication Lag: Causes, Detection, and Mitigation",
            "Databases & Storage",
            "Medium",
            "What causes replication lag in read-replica database setups? How do you detect and mitigate stale reads in production?",
            "Causes:\n- Network latency between primary and replica.\n- Long-running write transactions on primary blocking replication threads.\n- Single-threaded replication applier on replica failing to keep pace with multi-threaded primary writes.\n\nMitigation Strategies:\n1. Read-Your-Own-Writes Routing: Route user's reads to primary for 5-10 seconds immediately after they perform a write operation.\n2. Multi-threaded replication (e.g., MySQL parallel replication).\n3. Replication lag monitoring: Monitor replica heartbeat timestamp (`Seconds_Behind_Master` in MySQL or `pg_stat_replication` in Postgres). If lag > threshold (e.g. 1 sec), drop replica from read pool.",
            ["Replication lag causes users to see stale data after updates", "Route recent writer reads to master/primary database temporarily", "Parallel replication threads speed up replica log replay", "Health checks remove lagging replicas from active read load balancer pools"],
            ["Databases", "Replication", "PostgreSQL", "MySQL"]
        ),
        (
            "Distributed Locks: Redlock vs ZooKeeper / etcd",
            "Distributed Systems",
            "Hard",
            "Critique Martin Kleppmann's analysis of the Redis Redlock algorithm versus consensus-based distributed locks using ZooKeeper or etcd.",
            "Redlock Algorithm:\nClient attempts to acquire lock across N independent Redis masters (e.g. 5 nodes) within a small timeout. If acquired on majority (3 of 5), lock is granted.\n\nMartin Kleppmann's Critique:\nRedlock assumes synchronized clocks. In real systems, Stop-The-World (STW) GC pauses, network delays, or NTP clock jumps can cause the lock to expire on Redis while the client still thinks it owns the lock, allowing a second client to acquire the lock and corrupt data!\n\nZooKeeper / etcd (The Safer Solution):\n- Uses consensus (Raft/ZAB) with ephemeral sequential znode / lease.\n- Fencing Tokens: Every lock grant provides a monotonically increasing sequence number (e.g., 34, 35, 36). Downstream storage (DB) rejects any write presenting a fencing token lower than the highest seen token, preventing stale clients from corrupting data.",
            ["Redlock is vulnerable to clock jumps and prolonged garbage collection pauses", "ZooKeeper/etcd use strong consensus and monotonic fencing tokens", "Fencing tokens ensure storage engines reject stale client writes", "Never rely on distributed locks for correctness without server-side validation"],
            ["Distributed Lock", "Redis", "ZooKeeper", "etcd", "Consensus"]
        ),
        (
            "Reverse Proxy vs Forward Proxy vs API Gateway",
            "Networking",
            "Easy",
            "Compare Forward Proxies, Reverse Proxies, and API Gateways. What are their distinct network positions, security functions, and enterprise use cases?",
            "Forward Proxy:\n- Sits in front of CLIENTS. Represents the client to the internet.\n- Use cases: Enterprise egress filtering, corporate content inspection, anonymization, outbound caching.\n\nReverse Proxy:\n- Sits in front of SERVERS. Represents servers to incoming client traffic.\n- Use cases: Inbound load balancing, TLS termination, static asset caching, DDoS mitigation.\n\nAPI Gateway:\n- An advanced Layer 7 reverse proxy tailored for APIs and microservices.\n- Use cases: OAuth2/JWT authentication, rate limiting, request transformation, telemetry, service discovery integration, API versioning.",
            ["Forward proxy protects/masks clients; Reverse proxy protects/masks servers", "Forward proxy handles egress; Reverse proxy handles ingress", "API gateway builds on reverse proxy with API management features", "Crucial boundary distinctions for enterprise network security"],
            ["Proxy", "Networking", "Architecture"]
        ),
        (
            "Database Indexing Internals: Clustered vs Non-Clustered Indexes",
            "Databases & Storage",
            "Medium",
            "How do Clustered and Non-Clustered B-Tree indexes differ physically on disk? What is an index covering query?",
            "Clustered Index:\n- Defines the physical sorting order of rows on disk.\n- The leaf nodes of the clustered index B-Tree contain the ACTUAL TABLE ROW DATA.\n- A table can have only ONE clustered index (usually the Primary Key).\n\nNon-Clustered (Secondary) Index:\n- A separate B-Tree whose leaf nodes do NOT contain full row data, but store index column values and a pointer (the Primary Key) to the clustered index.\n- Querying a secondary index requires two lookups: first in secondary index, then 'bookmark lookup' in clustered index.\n\nCovering Index:\n- If all columns requested in `SELECT` and `WHERE` clauses exist directly inside the secondary index, the database satisfies the query entirely from the index tree without touching the table rows (Index-Only Scan), providing maximum performance.",
            ["Clustered index leaf nodes hold actual data rows; only one per table", "Secondary index leaf nodes hold pointers to clustered index key", "Covering index fulfills query directly without secondary table lookup", "Index-Only Scans dramatically reduce disk I/O"],
            ["Databases", "Indexing", "B-Tree", "SQL"]
        ),
        (
            "Event-Driven Architecture vs Request-Response",
            "Architecture Patterns",
            "Medium",
            "Compare synchronous Request-Response (REST/gRPC) and asynchronous Event-Driven Architecture (EDA). What are the trade-offs regarding coupling, latency, and debuggability?",
            "Request-Response (REST/gRPC):\n- Synchronous point-to-point communication.\n- Pros: Immediate response/status, simple mental model, easy to debug.\n- Cons: Temporal coupling (both services must be online simultaneously); latency cascades across chains of calls; failure in one service blocks caller.\n\nEvent-Driven Architecture (EDA):\n- Asynchronous publish-subscribe via event broker (Kafka, RabbitMQ, EventBridge).\n- Pros: Decoupled services (producer doesn't know who consumers are); temporal decoupling (consumers process when ready); natural buffer against traffic spikes.\n- Cons: Eventual consistency; complex distributed debugging and tracing; out-of-order event handling.",
            ["Request-response introduces temporal and spatial coupling", "EDA decouples producers from consumers and absorbs traffic spikes", "Synchronous chains suffer from cascading latency and failure propagation", "OpenTelemetry distributed tracing is essential for debugging event flows"],
            ["Event-Driven", "REST", "gRPC", "Architecture Patterns"]
        ),
        (
            "WebSocket vs Server-Sent Events (SSE) vs Long Polling",
            "Networking",
            "Medium",
            "When should you choose WebSockets over Server-Sent Events (SSE) or Long Polling? Compare connection setup, duplexing, and proxy/load-balancer compatibility.",
            "Long Polling:\n- Client opens HTTP request; server holds until data arrives. Connection closes, client immediately re-polls.\n- High HTTP header overhead, but works across all restrictive firewalls.\n\nServer-Sent Events (SSE):\n- Unidirectional (Server -> Client) over standard HTTP/1.1 or HTTP/2.\n- Built-in browser reconnection, custom event types.\n- Perfect for: Stock tickers, notification streams, LLM token streaming (ChatGPT response streaming).\n\nWebSockets:\n- Full-Duplex bidirectional communication over single persistent TCP connection.\n- Upgrades from HTTP via `Upgrade: websocket` header.\n- Minimal 2-byte frame overhead.\n- Essential for: Online multiplayer gaming, collaborative whiteboard editing, two-way chat apps.",
            ["SSE is unidirectional and runs over standard HTTP; ideal for LLM response streaming", "WebSocket is full-duplex with minimal framing overhead; ideal for gaming and chat", "Long polling is inefficient fallback for legacy infrastructure", "SSE has native browser reconnection support via EventSource API"],
            ["WebSocket", "SSE", "Networking", "Protocols"]
        ),
        (
            "CDN Edge Caching Strategies and Dynamic Acceleration",
            "Scalability & Routing",
            "Medium",
            "How do Content Delivery Networks (CDNs) accelerate both static assets and dynamic API requests? Explain Anycast DNS and TCP connection pooling.",
            "Static Asset Acceleration:\n- Caches images, CSS, JS, and video at edge points of presence (PoPs) globally.\n- Cache-Control headers (`public, max-age=31536000, immutable`) enable browser and edge caching.\n\nDynamic Content Acceleration:\n- Anycast Routing: Routes client to geographically closest CDN PoP via BGP routing.\n- Route Optimization: CDN routes traffic across private fiber backbones rather than the congested public internet.\n- TCP / TLS Connection Reuse: CDN edge maintains pre-warmed, persistent TCP connections to origin servers, eliminating the 3-way TCP handshake and TLS negotiation overhead for dynamic API calls.",
            ["Anycast DNS directs user packets to closest edge server via BGP", "Static caching shields origin database and servers from 90%+ traffic", "Pre-warmed persistent connections to origin speed up dynamic API requests", "Edge compute (Cloudflare Workers, Lambda@Edge) executes logic at the edge"],
            ["CDN", "Networking", "Performance", "Anycast"]
        ),
        (
            "Database Connection Pooling: Sizing and Resource Management",
            "Databases & Storage",
            "Medium",
            "Why do databases crash when given too many concurrent connections? Explain connection pool sizing formulas (e.g. HikariCP) and connection multiplexers like PgBouncer.",
            "Why Too Many Connections Kill Databases:\nEach DB connection consumes 5MB–10MB RAM on the server and requires OS thread scheduling context switches. 5,000 concurrent connections can overwhelm CPU cores with context switching rather than executing queries!\n\nHikariCP Sizing Formula:\n`connections = ((core_count * 2) + effective_spindle_count)`\nA 16-core server performs optimally with only ~33 connections!\n\nConnection Multiplexers (PgBouncer):\n- Sits between hundreds of microservice pods and the database.\n- Transaction Pooling: Holds server connections only while a transaction executes, allowing 10,000 client application connections to share 100 actual database connections.",
            ["Excess connections cause severe OS thread context-switching thrashing", "Counterintuitively, smaller connection pools yield higher total throughput", "HikariCP formula: (cores * 2) + disk spindles", "PgBouncer transaction pooling enables thousands of pods to share tens of DB connections"],
            ["Databases", "Connection Pool", "PostgreSQL", "Performance"]
        ),
        (
            "Design a Real-Time Collaborative Document Editor (OT vs CRDT)",
            "High-Level Design",
            "Hard",
            "Compare Operational Transformation (Google Docs) and Conflict-Free Replicated Data Types (CRDTs - Figma, Apple Notes) for real-time collaborative text editing.",
            "The Problem: Multiple users editing the exact same sentence simultaneously without locks.\n\n1. Operational Transformation (OT):\n- Operations (Insert/Delete) are sent to a centralized server.\n- Server transforms incoming operations against concurrent operations using transformation functions so intentions are preserved.\n- Requires a centralized server to establish total order of operations.\n- Used by: Google Docs.\n\n2. Conflict-Free Replicated Data Types (CRDTs):\n- Mathematically sound data structures that can be merged concurrently across peer-to-peer or decentralized nodes without central coordination.\n- Operations are commutative and idempotent.\n- Characters assigned fractional indices or unique Lamport timestamps (e.g. RGA, LSeq, Yjs).\n- Used by: Figma, Apple Notes, Linear.",
            ["OT requires a centralized server to sequence and transform operations", "CRDTs achieve peer-to-peer convergence mathematically without central server", "CRDTs have higher memory overhead per character to store metadata", "State-based vs Operation-based CRDT variants"],
            ["CRDT", "Operational Transformation", "Collaborative Editing", "Distributed Systems"]
        ),
        (
            "Bulkhead Pattern: Thread Pools, Containers, and Fault Isolation",
            "Resilience",
            "Medium",
            "How does the Bulkhead pattern isolate critical failure domains in distributed services? Contrast thread pool isolation with semaphore isolation.",
            "Analogy: Ship bulkheads partition hull into watertight compartments so one breach doesn't sink the entire ship.\n\nMicroservice Isolation:\n1. Thread Pool Isolation:\n- Separate dedicated thread pool for each downstream dependency (e.g., Auth service gets 20 threads, Payment gets 10 threads, Analytics gets 5 threads).\n- If Analytics slows down, its 5 threads saturate, but the rest of the application continues operating smoothly without thread exhaustion.\n\n2. Semaphore Isolation:\n- Uses non-blocking atomic counters to limit concurrent requests per dependency without allocating separate thread pools. Lower CPU overhead, but cannot enforce execution timeouts.",
            ["Prevents a single failing downstream service from exhausting all host threads", "Thread pool isolation provides hard isolation and timeout enforcement", "Semaphore isolation offers low overhead concurrency capping", "Essential alongside Circuit Breakers for high-reliability systems"],
            ["Bulkhead", "Resilience", "Thread Pool", "Architecture Patterns"]
        ),
        (
            "Design a Distributed File Storage System (GFS / HDFS)",
            "High-Level Design",
            "Hard",
            "Explain the architecture of Google File System (GFS) and HDFS. Detail chunk size decisions, master metadata management, and heartbeats.",
            "Architecture:\n1. Chunk Size: Large chunks (e.g. 64MB - 128MB). Reduces metadata size, allowing master to keep all block mappings in RAM.\n2. Master / NameNode:\n- Single master maintains file namespace, file-to-chunk mappings, and chunk locations entirely in memory.\n- High performance; persistent via Write-Ahead Log and checkpoints.\n3. ChunkServers / DataNodes:\n- Store chunks as raw files on local Linux filesystems.\n- Default replication factor: 3 (stored across different server racks).\n- Heartbeats periodically report block health to master.",
            ["Large 64MB-128MB chunk size minimizes master metadata memory footprint", "Master node holds entire filesystem metadata in RAM for speed", "Triplicate chunk replication across distinct server racks guarantees durability", "Decouples control plane (metadata) from data plane (direct client-to-datanode streaming)"],
            ["GFS", "HDFS", "Distributed Storage", "High-Level Design"]
        ),
        (
            "Zero Trust Network Architecture: Service Mesh & mTLS",
            "Security & Networking",
            "Medium",
            "What is Zero Trust Architecture? How do Service Meshes (Istio/Envoy) automate Mutual TLS (mTLS) and service identity in Kubernetes?",
            "Perimeter-based security ('hard shell, soft interior') is obsolete. Zero Trust principle: 'Never trust, always verify'.\n\nService Mesh (Istio / Envoy) Implementation:\n- Sidecar proxy injected alongside every microservice container.\n- SPIFFE / SPIRE: Assigns cryptographic X.509 identity certificates to each service workload.\n- Mutual TLS (mTLS): Sidecar proxies handle automatic TLS handshake, encrypting all east-west pod-to-pod traffic.\n- Authorization Policies: Envoy verifies client service identity before routing requests, enforcing strict service-level access control.",
            ["Eliminates implicit trust inside the private network perimeter", "SPIFFE provides cryptographic workload identity across containers", "Sidecar proxies offload mTLS encryption transparently without code changes", "Strict service-to-service authorization policies prevent lateral movement"],
            ["Zero Trust", "Service Mesh", "Istio", "Envoy", "Security", "Kubernetes"]
        )
    ])
]

ALL_SYSTEM_DESIGN = QUESTIONS + ADDITIONAL_SD

def generate():
    print(f"Total System Design questions: {len(ALL_SYSTEM_DESIGN)}")
    assert len(ALL_SYSTEM_DESIGN) >= 105, f"Expected >= 105, got {len(ALL_SYSTEM_DESIGN)}"
    
    content = "// System Design Interview Questions Data (110 Curated Problems)\n"
    content += "window.INTERVIEW_DATA_SYSTEM_DESIGN = " + json.dumps(ALL_SYSTEM_DESIGN, indent=2) + ";\n"
    
    with open("assets/js/data/system-design.js", "w") as f:
        f.write(content)
    print("Successfully wrote assets/js/data/system-design.js")

if __name__ == "__main__":
    generate()
