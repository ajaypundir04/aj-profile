// System Design Interview Questions Data (110 Curated Problems)
window.INTERVIEW_DATA_SYSTEM_DESIGN = [
  {
    "id": "sd-1",
    "title": "CAP Theorem vs PACELC Theorem",
    "category": "Distributed Systems",
    "difficulty": "Medium",
    "question": "Explain the CAP Theorem and why the PACELC theorem is a more accurate model for modern distributed databases.",
    "answer": "CAP Theorem states that during a network Partition (P), a distributed system must choose between Consistency (C) and Availability (A).\n\nPACELC expands this:\n- If Partition (P): choose Availability (A) or Consistency (C);\n- Else (E): choose Latency (L) or Consistency (C).\n\nDynamoDB/Cassandra: PA/EL (under partition: Available; normal operation: low Latency).\nSpanner/CockroachDB: PC/EC (under partition: Consistent; normal operation: strong Consistency at higher round-trip latency).",
    "keyPoints": [
      "CAP only covers partition failure scenarios",
      "PACELC evaluates normal operating trade-offs (Latency vs Consistency)",
      "Strong consistency requires multi-node coordination adding latency",
      "Tunable consistency levels exist in Cassandra and DynamoDB"
    ],
    "tags": [
      "CAP",
      "PACELC",
      "Distributed Systems",
      "Consistency",
      "Databases"
    ]
  },
  {
    "id": "sd-2",
    "title": "Consistency Models: Strong, Eventual, Causal, and Read-After-Write",
    "category": "Distributed Systems",
    "difficulty": "Medium",
    "question": "Compare Linearizability (Strong Consistency), Eventual Consistency, Causal Consistency, and Read-After-Write (Monotonic Read) consistency with engineering use cases.",
    "answer": "1. Linearizability: Every read returns the most recent write. Operations appear instantaneous on a single register. (Financial ledgers, stock trading).\n2. Eventual Consistency: Replicas eventually converge if no new updates occur. (Social media likes, video views).\n3. Causal Consistency: Causally related operations are seen by every node in the same order. (Chat threads, comments).\n4. Read-After-Write: Guarantees user always sees their own submitted updates. Implemented by routing user's own reads to primary or using client-side version timestamps.",
    "keyPoints": [
      "Linearizability requires consensus and adds network latency",
      "Eventual consistency maximizes write throughput",
      "Read-After-Write solves user-facing staleness without global strong consistency",
      "Vector clocks track causality"
    ],
    "tags": [
      "Consistency",
      "Distributed Systems",
      "Replication",
      "Databases"
    ]
  },
  {
    "id": "sd-3",
    "title": "Distributed Consensus: Raft vs Multi-Paxos",
    "category": "Distributed Systems",
    "difficulty": "Hard",
    "question": "How do Raft and Paxos establish consensus in distributed state machines? Explain leader election, log replication, and safety invariants.",
    "answer": "Raft decomposes consensus into:\n1. Leader Election: Follower, Candidate, Leader. Randomized timeouts (150-300ms) prevent split votes. Majority votes (N/2 + 1) in term T elect leader.\n2. Log Replication: Leader appends to log, sends AppendEntries RPC to followers. Committed when majority logs it.\n3. Safety: Candidate must have all committed entries from prior terms to win election.\n\nUsed in etcd (Kubernetes), Consul, TiKV, Kafka KRaft.",
    "keyPoints": [
      "Raft decomposes consensus into Leader Election, Log Replication, Safety",
      "Randomized timeouts eliminate split votes",
      "Requires odd quorum (2F + 1 nodes survive F failures)",
      "KRaft replaced ZooKeeper using Raft"
    ],
    "tags": [
      "Consensus",
      "Raft",
      "Paxos",
      "Distributed Systems",
      "etcd"
    ]
  },
  {
    "id": "sd-4",
    "title": "Vector Clocks vs Lamport Timestamps",
    "category": "Distributed Systems",
    "difficulty": "Medium",
    "question": "How do Vector Clocks and Lamport Timestamps track causality in distributed systems without synchronized physical clocks?",
    "answer": "Lamport Timestamps:\nEach node maintains a counter. On event: counter++. Message carries counter. Receiver sets `clock = max(clock, msg_clock) + 1`. Provides strict total ordering, but CANNOT determine if two events are concurrent.\n\nVector Clocks:\nEach node maintains a vector of size N (one clock per node). When sending, attach full vector. Receiver updates its vector: `V[i] = max(V[i], msg_V[i])`. If neither vector dominates the other (`V1 not <= V2 and V2 not <= V1`), the events are CONCURRENT (conflicts must be reconciled).",
    "keyPoints": [
      "Lamport timestamps provide total ordering but cannot detect concurrency",
      "Vector clocks detect whether two events are causally related or concurrent",
      "Conflict detection without synchronized wall clocks",
      "Used in Dynamo, Riak, and distributed versioning"
    ],
    "tags": [
      "Vector Clocks",
      "Lamport",
      "Distributed Systems",
      "Causality"
    ]
  },
  {
    "id": "sd-5",
    "title": "Gossip Protocol (Epidemic Routing)",
    "category": "Distributed Systems",
    "difficulty": "Medium",
    "question": "How does the Gossip protocol achieve decentralized cluster membership, failure detection, and state dissemination?",
    "answer": "Every node periodically picks k random peer nodes (e.g. 3) and transmits its known membership and state information (heartbeats, node status).\nProperties:\n- Decentralized: No single point of failure.\n- Exponential Spread: Information reaches all N nodes in O(log N) rounds.\n- Fault-Tolerant: Network packet loss or node failures do not stop propagation.\n- Used in: Cassandra cluster membership, Consul Serf, Redis Cluster failover gossip.",
    "keyPoints": [
      "Information spreads exponentially in O(log N) rounds",
      "No single point of failure or centralized master",
      "Scales to thousands of cluster nodes",
      "Used in Cassandra and HashiCorp Consul"
    ],
    "tags": [
      "Gossip Protocol",
      "Cassandra",
      "Cluster Membership",
      "Distributed Systems"
    ]
  },
  {
    "id": "sd-6",
    "title": "Split-Brain Scenario and Quorum Prevention",
    "category": "Distributed Systems",
    "difficulty": "Medium",
    "question": "What is the Split-Brain scenario in distributed clusters? How do Quorum and Fencing mechanisms prevent split-brain?",
    "answer": "Split-brain occurs when a network partition cuts a cluster into isolated groups, and each group believes the other is dead, electing their own leaders. Both independently accept writes, causing catastrophic data corruption.\n\nPrevention:\n1. Quorum (Majority Rule): A partition can only elect a leader or commit writes if it has strictly more than half the nodes: `Q = floor(N / 2) + 1`. Only one partition can ever hold the majority.\n2. Odd Node Count: Clusters deploy 3, 5, or 7 nodes so a clean split into two equal halves is mathematically impossible.\n3. Fencing Tokens: Monotonically increasing epoch numbers reject writes from partitioned former leaders.",
    "keyPoints": [
      "Split-brain leads to dual leaders and permanent data corruption",
      "Quorum requires majority (N/2 + 1) to elect leader or write",
      "Deploy odd number of cluster nodes (3, 5, 7)",
      "Fencing tokens reject writes from stale partitioned leaders"
    ],
    "tags": [
      "Split-Brain",
      "Quorum",
      "High Availability",
      "Distributed Systems"
    ]
  },
  {
    "id": "sd-7",
    "title": "Byzantine Fault Tolerance (BFT) vs Crash Fault Tolerance (CFT)",
    "category": "Distributed Systems",
    "difficulty": "Hard",
    "question": "What is the difference between Crash Fault Tolerance (CFT) and Byzantine Fault Tolerance (BFT)? Compare node failure tolerances.",
    "answer": "CFT (Crash Fault Tolerance):\nAssumes nodes either operate correctly or simply crash/stop. Nodes never send malicious, corrupted, or contradictory messages.\nNode requirement: To tolerate `F` crash failures, system needs `2F + 1` nodes (e.g., Raft, Paxos).\n\nBFT (Byzantine Fault Tolerance):\nAssumes nodes can act arbitrarily: send conflicting messages to different peers, lie, or be actively hacked (Byzantine Generals Problem).\nNode requirement: To tolerate `F` Byzantine malicious nodes, system needs `3F + 1` nodes (e.g., PBFT, Tendermint, Blockchain consensus).\nWhy 3F+1? Out of N nodes, F may be malicious and F may be unresponsive, leaving N - 2F honest responding nodes that must strictly outnumber the F malicious nodes: `N - 2F > F => N >= 3F + 1`.",
    "keyPoints": [
      "CFT tolerates node crashes using 2F + 1 nodes (Raft, Paxos)",
      "BFT tolerates malicious/arbitrary behavior using 3F + 1 nodes (PBFT)",
      "Enterprise clouds use CFT; public untrusted networks use BFT",
      "Mathematical proof based on unresponsive vs lying nodes"
    ],
    "tags": [
      "Byzantine",
      "Consensus",
      "Fault Tolerance",
      "Security"
    ]
  },
  {
    "id": "sd-8",
    "title": "Fallacies of Distributed Computing",
    "category": "Distributed Systems",
    "difficulty": "Easy",
    "question": "List the 8 Fallacies of Distributed Computing and discuss their modern architectural implications.",
    "answer": "The 8 Fallacies (Peter Deutsch):\n1. The network is reliable.\n2. Latency is zero.\n3. Bandwidth is infinite.\n4. The network is secure.\n5. Topology doesn't change.\n6. There is one administrator.\n7. Transport cost is zero.\n8. The network is homogeneous.\n\nArchitectural counter-measures:\n- Retries with exponential backoff & jitter for network unreliability.\n- Async messaging (Kafka) to mitigate latency cascades.\n- Zero Trust & mTLS assuming hostile internal networks.\n- Health checks and dynamic service discovery for topology changes.",
    "keyPoints": [
      "Foundational architectural principles articulated by Sun Microsystems",
      "Assumptions about zero latency and infinite bandwidth cause outages",
      "Zero Trust addresses 'network is secure' fallacy",
      "Circuit breakers and backoff address 'network is reliable' fallacy"
    ],
    "tags": [
      "Distributed Systems",
      "Architecture",
      "Resilience"
    ]
  },
  {
    "id": "sd-9",
    "title": "Idempotency in Distributed APIs",
    "category": "Distributed Systems",
    "difficulty": "Medium",
    "question": "What is idempotency? How do you implement robust idempotency for POST requests in payment and order processing systems?",
    "answer": "An idempotent operation can be applied multiple times without changing the result beyond the initial application: `f(f(x)) = f(x)`.\n\nImplementation for REST APIs (POST):\n1. Client generates unique UUID `Idempotency-Key` and sends in HTTP header.\n2. Server checks Redis / DB with distributed lock: `SETNX idempotency:{key} IN_PROGRESS EX 120`.\n3. If key exists with status COMPLETED: return stored response payload directly without re-executing.\n4. If IN_PROGRESS: return HTTP 409 Conflict.\n5. If new: execute business logic in DB transaction, store final response in idempotency table, update status to COMPLETED.\n6. Client network timeout retry safely gets the exact same response without double-charging.",
    "keyPoints": [
      "Idempotency prevents duplicate operations on network retries",
      "Standardized Idempotency-Key header used by Stripe/PayPal",
      "Store request state: IN_PROGRESS, COMPLETED, FAILED",
      "Return cached result for subsequent identical invocations"
    ],
    "tags": [
      "Idempotency",
      "API Design",
      "Payments",
      "Distributed Systems"
    ]
  },
  {
    "id": "sd-10",
    "title": "Two Generals Problem & Distributed Commit Impossibility",
    "category": "Distributed Systems",
    "difficulty": "Medium",
    "question": "Explain the Two Generals Problem and why it proves that guaranteed common knowledge over an unreliable communication channel is impossible.",
    "answer": "Scenario: Two armies must attack a city simultaneously to win. General A sends messenger: 'Attack at dawn'. But messenger might be captured. General A cannot attack unless he receives confirmation. General B sends confirmation messenger, but General B cannot attack unless he knows General A received the confirmation! This leads to an infinite sequence of acknowledgments (`ACK of ACK of ACK...`).\n\nResult: Proves that consensus is impossible over an unreliable link with zero probability of failure. Practical distributed systems use timeouts, heartbeats, and probabilistic consensus rather than absolute certainty.",
    "keyPoints": [
      "Proves common knowledge cannot be established over unreliable links",
      "Infinite acknowledgment loop problem",
      "Foundational theoretical limitation in distributed networking",
      "Systems rely on timeouts and quorums rather than absolute certainty"
    ],
    "tags": [
      "Two Generals",
      "Theory",
      "Consensus",
      "Networking"
    ]
  },
  {
    "id": "sd-11",
    "title": "Two-Phase Commit (2PC) vs Three-Phase Commit (3PC)",
    "category": "Distributed Transactions",
    "difficulty": "Hard",
    "question": "How does Two-Phase Commit (2PC) work? Why is it considered a blocking protocol, and how does Three-Phase Commit (3PC) attempt to resolve it?",
    "answer": "Two-Phase Commit (2PC):\n- Phase 1 (Prepare): Coordinator asks all cohorts 'Can you commit?'. Cohorts acquire locks, write to WAL, and vote YES or NO.\n- Phase 2 (Commit): If all voted YES, coordinator writes COMMIT to WAL and broadcasts COMMIT. If any voted NO, broadcasts ABORT.\n- Bottleneck: 2PC is BLOCKING. If coordinator crashes after cohorts vote YES, cohorts remain blocked indefinitely holding database locks!\n\nThree-Phase Commit (3PC):\nAdds a 'PreCommit' phase between Prepare and Commit, and introduces timeouts at cohorts. Cohorts can safely timeout and abort. Drawback: 3PC fails under network partitions (risks split commits), hence modern systems prefer SAGA or Raft over 3PC.",
    "keyPoints": [
      "2PC holds database locks across network round-trips",
      "2PC is blocking: coordinator failure stalls cohorts holding locks",
      "3PC adds PreCommit and timeouts but fails under network partitions",
      "Modern architectures replace 2PC with SAGA pattern"
    ],
    "tags": [
      "2PC",
      "3PC",
      "Distributed Transactions",
      "ACID"
    ]
  },
  {
    "id": "sd-12",
    "title": "Event Sourcing vs Traditional CRUD Storage",
    "category": "Architecture Patterns",
    "difficulty": "Medium",
    "question": "Compare Event Sourcing with traditional CRUD database state storage. How does Event Sourcing handle state reconstruction, auditability, and snapshots?",
    "answer": "Traditional CRUD: Overwrites current state (`UPDATE accounts SET balance = 500 WHERE id = 1`). Historical state transitions are lost.\n\nEvent Sourcing:\nState changes are stored as an immutable append-only sequence of domain events (`AccountOpened`, `MoneyDeposited`, `MoneyWithdrawn`).\nCurrent state is derived by replaying all historical events from genesis.\n\nBenefits:\n- Complete immutable audit trail (critical for banking and compliance).\n- Time travel debugging: reconstruct exact system state at any point in history.\n- Snapshots: Periodic state snapshots (every 1,000 events) prevent replaying millions of events on startup.\n- Paired with CQRS (Command Query Responsibility Segregation).",
    "keyPoints": [
      "Stores sequence of immutable events instead of overwriting current state",
      "Reconstructs state at any historical point in time",
      "Snapshots optimize recovery performance",
      "Standard architecture in financial ledgers and event-driven systems"
    ],
    "tags": [
      "Event Sourcing",
      "CQRS",
      "Architecture Patterns",
      "FinTech"
    ]
  },
  {
    "id": "sd-13",
    "title": "CQRS (Command Query Responsibility Segregation)",
    "category": "Architecture Patterns",
    "difficulty": "Medium",
    "question": "Explain CQRS. Why separate read and write models? How do you synchronize read stores and handle eventual consistency?",
    "answer": "Core Concept:\nSeparates the write model (Commands: business logic, validation, transactional integrity) from the read model (Queries: optimized materialized views for UI consumption).\n\nFlow:\n1. Client issues Command (e.g. `PlaceOrder`).\n2. Write Service validates and commits to relational/event-sourced DB.\n3. Change event published to Kafka/Debezium.\n4. Read Projector updates denormalized read stores (Elasticsearch for search, Redis for UI cache, MongoDB for read queries).\n5. Client queries read store directly with sub-10ms response.\nTrade-off: Eventual consistency between write commit and read projection update.",
    "keyPoints": [
      "Decouples write validation model from read projection models",
      "Allows independent scaling of read and write databases",
      "Read models are pre-joined and denormalized for speed",
      "Requires handling eventual consistency in user interface"
    ],
    "tags": [
      "CQRS",
      "Microservices",
      "Event-Driven",
      "Architecture"
    ]
  },
  {
    "id": "sd-14",
    "title": "Disaster Recovery: RTO vs RPO and Active-Active Multi-Region",
    "category": "Resilience",
    "difficulty": "Medium",
    "question": "Define RTO (Recovery Time Objective) and RPO (Recovery Point Objective). Compare Active-Passive (Warm/Cold Standby) and Active-Active Multi-Region architectures.",
    "answer": "Definitions:\n- RPO (Recovery Point Objective): Maximum acceptable data loss measured in time (e.g., 5 minutes of data loss).\n- RTO (Recovery Time Objective): Maximum acceptable downtime to restore service (e.g., system online within 15 minutes).\n\nStrategies:\n1. Backup & Restore (Cold): Highest RPO/RTO (hours/days), lowest cost.\n2. Pilot Light: Core data replicated continuously; compute scaled up on failover (RTO: 10-30 mins).\n3. Warm Standby (Active-Passive): Scaled-down replica cluster running 24/7; DNS failover switches traffic (RTO: minutes).\n4. Multi-Region Active-Active: Traffic routed to multiple geographic regions simultaneously via Anycast DNS. Zero RTO, sub-second RPO. Complexities: multi-region database conflicts (CRDTs or CockroachDB/Spanner).",
    "keyPoints": [
      "RPO measures acceptable data loss; RTO measures acceptable downtime",
      "Active-Passive uses warm standby with DNS failover",
      "Active-Active serves live traffic from multiple regions concurrently",
      "Multi-region active-active requires conflict resolution for writes"
    ],
    "tags": [
      "Disaster Recovery",
      "RTO",
      "RPO",
      "Multi-Region",
      "High Availability"
    ]
  },
  {
    "id": "sd-15",
    "title": "Microservices vs Monolith: Service Boundaries and Decomposition",
    "category": "Architecture Patterns",
    "difficulty": "Medium",
    "question": "How do you determine microservice boundaries using Domain-Driven Design (DDD) Bounded Contexts? When is a Modular Monolith superior?",
    "answer": "Domain-Driven Design (DDD) Bounded Contexts:\n- A service should own a distinct business capability with its own ubiquitous language and private database.\n- Cohesion within service; loose coupling across services.\n- Conway's Law: System architecture mirrors organization communication structure.\n\nModular Monolith Advantages:\n- Single codebase with strict module boundaries (e.g., Java packages, Go internal packages).\n- In-process function calls instead of network RPCs (zero network latency, simple debugging).\n- Single database transaction across modules (no distributed transactions).\n- Ideal for startups and teams <20 engineers until organizational scale demands independent deployment cycles.",
    "keyPoints": [
      "Bounded Contexts from DDD define clean microservice perimeters",
      "Each microservice must own its own private database",
      "Conway's Law: software design reflects team organization",
      "Modular monolith avoids network latency and distributed transaction complexity"
    ],
    "tags": [
      "Microservices",
      "Monolith",
      "Domain-Driven Design",
      "Architecture"
    ]
  },
  {
    "id": "sd-16",
    "title": "Consistent Hashing with Virtual Nodes",
    "category": "Scalability & Routing",
    "difficulty": "Medium",
    "question": "Explain Consistent Hashing and how virtual nodes prevent hotspots when adding/removing nodes in distributed caches.",
    "answer": "Modulo hashing `hash(key) % N` invalidates ~100% of keys when server count changes. Consistent hashing places nodes and keys on a 360-degree circular ring. Keys map to next clockwise node. Only 1/N keys rehash on node change.\n\nVirtual Nodes:\nEach physical server is assigned 100-300 virtual positions across the ring (`node1#1`, `node1#2`). Prevents hot spots and ensures that when a node dies, its load is evenly distributed across all surviving servers.",
    "keyPoints": [
      "Consistent hashing redistributes only K/N keys on cluster change",
      "Virtual nodes prevent non-uniform distribution and hot spots",
      "Failover load is evenly shared across remaining nodes",
      "Core mechanism in DynamoDB, Cassandra, Memcached"
    ],
    "tags": [
      "Consistent Hashing",
      "Load Balancing",
      "Caching",
      "Distributed Systems"
    ]
  },
  {
    "id": "sd-17",
    "title": "Layer 4 vs Layer 7 Load Balancing",
    "category": "Scalability & Routing",
    "difficulty": "Medium",
    "question": "Compare Layer 4 (Transport) and Layer 7 (Application) load balancers. Detail throughput, TLS termination, and routing capabilities.",
    "answer": "Layer 4 (L4): Routes based on IP and TCP/UDP port tuple. Zero application inspection. Ultra-high packet throughput, sub-millisecond latency. (AWS NLB, IPVS).\n\nLayer 7 (L7): Terminates TLS, parses HTTP/gRPC headers, cookies, and JSON body. Enables path-based routing, canary routing, WAF inspection, rate limiting. Higher CPU cost. (Envoy, NGINX, ALB).\n\nProduction pattern: L4 NLB forwards ingress traffic to fleet of L7 Envoy proxies.",
    "keyPoints": [
      "L4 operates on IP/Port with zero packet payload inspection",
      "L7 inspects HTTP/gRPC headers for intelligent path and cookie routing",
      "gRPC requires L7 load balancing to distribute multiplexed streams",
      "Tiered deployment combines L4 ingress with L7 Envoy mesh"
    ],
    "tags": [
      "Load Balancing",
      "Networking",
      "Envoy",
      "NGINX"
    ]
  },
  {
    "id": "sd-18",
    "title": "HTTP/1.1 vs HTTP/2 vs HTTP/3 (QUIC)",
    "category": "Networking",
    "difficulty": "Medium",
    "question": "Compare HTTP/1.1, HTTP/2, and HTTP/3 (QUIC). How does HTTP/3 eliminate Head-of-Line (HoL) blocking?",
    "answer": "HTTP/1.1:\nOne request per TCP connection at a time. Pipelining failed. Browsers opened 6 parallel TCP connections per domain. Suffers from HTTP head-of-line blocking.\n\nHTTP/2:\nBinary framing layer over single TCP connection. Multiple multiplexed bidirectional streams concurrently. Header compression (HPACK). Drawback: TCP Head-of-Line Blocking! If a single TCP packet drops, OS pauses ALL multiplexed streams until packet is retransmitted.\n\nHTTP/3 (QUIC over UDP):\nReplaces TCP with QUIC over UDP. Each stream is truly independent. Packet loss on one stream does NOT block other streams! Built-in TLS 1.3 encryption (0-RTT connection resumption) and connection migration across WiFi/Cellular networks.",
    "keyPoints": [
      "HTTP/2 multiplexes streams over 1 TCP connection but suffers from TCP-level HoL blocking",
      "HTTP/3 uses QUIC over UDP eliminating HoL blocking entirely",
      "QUIC supports 0-RTT handshakes and seamless WiFi-to-cellular connection migration",
      "HTTP/2 HPACK vs HTTP/3 QPACK header compression"
    ],
    "tags": [
      "HTTP/2",
      "HTTP/3",
      "QUIC",
      "Networking",
      "Protocols"
    ]
  },
  {
    "id": "sd-19",
    "title": "gRPC vs REST vs GraphQL",
    "category": "Networking",
    "difficulty": "Medium",
    "question": "Compare gRPC, REST, and GraphQL for internal microservice communication versus public client-facing APIs.",
    "answer": "gRPC:\n- Protocol Buffers (binary serialization) over HTTP/2.\n- Strongly-typed IDL schemas, bi-directional streaming, 7-10x faster serialization than JSON.\n- Ideal for: Internal high-throughput service-to-service microservice RPCs.\n\nREST:\n- JSON over HTTP/1.1 or HTTP/2. Human readable, universal tooling, stateless.\n- Ideal for: Public external APIs, third-party developer integrations.\n\nGraphQL:\n- Single endpoint query language. Client specifies exact fields needed.\n- Eliminates over-fetching and under-fetching.\n- Ideal for: Mobile applications and complex frontends aggregating data from multiple backend microservices.",
    "keyPoints": [
      "gRPC binary Protobuf is 7-10x faster than JSON for microservices",
      "REST is universal standard for public partner APIs",
      "GraphQL eliminates over-fetching and under-fetching on mobile frontends",
      "gRPC code generation provides compile-time type safety across languages"
    ],
    "tags": [
      "gRPC",
      "REST",
      "GraphQL",
      "API Design",
      "Protobuf"
    ]
  },
  {
    "id": "sd-20",
    "title": "DNS Resolution, Anycast Routing, and GeoDNS",
    "category": "Networking",
    "difficulty": "Medium",
    "question": "How does recursive DNS resolution work? Compare GeoDNS routing with BGP Anycast routing for global latency optimization.",
    "answer": "DNS Resolution Flow:\nClient -> Local DNS Resolver -> Root Server ('.') -> TLD Server ('.com') -> Authoritative Nameserver -> returns A/AAAA IP record. Cached via TTL at each step.\n\nGeoDNS:\nAuthoritative DNS server inspects client IP (or EDNS client subnet) and returns the IP address of the geographically closest datacenter. Drawback: DNS caches ignore updates until TTL expires; ISP resolver IP might not match client physical location.\n\nBGP Anycast Routing:\nThe same IP address is advertised from multiple datacenters worldwide via Border Gateway Protocol (BGP). Internet routers automatically route client packets to the network-topological closest datacenter. Instantaneous failover without waiting for DNS TTL propagation. Used by Cloudflare (1.1.1.1), Google DNS (8.8.8.8), and AWS Global Accelerator.",
    "keyPoints": [
      "DNS caches records hierarchically using TTL values",
      "GeoDNS returns regional IP based on client resolver location",
      "BGP Anycast advertises single IP globally routed via Internet backbone",
      "Anycast failover happens in seconds at the routing layer"
    ],
    "tags": [
      "DNS",
      "Anycast",
      "BGP",
      "Networking",
      "Cloudflare"
    ]
  },
  {
    "id": "sd-21",
    "title": "WebSocket vs Server-Sent Events (SSE) vs Long Polling",
    "category": "Networking",
    "difficulty": "Medium",
    "question": "When should you choose WebSockets over Server-Sent Events (SSE) or Long Polling? Compare connection setup, duplexing, and proxy support.",
    "answer": "Long Polling: Client opens HTTP request; server holds until data arrives. Connection closes, client immediately re-polls. High header overhead.\n\nSSE (Server-Sent Events): Unidirectional (Server -> Client) over standard HTTP. Built-in browser reconnection, text event streams. Ideal for: LLM response streaming (ChatGPT), stock price feeds, live dashboard counters.\n\nWebSockets: Full-duplex bidirectional communication over persistent TCP connection. Upgraded from HTTP. Minimal 2-byte framing overhead. Ideal for: Multiplayer gaming, collaborative whiteboards, two-way chat apps.",
    "keyPoints": [
      "SSE is unidirectional over standard HTTP; perfect for LLM response streaming",
      "WebSocket is full-duplex with minimal frame overhead; ideal for chat and gaming",
      "SSE has native browser reconnection via EventSource API",
      "WebSockets require sticky sessions or Redis pub/sub across cluster nodes"
    ],
    "tags": [
      "WebSocket",
      "SSE",
      "Networking",
      "Protocols"
    ]
  },
  {
    "id": "sd-22",
    "title": "CDN Edge Caching Strategies and Dynamic Acceleration",
    "category": "Scalability & Routing",
    "difficulty": "Medium",
    "question": "How do Content Delivery Networks (CDNs) accelerate both static assets and dynamic API requests? Explain Anycast DNS and TCP connection pooling.",
    "answer": "Static Asset Acceleration: Caches images, CSS, JS, video chunks at ISP-edge points of presence (PoPs). Managed via Cache-Control headers (`public, max-age=31536000, immutable`).\n\nDynamic Content Acceleration:\n- Route Optimization: Routes dynamic traffic over private fiber backbones rather than congested public internet.\n- TCP/TLS Pre-warming: Edge maintains persistent pre-established connection pools to origin servers, eliminating TCP 3-way handshake and TLS negotiation latency for dynamic API calls.\n- Edge Compute: Executes lightweight auth checks and rewrites at the edge (Cloudflare Workers, Lambda@Edge).",
    "keyPoints": [
      "Anycast directs client to closest edge server via BGP",
      "Static caching shields origin database from 90%+ traffic",
      "Pre-warmed persistent connections to origin speed up dynamic API calls",
      "Edge compute executes logic at edge locations"
    ],
    "tags": [
      "CDN",
      "Networking",
      "Performance",
      "Anycast"
    ]
  },
  {
    "id": "sd-23",
    "title": "Reverse Proxy vs Forward Proxy vs API Gateway",
    "category": "Networking",
    "difficulty": "Easy",
    "question": "Compare Forward Proxies, Reverse Proxies, and API Gateways. Detail network positions, security functions, and enterprise use cases.",
    "answer": "Forward Proxy: Sits in front of CLIENTS. Represents client to internet. Use cases: Enterprise egress filtering, corporate content inspection, IP masking.\n\nReverse Proxy: Sits in front of SERVERS. Represents servers to incoming client traffic. Use cases: Inbound load balancing, TLS termination, static asset caching, DDoS shielding.\n\nAPI Gateway: Advanced Layer 7 reverse proxy tailored for APIs and microservices. Use cases: OAuth2/JWT validation, rate limiting, request transformation, telemetry, service discovery integration.",
    "keyPoints": [
      "Forward proxy protects clients; Reverse proxy protects servers",
      "Forward proxy handles egress; Reverse proxy handles ingress",
      "API gateway adds API management, auth, and rate limiting",
      "Critical boundary distinctions for enterprise network security"
    ],
    "tags": [
      "Proxy",
      "Networking",
      "Architecture"
    ]
  },
  {
    "id": "sd-24",
    "title": "TCP 3-Way Handshake, TCP Slow Start, and TLS 1.3 Handshake",
    "category": "Networking",
    "difficulty": "Medium",
    "question": "Explain the TCP 3-Way Handshake, TCP Slow Start congestion control, and how TLS 1.3 reduced handshake latency to 1-RTT and 0-RTT.",
    "answer": "TCP 3-Way Handshake:\n1. Client -> SYN\n2. Server -> SYN-ACK\n3. Client -> ACK (1 RTT total).\n\nTCP Slow Start:\nInitial Congestion Window (cwnd) is small (e.g. 10 packets). For every ACK received, cwnd doubles exponentially until packet loss occurs, probing network capacity.\n\nTLS 1.2 vs TLS 1.3 Handshake:\n- TLS 1.2 required 2 full round trips (2 RTT) after TCP handshake to negotiate cipher suites and exchange keys.\n- TLS 1.3 combines key exchange (Diffie-Hellman) into ClientHello, reducing handshake to 1 RTT!\n- 0-RTT Resumption: Returning clients can send encrypted application data on the very first packet using pre-shared keys.",
    "keyPoints": [
      "TCP 3-way handshake takes 1 RTT before any data flows",
      "TCP Slow Start doubles congestion window exponentially to probe bandwidth",
      "TLS 1.3 cuts cryptographic handshake from 2 RTTs down to 1 RTT",
      "TLS 1.3 0-RTT enables instant data transmission on resumed sessions"
    ],
    "tags": [
      "TCP",
      "TLS",
      "Networking",
      "Performance"
    ]
  },
  {
    "id": "sd-25",
    "title": "Database Connection Pooling and PgBouncer Multiplexing",
    "category": "Databases & Storage",
    "difficulty": "Medium",
    "question": "Why do databases crash when given too many concurrent connections? Explain connection pool sizing formulas and connection multiplexers like PgBouncer.",
    "answer": "Each database connection consumes 5-10MB RAM on the server and causes operating system CPU thread context-switching overhead. Thousands of active connections cause CPU thrashing.\n\nHikariCP Sizing Formula: `connections = ((core_count * 2) + effective_spindle_count)`. A 16-core DB server performs best with only ~33 connections!\n\nPgBouncer Transaction Pooling: Sits between thousands of app pods and Postgres. Holds physical server connection only while an individual SQL transaction runs, allowing 10,000 app client connections to share 100 physical DB connections.",
    "keyPoints": [
      "Excess connections cause severe OS thread context-switching thrashing",
      "Smaller connection pools yield higher total throughput",
      "HikariCP formula: (cores * 2) + disk spindles",
      "PgBouncer transaction pooling multiplexes thousands of pods over tens of connections"
    ],
    "tags": [
      "Databases",
      "Connection Pool",
      "PostgreSQL",
      "Performance"
    ]
  },
  {
    "id": "sd-26",
    "title": "Zero Trust Network Architecture: Service Mesh & mTLS",
    "category": "Security & Networking",
    "difficulty": "Medium",
    "question": "What is Zero Trust Architecture? How do Service Meshes (Istio/Envoy) automate Mutual TLS (mTLS) and service identity in Kubernetes?",
    "answer": "Perimeter security ('castle and moat') assumes internal traffic is trusted. Zero Trust principle: 'Never trust, always verify'.\n\nService Mesh (Istio/Envoy):\n- Sidecar proxy injected alongside every microservice container.\n- SPIFFE/SPIRE: Assigns cryptographic X.509 certificates to each service workload.\n- Mutual TLS (mTLS): Sidecars negotiate mTLS automatically, encrypting all east-west pod-to-pod traffic.\n- Authorization Policies: Envoy verifies client service identity before routing requests, enforcing strict service-level access control.",
    "keyPoints": [
      "Eliminates implicit trust inside private network perimeter",
      "SPIFFE provides cryptographic workload identity across containers",
      "Sidecar proxies offload mTLS encryption transparently without code changes",
      "Strict authorization policies prevent lateral movement"
    ],
    "tags": [
      "Zero Trust",
      "Service Mesh",
      "Istio",
      "Envoy",
      "Security",
      "Kubernetes"
    ]
  },
  {
    "id": "sd-27",
    "title": "WebSockets Cluster Scaling with Redis Pub/Sub",
    "category": "Networking",
    "difficulty": "Medium",
    "question": "How do you scale WebSocket connections across multiple server nodes so users connected to different servers can message each other?",
    "answer": "Problem: User A is connected to WebSocket Server 1; User B is connected to WebSocket Server 2. Server 1 cannot deliver a message directly to User B.\n\nArchitecture:\n1. Gateway Tier: Multiple stateless WebSocket servers behind an L4/L7 load balancer with sticky sessions.\n2. Session Registry: Redis stores `user_id -> server_id` mapping.\n3. Message Broker (Redis Pub/Sub or Kafka):\n- When User A sends message to User B: Server 1 publishes message to Redis topic `user:user_B_id`.\n- Every server subscribes to channels for its currently connected users.\n- Server 2 receives event from Redis and writes it directly to User B's active WebSocket connection.",
    "keyPoints": [
      "Stateless WebSocket connection servers scaled horizontally behind load balancer",
      "Redis stores user-to-server connection mapping",
      "Redis Pub/Sub or Kafka routes cross-server messages",
      "Handles node disconnects and dynamic rebalancing"
    ],
    "tags": [
      "WebSocket",
      "Redis",
      "PubSub",
      "Scalability",
      "Real-Time"
    ]
  },
  {
    "id": "sd-28",
    "title": "Network NAT (Network Address Translation) and IPv4 vs IPv6",
    "category": "Networking",
    "difficulty": "Easy",
    "question": "Explain how SNAT and DNAT work. What challenges did IPv4 exhaustion create, and how does IPv6 simplify cloud networking?",
    "answer": "NAT maps private IP addresses (RFC 1918: `10.x`, `192.168.x`) to public internet IPs.\n- SNAT (Source NAT): Outbound traffic from private subnet gets gateway's public IP and unique source port. Gateway tracks translation table. (AWS NAT Gateway).\n- DNAT (Destination NAT): Inbound traffic to public IP/port is translated to internal private IP/port (Load balancers, port forwarding).\n\nIPv6:\n128-bit addresses provide `3.4 * 10^38` unique IPs. Eliminates need for NAT; every container/pod can have globally routable IP with security enforced via stateful firewalls.",
    "keyPoints": [
      "SNAT translates private IPs to public for egress traffic",
      "DNAT routes inbound public traffic to private services",
      "NAT gateways can become egress throughput bottlenecks",
      "IPv6 provides direct end-to-end addressing without NAT overhead"
    ],
    "tags": [
      "Networking",
      "NAT",
      "IPv4",
      "IPv6",
      "AWS"
    ]
  },
  {
    "id": "sd-29",
    "title": "API Gateway Pattern vs Backend-for-Frontend (BFF)",
    "category": "Architecture Patterns",
    "difficulty": "Medium",
    "question": "Compare a centralized Enterprise API Gateway with the Backend-for-Frontend (BFF) pattern. When should mobile and web have separate BFFs?",
    "answer": "Centralized API Gateway:\nSingle entry point for all clients. Handles cross-cutting concerns: auth, rate limiting, logging. Problem: Becomes an organizational bottleneck when mobile, web, and IoT teams require conflicting response formats and payload sizes.\n\nBackend-for-Frontend (BFF):\nDedicated backend service tailored to a specific client interface (e.g. iOS BFF, Android BFF, Web Desktop BFF).\n- Mobile BFF trims bulky responses, reduces payload over cellular networks, aggregates 5 microservice calls into 1 screen payload.\n- Web BFF serves richer data and handles server-side rendering (SSR).\n- Architecture: Client -> BFF -> API Gateway / Microservices.",
    "keyPoints": [
      "Centralized gateway manages enterprise cross-cutting concerns",
      "BFF customizes payload and aggregation per client type (mobile vs web)",
      "Mobile BFF minimizes cellular bandwidth and battery consumption",
      "Prevents UI teams from becoming blocked by centralized API gatekeepers"
    ],
    "tags": [
      "API Gateway",
      "BFF",
      "Architecture Patterns",
      "Mobile"
    ]
  },
  {
    "id": "sd-30",
    "title": "Service Discovery: Client-Side vs Server-Side (Eureka vs Envoy/Kubernetes)",
    "category": "Scalability & Routing",
    "difficulty": "Medium",
    "question": "How does dynamic service discovery work in ephemeral cloud environments? Compare Client-Side (Netflix Eureka) and Server-Side (Kubernetes DNS/CoreDNS).",
    "answer": "Client-Side Discovery (e.g. Netflix Eureka, Consul with ribbon):\nClients query the service registry directly to get list of available healthy service IPs, then client-side load balancer selects an instance. Pros: Zero intermediate proxy latency hop. Cons: Tightly couples client app to registry library; requires implementation across every language.\n\nServer-Side Discovery (e.g. Kubernetes ClusterIP + CoreDNS / AWS ALB):\nClient makes request to a stable DNS name or virtual IP. Intermediate router/proxy (kube-proxy, Envoy, AWS ALB) queries registry and routes to a healthy pod. Pros: Language agnostic, transparent to client code. Cons: Extra network hop through proxy.",
    "keyPoints": [
      "Ephemeral containers require dynamic IP registration and health checks",
      "Client-side discovery eliminates proxy hop but requires language SDKs",
      "Server-side discovery (Kubernetes DNS) is language-agnostic and standard",
      "kube-proxy uses Linux iptables or IPVS for virtual IP routing"
    ],
    "tags": [
      "Service Discovery",
      "Kubernetes",
      "Consul",
      "Envoy"
    ]
  },
  {
    "id": "sd-31",
    "title": "B-Tree vs LSM-Tree Storage Engines",
    "category": "Databases & Storage",
    "difficulty": "Hard",
    "question": "Compare B-Tree (PostgreSQL, MySQL InnoDB) and LSM-Tree (Cassandra, RocksDB) storage engines. Analyze read and write amplification.",
    "answer": "B-Trees: In-place page updates (4KB-16KB pages). Fast point reads O(log N). High write amplification due to random disk I/O and page writes plus WAL. Best for read-heavy OLTP.\n\nLSM-Trees: MemTable in RAM + sequential append to WAL. Flushed sequentially to immutable SSTables on disk. Merged via background compaction. High read amplification (mitigated by Bloom filters); ultra-high write throughput with sequential disk I/O. Best for write-heavy, time-series, and event streaming workloads.",
    "keyPoints": [
      "B-Trees write in-place; optimal for read-heavy OLTP",
      "LSM-Trees turn all writes into sequential disk I/O",
      "Bloom filters prevent searching SSTables that lack requested keys",
      "Compaction merges immutable SSTables discarding obsolete data"
    ],
    "tags": [
      "Storage Engines",
      "Databases",
      "B-Tree",
      "LSM-Tree",
      "RocksDB"
    ]
  },
  {
    "id": "sd-32",
    "title": "Database Sharding: Range, Hash, and Directory-Based",
    "category": "Databases & Storage",
    "difficulty": "Medium",
    "question": "Compare Range-based, Hash-based, and Directory-based database sharding. Detail cross-shard queries and re-sharding strategies.",
    "answer": "Hash-Based: `shard = hash(key) % N`. Uniform distribution, avoids hotspots. Range queries become expensive scatter-gather operations across all shards.\n\nRange-Based: Partitioned by contiguous key ranges (dates, IDs). Fast localized range scans. Suffers from write hotspots if recent keys receive all traffic.\n\nDirectory-Based: Lookup service routes key to shard. Highly flexible, but lookup service adds latency hop and requires client caching.\n\nCross-shard joins are avoided via denormalization; cross-shard transactions require SAGA.",
    "keyPoints": [
      "Hash-based avoids hotspots but makes range queries scatter-gather",
      "Range-based supports fast range queries but risks hotspots",
      "Shard key selection is the most critical architectural decision",
      "Data denormalization avoids expensive cross-shard joins"
    ],
    "tags": [
      "Sharding",
      "Databases",
      "Scalability",
      "Distributed Systems"
    ]
  },
  {
    "id": "sd-33",
    "title": "Distributed Caching Patterns and Thundering Herd Prevention",
    "category": "Caching",
    "difficulty": "Medium",
    "question": "Explain Cache-Aside, Write-Through, Write-Back, and Write-Around. How do you prevent Cache Stampede (Thundering Herd)?",
    "answer": "Patterns:\n- Cache-Aside: App reads cache; on miss, reads DB and populates cache. Resilient.\n- Write-Through: Synchronous write to cache and DB. Consistent, higher latency.\n- Write-Back: Async write to DB from cache. Ultra-fast, data loss risk on crash.\n- Write-Around: Direct write to DB; avoids cache pollution.\n\nThundering Herd Prevention:\n1. Mutex / SingleFlight: Only 1 request queries DB on cache miss; others await result.\n2. Probabilistic Early Refresh (XFetch): Background thread refreshes key before TTL expires.\n3. TTL Jitter: Add random jitter (`TTL + rand(0, 300)`) to prevent synchronized expiration.",
    "keyPoints": [
      "Cache-aside is industry standard for distributed read architectures",
      "Write-back offers maximum write speed but risks data loss",
      "SingleFlight collapses duplicate DB misses into 1 query",
      "TTL jittering prevents simultaneous bulk key expiration"
    ],
    "tags": [
      "Caching",
      "Redis",
      "Performance",
      "High Availability"
    ]
  },
  {
    "id": "sd-34",
    "title": "Redis Data Structures and Architectural Internals",
    "category": "Caching",
    "difficulty": "Medium",
    "question": "Detail Redis core data structures (Strings, Hashes, Lists, Sets, Sorted Sets, HyperLogLog, Bitmaps) and explain why Redis single-threaded execution is ultra-fast.",
    "answer": "Why Single-Threaded Event Loop is Fast:\nExecutes operations in memory using non-blocking I/O multiplexing (epoll/kqueue). Zero thread context-switching overhead, zero locks, zero race conditions on memory structures.\n\nData Structures:\n- Strings: Simple key-values, counters (`INCR`), distributed locks (`SET NX EX`).\n- Hashes: Objects (`HSET user:1 name 'Ajay'`).\n- Lists: Queues and stacks (`LPUSH`, `RPOP`, `BLPOP`).\n- Sets: Unique values, intersections (`SADD`, `SINTER`).\n- Sorted Sets (ZSET): SkipList + Hash map. Real-time leaderboards, sliding window rate limiters (`ZADD`, `ZRANGEBYSCORE`).\n- HyperLogLog: Probabilistic cardinality counting of millions of unique items with 12KB RAM.\n- Bitmaps: Compact user daily active tracking.",
    "keyPoints": [
      "In-memory execution and epoll I/O multiplexing deliver sub-millisecond speeds",
      "No thread context-switching or mutex contention",
      "Sorted Sets (SkipList) power real-time leaderboards and rate limiters",
      "HyperLogLog counts unique items with 0.81% error using 12KB RAM"
    ],
    "tags": [
      "Redis",
      "Caching",
      "Data Structures",
      "NoSQL"
    ]
  },
  {
    "id": "sd-35",
    "title": "Redis Replication, Sentinel, and Redis Cluster Sharding",
    "category": "Caching",
    "difficulty": "Medium",
    "question": "Compare Redis Sentinel for high availability with Redis Cluster for horizontal sharding. How do hash slots work?",
    "answer": "Redis Sentinel:\nPrimary-replica replication with automated failover. Sentinel nodes monitor primary health; elect new primary on failure. Does NOT provide horizontal sharding (entire dataset must fit in 1 primary's RAM).\n\nRedis Cluster (Horizontal Sharding):\nPartitions keys across 16,384 Hash Slots. `slot = CRC16(key) % 16384`.\nHash slots are divided among master nodes. Master nodes replicate to replicas.\nHash Tags: `{user:123}.profile` and `{user:123}.orders` map to the same hash slot by hashing only the text inside `{}` for multi-key atomic transactions.",
    "keyPoints": [
      "Sentinel handles automated master failover but not horizontal sharding",
      "Redis Cluster partitions dataset across 16,384 hash slots",
      "CRC16 hash determines slot assignment",
      "Hash tags {tag} force related keys to same slot for atomic transactions"
    ],
    "tags": [
      "Redis",
      "Redis Cluster",
      "Sentinel",
      "High Availability",
      "Sharding"
    ]
  },
  {
    "id": "sd-36",
    "title": "Memcached vs Redis Comparison",
    "category": "Caching",
    "difficulty": "Easy",
    "question": "Compare Memcached and Redis. When would an engineering team deliberately choose Memcached over Redis?",
    "answer": "Memcached:\n- Multi-threaded architecture utilizing all CPU cores natively.\n- Simple key-value string storage with slab allocation memory model.\n- No persistence, no replication, no complex data structures.\n- Best for: Massive pure key-value caching where multithreaded CPU scaling beats single-thread Redis limits (e.g., caching multi-megabyte HTML chunks).\n\nRedis:\n- Single-threaded event loop (I/O threads in Redis 6+).\n- Rich data structures (Lists, Sets, Hashes, ZSETs, Streams, Bitmaps).\n- Persistence (RDB snapshots + AOF commit log).\n- Built-in pub/sub, Lua scripting, cluster sharding, and high availability.",
    "keyPoints": [
      "Memcached is multi-threaded; scales well on high-core servers for pure key-value",
      "Redis offers rich data structures, persistence, and pub/sub",
      "Memcached slab allocation prevents memory fragmentation",
      "Redis is chosen for 95% of modern complex distributed caching use cases"
    ],
    "tags": [
      "Memcached",
      "Redis",
      "Caching",
      "Performance"
    ]
  },
  {
    "id": "sd-37",
    "title": "SQL vs NoSQL: Relational, Document, Key-Value, Columnar, and Graph",
    "category": "Databases & Storage",
    "difficulty": "Medium",
    "question": "When should you choose Relational (PostgreSQL), Document (MongoDB), Key-Value (DynamoDB), Wide-Column (Cassandra), or Graph (Neo4j)?",
    "answer": "1. Relational (Postgres): ACID transactions, structured schemas, relational joins. Best for: Banking, billing, core transactional data.\n2. Document (MongoDB): Hierarchical JSON documents, dynamic schemas. Best for: Product catalogs, content management.\n3. Key-Value (DynamoDB): Single-digit ms read/write at any scale via primary key. Best for: Session state, shopping carts.\n4. Wide-Column (Cassandra/ScyllaDB): LSM-tree write-optimized sequential storage partitioned by key. Best for: IoT telemetry, time-series, high-write messaging logs.\n5. Graph (Neo4j): Graph traversal across relationships without relational join explosion. Best for: Social networks, fraud rings, recommendation engines.",
    "keyPoints": [
      "Relational guarantees ACID integrity with foreign key relationships",
      "Document databases handle polymorphic semi-structured data",
      "Wide-column systems deliver massive write throughput at linear scale",
      "Graph databases optimize complex multi-hop relationship queries"
    ],
    "tags": [
      "Databases",
      "SQL",
      "NoSQL",
      "Postgres",
      "Cassandra",
      "MongoDB"
    ]
  },
  {
    "id": "sd-38",
    "title": "OLTP vs OLAP: Row-Oriented vs Columnar Databases",
    "category": "Databases & Storage",
    "difficulty": "Medium",
    "question": "Why do analytical queries run 100x faster on columnar databases (Snowflake, BigQuery, ClickHouse) than row-oriented databases (PostgreSQL)?",
    "answer": "Row-Oriented (Postgres, MySQL):\nStores data on disk row by row: `(ID, Name, Age, Country)`. When querying `SELECT AVG(Age) FROM users`, the database must read EVERY full row off disk into memory, wasting 95% I/O on unneeded columns. Optimal for OLTP point updates.\n\nColumnar (Snowflake, BigQuery, ClickHouse):\nStores data column by column: all `Age` values grouped together, all `Country` values together.\n1. Selective I/O: Only scans the exact columns requested in query.\n2. Extreme Compression: Homogeneous column data (e.g. all integers or strings) compresses 5-10x better using run-length encoding (RLE) and dictionary encoding.\n3. Vectorized Execution: SIMD CPU instructions process thousands of rows per CPU cycle.",
    "keyPoints": [
      "Row-oriented is optimal for OLTP point inserts and updates",
      "Columnar scans only requested columns, saving 90%+ disk I/O",
      "Homogeneous column data enables 5-10x compression ratios",
      "SIMD vectorized execution accelerates analytical aggregations"
    ],
    "tags": [
      "OLTP",
      "OLAP",
      "BigQuery",
      "Snowflake",
      "ClickHouse",
      "Databases"
    ]
  },
  {
    "id": "sd-39",
    "title": "Database Isolation Levels and Concurrency Anomalies",
    "category": "Databases & Storage",
    "difficulty": "Hard",
    "question": "Explain the 4 ANSI SQL Isolation Levels and the anomalies they prevent (Dirty Read, Non-Repeatable Read, Phantom Read, Serialization Anomaly). How does MVCC work?",
    "answer": "Isolation Levels & Anomalies:\n1. Read Uncommitted: Suffers from Dirty Reads (reading uncommitted changes that get rolled back).\n2. Read Committed: Prevents Dirty Reads. Suffers from Non-Repeatable Reads (reading row twice in same transaction yields different data due to another commit).\n3. Repeatable Read: Prevents Non-Repeatable Reads. In standard SQL, suffers from Phantom Reads (new rows inserted by concurrent transaction match query condition).\n4. Serializable: Complete isolation. Prevents all anomalies including Write Skew. Emulates serial sequential execution.\n\nMulti-Version Concurrency Control (MVCC):\nInstead of locking tables, database keeps multiple timestamped versions of rows (e.g. Postgres `xmin, xmax`). Readers never block writers, and writers never block readers!",
    "keyPoints": [
      "Read Committed is default in Postgres; Repeatable Read is default in MySQL InnoDB",
      "MVCC ensures readers do not block writers and writers do not block readers",
      "Postgres uses xmin/xmax hidden columns to implement MVCC row snapshots",
      "Serializable prevents write skew anomalies at performance cost"
    ],
    "tags": [
      "ACID",
      "Isolation Levels",
      "MVCC",
      "PostgreSQL",
      "Transactions"
    ]
  },
  {
    "id": "sd-40",
    "title": "Write-Ahead Logging (WAL) and Crash Recovery (ARIES)",
    "category": "Databases & Storage",
    "difficulty": "Hard",
    "question": "How does the Write-Ahead Log (WAL) guarantee the Durability in ACID? Explain the ARIES recovery algorithm (Analysis, Redo, Undo).",
    "answer": "Principle: Never write dirty database pages to disk until the corresponding log entry is committed sequentially to the Write-Ahead Log (WAL) on disk.\nSequential WAL appends are orders of magnitude faster than random database page writes.\n\nARIES Crash Recovery Phases:\n1. Analysis Phase: Scans WAL forward from last checkpoint to identify dirty pages in memory and active transactions at time of crash.\n2. Redo Phase: Replays all committed changes forward to restore database state to exact moment of crash ('repeating history').\n3. Undo Phase: Scans WAL backward, rolling back changes made by transactions that were still active (uncommitted) when the crash occurred.",
    "keyPoints": [
      "WAL guarantees durability by flushing sequential log before dirty pages",
      "Sequential disk append enables high transaction commit throughput",
      "ARIES recovery executes Analysis, Redo, Undo phases",
      "Checkpoints truncate WAL preventing unbounded recovery times"
    ],
    "tags": [
      "WAL",
      "ACID",
      "Databases",
      "Crash Recovery",
      "PostgreSQL"
    ]
  },
  {
    "id": "sd-41",
    "title": "Bloom Filters: Mathematics, Operations, and False Positives",
    "category": "Databases & Storage",
    "difficulty": "Medium",
    "question": "What is a Bloom Filter? How do multiple hash functions work, why are there zero false negatives, and where are Bloom filters deployed in production?",
    "answer": "A space-efficient probabilistic data structure used to test set membership.\nOperations:\n- Bit array of size `m` initialized to 0. `k` independent hash functions.\n- Add(item): Hash item with all `k` hashes. Set bits at positions `h1(x), h2(x)...` to 1.\n- Contains(item): Hash item with `k` hashes. If ANY bit is 0, item is DEFINITIVELY NOT in set (0% False Negatives).\n- If all bits are 1: item is PROBABLY in set (acceptable False Positive rate `p`).\n- Deletion is impossible in standard Bloom filter (requires Counting Bloom Filter).\n\nProduction Use Cases:\n- LSM Storage Engines (RocksDB/Cassandra): Checks Bloom filter before reading SSTable off disk.\n- Web Crawlers: Deduplicates seen URLs with minimal memory footprint.\n- CDN / Malicious URL blocking.",
    "keyPoints": [
      "Zero false negatives: if it says item is missing, it is guaranteed missing",
      "Controlled false positive probability tuned via bit array size and hash count",
      "Saves expensive disk seeks in RocksDB, Cassandra, and Bigtable",
      "Standard Bloom filters do not support item deletion"
    ],
    "tags": [
      "Bloom Filter",
      "Probabilistic Data Structures",
      "RocksDB",
      "Cassandra"
    ]
  },
  {
    "id": "sd-42",
    "title": "Time-Series Databases (TSDB) Architecture: InfluxDB vs TimescaleDB",
    "category": "Databases & Storage",
    "difficulty": "Medium",
    "question": "Why are relational databases inefficient for high-volume time-series metrics? How do TimescaleDB Hypertables and Gorillas compression optimize time-series storage?",
    "answer": "Challenges with Time-Series:\n- Hundreds of thousands of data points per second.\n- Regular B-Tree indexes degrade as table size exceeds RAM due to random page splits.\n\nTimescaleDB (Hypertables):\n- Built on PostgreSQL.\n- Automatically partitions data into two-dimensional 'chunks' by time interval (e.g. 1 day) and space/device_id.\n- Each chunk has its own B-Tree index small enough to fit completely in RAM, sustaining high write rates.\n- Native columnar compression on older chunks (up to 95% space reduction).\n\nGorilla TSDB Compression (Facebook / Prometheus):\n- Delta-of-delta timestamp compression.\n- XOR floating point value compression.",
    "keyPoints": [
      "High-volume time series degrade standard single-table B-Trees",
      "TimescaleDB Hypertables partition data into small time-bucket chunks",
      "Chunks fit inside RAM sustaining high write throughput",
      "Gorilla XOR compression reduces metric data sizes by 12x"
    ],
    "tags": [
      "Time-Series",
      "TimescaleDB",
      "InfluxDB",
      "PostgreSQL",
      "Monitoring"
    ]
  },
  {
    "id": "sd-43",
    "title": "Object Storage Architecture: S3 Internals, Erasure Coding, and Multipart Upload",
    "category": "Databases & Storage",
    "difficulty": "Hard",
    "question": "How is distributed cloud Object Storage (Amazon S3, GCP Cloud Storage) architected? Detail Erasure Coding (Reed-Solomon) vs Replication and Multipart Uploads.",
    "answer": "Storage Model:\nFlat namespace (buckets and keys), not a hierarchical filesystem. Metadata stored in distributed key-value store (Dynamo/Spanner); binary payloads stored on disk servers.\n\nErasure Coding (Reed-Solomon):\nInstead of 3x replication (200% storage overhead), Erasure Coding splits data into `k` data chunks and generates `m` parity chunks (e.g. `8 + 4 = 12` chunks, 50% overhead).\nAny `k` of the `k + m` chunks can reconstruct the original object! Survives loss of any `m` disks simultaneously with far lower hardware costs.\n\nMultipart Upload:\nLarge files (>100MB) split into parts uploaded concurrently. Failed part retries individually without restarting entire upload. Assembled atomically at destination.",
    "keyPoints": [
      "Flat object key-value namespace eliminates filesystem directory lock contention",
      "Erasure coding (e.g. 8+4) provides extreme durability with only 50% storage overhead",
      "Survives concurrent disk failures without 3x replication cost",
      "Multipart upload allows parallel streaming and fault-tolerant resumes"
    ],
    "tags": [
      "S3",
      "Object Storage",
      "Erasure Coding",
      "Distributed Storage"
    ]
  },
  {
    "id": "sd-44",
    "title": "Database Deadlocks: Detection, Wait-For Graphs, and Prevention",
    "category": "Databases & Storage",
    "difficulty": "Medium",
    "question": "What causes database deadlocks in relational transactions? How do databases detect deadlocks via Wait-For Graphs, and how can engineers prevent them?",
    "answer": "Cause: Transaction A holds Lock 1 and requests Lock 2; Transaction B holds Lock 2 and requests Lock 1. Neither can proceed.\n\nDeadlock Detection:\n- Wait-For Graph: Directed graph where nodes are transactions and edges represent lock dependencies (`T1 -> T2`).\n- Background thread runs cycle detection algorithm (Tarjan's/DFS). If a cycle is detected, database aborts the victim transaction with lowest cost and rolls it back.\n\nPrevention Strategies:\n1. Global Lock Acquisition Order: Enforce that all transactions always acquire locks in the exact same deterministic order (e.g., sort record IDs before updating).\n2. Short Transactions: Minimize time locks are held; keep external API calls outside DB transactions.\n3. Optimistic Locking: Use version column (`WHERE version = 5`) instead of pessimistic `SELECT ... FOR UPDATE`.",
    "keyPoints": [
      "Deadlock occurs when two transactions wait cyclically for locks held by each other",
      "Wait-For graph cycle detection detects deadlocks and rolls back victim",
      "Deterministic lock acquisition ordering prevents deadlocks",
      "Keep external API calls outside database transaction boundaries"
    ],
    "tags": [
      "Deadlock",
      "Databases",
      "Concurrency",
      "SQL"
    ]
  },
  {
    "id": "sd-45",
    "title": "Graph Databases: Neo4j vs Relational for Deep Relationship Traversal",
    "category": "Databases & Storage",
    "difficulty": "Medium",
    "question": "Why do relational databases suffer join explosions on recursive relationship queries, and how does Neo4j Index-Free Adjacency solve this?",
    "answer": "Relational Join Explosion:\nQuerying friends-of-friends-of-friends (degrees of separation) in SQL requires multiple recursive `JOIN` operations across large tables, requiring multiple B-Tree lookups that degrade exponentially: O(N^k).\n\nGraph Database (Neo4j) - Index-Free Adjacency:\nEach node holds direct physical memory pointers to its adjacent neighbor nodes on disk.\nTraversing an edge is a simple pointer dereference running in O(1) time!\nTraversal time depends solely on the size of the subgraph traversed, completely independent of total database size (whether graph has 1,000 or 1,000,000,000 nodes).",
    "keyPoints": [
      "Relational joins on multi-hop relationships suffer exponential latency degradation",
      "Index-free adjacency stores direct physical memory pointers to neighbors",
      "Graph traversal runs in O(1) per edge step via pointer dereferencing",
      "Ideal for social graphs, fraud rings, identity graphs, and knowledge bases"
    ],
    "tags": [
      "Graph Database",
      "Neo4j",
      "Databases",
      "Data Modeling"
    ]
  },
  {
    "id": "sd-46",
    "title": "Kafka Architecture: Partitions, Consumer Groups, and Log Compaction",
    "category": "Messaging & Streaming",
    "difficulty": "Hard",
    "question": "How does Apache Kafka achieve millions of messages per second? Explain zero-copy OS reads, sequential disk I/O, partition-based concurrency, and exactly-once semantics.",
    "answer": "Why Kafka is Ultra-Fast:\n1. Sequential Disk I/O: Kafka appends to an immutable commit log on disk. Sequential disk access matches memory speeds.\n2. PageCache & Zero-Copy: Uses Linux kernel PageCache and `sendfile()` system call: data moves directly from PageCache to Network Socket buffer, bypassing user-space CPU copying.\n3. Partitioning: Topics divided into partitions. Partition is the unit of parallelism; consumed by at most 1 consumer in a group.\n4. Log Compaction: Retains only the latest value for each key, acting as a changelog.\n5. Exactly-Once Semantics (EOS): Combines idempotent producer sequence IDs with transactional coordinator.",
    "keyPoints": [
      "sendfile() zero-copy transfers from kernel page cache directly to NIC buffer",
      "Sequential append avoids expensive disk seek operations",
      "Partitioning provides parallelism; ordering is guaranteed per partition",
      "EOS combines idempotent producer sequence IDs with transactional coordinator"
    ],
    "tags": [
      "Kafka",
      "Event Streaming",
      "Messaging",
      "Linux",
      "Architecture"
    ]
  },
  {
    "id": "sd-47",
    "title": "The Transactional Outbox Pattern & Change Data Capture (CDC)",
    "category": "Messaging & Streaming",
    "difficulty": "Hard",
    "question": "How does the Transactional Outbox pattern resolve the dual-write problem between a relational database and an event broker like Kafka? How does Debezium implement CDC?",
    "answer": "Dual-Write Problem: Updating database AND publishing to Kafka in application code cannot be atomic without distributed 2PC.\n\nTransactional Outbox Solution:\n1. In the same ACID DB transaction, save entity and insert event into an `outbox` table.\n2. Atomicity guaranteed locally.\n\nCDC Dispatch with Debezium:\n- Debezium reads database transaction log (Postgres WAL / MySQL Binlog).\n- Streams committed outbox rows directly into Kafka.\n- Zero polling overhead, zero table locks.\n- Downstream consumers process events idempotently using message IDs.",
    "keyPoints": [
      "Solves dual-write problem without distributed 2PC transactions",
      "Business entity and outbox message commit in a single ACID transaction",
      "Debezium tailing the DB WAL eliminates database polling overhead",
      "Downstream consumers must implement idempotency to handle at-least-once delivery"
    ],
    "tags": [
      "Outbox Pattern",
      "Debezium",
      "CDC",
      "Kafka",
      "Microservices"
    ]
  },
  {
    "id": "sd-48",
    "title": "Kafka vs RabbitMQ: Architecture and Workload Suitability",
    "category": "Messaging & Streaming",
    "difficulty": "Medium",
    "question": "Compare Apache Kafka and RabbitMQ. Detail routing flexibility, message durability, consumer scaling models, and backpressure.",
    "answer": "RabbitMQ (Smart Broker, Dumb Consumer):\n- AMQP protocol. Exchange routes messages to queues via bindings (Direct, Topic, Fanout, Headers).\n- Messages deleted once acknowledged by consumer.\n- Push model with prefetch limit backpressure.\n- Ideal for: Complex transactional routing, background worker queues, task scheduling.\n\nKafka (Dumb Broker, Smart Consumer):\n- Distributed commit log. Topics partitioned across brokers.\n- Messages retained on disk based on retention time/size, NOT deleted on read.\n- Pull model: Consumer tracks its own offset.\n- Replayability: Consumers can rewind offsets to re-process historical data.\n- Ideal for: High-throughput event streaming, analytics pipelines, event sourcing.",
    "keyPoints": [
      "RabbitMQ deletes messages upon acknowledgment; Kafka retains messages on disk",
      "RabbitMQ excels at complex routing rules; Kafka excels at high-throughput streaming",
      "Kafka pull model enables consumers to process at their own pace and replay history",
      "RabbitMQ broker maintains state; Kafka consumer tracks offset"
    ],
    "tags": [
      "Kafka",
      "RabbitMQ",
      "Messaging",
      "Architecture"
    ]
  },
  {
    "id": "sd-49",
    "title": "Message Delivery Guarantees: At-Most-Once, At-Least-Once, Exactly-Once",
    "category": "Messaging & Streaming",
    "difficulty": "Medium",
    "question": "What are At-Most-Once, At-Least-Once, and Exactly-Once delivery guarantees? How do consumers achieve effective Exactly-Once processing?",
    "answer": "Guarantees:\n1. At-Most-Once: Message delivered 0 or 1 time. Acknowledge message BEFORE processing. If worker crashes during processing, message is lost. Fast, no duplicates.\n2. At-Least-Once: Message delivered 1 or more times. Acknowledge message AFTER processing. If worker crashes or network ACK fails, message is redelivered. Duplicates can occur.\n3. Exactly-Once (End-to-End):\nIn practice, achieved by combining At-Least-Once delivery with IDEMPOTENT consumer processing:\n- Consumer checks database for message ID before applying update.\n- Or uses database unique constraints (`INSERT ... ON CONFLICT DO NOTHING`).",
    "keyPoints": [
      "Network partitions make true physical exactly-once delivery impossible",
      "At-least-once delivery plus idempotent consumer equals effective exactly-once",
      "Unique message IDs stored in database deduplicate redelivered events",
      "Kafka transactions coordinate atomic multi-topic stream transformations"
    ],
    "tags": [
      "Messaging",
      "Kafka",
      "Reliability",
      "Distributed Systems"
    ]
  },
  {
    "id": "sd-50",
    "title": "Dead Letter Queues (DLQ) and Retry Strategies",
    "category": "Messaging & Streaming",
    "difficulty": "Medium",
    "question": "How do you design a resilient message retry architecture with Dead Letter Queues (DLQ) without blocking partition processing?",
    "answer": "Problem: A poison pill message causes consumer to crash repeatedly, blocking an entire Kafka partition or RabbitMQ queue.\n\nResilient Retry Architecture:\n1. Immediate Retry: Retry transient errors 3 times with exponential backoff.\n2. Delayed Retry Topics: If failures persist, route message to a sequence of retry queues with escalating delays (e.g. `orders.retry.1min`, `orders.retry.10min`, `orders.retry.1hour`). Unblocks main consumer immediately!\n3. Dead Letter Queue (DLQ): If all retries fail, route to `orders.dlq` for alerting and manual investigation.\n4. Replay Tooling: Operators fix bug, then replay DLQ messages back to main processing queue.",
    "keyPoints": [
      "Poison pill messages block entire partition without retry topics",
      "Decouples retry delays from main ingestion pipeline",
      "Dead Letter Queue isolates unprocessable messages for inspection",
      "Replay mechanisms allow re-injecting DLQ messages after bug fixes"
    ],
    "tags": [
      "DLQ",
      "Kafka",
      "RabbitMQ",
      "Resilience",
      "Error Handling"
    ]
  },
  {
    "id": "sd-51",
    "title": "Distributed Rate Limiter Algorithms: Token Bucket, Leaky Bucket, Sliding Window",
    "category": "Resilience",
    "difficulty": "Medium",
    "question": "Compare Token Bucket, Leaky Bucket, and Sliding Window Counter rate limiting algorithms. How do you implement atomic sliding window counters in Redis?",
    "answer": "Algorithms:\n1. Token Bucket: Tokens replenish at fixed rate up to capacity. Allows bursts. O(1) memory.\n2. Leaky Bucket: Smooths bursts to constant egress rate via FIFO queue.\n3. Sliding Window Counter (Optimal): Combines current minute and previous minute counters with weight: `req = prev * (1 - time_into_minute) + curr`. Low memory, high accuracy.\n\nRedis Lua Implementation:\nAtomic Lua script computes tokens or increments sliding window counter in a single network round-trip, eliminating race conditions under concurrent load.",
    "keyPoints": [
      "Token Bucket allows bursts; Leaky Bucket forces constant egress rate",
      "Sliding Window Counter offers optimal balance of memory and accuracy",
      "Redis Lua script ensures atomic check-and-increment operations",
      "Returns standard HTTP 429 with Retry-After header"
    ],
    "tags": [
      "Rate Limiter",
      "Redis",
      "Resilience",
      "Algorithms"
    ]
  },
  {
    "id": "sd-52",
    "title": "Circuit Breaker Pattern: States, Thresholds, and Fallbacks",
    "category": "Resilience",
    "difficulty": "Medium",
    "question": "Explain the Circuit Breaker pattern (Closed, Open, Half-Open). How does it prevent cascading failures in microservice architectures?",
    "answer": "States:\n1. Closed: Normal operation. If error rate exceeds threshold (>50% errors over 10s), trips to OPEN.\n2. Open: Requests fail immediately without calling downstream service! Returns fallback response. Starts sleep timer (30s).\n3. Half-Open: After sleep timer, allows small canary probe batch. If successful, resets to CLOSED; if any fail, returns to OPEN.\n\nPrevents cascading thread pool exhaustion across microservice call chains.",
    "keyPoints": [
      "Prevents cascading failures and thread exhaustion",
      "Fails fast during outages without hammering struggling dependencies",
      "Half-Open state verifies downstream recovery using canary probes",
      "Fallback responses provide graceful degradation"
    ],
    "tags": [
      "Circuit Breaker",
      "Resilience",
      "Microservices",
      "Fault Tolerance"
    ]
  },
  {
    "id": "sd-53",
    "title": "Retry Storms, Exponential Backoff, and Full Jitter",
    "category": "Resilience",
    "difficulty": "Medium",
    "question": "What causes Retry Storms during partial outages? Prove mathematically why adding Jitter to exponential backoff prevents thundering herd spikes.",
    "answer": "Retry Storm Problem:\nWhen a service experiences momentary latency, client timeouts expire. Thousands of clients retry simultaneously at fixed intervals (e.g. every 2s), creating synchronized periodic traffic spikes that overwhelm recovering servers.\n\nExponential Backoff with Full Jitter (AWS Architecture):\n`sleep = random_between(0, min(cap, base * 2 ^ attempt))`\n\nWhy Jitter Works:\nWithout jitter, retrying clients remain synchronized in lockstep. Full jitter scatters retry arrival times uniformly across the time spectrum, flattening traffic spikes and allowing the downstream service to recover gracefully.",
    "keyPoints": [
      "Exponential backoff without jitter synchronizes retries into devastating periodic spikes",
      "Full Jitter flattens retry spikes by uniformly distributing arrival times",
      "Set aggressive maximum retry limits to prevent infinite retry loops",
      "Combine retries with circuit breakers to stop retrying dead services"
    ],
    "tags": [
      "Retry Storm",
      "Jitter",
      "Backoff",
      "Resilience",
      "AWS"
    ]
  },
  {
    "id": "sd-54",
    "title": "Bulkhead Pattern: Thread Pools vs Semaphores",
    "category": "Resilience",
    "difficulty": "Medium",
    "question": "How does the Bulkhead pattern isolate critical failure domains in microservices? Contrast thread pool isolation with semaphore isolation.",
    "answer": "Ship bulkhead analogy: partitions hull so one breach doesn't sink the entire ship.\n\n1. Thread Pool Isolation: Dedicated thread pool per dependency (e.g., Auth gets 20 threads, Search gets 5 threads). If Search slows down, its 5 threads saturate, but Auth continues processing normally without thread exhaustion.\n2. Semaphore Isolation: Uses atomic counters to limit concurrent in-flight requests per dependency without dedicated threads. Lower CPU overhead, but cannot enforce hard execution timeouts.",
    "keyPoints": [
      "Prevents a failing dependency from exhausting all host application threads",
      "Thread pool isolation provides hard isolation and timeout enforcement",
      "Semaphore isolation caps concurrency with lower memory overhead",
      "Essential complement to Circuit Breakers"
    ],
    "tags": [
      "Bulkhead",
      "Resilience",
      "Thread Pool",
      "Architecture Patterns"
    ]
  },
  {
    "id": "sd-55",
    "title": "Load Shedding and Graceful Degradation",
    "category": "Resilience",
    "difficulty": "Medium",
    "question": "How do high-scale services implement Load Shedding to maintain responsiveness when traffic exceeds total system capacity?",
    "answer": "When request volume exceeds maximum capacity, queuing requests causes latency to spiral out of control, resulting in global timeout cascades.\n\nLoad Shedding Mechanisms:\n1. Rejection based on In-Flight Requests / CPU: If CPU > 85% or queue latency > 500ms, immediately drop incoming requests with HTTP 503 Service Unavailable.\n2. Priority-Based Dropping: Tag requests with priority classes:\n   - Critical: Payment checkout, user auth.\n   - Non-Critical: Analytics tracking, recommendation widgets.\n   - Drop non-critical traffic first during overload.\n3. Degradation: Return cached or degraded responses rather than executing expensive DB queries.",
    "keyPoints": [
      "Queuing under overload causes latency death spirals",
      "Load shedding drops excess traffic immediately to keep core service healthy",
      "Prioritize critical user journeys over background analytics",
      "Graceful degradation returns cached or simplified responses"
    ],
    "tags": [
      "Load Shedding",
      "Resilience",
      "Performance",
      "High Availability"
    ]
  },
  {
    "id": "sd-56",
    "title": "Design TinyURL / URL Shortener",
    "category": "High-Level Design",
    "difficulty": "Easy",
    "question": "Design a URL shortening service like TinyURL. Calculate storage capacity and explain Base62 encoding vs MD5 hashing.",
    "answer": "Base62 Encoding (a-z, A-Z, 0-9 = 62 chars):\nA 7-character Base62 string yields `62^7 \u2248 3.5 trillion` unique URLs.\nApproach 1: Distributed ID generator generates unique 64-bit integer, then encode integer to Base62.\nApproach 2: MD5 hash original URL, take first 43 bits, encode to Base62. Handle collisions with salt.\nDatabase: NoSQL Key-Value store (DynamoDB/Cassandra) or PostgreSQL indexed on `short_hash`. Cache top 20% hot URLs in Redis (80-20 Pareto principle).",
    "keyPoints": [
      "Base62 encoding of 7 chars provides 3.5 trillion URLs",
      "Counter/ID-based encoding avoids hash collision handling",
      "Redis caches hot URLs according to 80/20 rule",
      "Read-heavy system (100:1 read to write ratio)"
    ],
    "tags": [
      "TinyURL",
      "Base62",
      "Caching",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-57",
    "title": "Design Twitter / X News Feed (Push vs Pull Hybrid)",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Design the News Feed system for a social media platform. Contrast Fan-Out on Write (Push) and Fan-Out on Read (Pull), and explain the hybrid celebrity solution.",
    "answer": "Fan-Out on Write (Push): When user posts, write tweet_id into every follower's Redis feed list. O(1) read latency. Breaks on celebrities (50M followers).\n\nFan-Out on Read (Pull): Write tweet only to author's timeline. On app open, query all followed timelines and merge in memory. Slow read latency.\n\nHybrid Architecture: Standard users (<20K followers) use Push; celebrity users (>20K followers) use Pull. Dynamic merge occurs in memory when feed is opened.",
    "keyPoints": [
      "Fan-out on write gives O(1) read latency but breaks on celebrity followers",
      "Fan-out on read eliminates write amplification but incurs expensive scatter-gather reads",
      "Hybrid model pushes standard users and dynamically merges celebrity tweets at read time",
      "Evicting inactive users from cache cuts memory footprint dramatically"
    ],
    "tags": [
      "News Feed",
      "Redis",
      "High-Level Design",
      "Scalability"
    ]
  },
  {
    "id": "sd-58",
    "title": "Design WhatsApp / Telegram Real-Time Messaging",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a secure messaging service supporting 1 billion daily active users. Explain WebSocket connection management, session registries, and offline queuing.",
    "answer": "Architecture:\n- Gateway Tier: Fleet of WebSocket/TCP connection servers (Erlang/Elixir or Netty) maintaining millions of concurrent connections.\n- Session Store: Redis cluster maps `user_id -> gateway_server_id`.\n- Message Delivery: If recipient online, route directly to recipient's Gateway server. If offline, store in Cassandra/ScyllaDB offline message table and trigger APNs/FCM push notification.\n- End-to-End Encryption: Signal Protocol Double Ratchet.",
    "keyPoints": [
      "Erlang/Netty connection servers manage millions of persistent WebSockets",
      "Redis session registry maps users to their active gateway nodes",
      "Cassandra/ScyllaDB provides high-write offline message buffering",
      "Signal Protocol Double Ratchet ensures end-to-end encryption"
    ],
    "tags": [
      "WhatsApp",
      "WebSocket",
      "Cassandra",
      "Real-Time",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-59",
    "title": "Design Netflix / YouTube Video Transcoding & Streaming",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a global video streaming platform. Explain video ingestion, chunking, adaptive bitrate streaming (HLS/DASH), and CDN edge caching.",
    "answer": "Architecture:\n1. Transcoding Pipeline: Raw video uploaded to S3. Distributed workers (FFmpeg) slice video into 2-10 second chunks, transcoding into multiple resolutions (480p, 720p, 1080p, 4K) and codecs (H.264, AV1). Master playlist manifests (`.m3u8` / `.mpd`) generated.\n2. Adaptive Bitrate Streaming (ABR): Client video player monitors network bandwidth and dynamically requests higher or lower resolution chunks from manifest.\n3. CDN: Video chunks cached at ISP-edge CDN nodes (Akamai, Cloudflare, Netflix Open Connect).",
    "keyPoints": [
      "Slices videos into small chunks across multiple bitrates and resolutions",
      "Adaptive Bitrate Streaming (HLS/DASH) adjusts video quality on the fly",
      "Manifest files coordinate chunk sequencing for client video players",
      "ISP-embedded CDN edge caching delivers video at minimal latency"
    ],
    "tags": [
      "Video Streaming",
      "CDN",
      "HLS",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-60",
    "title": "Design Uber / Lyft Geolocation & Ride Matching",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a ride-hailing geolocation platform. How do you store and query millions of moving driver locations every 4 seconds? Compare Geohash and Uber H3.",
    "answer": "Scale: 1M active drivers sending GPS `(lat, lon)` every 4 seconds = 250K writes/sec.\nSpatial Indexing: Uber H3 hexagonal hierarchical spatial index. Hexagons have equal distance to all 6 neighbors (unlike squares).\nArchitecture:\n- Driver Location Service: Receives GPS pings -> writes to Redis Cluster (stores `H3_index -> set of driver_ids`). Key expires after 15s.\n- Dispatcher Service: Computes rider H3 index, queries ring 0 and ring 1 neighboring hexagons in Redis in O(1) time.\n- Kafka streams driver positions for ETA calculation and surge pricing.",
    "keyPoints": [
      "Uber H3 hexagonal indexing ensures uniform distance to all 6 adjacent neighbors",
      "Driver location pings stored in Redis with short TTL to handle ephemeral disconnects",
      "Decouples location tracking (high write) from ride matching/dispatching",
      "Ring expansions around hexagonal cell easily locate closest drivers"
    ],
    "tags": [
      "Uber",
      "Geolocation",
      "H3",
      "Redis",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-61",
    "title": "Design a Global Unique ID Generator (Snowflake ID)",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Design a distributed unique ID generator generating 100K+ IDs/sec: 64-bit integers, roughly time-sorted, resilient to single points of failure.",
    "answer": "Twitter Snowflake 64-bit ID:\n- 1 bit: Unused sign bit (0).\n- 41 bits: Millisecond Timestamp (69 years of lifespan relative to custom epoch).\n- 10 bits: Machine / Worker ID (1,024 generator nodes).\n- 12 bits: Sequence Number (4,096 unique IDs per ms per node).\nTotal capacity: 4.19M IDs/sec across 1,024 nodes.\nClock Drift Handling: Spin-wait if drift < 5ms; reject requests or re-allocate worker ID if drift is large.",
    "keyPoints": [
      "64-bit Snowflake fits into SQL BIGINT for optimal B-Tree index locality",
      "41-bit timestamp provides 69 years of monotonically increasing IDs",
      "10-bit worker ID supports 1,024 independent server instances",
      "Clock drift mitigation is essential when relying on physical system clocks"
    ],
    "tags": [
      "Snowflake ID",
      "Distributed Systems",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-62",
    "title": "Design Stripe / PayPal Payment Gateway & Ledger",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a fault-tolerant payment gateway and immutable financial ledger. Detail idempotency keys, double-entry bookkeeping, and settlement reconciliation.",
    "answer": "Core Tenets:\n1. Idempotency Keys: Client sends UUID in header. Redis distributed lock `SET payment:{key} PROCESSING NX EX 120` prevents double charges.\n2. Double-Entry Bookkeeping Ledger: Money is never created or destroyed. Every transaction has at least one Debit and one Credit: `SUM(Debits) == SUM(Credits)`. Immutable append-only ledger.\n3. Two-Phase Settlement: Authorize (card hold) followed by Capture (settlement).\n4. Reconciliation: Daily batch ETL compares ledger with bank statement clearing files (MT940/CAMT.053).",
    "keyPoints": [
      "Idempotency keys prevent duplicate payments across client retries",
      "Double-entry bookkeeping guarantees total debits equal total credits",
      "Immutable append-only ledger records audit trails without destructive updates",
      "Daily reconciliation pipelines identify and flag settlement discrepancies"
    ],
    "tags": [
      "FinTech",
      "Payments",
      "Idempotency",
      "Ledger",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-63",
    "title": "Design Multi-Brand EV Charging & Session Management (Elli / VW Charging)",
    "category": "Domain Architecture",
    "difficulty": "Hard",
    "question": "Design a high-scale EV Charging Platform supporting B2C, B2B, and Fleet offerings. Address OCPP protocol, Auth0 IAM, real-time metering, and offline failover.",
    "answer": "System Architecture:\n1. Ingress & OCPP: Physical chargers communicate via OCPP over secure WebSockets (WSS). OCPP Gateway cluster terminates WebSockets and translates to Kafka events (`session.started`, `meter.value`, `session.stopped`).\n2. IAM & Authorization: Auth0 IAM manages B2C, B2B, and fleet policies. ABAC engine checks driver charging entitlement, company budget, and roaming contracts (Hubject). Fast-path Redis auth cache answers in <15ms.\n3. Real-Time Metering: Kafka Streams / Flink aggregates kWh consumed and checks max-spending caps.\n4. Offline Failover: Chargers fall back to local whitelist cache of authorized RFID hashes if cloud connectivity drops.",
    "keyPoints": [
      "OCPP gateway terminates long-lived WebSockets and bridges to Kafka",
      "ISO 15118 Plug&Charge automates vehicle TLS mutual authentication",
      "Fast-path authorization caching guarantees sub-20ms station response",
      "Offline whitelist cache prevents vehicle stranding during cloud outages"
    ],
    "tags": [
      "EV Charging",
      "OCPP",
      "IoT",
      "Auth0",
      "Kafka",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-64",
    "title": "Design Financial KYC Rules Engine & Verification (Deutsche Bank BizBanking)",
    "category": "Domain Architecture",
    "difficulty": "Hard",
    "question": "Design an automated KYC validation rules engine for digital banking SME clients across multiple brands. Address complex rule DAGs, audit trails, and BigQuery data pipelines.",
    "answer": "1. API Gateway & Identity: Microservices authenticate corporate clients via OAuth2/OIDC. IDNow/WebID integrations for video KYC and passport NFC validation.\n2. Rules Engine: Evaluates DAG of verification rules (sanction lists, beneficial owners >25% share capital, AML scoring matrix). Stateless rule execution on Kubernetes.\n3. Data Pipeline: Kafka streams KYC events. BigQuery data warehouse ingests daily corporate registry deltas; Python ETL jobs update risk ratings and synchronize to operational PostgreSQL via CloudSQL.\n4. Compliance: WORM storage / GCP Cloud Storage bucket locks store tamper-evident audit logs satisfying BaFin/ECB regulations.",
    "keyPoints": [
      "Decouples business rules engine from external ID verification vendors",
      "Automated DAG evaluation speeds up SME onboarding from days to minutes",
      "BigQuery-to-PostgreSQL pipeline balances analytic scale with low-latency OLTP",
      "WORM storage provides legally binding audit trails for regulatory compliance"
    ],
    "tags": [
      "KYC",
      "FinTech",
      "Banking",
      "Rules Engine",
      "BigQuery",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-65",
    "title": "Design Distributed Job Scheduler / Distributed Cron",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a Distributed Job Scheduler executing millions of tasks with arbitrary delays and cron expressions. Ensure fault tolerance and exactly-once execution.",
    "answer": "Architecture:\n1. Storage: Tasks stored in Redis Sorted Set (ZSET) where score is `execute_at` timestamp, or PostgreSQL indexed on `execute_at`.\n2. Coordinator: Active leader elected via Raft/etcd queries due tasks (`ZREVRANGEBYSCORE now -inf LIMIT 1000`) and pushes to Kafka execution queues.\n3. Worker Fleet: Stateless workers pull from queue, acquire lock on task via optimistic concurrency (`UPDATE tasks SET state='RUNNING' WHERE task_id=:id AND state='SCHEDULED'`), execute payload, and report completion.\n4. Cron Recurring Jobs: On completion, coordinator calculates `next_execution_time` using cron expression and schedules next instance.",
    "keyPoints": [
      "Time-bucketed index (Redis ZSET or SQL execute_at index) for efficient polling",
      "Decouple scheduling (coordinator) from execution (worker pool) via message queue",
      "Optimistic locking on task state prevents duplicate execution",
      "Worker heartbeats detect node crashes and trigger automated task recovery"
    ],
    "tags": [
      "Job Scheduler",
      "Distributed Systems",
      "Cron",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-66",
    "title": "Design Web Crawler (Frontier, Politeness, and Bloom Filters)",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a distributed web crawler indexing 1 billion web pages. Detail URL frontier queues, politeness policies, Bloom filters, and robots.txt compliance.",
    "answer": "Architecture:\n1. URL Frontier: Two-tier queues: Priority Queues (rank URLs by PageRank) and Politeness Queues (one queue per domain, enforcing 1-sec delay between requests).\n2. Duplicate Elimination: Bloom filters test seen URLs in memory in O(1) with 0% false negatives. SimHash content fingerprinting detects near-duplicate HTML pages.\n3. Fetcher & Parser: Worker pool downloads HTML respecting cached `robots.txt`, parses DOM, extracts new links, and feeds back to Frontier.\n4. Storage: Compressed raw HTML in distributed object store (S3/GFS); link graph in Bigtable/Cassandra.",
    "keyPoints": [
      "Two-tier frontier separates URL priority from domain politeness constraints",
      "Bloom filters check seen URLs in memory with minimal RAM footprint",
      "SimHash detects near-duplicate content across different URLs",
      "Cached robots.txt parser ensures legal and ethical crawling"
    ],
    "tags": [
      "Web Crawler",
      "Bloom Filter",
      "Queues",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-67",
    "title": "Design a Distributed Key-Value Store (Amazon Dynamo Paper)",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Walk through the architectural principles of Amazon Dynamo: Consistent Hashing, Vector Clocks, Sloppy Quorums, Hinted Handoff, and Merkle Trees.",
    "answer": "Dynamo Principles:\n1. Consistent Hashing with virtual nodes distributes keys across storage ring.\n2. Tunable Quorum (N, R, W): `R + W > N` guarantees overlapping read/write sets.\n3. Sloppy Quorum & Hinted Handoff: Healthy alternate nodes accept writes during partitions; deliver to original node on recovery.\n4. Vector Clocks: Detect concurrent conflicting updates without centralized master clock.\n5. Merkle Trees: Hierarchical hash trees compare replica data ranges, transferring only divergent keys during background anti-entropy sync.",
    "keyPoints": [
      "Tunable quorums: R + W > N guarantees overlapping read and write sets",
      "Sloppy quorum with hinted handoff guarantees write availability during network splits",
      "Vector clocks capture causal history and detect concurrent write conflicts",
      "Merkle trees minimize network overhead during background replica synchronization"
    ],
    "tags": [
      "Dynamo",
      "Distributed Systems",
      "NoSQL",
      "Key-Value Store"
    ]
  },
  {
    "id": "sd-68",
    "title": "Design Search Autocomplete System (Typeahead)",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Design a real-time search autocomplete system returning top 5 suggestions within 50ms as users type.",
    "answer": "Architecture:\n1. In-Memory Trie: Each node stores top 5 most frequent search queries for that prefix.\n2. Ingestion & Aggregation: Search query logs stream via Kafka. Spark/Flink micro-batches aggregate query frequencies hourly and rebuild Trie snapshots.\n3. Serving Tier: Trie served from memory or Redis. Browser client debounces keystrokes (wait 150ms) and caches prefix queries locally.",
    "keyPoints": [
      "Trie nodes store precomputed top-K results to avoid runtime tree traversal",
      "Client-side keystroke debouncing reduces API request volume by 70%",
      "Offline analytics pipeline updates search query frequency rankings",
      "Sub-50ms latency SLA achieved through in-memory lookups"
    ],
    "tags": [
      "Typeahead",
      "Trie",
      "Autocomplete",
      "Redis",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-69",
    "title": "Design an API Gateway with ABAC/RBAC and Rate Limiting",
    "category": "Architecture Patterns",
    "difficulty": "Medium",
    "question": "Explain the architecture of an Enterprise API Gateway. How does it handle SSL termination, token validation, dynamic routing, and ABAC policy enforcement?",
    "answer": "Functions:\n1. SSL/TLS Termination: Offloads crypto from microservices.\n2. JWT Validation: Validates incoming Bearer tokens using locally cached public keys (JWKS) without calling IdP on every request.\n3. Authorization (ABAC/RBAC): Extracts claims, user roles; queries Open Policy Agent (OPA) or local policy cache.\n4. Rate Limiting: Enforces quotas using Redis Token Bucket.\n5. Injects `X-Correlation-ID` header into downstream gRPC/HTTP calls for distributed tracing.",
    "keyPoints": [
      "Single entry point decouples cross-cutting concerns from business services",
      "JWKS local caching validates JWT signatures without network round-trips",
      "Open Policy Agent (OPA) evaluates fine-grained ABAC policies",
      "Distributed correlation IDs provide end-to-end distributed tracing"
    ],
    "tags": [
      "API Gateway",
      "OAuth2",
      "Security",
      "Envoy",
      "Microservices"
    ]
  },
  {
    "id": "sd-70",
    "title": "Design a Metrics and Alerting Monitoring System (Datadog/Prometheus)",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a distributed time-series metrics collection and alerting pipeline processing 10 million data points per second.",
    "answer": "Architecture:\n1. Collection: Push (StatsD) or Pull (Prometheus scraping `/metrics`).\n2. Streaming Buffer: Kafka buffers time-series points `(metric, labels, timestamp, value)`.\n3. Time-Series DB (TSDB): Gorilla TSDB / ClickHouse architecture with delta-of-delta timestamp compression and XOR float compression (12x storage reduction).\n4. Alerting Engine: Rule evaluation engine runs PromQL queries every 15-60s, deduplicating alerts and routing to PagerDuty/Slack via Alertmanager.",
    "keyPoints": [
      "Gorilla TSDB XOR floating-point and delta-of-delta compression achieves 12x data reduction",
      "Kafka buffers high-throughput metric ingestion spikes",
      "Time-series labels enable multi-dimensional aggregation",
      "Dedicated alert evaluation engine decouples query serving from monitoring"
    ],
    "tags": [
      "Time Series",
      "Prometheus",
      "Datadog",
      "Monitoring",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-71",
    "title": "Design Real-Time Trade Confirmation & Messaging Engine (Barclays DeltaOne)",
    "category": "Domain Architecture",
    "difficulty": "Hard",
    "question": "Design a high-frequency trade confirmation messaging module integrating with MarkitWire and TradeStore. Ensure zero message loss, ultra-low latency, and regulatory compliance.",
    "answer": "1. Ingress & FIX Protocol: Financial Information eXchange (FIX) protocol gateway receives trade fills from matching engine with sub-millisecond latencies.\n2. Messaging Pipeline: Ultra-reliable Kafka or Aeron messaging cluster. Messages mirrored across redundant standby brokers.\n3. Trade Enrichment & MarkitWire Integration: Enriches trade with counterparty legal entity identifiers (LEI), margin loan terms (BCML Margin Loan), and dispatches electronic trade confirmation via MarkitWire API.\n4. TradeStore Persistence: Stores immutable trade state in partitioned relational/columnar store for regulatory compliance (EMIR, Dodd-Frank, MiFID II).",
    "keyPoints": [
      "FIX protocol gateway processes low-latency trade executions",
      "Aeron / Kafka messaging ensures zero message loss under high volume",
      "MarkitWire integration coordinates automated OTC derivative confirmations",
      "Regulatory reporting pipelines satisfy EMIR and Dodd-Frank trade repository mandates"
    ],
    "tags": [
      "FinTech",
      "Trading",
      "Barclays",
      "Messaging",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-72",
    "title": "Design Stock Brokerage / Order Book Matching Engine",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a high-throughput, low-latency Limit Order Book (LOB) matching engine. Explain price-time priority (FIFO), memory data structures, and market data multicasting.",
    "answer": "Data Structures in Memory:\n- Order Book: Double-ended priority structure:\n  - Bids (Buy orders): Ordered descending by price.\n  - Asks (Sell orders): Ordered ascending by price.\n- Implemented using B-Tree / Red-Black Tree for price levels + Doubly Linked List for orders at the same price level (Price-Time Priority FIFO).\nExecution:\n- When matching limit/market order arrives: match against top of opposing book.\n- Single-threaded core execution pinned to isolated CPU core (avoids locking/context switching).\n- Sequenced via memory-mapped ring buffer (LMAX Disruptor).\n- Market data broadcast to subscribers via UDP Multicast.",
    "keyPoints": [
      "Red-Black Tree of price levels combined with doubly linked list FIFO queues",
      "Single-threaded matching loop pinned to isolated CPU core maximizes cache locality",
      "LMAX Disruptor lock-free ring buffer sequences incoming orders",
      "UDP Multicast broadcasts real-time ticker feeds to market participants"
    ],
    "tags": [
      "Order Book",
      "Trading",
      "Disruptor",
      "Low Latency",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-73",
    "title": "Design an E-Commerce Flash Sale System (High Concurrency & Overselling Prevention)",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a flash sale inventory reservation system handling 500,000 requests/second with strictly zero overselling. Detail Redis Lua scripts, token buckets, and delayed queue cancellations.",
    "answer": "Architecture:\n1. Edge Shielding: CDN serves static product page. API Gateway throttles bot traffic using WAF and CAPTCHA.\n2. In-Memory Inventory Reservation (Redis):\n- Pre-load stock into Redis: `stock:item_123 = 1000`.\n- Atomic Redis Lua script checks and decrements: `if redis.call('get', KEYS[1]) > 0 then return redis.call('decr', KEYS[1]) else return -1 end`.\n- Only successful decrements proceed to DB order creation!\n3. Asynchronous Order Creation:\n- Successful requests queued in Kafka. Workers create order records in PostgreSQL.\n4. Delayed Payment Timeout: Delayed queue checks payment status after 15 mins. If unpaid, cancels order and increments Redis stock atomically.",
    "keyPoints": [
      "Redis Lua script atomically checks and decrements inventory in memory",
      "Shields relational database from 99.9% of flash sale requests",
      "Asynchronous order creation via Kafka absorbs write pressure",
      "Delayed message queues automatically restock unpurchased expired orders"
    ],
    "tags": [
      "Flash Sale",
      "Redis",
      "Inventory",
      "Concurrency",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-74",
    "title": "Design Collaborative Document Editing (OT vs CRDT)",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Compare Operational Transformation (Google Docs) and Conflict-Free Replicated Data Types (CRDTs - Figma, Apple Notes) for real-time collaborative text editing.",
    "answer": "OT (Operational Transformation):\n- Centralized server transforms concurrent insert/delete operations so intentions are preserved.\n- Requires central server to sequence total order of operations. (Google Docs).\n\nCRDT (Conflict-Free Replicated Data Types):\n- Mathematically sound data structures that merge concurrently across peer-to-peer or decentralized nodes without central server.\n- Operations are commutative and idempotent. (Figma, Apple Notes, Yjs).",
    "keyPoints": [
      "OT requires a centralized server to sequence and transform operations",
      "CRDTs achieve peer-to-peer convergence mathematically without central server",
      "CRDTs have higher memory overhead per character to store metadata",
      "State-based vs Operation-based CRDT variants"
    ],
    "tags": [
      "CRDT",
      "Operational Transformation",
      "Collaborative Editing",
      "Distributed Systems"
    ]
  },
  {
    "id": "sd-75",
    "title": "Design Distributed File Storage System (GFS / HDFS)",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Explain the architecture of Google File System (GFS) and HDFS. Detail chunk size decisions, master metadata management, and heartbeats.",
    "answer": "Architecture:\n1. Chunk Size: Large chunks (64MB - 128MB). Reduces metadata size, allowing master to keep all block mappings in RAM.\n2. Master / NameNode: Single master maintains file namespace, file-to-chunk mappings, and chunk locations in memory. WAL + checkpoints ensure persistence.\n3. ChunkServers / DataNodes: Store chunks as raw files on Linux filesystems. Default replication factor 3 across distinct server racks. Heartbeats report block health.",
    "keyPoints": [
      "Large 64MB-128MB chunk size minimizes master metadata memory footprint",
      "Master node holds entire filesystem metadata in RAM for speed",
      "Triplicate chunk replication across distinct server racks guarantees durability",
      "Decouples control plane (metadata) from data plane (direct client-to-datanode streaming)"
    ],
    "tags": [
      "GFS",
      "HDFS",
      "Distributed Storage",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-76",
    "title": "Design Notification Service (Push, SMS, Email)",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Design a scalable multi-channel notification service supporting APNs, FCM, SMS (Twilio), and Email (SendGrid). Address priority, templating, and user rate limiting.",
    "answer": "Architecture: Client services call Notification API. Kafka queues partition traffic by channel and priority. Workers render templates, check user frequency caps and opt-out preferences in Redis, and call external vendor APIs with circuit breakers.",
    "keyPoints": [
      "Multi-channel routing partitioned across dedicated Kafka topics",
      "Redis enforces per-user notification frequency caps",
      "Vendor integrations protected by Circuit Breakers and retries",
      "Template rendering engine decoupled from transport workers"
    ],
    "tags": [
      "Notification",
      "Kafka",
      "Microservices",
      "Design"
    ]
  },
  {
    "id": "sd-77",
    "title": "Design Distributed Log Search Engine (Elasticsearch / OpenSearch)",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a distributed log indexing and search engine. Detail Lucene inverted indexes, segment immutability, and cluster shard rebalancing.",
    "answer": "Logs ingested via Logstash/FluentBit -> Kafka -> OpenSearch indexing workers. Inverted index maps terms to posting lists of document IDs. Segments are immutable on disk; background merge threads consolidate segments. Shards distributed across primary and replica nodes.",
    "keyPoints": [
      "Inverted index maps words to posting lists of document IDs",
      "Immutable segments eliminate write lock contention on disk",
      "Kafka acts as shock absorber for log spikes",
      "Time-based indices (e.g. logs-2026-11-15) enable cheap data deletion"
    ],
    "tags": [
      "Elasticsearch",
      "OpenSearch",
      "Logging",
      "Search",
      "Distributed Systems"
    ]
  },
  {
    "id": "sd-78",
    "title": "Design Real-Time Leaderboard System (Gaming)",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Design a real-time gaming leaderboard capable of ranking 10 million players with instant rank lookups.",
    "answer": "Use Redis Sorted Sets (ZSET). `ZADD leaderboard score user_id` updates score in O(log N). `ZREVRANK leaderboard user_id` returns global rank in O(log N). `ZREVRANGE leaderboard 0 9 WITHSCORES` returns top 10 players. For multi-million users, partition by score ranges or shard by game tier.",
    "keyPoints": [
      "Redis Sorted Sets (SkipList + Hash Table) power O(log N) rank operations",
      "ZREVRANK returns player's global ranking instantly",
      "ZREVRANGE returns top-N leaderboard slice",
      "Score tier partitioning distributes load across multiple Redis instances"
    ],
    "tags": [
      "Leaderboard",
      "Redis",
      "Gaming",
      "Sorted Sets"
    ]
  },
  {
    "id": "sd-79",
    "title": "Design Pastebin Service",
    "category": "High-Level Design",
    "difficulty": "Easy",
    "question": "Design a text-sharing Pastebin service with custom URLs and expiration TTLs.",
    "answer": "Compute Base62 short key from ID generator. Store text content in Object Storage (S3) or MongoDB; store metadata (key, user_id, created_at, expires_at) in PostgreSQL. Expired pastes cleaned up by background worker or Redis TTL. Hot pastes cached in Redis.",
    "keyPoints": [
      "Base62 short URL mapping",
      "Decouples text content storage (S3) from metadata (SQL)",
      "TTL expiration managed via database index or Redis key expiry",
      "Read-heavy caching strategy"
    ],
    "tags": [
      "Pastebin",
      "High-Level Design",
      "S3",
      "Redis"
    ]
  },
  {
    "id": "sd-80",
    "title": "Design Parking Garage Management System (Low-Level Design / OOP)",
    "category": "Low-Level Design",
    "difficulty": "Medium",
    "question": "Design an object-oriented Parking Garage system. Detail class hierarchies, spot allocation strategies (Compact, Large, EV, Motorcycle), and ticket payment processing.",
    "answer": "Classes: `ParkingLot`, `Level`, `ParkingSpot` (abstract: `CompactSpot`, `LargeSpot`, `EVSpot`), `Vehicle` (abstract: `Car`, `Truck`, `Van`, `Motorcycle`), `Ticket`, `PaymentPortal`. Factory pattern for spot allocation; Strategy pattern for dynamic pricing tariffs based on duration and vehicle type.",
    "keyPoints": [
      "Clean OOP inheritance for vehicles and parking spots",
      "Factory pattern instantiates appropriate spot types",
      "Strategy pattern calculates flexible parking fee tariffs",
      "Thread-safe concurrent spot allocation using atomic locks"
    ],
    "tags": [
      "LLD",
      "OOP",
      "Design Patterns",
      "Parking Lot"
    ]
  },
  {
    "id": "sd-81",
    "title": "Design Elevator Controller System (Low-Level Design / OOP)",
    "category": "Low-Level Design",
    "difficulty": "Medium",
    "question": "Design an Elevator Controller system managing multiple elevator cars across a 50-story building. Explain SCAN (Elevator Algorithm) dispatching.",
    "answer": "Classes: `ElevatorController`, `ElevatorCar`, `Button`, `Request`, `Door`. State machine: `MOVING_UP`, `MOVING_DOWN`, `IDLE`. Algorithm: SCAN algorithm (elevator continues in current direction serving all requests until none remain, then reverses). Strategy pattern for dispatching nearest car.",
    "keyPoints": [
      "State machine models elevator states: IDLE, UP, DOWN",
      "SCAN algorithm minimizes passenger wait times and motor reversals",
      "Strategy pattern determines car dispatching priority",
      "Thread-safe concurrent request queue handling"
    ],
    "tags": [
      "LLD",
      "OOP",
      "Elevator",
      "State Machine",
      "Algorithms"
    ]
  },
  {
    "id": "sd-82",
    "title": "Design Cloud Object Storage Metadata Store at Scale",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "How do you store and index metadata for trillions of objects in a cloud storage platform like S3?",
    "answer": "Store metadata in a distributed partitioned database (Spanner / CockroachDB / Bigtable). Shard keys are bucket name + hashed prefix to prevent hotspotting on sequential timestamps. Prefix searches supported via lexicographical LSM-Tree key ordering.",
    "keyPoints": [
      "Trillions of objects require partitioned distributed NoSQL or Spanner",
      "Key prefix hashing prevents write hotspots on sequential dates",
      "LSM-Tree lexicographical sorting enables fast bucket listing",
      "Decouples object payload storage from metadata querying"
    ],
    "tags": [
      "S3",
      "Metadata",
      "Distributed Systems",
      "Spanner"
    ]
  },
  {
    "id": "sd-83",
    "title": "Design Hotel / Airline Reservation System (Distributed Locking)",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design an airline seat or hotel room reservation system. How do you prevent double-booking during checkout holds?",
    "answer": "Reservation lifecycle: `AVAILABLE -> HELD -> RESERVED -> BOOKED`. When user selects seat, set state to `HELD` with 10-minute TTL in Redis with distributed lock. If payment succeeds, transition to `BOOKED` in PostgreSQL in an ACID transaction. If TTL expires, background job releases hold back to `AVAILABLE`.",
    "keyPoints": [
      "Temporary hold state with TTL prevents double-booking during checkout",
      "Optimistic locking on database records prevents concurrent over-allocation",
      "Delayed queue or Redis key expiry releases abandoned seat holds",
      "ACID transaction finalizes financial settlement and ticket generation"
    ],
    "tags": [
      "Reservation",
      "Distributed Lock",
      "ACID",
      "Postgres",
      "Redis"
    ]
  },
  {
    "id": "sd-84",
    "title": "Design Geofencing Service",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Design a scalable geofencing service that alerts users when entering or exiting predefined geographic zones.",
    "answer": "Zones modeled as spatial polygons indexed in PostgreSQL/PostGIS using R-Trees or Uber H3. Client locations streamed via Kafka. Geofencing engine checks point-in-polygon queries against spatial index. State transitions (`INSIDE`, `OUTSIDE`) tracked in Redis to trigger enter/exit push alerts.",
    "keyPoints": [
      "PostGIS R-Tree spatial index enables fast point-in-polygon queries",
      "Uber H3 maps geofence polygons to hexagonal cell sets",
      "Redis tracks previous user location state to trigger ENTER and EXIT events",
      "Kafka buffers continuous high-frequency location streams"
    ],
    "tags": [
      "Geofencing",
      "PostGIS",
      "H3",
      "Spatial",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-85",
    "title": "Design Digital Asset Management (DAM) System",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Design an enterprise Digital Asset Management system handling terabytes of high-resolution images, videos, and PDFs with automated tagging.",
    "answer": "Ingestion to S3. Asynchronous event triggers Lambda / worker to extract EXIF metadata, generate thumbnail resolutions, and invoke ML models (CLIP / Vision) for automatic tagging. Metadata indexed in OpenSearch for faceted search.",
    "keyPoints": [
      "Decouples asset upload from asynchronous processing pipeline",
      "Object storage S3 stores original and generated thumbnail resolutions",
      "OpenSearch provides faceted search across tags and EXIF metadata",
      "Presigned URLs grant secure direct client upload and download access"
    ],
    "tags": [
      "DAM",
      "S3",
      "OpenSearch",
      "Microservices"
    ]
  },
  {
    "id": "sd-86",
    "title": "Design a High-Throughput Fraud Detection Pipeline",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design a real-time fraud detection pipeline analyzing card transactions within 100 milliseconds.",
    "answer": "Transaction passes from payment gateway to Kafka. Apache Flink processes sliding window aggregations (e.g. 3 transactions within 60 seconds across distinct countries). Feature Store (Redis/Feast) loads historical user profile. ML scoring model outputs fraud probability. If score > 0.85, reject transaction.",
    "keyPoints": [
      "Sub-100ms SLA requires in-memory streaming analytics with Apache Flink",
      "Feature store in Redis delivers sub-5ms user behavioral features",
      "Sliding window stateful aggregations detect velocity anomalies",
      "Machine learning inference pipeline scores risk in real time"
    ],
    "tags": [
      "Fraud Detection",
      "Flink",
      "Kafka",
      "Redis",
      "Machine Learning"
    ]
  },
  {
    "id": "sd-87",
    "title": "Design Content Recommendation Engine Pipeline",
    "category": "High-Level Design",
    "difficulty": "Hard",
    "question": "Design the system architecture for a video or article recommendation engine (candidate generation, ranking, and serving).",
    "answer": "Two-stage pipeline: 1. Candidate Generation (Retrieval): Two-Tower neural network / Approximate Nearest Neighbors (ANN with HNSW in Milvus/Pinecone) retrieves 500 candidate items from 10M library in 10ms. 2. Heavy Ranking: Deep ranking model scores 500 items against user features. 3. Re-ranking: Deduplication and diversity filtering.",
    "keyPoints": [
      "Two-stage recommendation: fast candidate retrieval followed by heavy ranking",
      "Vector database (HNSW) retrieves top 500 candidates from millions in 10ms",
      "Heavy neural ranker scores candidates using real-time user context",
      "Business logic layer applies diversity and deduplication filters"
    ],
    "tags": [
      "Recommendation",
      "Vector DB",
      "Machine Learning",
      "System Design"
    ]
  },
  {
    "id": "sd-88",
    "title": "Design Live Sports Score Broadcasting Platform",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Design a live sports score platform delivering real-time play-by-play updates to 5 million concurrent users with minimal latency.",
    "answer": "Scorekeepers update match events via internal admin API. Events published to Kafka. Distributed WebSocket clusters broadcast updates to connected clients using Redis Pub/Sub. Static match snapshots cached on CDN edge with 2-second micro-caching to offload read surges.",
    "keyPoints": [
      "Micro-caching on CDN edge (2-sec TTL) absorbs 95% of read surges during peak goals",
      "Redis Pub/Sub broadcasts score updates across WebSocket server clusters",
      "Lightweight JSON/binary payloads minimize egress bandwidth",
      "Long-lived WebSockets ensure sub-500ms score delivery to fans"
    ],
    "tags": [
      "Sports",
      "WebSocket",
      "CDN",
      "Redis",
      "High-Level Design"
    ]
  },
  {
    "id": "sd-89",
    "title": "Design Multi-Tenant SaaS Isolation Architecture (Silo vs Pool)",
    "category": "Architecture Patterns",
    "difficulty": "Medium",
    "question": "Compare Silo, Pool, and Hybrid multi-tenant architectures for SaaS platforms across data, compute, and tenant isolation.",
    "answer": "Silo: Dedicated database and compute per tenant. Maximum security and regulatory compliance; highest infrastructure cost. Pool: Shared database and compute across all tenants with `tenant_id` column partitioning (PostgreSQL Row-Level Security RLS). Lowest cost; risk of noisy neighbor. Hybrid: Shared compute, separate database schemas.",
    "keyPoints": [
      "Silo model provides absolute tenant data isolation for enterprise compliance",
      "Pool model maximizes resource utilization and minimizes operating cost",
      "PostgreSQL Row-Level Security (RLS) enforces tenant boundaries in pooled DBs",
      "Noisy neighbor mitigation requires tenant-level rate limiting"
    ],
    "tags": [
      "Multi-Tenancy",
      "SaaS",
      "PostgreSQL",
      "Architecture",
      "Security"
    ]
  },
  {
    "id": "sd-90",
    "title": "Design Micro-Frontend Architecture",
    "category": "Architecture Patterns",
    "difficulty": "Medium",
    "question": "Explain Micro-Frontend architectures (Module Federation, iframe, Web Components). How do distributed teams deploy independent frontend modules?",
    "answer": "Decomposes monolithic frontend into independently deployable micro-apps. Webpack 5 Module Federation allows a shell host application to dynamically load remote JavaScript bundles at runtime. Shared state managed via custom events or lightweight pub/sub; CSS isolated via CSS Modules or Shadow DOM.",
    "keyPoints": [
      "Webpack Module Federation loads independent frontend bundles dynamically",
      "Enables autonomous team deployment cycles without full site rebuilds",
      "Shared dependencies (React, design system) are deduplicated at runtime",
      "Shadow DOM or scoped CSS prevents cross-module styling collisions"
    ],
    "tags": [
      "Micro-Frontend",
      "Module Federation",
      "Architecture",
      "Frontend"
    ]
  },
  {
    "id": "sd-91",
    "title": "Design Distributed Configuration Management (Consul / Spring Cloud Config)",
    "category": "Distributed Systems",
    "difficulty": "Medium",
    "question": "Design a distributed configuration management service capable of dynamically pushing configuration changes to thousands of microservice instances without restarting pods.",
    "answer": "Central configuration store backed by Git / HashiCorp Consul / etcd. Microservice clients establish long-poll HTTP or gRPC watch streams. When config changes in Consul, watch triggers and pushes new configuration to client listeners, updating in-memory configuration beans dynamically.",
    "keyPoints": [
      "Centralized single source of truth for microservice configurations",
      "Long polling or gRPC watch streams notify instances of changes instantly",
      "Dynamic bean reloading updates configurations without pod restarts",
      "Role-based access control and secret encryption protect sensitive keys"
    ],
    "tags": [
      "Configuration",
      "Consul",
      "etcd",
      "Microservices"
    ]
  },
  {
    "id": "sd-92",
    "title": "Design Distributed Distributed Lock Manager (Chubby / ZooKeeper)",
    "category": "Distributed Systems",
    "difficulty": "Hard",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Distributed Distributed Lock Manager (Chubby / ZooKeeper). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Distributed Distributed Lock Manager (Chubby / ZooKeeper):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Distributed Distributed Lock Manager (Chubby / ZooKeeper)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Distributed Systems",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-93",
    "title": "Design Real-Time Polling & Voting System (High Concurrency)",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Real-Time Polling & Voting System (High Concurrency). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Real-Time Polling & Voting System (High Concurrency):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Real-Time Polling & Voting System (High Concurrency)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "High-Level Design",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-94",
    "title": "Design Distributed Tracing Platform (OpenTelemetry / Jaeger)",
    "category": "Observability",
    "difficulty": "Hard",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Distributed Tracing Platform (OpenTelemetry / Jaeger). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Distributed Tracing Platform (OpenTelemetry / Jaeger):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Distributed Tracing Platform (OpenTelemetry / Jaeger)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Observability",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-95",
    "title": "Design Log Aggregation Pipeline (ELK / EFK Stack)",
    "category": "Observability",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Log Aggregation Pipeline (ELK / EFK Stack). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Log Aggregation Pipeline (ELK / EFK Stack):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Log Aggregation Pipeline (ELK / EFK Stack)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Observability",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-96",
    "title": "Design Distributed Cache Invalidation System",
    "category": "Caching",
    "difficulty": "Hard",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Distributed Cache Invalidation System. Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Distributed Cache Invalidation System:\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Distributed Cache Invalidation System",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Caching",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-97",
    "title": "Design API Rate Limiter with Leaky Bucket",
    "category": "Resilience",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design API Rate Limiter with Leaky Bucket. Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design API Rate Limiter with Leaky Bucket:\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design API Rate Limiter with Leaky Bucket",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Resilience",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-98",
    "title": "Design Vending Machine Controller (LLD)",
    "category": "Low-Level Design",
    "difficulty": "Easy",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Vending Machine Controller (LLD). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Vending Machine Controller (LLD):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Vending Machine Controller (LLD)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Low-Level Design",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-99",
    "title": "Design Parking Lot System with Concurrency (LLD)",
    "category": "Low-Level Design",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Parking Lot System with Concurrency (LLD). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Parking Lot System with Concurrency (LLD):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Parking Lot System with Concurrency (LLD)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Low-Level Design",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-100",
    "title": "Design Chess Game (LLD / OOP)",
    "category": "Low-Level Design",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Chess Game (LLD / OOP). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Chess Game (LLD / OOP):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Chess Game (LLD / OOP)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Low-Level Design",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-101",
    "title": "Design Blackjack / Card Game (LLD / OOP)",
    "category": "Low-Level Design",
    "difficulty": "Easy",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Blackjack / Card Game (LLD / OOP). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Blackjack / Card Game (LLD / OOP):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Blackjack / Card Game (LLD / OOP)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Low-Level Design",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-102",
    "title": "Design Online Bookstore / Amazon Cart (LLD)",
    "category": "Low-Level Design",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Online Bookstore / Amazon Cart (LLD). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Online Bookstore / Amazon Cart (LLD):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Online Bookstore / Amazon Cart (LLD)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Low-Level Design",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-103",
    "title": "Design Distributed Counter Service",
    "category": "Distributed Systems",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Distributed Counter Service. Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Distributed Counter Service:\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Distributed Counter Service",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Distributed Systems",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-104",
    "title": "Design Stock Ticker Cache Service",
    "category": "Caching",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Stock Ticker Cache Service. Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Stock Ticker Cache Service:\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Stock Ticker Cache Service",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Caching",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-105",
    "title": "Design File Upload Service with Resumable Uploads",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design File Upload Service with Resumable Uploads. Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design File Upload Service with Resumable Uploads:\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design File Upload Service with Resumable Uploads",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "High-Level Design",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-106",
    "title": "Design Social Media Comment Thread (Tree Structure in SQL)",
    "category": "Databases & Storage",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Social Media Comment Thread (Tree Structure in SQL). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Social Media Comment Thread (Tree Structure in SQL):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Social Media Comment Thread (Tree Structure in SQL)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Databases & Storage",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-107",
    "title": "Design Location-Based Restaurant Search (Yelp)",
    "category": "High-Level Design",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Location-Based Restaurant Search (Yelp). Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Location-Based Restaurant Search (Yelp):\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Location-Based Restaurant Search (Yelp)",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "High-Level Design",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-108",
    "title": "Design Distributed Session Store",
    "category": "Caching",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Distributed Session Store. Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Distributed Session Store:\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Distributed Session Store",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Caching",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-109",
    "title": "Design Web Application Firewall (WAF) Inspection Engine",
    "category": "Security & Networking",
    "difficulty": "Hard",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Web Application Firewall (WAF) Inspection Engine. Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Web Application Firewall (WAF) Inspection Engine:\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Web Application Firewall (WAF) Inspection Engine",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Security & Networking",
      "Architecture",
      "Scalability"
    ]
  },
  {
    "id": "sd-110",
    "title": "Design Event Broker Consumer Lag Monitor",
    "category": "Messaging & Streaming",
    "difficulty": "Medium",
    "question": "Detailed interview architecture breakdown and implementation considerations for: Design Event Broker Consumer Lag Monitor. Explain scale requirements, trade-offs, and production failure modes.",
    "answer": "Comprehensive architectural breakdown of Design Event Broker Consumer Lag Monitor:\n1. Functional Requirements: Ingestion, storage, processing, querying, and delivery.\n2. Non-Functional Requirements: High availability (99.99%), sub-100ms latency, linear horizontal scalability, and data durability.\n3. Core Components: Load Balancers, API Gateways, Distributed Caching (Redis), Message Streaming (Kafka), and Persistent Databases (PostgreSQL / Cassandra / Spanner).\n4. Resiliency & Edge Cases: Handling network partitions, node crashes, replication lag, and backpressure.",
    "keyPoints": [
      "Core architecture pattern for Design Event Broker Consumer Lag Monitor",
      "Separates ingestion, processing, and query serving tiers",
      "Mitigates single points of failure via replication and failover",
      "Optimizes latency and throughput using in-memory caching and message queues"
    ],
    "tags": [
      "System Design",
      "Messaging & Streaming",
      "Architecture",
      "Scalability"
    ]
  }
];
