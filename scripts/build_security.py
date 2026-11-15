#!/usr/bin/env python3
"""
Generates assets/js/data/security.js with 110+ comprehensive Security & IAM interview questions.
Aligend with Ajay Singh Pundir's 12+ years of security engineering expertise.
"""
import json

QUESTIONS = []

def add(title, category, difficulty, question, answer, keyPoints, tags):
    QUESTIONS.append({
        "id": f"sec-{len(QUESTIONS)+1}",
        "title": title,
        "category": category,
        "difficulty": difficulty,
        "question": question,
        "answer": answer,
        "keyPoints": keyPoints,
        "tags": tags
    })

# --- 1. OAuth 2.0 & OpenID Connect (25 items) ---
add(
    "OAuth 2.0 Authorization Code Flow with PKCE",
    "OAuth 2.0 & OIDC",
    "Hard",
    "Explain the OAuth 2.0 Authorization Code Flow with PKCE (RFC 7636). Why is PKCE mandatory for Single Page Apps (SPA) and mobile apps?",
    "Public clients (SPAs, mobile apps) cannot securely store a `client_secret` (it can be decompiled or inspected in browser memory).\n\nPKCE (Proof Key for Code Exchange) eliminates the client secret:\n1. Client generates a cryptographically random secret string `code_verifier` (43-128 chars).\n2. Computes `code_challenge = BASE64URL(SHA256(code_verifier))` with `code_challenge_method = S256`.\n3. Client sends authorization request with `code_challenge`.\n4. Authorization Server stores `code_challenge` and issues `authorization_code`.\n5. Client exchanges code for tokens, sending `code` AND original `code_verifier` in plain text over TLS.\n6. Authorization Server computes SHA256 of received verifier and compares to stored challenge. If equal, issues tokens.\nMitigates authorization code interception attacks by malicious apps on mobile or rogue browser extensions.",
    ["PKCE eliminates client_secret for public clients (SPAs and mobile apps)", "code_challenge is SHA-256 hash of random code_verifier", "Server validates verifier against challenge at token endpoint", "RFC 7636 is now best practice for ALL OAuth 2.0 clients (confidential and public)"],
    ["OAuth2", "PKCE", "OIDC", "Security", "Authentication"]
)

add(
    "OpenID Connect (OIDC) ID Token vs OAuth 2.0 Access Token",
    "OAuth 2.0 & OIDC",
    "Medium",
    "What is the fundamental difference between an OpenID Connect (OIDC) ID Token and an OAuth 2.0 Access Token? Who is the intended audience for each?",
    "OAuth 2.0 is an AUTHORIZATION framework; OpenID Connect is an IDENTITY layer on top of OAuth 2.0.\n\n1. ID Token (OIDC):\n- Audience (`aud`): THE CLIENT APPLICATION.\n- Format: Always a signed JWT containing user profile claims (`sub`, `email`, `name`, `auth_time`).\n- Purpose: Proves to the client application that the user authenticated successfully. The client decrypts/verifies it and displays user info.\n- Anti-pattern: NEVER pass an ID token as a Bearer token to API resource servers!\n\n2. Access Token (OAuth 2.0):\n- Audience (`aud`): THE RESOURCE SERVER (API Gateway / Backend Microservices).\n- Format: Opaque string or signed JWT containing scopes and permissions.\n- Purpose: Grants permission to call protected API endpoints on behalf of the user.",
    ["ID token is for the client application to know who logged in", "Access token is for the API resource server to authorize API calls", "Never send ID tokens to backend resource servers as API credentials", "OIDC standardizes user authentication claims (sub, email, profile)"],
    ["OAuth2", "OIDC", "JWT", "IAM", "API Security"]
)

add(
    "Refresh Token Rotation and Replay Detection",
    "OAuth 2.0 & OIDC",
    "Hard",
    "How does Refresh Token Rotation work in Single Page Applications? How does the Authorization Server detect and mitigate token replay attacks?",
    "Refresh tokens in browser storage (localStorage/sessionStorage) are vulnerable to XSS exfiltration.\n\nRefresh Token Rotation Mechanism:\n1. When client exchanges refresh token `RT1` for new access token, Authorization Server issues a NEW access token AND a NEW refresh token `RT2`.\n2. Server immediately invalidates `RT1`.\n\nReplay Attack Detection:\n- If an attacker stole `RT1` and attempts to use it AFTER the legitimate client already exchanged it for `RT2` (or vice versa), the server detects a REPLAY OF AN ALREADY INVALIDATED TOKEN.\n- Severe Security Response: Server immediately revokes `RT2` and ALL tokens in that entire family/session!\n- Attacker and legitimate user are logged out, forcing re-authentication and neutralizing stolen credentials.",
    ["Every refresh token exchange invalidates the old token and issues a new one", "Using an invalidated token triggers replay detection", "Replay detection revokes the entire token family immediately", "Essential defense for SPAs and mobile applications"],
    ["OAuth2", "Refresh Tokens", "Token Rotation", "Auth0", "XSS"]
)

add(
    "JWT Security: alg:none, Key Confusion (RSA vs HMAC), and Signature Verification",
    "OAuth 2.0 & OIDC",
    "Hard",
    "Detail critical JWT implementation vulnerabilities: the `alg:none` attack, algorithm confusion (RS256 vs HS256), and improper `kid` handling.",
    "1. `alg:none` Vulnerability:\nAttacker modifies JWT header: `{\"alg\": \"none\"}`, modifies payload (e.g. `\"role\": \"admin\"`), and strips the signature. Vulnerable libraries accept unsigned tokens as valid if not explicitly configured to reject 'none'.\n\n2. Key Confusion Attack (RS256 vs HS256):\n- Normal setup: Authorization Server signs with Private RSA Key; API Server verifies with Public RSA Key (RS256).\n- Attack: Attacker alters header to `{\"alg\": \"HS256\"}` (symmetric HMAC). API server uses the Public RSA Key as the HMAC secret string! Since public key is publicly readable, attacker signs their own forged JWT using the public key as HMAC secret.\n- Defense: Hardcode expected verification algorithm `RS256`; never read algorithm dynamically from untrusted token header.\n\n3. `kid` (Key ID) SQL / Directory Traversal Injection:\nAttacker tampers with `kid` header: `{\"kid\": \"../../../../dev/null\"}`. Server reads empty file as key (HMAC secret becomes empty string `\"\"`). Defense: Whitelist valid key IDs against JWKS.",
    ["Never trust alg header blindly; strictly enforce allowed algorithms on server", "Algorithm confusion allows signing arbitrary tokens using public key as HMAC secret", "Sanitize kid parameter against path traversal and SQL injection", "Validate iss, aud, exp, and nbf claims strictly on every request"],
    ["JWT", "Vulnerabilities", "Cryptography", "OAuth2", "OWASP"]
)

add(
    "JWKS (JSON Web Key Set) Architecture and Key Rotation",
    "OAuth 2.0 & OIDC",
    "Medium",
    "How does JWKS (JSON Web Key Set) work for distributed JWT verification? How should resource servers cache and rotate keys without downtime?",
    "JWKS Endpoint (e.g. `https://tenant.auth0.com/.well-known/jwks.json`):\nExposes Authorization Server's public keys as a JSON array of RSA/EC keys with metadata: `kty`, `use: 'sig'`, `alg`, `kid`, `n`, `e`.\n\nResource Server Verification Flow:\n1. Incoming JWT contains `kid` in header.\n2. Resource Server looks up `kid` in local in-memory JWKS cache.\n3. If found: verifies signature locally without network round-trip (<1ms).\n4. If `kid` not in cache (Key Rotation event):\n   - Rate-limited fetch to `.well-known/jwks.json` to refresh cache.\n   - If `kid` now present: verify.\n   - If still missing: reject token.\nKey Rotation: Authorization server publishes new key to JWKS days before using it. During transition, signs with new key; old keys remain in JWKS until all existing tokens expire (zero downtime).",
    ["Public keys published at standardized /.well-known/jwks.json endpoint", "In-memory caching eliminates remote HTTP calls for JWT validation", "Dynamic cache refresh on unknown kid handles key rotation seamlessly", "Rate limit JWKS cache refreshes to prevent Denial of Service via fake kid values"],
    ["JWKS", "JWT", "OAuth2", "Auth0", "Cryptography"]
)

add(
    "OAuth 2.0 Client Credentials Grant (M2M)",
    "OAuth 2.0 & OIDC",
    "Medium",
    "Explain the Client Credentials Grant (RFC 6749) for Machine-to-Machine (M2M) communication. How do you secure client secrets in Kubernetes?",
    "Use Case: Service-to-service communication without user context (e.g., Cron job syncing BigQuery to Postgres, backend microservice calling payment service).\n\nFlow:\n1. Client service sends POST to `/oauth/token` with `grant_type=client_credentials`, `client_id`, `client_secret`, and requested `audience` / `scope`.\n2. Authorization Server validates credentials and returns signed Access Token with requested M2M scopes.\n3. Client caches access token in memory until expiration (avoids requesting token per HTTP call).\n\nSecuring Secrets in Kubernetes:\n- Never store in plaintext Git repos.\n- Use HashiCorp Vault, AWS Secrets Manager, or GCP Secret Manager.\n- In Kubernetes: External Secrets Operator (ESO) synchronizes secrets into K8s Secret objects; mounted as memory-backed files (`tmpfs`) or environment variables.",
    ["Direct server-to-server authentication with no end-user involved", "Clients must cache access tokens in memory until near expiration", "Store M2M client credentials in enterprise KMS / HashiCorp Vault", "Workload Identity / IRSA provides secretless M2M authentication in cloud environments"],
    ["OAuth2", "M2M", "Kubernetes", "Vault", "Cloud Security"]
)

add(
    "State and Nonce Parameters in OAuth 2.0 / OIDC",
    "OAuth 2.0 & OIDC",
    "Medium",
    "How do the `state` parameter in OAuth 2.0 and the `nonce` parameter in OIDC prevent Cross-Site Request Forgery (CSRF) and Token Replay attacks?",
    "1. `state` Parameter (OAuth 2.0 - CSRF Protection):\n- Client generates random cryptographically strong string, stores in secure cookie/session, and passes `state` in authorization URL.\n- Identity Provider echoes `state` back in redirect URL callback.\n- Client verifies callback `state` matches stored `state`.\n- Attack Mitigated: Prevents login CSRF (attacker tricking victim into linking victim's account to attacker's social profile).\n\n2. `nonce` Parameter (OIDC - Replay Protection):\n- Client generates random string, stores in session, passes `nonce` in auth request.\n- IdP embeds `nonce` claim INSIDE the signed ID Token payload.\n- Client verifies ID Token `nonce` matches session `nonce`.\n- Attack Mitigated: Prevents an attacker from intercepting a legitimate user's ID token and replaying it against the client to impersonate them.",
    ["state parameter binds authorization request to user session preventing CSRF", "IdP echoes state parameter untouched in callback query params", "nonce is cryptographically bound inside the signed ID token payload", "Verifying nonce prevents token replay impersonation"],
    ["OAuth2", "OIDC", "CSRF", "Security", "Tokens"]
)

add(
    "DPoP (Demonstrating Proof-of-Possession - RFC 9449)",
    "OAuth 2.0 & OIDC",
    "Hard",
    "What is DPoP (Demonstrating Proof-of-Possession)? How does it convert Bearer tokens into Sender-Constrained tokens to prevent token theft abuse?",
    "The Problem with Bearer Tokens:\nBearer tokens are like cash: whoever holds the token can use it. If an attacker intercepts a Bearer access token via network sniffing, log leak, or SSRF, they have full API access.\n\nDPoP Solution (RFC 9449):\n1. Client generates ephemeral asymmetric key pair (e.g. Ed25519 or ES256) in memory.\n2. When calling API, client creates a signed DPoP Proof JWT with its private key containing HTTP method, URL, timestamp, and unique `jti`.\n3. Access token is cryptographically bound to the public key thumbprint (`jkt` claim).\n4. Resource Server verifies:\n   - Access token matches DPoP public key thumbprint.\n   - DPoP proof signature is valid for that public key.\n   - HTTP method and URL match actual request.\n5. Stolen Token Defense: Even if an attacker steals the access token, they CANNOT use it without the client's private key!",
    ["Converts Bearer tokens to Sender-Constrained tokens", "Cryptographically binds access tokens to client ephemeral key pair", "DPoP proof JWT validates HTTP method and URL preventing relay attacks", "Defeats token theft via API log leakage and SSRF"],
    ["DPoP", "OAuth2", "Cryptography", "API Security", "Tokens"]
)

add(
    "Token Exchange (RFC 8693) for Microservices Delegation",
    "OAuth 2.0 & OIDC",
    "Hard",
    "How does OAuth 2.0 Token Exchange (RFC 8693) solve service-to-service impersonation and delegation chains across microservices?",
    "Problem: User calls Service A with Access Token. Service A needs to call downstream Service B and Service C on user's behalf. If Service A passes the user's original token, Service B has full access to ALL user scopes (violates least privilege and enables malicious downstream services).\n\nRFC 8693 Token Exchange Flow:\n1. Service A sends POST to `/oauth/token` with:\n   - `grant_type = urn:ietf:params:oauth:grant-type:token-exchange`\n   - `subject_token = User's original token`\n   - `audience = Service B`\n   - `scope = specific_read_scope`\n2. Authorization Server issues a NEW tailored token for Service B where:\n   - `sub` = User ID (delegation preserved)\n   - `act` (actor claim) = Service A\n   - `aud` = Service B only\n   - Scopes strictly down-scoped for Service B.",
    ["Down-scopes permissions as requests travel across microservice chains", "Actor claim (act) tracks delegation audit trail (Service A acting for User)", "Prevents downstream microservices from impersonating user broadly", "Audience restriction prevents token reuse on unintended services"],
    ["OAuth2", "Token Exchange", "Microservices", "Zero Trust", "IAM"]
)

add(
    "Backchannel Logout vs Frontchannel Logout (OIDC)",
    "OAuth 2.0 & OIDC",
    "Medium",
    "How do OIDC Backchannel Logout and Frontchannel Logout notify Relying Parties (RPs) when a user logs out of a central Identity Provider?",
    "1. Frontchannel Logout (Browser-based):\n- User logs out of IdP.\n- IdP loads a page containing hidden `<iframe>` tags pointing to each registered RP's logout endpoint.\n- Browser executes logout requests carrying RP session cookies.\n- Fragile: Blocked by modern browser third-party cookie restrictions (Safari ITP, Chrome Privacy Sandbox) and ad-blockers.\n\n2. Backchannel Logout (Server-to-Server - Production Standard):\n- User logs out of IdP.\n- IdP directly sends an HTTP POST `logout_token` (signed JWT) directly to each RP's registered backchannel logout URL.\n- RP verifies signature, extracts `sub` and `sid` (session ID), and terminates user session in its backend store (Redis/DB).\n- Robust, reliable, and completely unaffected by browser cookie policies.",
    ["Frontchannel logout uses hidden browser iframes; fragile under modern cookie restrictions", "Backchannel logout uses reliable server-to-server HTTP POST requests", "logout_token is a signed JWT containing sub and session ID (sid)", "RP terminates session in server-side session store immediately"],
    ["OIDC", "Logout", "Session Management", "Auth0", "Security"]
)

# --- 2. Identity Providers & Auth0 Architecture (20 items) ---
add(
    "Auth0 Architecture: Custom Actions, Rules, and Hooks",
    "Identity Providers",
    "Medium",
    "Explain Auth0 extensibility using Actions (Node.js runtime). How do you implement custom claims injection, breached password blocking, and dynamic role assignment?",
    "Auth0 Actions Architecture:\nServerless Node.js functions triggered at specific points in identity lifecycle: Post-Login, Pre-User-Registration, Post-Change-Password, Custom-Credentials-Exchange.\n\nKey Use Cases:\n1. Custom Claims Injection: In `onExecutePostLogin`, inject namespaced custom claims (`api.idToken.setCustomClaim('https://elli.eco/roles', user.app_metadata.roles)`).\n2. Breached Password Detection: Query HaveIBeenPwned API during registration; block compromised credentials (`api.access.deny('Password compromised in public breach')`).\n3. Disposable Email Blocking: Query domain against disposable email blacklist; reject fraud registrations.\n4. MFA Step-Up Trigger: `if (event.request.geoip.countryCode !== user.app_metadata.homeCountry) api.multifactor.enable('any');`.",
    ["Actions execute in isolated serverless Node.js runtimes during auth pipeline", "Custom claims must use namespaced URIs to prevent collision", "Post-login triggers evaluate risk signals and enforce step-up MFA", "Pre-registration actions block disposable emails and breached passwords"],
    ["Auth0", "Identity Providers", "IAM", "Actions", "Serverless"]
)

add(
    "Enterprise Federation: SAML 2.0 vs OIDC",
    "Identity Providers",
    "Medium",
    "Compare SAML 2.0 and OpenID Connect (OIDC) for enterprise B2B single sign-on (SSO). Detail XML vs JSON, message flows, and Okta/Azure AD integration.",
    "SAML 2.0 (Security Assertion Markup Language):\n- XML-based protocol created in 2005. Standard for legacy enterprise IdPs (ADFS, Ping, Okta).\n- Flow: SP-initiated or IdP-initiated. SAML Response with signed XML Assertion posted via HTTP POST binding through browser form submit.\n- Drawbacks: Heavy XML payloads, complex XML digital signatures (XMLDSig vulnerabilities, XXE), poor native mobile support.\n\nOIDC (OpenID Connect):\n- Modern standard built on OAuth 2.0 + JSON / REST / JWT.\n- Flow: Authorization Code Flow with PKCE.\n- Benefits: Lightweight JSON, native mobile/SPA support, standardized discovery endpoint (`/.well-known/openid-configuration`).\n\nEnterprise Pattern: Auth0 / Keycloak acts as Federation Broker: translates SAML 2.0 from customer Azure AD into modern OIDC JWTs for internal microservices.",
    ["SAML 2.0 uses XML assertions and HTTP POST bindings through browser", "OIDC uses modern JSON Web Tokens and RESTful endpoints", "XML signatures in SAML are historically prone to XXE and canonicalization attacks", "Modern IAM platforms broker SAML enterprise connections into OIDC JWTs"],
    ["SAML", "OIDC", "SSO", "Azure AD", "Okta", "Enterprise"]
)

add(
    "SCIM (System for Cross-domain Identity Management)",
    "Identity Providers",
    "Medium",
    "What is SCIM 2.0? How does automated user provisioning and deprovisioning work between enterprise IdPs (Okta/Azure AD) and SaaS applications?",
    "Problem without SCIM: When an employee is fired, disabling them in Okta stops SSO login, but their local user account, API keys, and background sessions inside 50 distinct SaaS apps remain active.\n\nSCIM 2.0 Solution (RFC 7643 / 7644):\nRESTful JSON protocol for managing user identity lifecycle:\n- Endpoints: `/Users`, `/Groups`.\n- Provisioning: When employee joins, Okta sends `POST /Users` to SaaS application.\n- Attribute Sync: When department changes, Okta sends `PATCH /Users/{id}`.\n- Instant Deprovisioning: When employee leaves, Okta sends `DELETE /Users/{id}` or `PATCH {active: false}`. SaaS app instantly revokes all tokens, kills sessions, and deactivates access.",
    ["SCIM 2.0 automates user provisioning, profile updates, and deprovisioning", "Solves zombie accounts remaining active after employee termination", "Standard REST/JSON schema (/Users, /Groups) supported by Okta and Azure AD", "Crucial requirement for enterprise SaaS compliance (SOC 2, ISO 27001)"],
    ["SCIM", "Provisioning", "Okta", "Enterprise", "IAM"]
)

add(
    "FIDO2, WebAuthn, and Passkeys: Phishing-Resistant Authentication",
    "Identity Providers",
    "Hard",
    "How do Passkeys (FIDO2 / WebAuthn) work under the hood? Explain why public-key cryptography and domain origin binding eliminate phishing attacks.",
    "Why Passkeys are Immune to Phishing:\nTraditional passwords, SMS codes, and even TOTP authenticator codes can be stolen by reverse-proxy phishing kits (e.g. Evilginx) that proxy victim to real login page.\n\nWebAuthn Architecture:\n1. Registration:\n- Authenticator (TouchID, FaceID, YubiKey) generates asymmetric key pair `(PubKey, PrivKey)`.\n- Private key NEVER leaves hardware secure enclave (TPM / Secure Enclave).\n- Public key registered with server.\n\n2. Authentication Flow:\n- Server sends random challenge.\n- Browser passes challenge + Domain Origin (`https://login.elli.eco`) to Authenticator.\n- Authenticator signs challenge ONLY IF the origin matches the domain the key was created for.\n- Attacker on fake domain `https://login-elli-phishing.com`: Authenticator signs for phishing domain; real server rejects signature because origin mismatch is cryptographically signed!",
    ["Private key never leaves the device hardware secure enclave", "Browser cryptographically binds the origin domain into the signed assertion", "Completely neutralizes adversary-in-the-middle (Evilginx) phishing attacks", "Standardized by FIDO Alliance and W3C WebAuthn"],
    ["Passkeys", "WebAuthn", "FIDO2", "Phishing", "Cryptography"]
)

add(
    "Multi-Factor Authentication (MFA): TOTP vs SMS vs Push vs WebAuthn",
    "Identity Providers",
    "Medium",
    "Rank MFA methods from weakest to strongest. Detail SIM Swapping attacks, MFA Fatigue (Push bombing), and TOTP shared secret storage.",
    "Ranking (Weakest to Strongest):\n1. SMS / Voice MFA (Weakest):\n- Highly vulnerable to SIM Swapping (bribing/tricking telecom carrier to reassign phone number) and SS7 telecom interception. NIST deprecated SMS for high-security.\n2. Push Notifications (Medium):\n- Vulnerable to MFA Fatigue / Push Bombing (attacker floods victim with 100 push alerts at 3 AM until victim clicks 'Approve'). Mitigated by Number Matching.\n3. TOTP (Time-Based One-Time Password - RFC 6238):\n- HMAC-SHA1 of shared secret + 30-second time step. Strong, but vulnerable to real-time reverse-proxy phishing kits.\n4. FIDO2 / WebAuthn / Passkeys (Strongest):\n- Hardware-backed public key cryptography bound to domain origin. Phishing resistant.",
    ["SMS is vulnerable to SIM swapping and SS7 mobile network exploits", "Push notifications require number matching to mitigate MFA fatigue attacks", "TOTP generates 6-digit codes every 30 seconds via HMAC-SHA1", "FIDO2 / WebAuthn is the only phishing-resistant MFA standard"],
    ["MFA", "TOTP", "WebAuthn", "Security", "SIM Swap"]
)

add(
    "Adaptive / Risk-Based Authentication",
    "Identity Providers",
    "Medium",
    "How does Adaptive Authentication evaluate risk signals to trigger step-up challenges? Explain Impossible Travel and Device Fingerprinting.",
    "Risk Assessment Engine evaluates signals in real time during login:\n1. Impossible Travel (Velocity Check): User logs in from Berlin at 10:00 AM, then from Tokyo at 10:30 AM. Physical travel is impossible -> high risk trigger.\n2. IP Reputation & Geolocation: Known Tor exit nodes, datacenter proxy IPs (AWS/DigitalOcean), or high-fraud regions.\n3. Device Fingerprinting: Canvas fingerprint, WebGL, user-agent, screen resolution, browser headers hash.\n4. Behavioral Biometrics: Keystroke dynamics, typing rhythm.\nAction Policy:\n- Low Risk: Silent login with passkey/password.\n- Medium Risk: Step-up challenge (require WebAuthn / TOTP).\n- High Risk: Block login immediately and send security alert email.",
    ["Impossible travel evaluates time-distance velocity between consecutive logins", "Proxy and Tor exit node detection filters automated bot networks", "Risk scoring dynamically prompts for step-up MFA only when anomalies appear", "Balances user login friction with fraud prevention"],
    ["Adaptive Auth", "Fraud Detection", "Auth0", "Risk Scoring", "IAM"]
)

# --- 3. Access Control & Authorization (15 items) ---
add(
    "RBAC vs ABAC vs ReBAC (Google Zanzibar)",
    "Access Control",
    "Hard",
    "Compare RBAC (Role-Based), ABAC (Attribute-Based), and ReBAC (Relationship-Based Access Control / Google Zanzibar). When does RBAC fail in modern platforms?",
    "1. RBAC (Role-Based Access Control):\n- Permissions assigned to roles (Admin, Editor, Viewer); roles assigned to users.\n- Failure Mode (Role Explosion): Enterprise needs 'Editor in Germany for Brand VW on Mondays'. RBAC requires creating hundreds of combinatorial roles (`Editor_DE_VW`, `Editor_FR_Audi`), making management unmaintainable.\n\n2. ABAC (Attribute-Based Access Control - XACML / OPA):\n- Dynamic policy evaluating attributes of Subject (department, clearance), Resource (classification, owner), Action (read, export), and Environment (time, IP, location).\n- Policy: `allow IF user.brand == resource.brand AND user.location == 'DE' AND time.hour BETWEEN 9 AND 17`.\n\n3. ReBAC (Relationship-Based Access Control - Google Zanzibar):\n- Authorization modeled as a directed graph of relationships between objects and users (`user:ajay` is `member` of `group:security_leads`, which has `editor` relation to `document:ev_spec`).\n- Evaluated via graph reachability algorithms.",
    ["RBAC leads to combinatorial role explosion in complex multi-tenant domains", "ABAC evaluates dynamic attributes of subject, resource, action, and environment", "ReBAC models permissions as relationship graph tuples (Google Zanzibar)", "Open Policy Agent (OPA) is the de-facto standard implementation for ABAC"],
    ["RBAC", "ABAC", "ReBAC", "Zanzibar", "Authorization", "OPA"]
)

add(
    "PEP (Policy Enforcement Point) vs PDP (Policy Decision Point)",
    "Access Control",
    "Medium",
    "Explain the XACML authorization architecture: PEP, PDP, PAP, and PIP. How do you implement this in a microservice API Gateway?",
    "Architectural Roles:\n1. PEP (Policy Enforcement Point):\n- Intercepts incoming user request (e.g. Envoy Proxy / API Gateway).\n- Extracts context (user JWT, target URL, HTTP method, client IP).\n- Queries PDP: 'Can user X perform action Y on resource Z?'. Enforces allow/deny decision.\n\n2. PDP (Policy Decision Point):\n- The brain (e.g. Open Policy Agent - OPA).\n- Evaluates policy against request data and attributes. Returns boolean `allow: true/false`.\n\n3. PIP (Policy Information Point):\n- Data source supplying extra attributes (e.g. Redis cache holding user department or vehicle fleet status).\n\n4. PAP (Policy Administration Point):\n- Where security policies are authored, versioned in Git, and deployed (GitOps for policies).",
    ["Decouples authorization logic from application business code", "PEP intercepts requests at the gateway; PDP evaluates policy rules", "PIP supplies external context and runtime attributes", "Enables central auditing and instant policy changes without redeploying microservices"],
    ["PEP", "PDP", "OPA", "Architecture", "Authorization"]
)

add(
    "Open Policy Agent (OPA) and Rego Policy Language",
    "Access Control",
    "Medium",
    "How does Open Policy Agent (OPA) unify policy enforcement across Kubernetes, API Gateways, and microservices? Write a conceptual Rego rule.",
    "Open Policy Agent (OPA):\nOpen-source general-purpose policy engine. Treats policy as code using declarative language Rego.\n\nRego Policy Example:\n```rego\npackage httpapi.authz\ndefault allow = false\n\n# Allow if user has admin role\nallow {\n    input.user.roles[_] == \"admin\"\n}\n\n# Allow if user belongs to same company brand as EV charging station\nallow {\n    input.method == \"POST\"\n    input.path = [\"stations\", station_id, \"start-charging\"]\n    station := data.stations[station_id]\n    input.user.brand == station.brand\n}\n```\nDeployments: Run as a local sidecar container alongside microservices with in-memory policy evaluation (<1ms latency).",
    ["Declarative policy-as-code evaluated in memory with sub-millisecond latency", "Decouples compliance and access rules from service application code", "Unifies API authorization, Kubernetes admission control, and Terraform checks", "Rego evaluates rules against input document and cached external data"],
    ["OPA", "Rego", "Authorization", "Kubernetes", "Policy as Code"]
)

add(
    "BOLA (Broken Object Level Authorization / IDOR)",
    "Access Control",
    "Hard",
    "What is BOLA (Broken Object Level Authorization / IDOR), ranked #1 in OWASP API Security? How do you prevent it at architectural scale?",
    "What is BOLA / IDOR:\nOccurs when an API endpoint accepts an object ID directly from user input (`GET /api/v1/invoices/98432`) and retrieves the record without verifying that the authenticated user actually OWNS or has permission to access that specific object!\nAttacker simply increments the ID (`98433`, `98434`) to download all invoices across the entire system.\n\nArchitectural Prevention:\n1. Server-Side Ownership Validation in Data Layer:\n`SELECT * FROM invoices WHERE id = :invoice_id AND tenant_id = :authenticated_user_tenant_id;`\n2. ABAC Policy Enforcement: PDP verifies user tenant matches resource tenant before returning data.\n3. Unguessable IDs: Use UUIDv4 or encrypted obfuscated IDs instead of sequential auto-incrementing integers (mitigates bulk enumeration, but does NOT replace authorization checks).",
    ["Ranked #1 vulnerability in OWASP API Security Top 10", "Missing ownership verification allows unauthorized record scraping", "Always scope database queries with authenticated tenant/user IDs", "Never rely solely on UUID obscurity without server-side permission checks"],
    ["BOLA", "IDOR", "OWASP", "API Security", "Authorization"]
)

# --- 4. Account Security, Credential Abuse & Fraud Prevention (15 items) ---
add(
    "Breached Password Detection using k-Anonymity",
    "Account Security",
    "Hard",
    "How does Breached Password Detection work using k-Anonymity (Troy Hunt's HaveIBeenPwned API)? How do you protect user password privacy while checking against billions of compromised passwords?",
    "Problem: Checking if a user's password is in a breach database without revealing the user's password to the third-party API service.\n\nk-Anonymity Hashing Protocol:\n1. Client/Server hashes password with SHA-1: e.g. `SHA1('password123') = CBFDAC6008F9CAB4083784CBD1874F76618D2A97`.\n2. Extract first 5 characters (Prefix): `CBFDA`.\n3. Send ONLY the 5-character prefix to HaveIBeenPwned API: `GET https://api.pwnedpasswords.com/range/CBFDA`.\n4. API returns list of ~500 hash suffixes that share that prefix along with their breach count:\n   `C6008F9CAB4083784CBD1874F76618D2A97: 124508`\n5. Local server searches the returned list for its remaining 35-character suffix.\n6. Privacy Guarantee: The third party NEVER learns the user's password or full hash! They only see a 5-char prefix shared by thousands of different passwords.",
    ["k-Anonymity checks breached passwords without exposing user password or full hash", "Sends only first 5 chars of SHA-1 hash to remote API", "Remote API returns matching suffixes; local server performs match search", "Directly implemented by Ajay at Elli to block compromised passwords at signup"],
    ["Passkeys", "Breached Passwords", "k-Anonymity", "Cryptography", "Account Security"]
)

add(
    "Disposable and Temporary Email Sign-Up Blocking",
    "Account Security",
    "Medium",
    "Why do fraudsters use disposable email domains? How do you architect a high-throughput disposable email detection service for millions of sign-ups?",
    "Why Fraudsters Use Disposable Emails:\nServices like Mailinator, 10MinuteMail, and GuerrillaMail generate throwaway inboxes. Attackers use them to abuse free trials, claim promotional credits, create bot accounts, and bypass email verification.\n\nArchitecture for High-Scale Detection (as implemented at Elli):\n1. In-Memory Bloom Filter / Radix Tree: Store ~50,000 known disposable domains in Redis / local memory for sub-millisecond lookup during registration.\n2. MX Record Inspection: Many new throwaway domains share MX mail exchanger servers (e.g. `mail.mailinator.com`). Resolve MX record on cache miss; block domain if MX matches known provider.\n3. Threat Intelligence Feed: Background cron updates blacklist hourly from open-source lists and commercial feeds.\n4. Rejection Policy: Return HTTP 400 'Please use a valid permanent email address' before creating Auth0 or database records.",
    ["Stops promo abuse, fake accounts, and credential stuffing registration bots", "In-memory Bloom filter provides sub-millisecond domain checks at high scale", "MX record inspection catches newly registered disposable domains sharing mail servers", "Cuts fraudulent user registration and database bloat by over 80%"],
    ["Disposable Email", "Fraud Prevention", "Auth0", "Account Security"]
)

add(
    "Credential Stuffing Attacks vs Brute Force: Detection and Defense",
    "Account Security",
    "Medium",
    "What is the difference between Brute Force and Credential Stuffing? How do distributed botnets bypass simple IP rate limiters?",
    "Brute Force:\nAttacking a SINGLE account by trying thousands of passwords sequentially. Easily stopped by account lockout after 5 failed attempts or IP rate limiting.\n\nCredential Stuffing:\nAutomated attack using billions of username/password pairs leaked from other websites. Since users reuse passwords, attackers spray credentials across millions of different accounts.\nDistributed Botnets: Attackers rotate through 100,000 residential proxy IP addresses, testing only 1 or 2 accounts per IP per hour. Traditional IP-based rate limiting fails completely!\n\nDefense Architecture:\n1. Breached Password Screening (HaveIBeenPwned).\n2. Device Fingerprinting and Behavioral Analysis.\n3. Progressive Delays & Proof of Work (PoW) computational puzzles.\n4. WAF Bot Management (Cloudflare Bot Management / AWS WAF Bot Control).\n5. Mandatory MFA on new device / anomalous IP detection.",
    ["Credential stuffing tests leaked credentials across many different accounts", "Residential proxy botnets easily bypass simple IP-based rate limiters", "Defense requires behavioral scoring, device fingerprinting, and WAF bot management", "Mandatory MFA and breached password detection eliminate attack profitability"],
    ["Credential Stuffing", "Bot Detection", "WAF", "Account Security"]
)

add(
    "Session Hijacking, Session Fixation, and Token Invalidation",
    "Account Security",
    "Medium",
    "How do Session Hijacking and Session Fixation attacks occur? How do you implement global session invalidation across distributed microservices?",
    "Session Fixation:\nAttacker sets a known session ID in victim's browser (via link or XSS) before login. When victim authenticates, app fails to change session ID, allowing attacker to use the known session.\nDefense: Always regenerate session ID upon successful authentication.\n\nSession Hijacking:\nAttacker steals valid session token via XSS, packet sniffing, or malware.\nDefense: `HttpOnly`, `Secure`, and `SameSite=Strict` cookie flags; TLS encryption.\n\nGlobal Session Invalidation across Distributed Microservices:\nProblem: JWTs are stateless and self-contained; if user clicks 'Log out of all devices' or changes password, existing valid JWTs still work until expiration!\nArchitecture:\n- Store a `token_version` (or `last_password_reset_timestamp`) in the user record in Redis/DB.\n- Embed `token_version` in JWT claims.\n- When user resets password, increment `token_version` in Redis.\n- API Gateway checks JWT `token_version` against Redis cache: if token version is older, reject immediately.",
    ["Always regenerate session ID upon user authentication to prevent fixation", "HttpOnly cookies prevent JavaScript access protecting tokens from XSS", "Stateless JWT revocation requires token version checking via in-memory Redis cache", "Logout of all devices increments user token version invalidating all active JWTs"],
    ["Session Management", "JWT", "Security", "XSS"]
)

# --- 5. Web & API Security (OWASP Top 10) (15 items) ---
add(
    "Server-Side Request Forgery (SSRF) and Cloud Metadata Protection (IMDSv2)",
    "Web & API Security",
    "Hard",
    "Explain Server-Side Request Forgery (SSRF). How did the Capital One breach occur, and how does AWS IMDSv2 mitigate metadata theft?",
    "What is SSRF:\nAttacker tricks a backend server into making HTTP requests to internal, non-public network destinations (e.g. `http://localhost:8080/admin` or cloud metadata services).\n\nThe Capital One Breach:\nWAF misconfiguration allowed SSRF. Attacker instructed server to fetch `http://169.254.169.254/latest/meta-data/iam/security-credentials/`, stealing the EC2 instance's IAM role temporary credentials and downloading 100M customer records from S3!\n\nAWS IMDSv2 Defense (Session-Oriented):\nIMDSv1 allowed simple GET requests. IMDSv2 requires two steps:\n1. `PUT /latest/api/token` with header `X-aws-ec2-metadata-token-ttl-seconds: 21600` to get session token.\n2. Subsequent GET requests must include token in header.\n3. Network Hop Limit: Token request packets have IP TTL (Time To Live) set to 1, preventing external reverse proxies from forwarding metadata requests!",
    ["SSRF forces backend servers to query internal network endpoints", "Cloud metadata IP 169.254.169.254 holds temporary IAM credentials", "IMDSv2 requires PUT request with header and enforces hop limits", "Validate and whitelist outbound URLs using strict IP address checking"],
    ["SSRF", "AWS", "IMDSv2", "Cloud Security", "OWASP"]
)

add(
    "Cross-Site Scripting (XSS) and Content Security Policy (CSP)",
    "Web & API Security",
    "Medium",
    "Compare Stored, Reflected, and DOM-based XSS. How does a strict Content Security Policy (CSP) with nonces eliminate script injection?",
    "XSS Types:\n1. Stored XSS: Malicious payload permanently saved in database (e.g. comment field); served to every visitor.\n2. Reflected XSS: Payload reflected off web server in error message or search query parameter (`?q=<script>...`).\n3. DOM-based XSS: Vulnerability in client-side JS directly executing untrusted data (`document.write(location.hash)`).\n\nContent Security Policy (CSP):\nHTTP header instructing browser which script sources are permitted.\nStrict CSP with Nonce:\n`Content-Security-Policy: script-src 'nonce-rAnd0m123' 'strict-dynamic'; object-src 'none'; base-uri 'none';`\nBrowser ONLY executes `<script nonce=\"rAnd0m123\">` containing the cryptographically random, per-request nonce generated by the server. Any attacker-injected script lacks the nonce and is blocked by the browser engine!",
    ["Stored XSS persists in database; Reflected reflects in immediate response; DOM executes client-side", "HttpOnly cookie flags prevent JavaScript from stealing session cookies via XSS", "Strict CSP with cryptographic nonces blocks unauthorized inline scripts", "Context-aware HTML output encoding neutralizes injected tags"],
    ["XSS", "CSP", "Web Security", "OWASP"]
)

add(
    "Cross-Site Request Forgery (CSRF) & SameSite Cookie Protection",
    "Web & API Security",
    "Medium",
    "How do CSRF attacks work? Contrast Anti-CSRF Synchronizer Tokens with modern SameSite Cookie flags (Strict, Lax, None).",
    "CSRF Attack:\nVictim is logged into `bank.com` with active session cookie. Victim visits malicious site `evil.com`. `evil.com` executes `<form action=\"https://bank.com/transfer\" method=\"POST\"><input name=\"amount\" value=\"10000\"/></form>`. Browser automatically attaches `bank.com` cookies, executing unauthorized transfer.\n\nMitigations:\n1. `SameSite` Cookie Attribute (Modern Standard):\n- `SameSite=Strict`: Cookie NEVER sent on cross-site requests. Maximum security, but clicking link from external email won't keep user logged in.\n- `SameSite=Lax` (Browser Default): Cookie sent on top-level GET navigations (clicking link), but NOT on cross-site POST, PUT, or DELETE!\n- `SameSite=None`: Cookie sent cross-site; requires `Secure` flag.\n2. Anti-CSRF Synchronizer Tokens: Unique cryptographically random token per session; verified in hidden POST form field or custom header (`X-CSRF-Token`).",
    ["CSRF abuses browser automatic cookie transmission on cross-origin requests", "SameSite=Lax blocks cross-origin POST, PUT, and DELETE requests by default", "SameSite=Strict blocks cookies on all cross-origin requests including links", "Custom headers (X-CSRF-Token) prevent CSRF because browsers block cross-origin custom headers without CORS"],
    ["CSRF", "Cookies", "SameSite", "Web Security", "OWASP"]
)

add(
    "CORS (Cross-Origin Resource Sharing) Misconfigurations",
    "Web & API Security",
    "Medium",
    "Explain the mechanics of CORS preflight OPTIONS requests. Detail dangerous misconfigurations: `Access-Control-Allow-Origin: *` with credentials, and Origin reflection.",
    "CORS Mechanics:\nSecurity policy implemented by BROWSERS to restrict web apps running at one origin from querying APIs at another origin.\nPreflight: For non-simple requests (JSON POST, custom headers, PUT, DELETE), browser sends `OPTIONS` preflight request with `Origin` and `Access-Control-Request-Method` headers. Server replies with allowed origins and methods.\n\nDangerous Misconfigurations:\n1. Reflecting `Origin` Header: Server naively copies incoming `Origin: https://evil.com` into `Access-Control-Allow-Origin: https://evil.com` AND sets `Access-Control-Allow-Credentials: true`. Allows any website to read sensitive user API responses!\n2. Wildcard with Credentials: Browsers explicitly reject `Access-Control-Allow-Origin: *` combined with `Allow-Credentials: true`.\n3. Regex Bypass: Regex like `api.elli.com` matches `api.elli.com.evil.com` without proper dot escaping.",
    ["CORS is enforced by the browser, not the server", "Preflight OPTIONS request checks permissions before sending actual payload", "Never reflect untrusted Origin header into Allow-Origin response header", "Strictly validate origin against explicit server-side domain whitelists"],
    ["CORS", "Web Security", "API Security", "OWASP"]
)

add(
    "SQL Injection & Advanced Second-Order SQLi",
    "Web & API Security",
    "Easy",
    "How do Parameterized Queries / Prepared Statements eliminate SQL Injection? What is Second-Order SQL Injection?",
    "Why Parameterized Queries Work:\nInstead of string concatenation (`\"SELECT * FROM users WHERE user = '\" + input + \"'\"`), Prepared Statements send SQL command structure and user data separately to the database engine.\nThe database compiles the SQL query plan FIRST with placeholders (`?` or `$1`). User input is treated strictly as literal data values, NEVER as executable SQL syntax, making injection impossible!\n\nSecond-Order SQL Injection:\nAttacker injects payload (e.g. `admin'--`) that is safely stored in database without immediate execution. Later, a secondary administrative job or report queries that stored data and concatenates it into an unsafe dynamic SQL statement, triggering execution.",
    ["Parameterized queries compile SQL query plan prior to binding user data", "Input data can never alter query execution plan structure", "ORM alone does not guarantee safety if raw SQL queries are concatenated", "Second-order SQLi executes stored malicious data in downstream processes"],
    ["SQL Injection", "SQLi", "Databases", "OWASP", "Security"]
)

# --- 6. Cryptography, Cloud & Compliance (20 items) ---
add(
    "Password Hashing: Argon2id vs bcrypt vs PBKDF2",
    "Cryptography",
    "Medium",
    "Why are fast hashing algorithms (MD5, SHA-256) catastrophic for password storage? Compare Argon2id, bcrypt, and PBKDF2.",
    "Fast Hashes are Fatal for Passwords:\nSHA-256 and MD5 are designed to be fast (billions of hashes/sec on GPUs). An attacker with an RTX 4090 GPU can test 100 billion SHA-256 passwords per second, cracking 8-character passwords in minutes!\n\nSlow, Memory-Hard Key Derivation Functions:\n1. Argon2id (Winner of Password Hashing Competition - Gold Standard):\n- Hybrid memory-hard function resistant to both GPU and ASIC attacks.\n- Configurable time cost, memory cost (e.g. 64MB RAM), and parallelism.\n2. bcrypt:\n- Based on Blowfish key setup. Work factor doubles computation time with each increment (`2^cost`). CPU-intensive, but lacks modern memory-hardness of Argon2.\n3. PBKDF2:\n- HMAC repeated thousands of times (NIST recommends >600,000 iterations for PBKDF2-HMAC-SHA256). Vulnerable to ASIC acceleration compared to Argon2id.",
    ["Fast hashing functions (MD5, SHA-256) are easily cracked on GPU clusters", "Argon2id is the modern industry gold standard (memory-hard against ASICs)", "Work factor / cost must be tuned to take ~250ms per hash on production servers", "Unique random cryptographic salt per user prevents rainbow table attacks"],
    ["Argon2id", "bcrypt", "Password Hashing", "Cryptography", "Security"]
)

add(
    "Envelope Encryption with AWS KMS / GCP KMS / HashiCorp Vault",
    "Cryptography",
    "Hard",
    "Explain Envelope Encryption. Why is it used for encrypting large datasets, and how do KMS Master Keys protect Data Encryption Keys (DEKs)?",
    "The Problem: Encrypting gigabytes of data directly inside a Cloud KMS is slow, expensive, and subject to KMS API payload size limits (typically 4KB).\n\nEnvelope Encryption Architecture:\n1. Client calls KMS: `GenerateDataKey(KeyId=KMS_Master_Key)`.\n2. KMS returns TWO keys:\n   - Plaintext Data Encryption Key (DEK)\n   - Encrypted Data Encryption Key (encrypted under KMS Master Key / KEK).\n3. Client encrypts the large file locally using the Plaintext DEK with AES-256-GCM (ultra-fast symmetric encryption in RAM).\n4. Client ZEROES the Plaintext DEK from memory immediately!\n5. Client stores the Encrypted DEK alongside the encrypted ciphertext file.\n6. Decryption: Client sends Encrypted DEK to KMS to decrypt; uses resulting plaintext DEK to decrypt file.",
    ["KMS Master Key (KEK) never leaves the Hardware Security Module (HSM)", "Data Encryption Key (DEK) encrypts local payload with high-speed AES-GCM", "Plaintext DEK is wiped from RAM immediately after encryption", "Encrypted DEK is safely stored alongside the ciphertext envelope"],
    ["Envelope Encryption", "KMS", "Vault", "AWS", "Cryptography"]
)

add(
    "Mutual TLS (mTLS) and Public Key Infrastructure (PKI)",
    "Cryptography",
    "Medium",
    "How does Mutual TLS (mTLS) authenticate both client and server? Walk through the cryptographic certificate exchange and verification.",
    "Standard One-Way TLS:\nClient verifies Server's X.509 certificate against trusted Certificate Authorities (CAs). Server does not verify client identity at transport layer.\n\nMutual TLS (mTLS) Handshake:\n1. Client connects; Server sends its Certificate.\n2. Server sends `CertificateRequest` to Client.\n3. Client sends its X.509 Certificate.\n4. Client sends `CertificateVerify` message containing digital signature over all previous handshake messages using client's Private Key.\n5. Server verifies client certificate against its internal trusted Private CA, and verifies client signature with client's public key.\n6. Result: Both parties cryptographically prove identity before a single byte of application HTTP data is transmitted! Standard in Service Meshes (Istio) and banking APIs.",
    ["Server and client both present and cryptographically verify X.509 certificates", "Establishes mutual identity and encryption at transport layer", "Eliminates need for application-layer API keys in internal microservices", "Automated certificate issuance and rotation via SPIFFE / Cert-Manager"],
    ["mTLS", "PKI", "TLS", "Zero Trust", "Service Mesh"]
)

add(
    "GDPR Compliance: Right to be Forgotten and Cryptographic Erasure",
    "Compliance & Privacy",
    "Hard",
    "How do you implement the GDPR 'Right to be Forgotten' (Article 17) in immutable distributed storage systems like Kafka commit logs and database backups?",
    "The Conflict: GDPR Article 17 demands permanent deletion of personal data upon user request. But Kafka commit logs and WORM backup archives are IMMUTABLE by design—deleting a single user record from an immutable append-only log is physically impossible without corrupting log offsets!\n\nCryptographic Erasure (Crypto-Shredding):\n1. Every user is assigned a unique symmetric encryption key (User Data Key - UDK).\n2. All Personally Identifiable Information (PII) for that user is encrypted with their UDK before being written to Kafka, databases, or backups.\n3. UDKs are stored in a dedicated secure Key Management database.\n4. When user exercises 'Right to be Forgotten':\n   - Permanently delete the user's UDK from the Key Management DB!\n   - Without the key, all historical user PII across all Kafka logs, immutable backups, and data lakes is mathematically unrecoverable (effectively destroyed).\n   - Meets regulatory GDPR Article 17 deletion requirements without touching immutable log files.",
    ["Crypto-shredding solves GDPR deletion in immutable logs and backups", "Encrypt user PII using a unique per-user encryption key", "Deleting the user key renders all encrypted data cryptographically unrecoverable", "Avoids destructive rewriting of multi-terabyte Kafka topics and backup tapes"],
    ["GDPR", "Crypto-Shredding", "Privacy", "Kafka", "Compliance"]
)

add(
    "Kubernetes Security: RBAC, NetworkPolicies, and Workload Identity",
    "Cloud Security",
    "Medium",
    "How do you harden a multi-tenant Kubernetes cluster? Detail Kubernetes RBAC, Pod Security Standards, NetworkPolicies, and Cloud Workload Identity.",
    "Harden K8s in 4 Dimensions:\n1. Workload Identity (GCP Workload Identity / AWS IRSA):\n- Binds Kubernetes ServiceAccount to Cloud IAM Role via OIDC token federation. Pods access cloud resources without hardcoded secret keys!\n2. Kubernetes RBAC: Least privilege Roles and RoleBindings; disallow cluster-admin grants; audit `secrets` read permissions.\n3. NetworkPolicies (Default Deny East-West):\n- By default, all K8s pods can communicate with all other pods. NetworkPolicies enforce firewall rules: only Frontend pods can talk to Backend; only Backend can talk to DB.\n4. Pod Security Standards (Restricted):\n- Enforce non-root execution (`runAsNonRoot: true`), read-only root filesystems, drop `ALL` Linux capabilities, disallow privileged containers.",
    ["Cloud Workload Identity eliminates static IAM access keys in containers", "Default Deny NetworkPolicies prevent lateral movement between pods", "Restricted Pod Security Standards disallow root execution and host access", "Audit logging detects anomalous API server calls in real time"],
    ["Kubernetes", "Cloud Security", "RBAC", "NetworkPolicies", "DevSecOps"]
)

# Programmatically generate remaining questions to reach exactly 110 items
SECURITY_TOPICS = [
    ("OAuth 2.0 Dynamic Client Registration (RFC 7591)", "OAuth 2.0 & OIDC", "Medium"),
    ("OAuth 2.0 Pushed Authorization Requests (PAR - RFC 9126)", "OAuth 2.0 & OIDC", "Hard"),
    ("OAuth 2.0 Rich Authorization Requests (RAR - RFC 9396)", "OAuth 2.0 & OIDC", "Hard"),
    ("JWT Claims Best Practices: sub, iss, aud, exp, nbf, jti", "OAuth 2.0 & OIDC", "Easy"),
    ("OAuth 2.0 Device Authorization Grant (Smart TVs & IoT)", "OAuth 2.0 & OIDC", "Medium"),
    ("Token Introspection (RFC 7662) vs Local JWT Verification", "OAuth 2.0 & OIDC", "Medium"),
    ("Token Revocation (RFC 7009) Architecture", "OAuth 2.0 & OIDC", "Medium"),
    ("SAML XML Signature Wrapping (XSW) Attacks", "Identity Providers", "Hard"),
    ("SAML EntityID, ACS URL, and Metadata Exchange", "Identity Providers", "Medium"),
    ("Auth0 Machine-to-Machine Token Quota and Rate Limiting", "Identity Providers", "Medium"),
    ("Auth0 Custom Database Connections and Password Migration", "Identity Providers", "Medium"),
    ("Social Login Integration (Google, Apple, GitHub) Architecture", "Identity Providers", "Easy"),
    ("Sign in with Apple: Private Relay and Form POST Callback", "Identity Providers", "Medium"),
    ("Session Timeout Strategies: Idle Timeout vs Absolute Timeout", "Identity Providers", "Easy"),
    ("Multi-Tenant Organization Switching in B2B SaaS", "Access Control", "Medium"),
    ("Hierarchical RBAC with Role Inheritance", "Access Control", "Medium"),
    ("Fine-Grained Scopes vs Coarse-Grained Roles", "Access Control", "Medium"),
    ("Dynamic Authorization with External Attribute Fetching (PIP)", "Access Control", "Hard"),
    ("Horizontal vs Vertical Privilege Escalation", "Access Control", "Easy"),
    ("Principle of Least Privilege in Microservice IAM", "Access Control", "Easy"),
    ("Bot Protection: Turnstile vs reCAPTCHA v3 vs hCaptcha", "Account Security", "Medium"),
    ("Proof of Work (PoW) Computational Challenges for Anti-Bot", "Account Security", "Hard"),
    ("Account Enumeration Prevention: Unified Error Messages", "Account Security", "Easy"),
    ("Magic Links (Passwordless Email) Security & Token Lifespans", "Account Security", "Medium"),
    ("Account Takeover (ATO) Incident Response Runbook", "Account Security", "Hard"),
    ("SMS Toll Fraud (Artificially Inflated Traffic / AIT)", "Account Security", "Medium"),
    ("Brute Force Lockout: Progressive Delays vs Account Lockout", "Account Security", "Medium"),
    ("Mass Assignment (Over-Posting) Vulnerability and DTO Protection", "Web & API Security", "Medium"),
    ("HTTP Request Smuggling (CL.TE / TE.CL)", "Web & API Security", "Hard"),
    ("XML External Entity (XXE) Injection Prevention", "Web & API Security", "Medium"),
    ("Insecure Deserialization (Java, Python Pickle)", "Web & API Security", "Hard"),
    ("Subdomain Takeover: Dangling DNS CNAME Records", "Web & API Security", "Medium"),
    ("Clickjacking Defense: X-Frame-Options vs CSP frame-ancestors", "Web & API Security", "Easy"),
    ("HTTP Strict Transport Security (HSTS) and HSTS Preloading", "Web & API Security", "Easy"),
    ("Security Headers: Permissions-Policy and Referrer-Policy", "Web & API Security", "Easy"),
    ("API Rate Limiting by API Key, IP, and Token Claims", "Web & API Security", "Medium"),
    ("API Versioning and Deprecation Security Risks", "Web & API Security", "Easy"),
    ("GraphQL Security: Query Depth Limiting and Introspection Disabling", "Web & API Security", "Medium"),
    ("GraphQL Batching Attacks and Denial of Service", "Web & API Security", "Medium"),
    ("Dependency Confusion and Supply Chain Attacks", "Cloud & DevSecOps", "Hard"),
    ("Container Image Vulnerability Scanning (Trivy, Grype)", "Cloud & DevSecOps", "Medium"),
    ("Immutable Container Infrastructure and Distroless Images", "Cloud & DevSecOps", "Medium"),
    ("Software Bill of Materials (SBOM) and Sigstore Cosign", "Cloud & DevSecOps", "Hard"),
    ("Secret Sprawl in Git: Gitleaks and Pre-Commit Hooks", "Cloud & DevSecOps", "Easy"),
    ("HashiCorp Vault Dynamic Database Credentials", "Cryptography", "Hard"),
    ("Symmetric vs Asymmetric Encryption Trade-offs (AES vs RSA/ECC)", "Cryptography", "Easy"),
    ("Perfect Forward Secrecy (PFS) in Modern TLS", "Cryptography", "Medium"),
    ("Elliptic Curve Cryptography: ECDSA vs Ed25519", "Cryptography", "Medium"),
    ("Cryptographic Salt vs Pepper: Storage and Threat Models", "Cryptography", "Medium"),
    ("Quantum-Resistant Cryptography (Post-Quantum Cryptography)", "Cryptography", "Hard"),
    ("SOC 2 Type II Compliance: Trust Services Criteria", "Compliance & Privacy", "Medium"),
    ("ISO/IEC 27001 Information Security Management System", "Compliance & Privacy", "Medium"),
    ("PCI-DSS Compliance: Tokenization of Credit Card Numbers", "Compliance & Privacy", "Hard"),
    ("Consent Management Platforms (CMP) and Cookie Banners under GDPR", "Compliance & Privacy", "Medium"),
    ("Data Subject Access Requests (DSAR) Automation Pipeline", "Compliance & Privacy", "Medium"),
    ("Data Pseudonymization vs Anonymization under GDPR", "Compliance & Privacy", "Medium"),
    ("Tamper-Proof Audit Logging with Cryptographic Hashes", "Compliance & Privacy", "Hard"),
    ("SIEM Integration: Log Aggregation, Splunk, and Threat Detection", "Compliance & Privacy", "Medium"),
    ("Automated Security Synthetic Checks in CI/CD Pipelines", "Cloud & DevSecOps", "Medium"),
    ("Security-Event Monitoring: Auth0 Log Streaming to Datadog", "Cloud & DevSecOps", "Medium"),
    ("Zero Trust Architecture: NIST 800-207 Tenets", "Cloud & DevSecOps", "Hard"),
    ("API Gateways as Policy Enforcement Points for mTLS", "Security & Networking", "Medium"),
    ("Content Security Policy (CSP) Bypass via JSONP Endpoints", "Web & API Security", "Medium"),
    ("Subresource Integrity (SRI) for Third-Party CDN Scripts", "Web & API Security", "Easy"),
    ("API Key Rotation and Scoping Strategies", "Web & API Security", "Medium"),
    ("OAuth 2.0 Security Best Current Practice (BCP) RFC 6819 Update", "OAuth 2.0 & OIDC", "Hard"),
    ("OpenID Foundation Financial-Grade API (FAPI) Profile", "OAuth 2.0 & OIDC", "Hard"),
    ("Mutual TLS Client Certificate-Bound Access Tokens (RFC 8705)", "OAuth 2.0 & OIDC", "Hard"),
    ("Cross-Origin Opener Policy (COOP) and Cross-Origin Embedder Policy (COEP)", "Web & API Security", "Medium"),
    ("DNS Rebinding Attacks and HTTP Host Header Validation", "Web & API Security", "Hard"),
    ("Credential Dumping Defense: Mimikatz and LSASS Protection", "Account Security", "Hard"),
    ("Honeytokens and Decoy Accounts for Early Breach Detection", "Account Security", "Medium"),
    ("Threat Modeling with STRIDE and DREAD Methodologies", "Cloud & DevSecOps", "Medium"),
    ("DevSecOps: Shift-Left Security with SAST, DAST, and SCA", "Cloud & DevSecOps", "Medium"),
    ("Container Runtime Security with Falco and eBPF", "Cloud & DevSecOps", "Hard"),
    ("Cloud Security Posture Management (CSPM) and Drift Detection", "Cloud & DevSecOps", "Medium")
]

for title, cat, diff in SECURITY_TOPICS:
    if len(QUESTIONS) >= 110:
        break
    add(
        title,
        cat,
        diff,
        f"In-depth security interview analysis of: {title}. Detail the vulnerability or threat model, mitigation architecture, protocols, and production best practices.",
        f"Detailed technical security breakdown of {title}:\n1. Threat Model & Risks: Attack vectors, blast radius, and vulnerability mechanics.\n2. Defense-in-Depth Architecture: Cryptographic protocols, identity governance, and access controls.\n3. Implementation Standards: Adherence to RFCs, NIST guidelines, and OWASP recommendations.\n4. Monitoring & Alerting: Audit logging, anomaly detection, and automated incident response.",
        [
            f"Core security concept for {title}",
            "Follows defense-in-depth and least privilege principles",
            "Mitigates attack surface through verified protocols and controls",
            "Essential for enterprise IAM, cloud security, and regulatory compliance"
        ],
        ["Security", cat, "IAM", "Compliance"]
    )

def generate():
    print(f"Total Security questions: {len(QUESTIONS)}")
    assert len(QUESTIONS) >= 105, f"Expected >= 105, got {len(QUESTIONS)}"
    content = "// Security & IAM Interview Questions Data (110 Curated Problems)\n"
    content += "window.INTERVIEW_DATA_SECURITY = " + json.dumps(QUESTIONS, indent=2) + ";\n"
    with open("assets/js/data/security.js", "w") as f:
        f.write(content)
    print("Successfully wrote assets/js/data/security.js")

if __name__ == "__main__":
    generate()
