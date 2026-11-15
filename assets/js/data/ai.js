// AI & Machine Learning Interview Questions Data (110 Curated Problems)
window.INTERVIEW_DATA_AI = [
  {
    "id": "ai-1",
    "title": "Scaled Dot-Product Attention: Math, Dimensions, and Scaling Factor",
    "category": "Transformer Architecture",
    "difficulty": "Medium",
    "question": "Derive the Scaled Dot-Product Attention formula: `Attention(Q, K, V) = softmax(Q * K^T / sqrt(d_k)) * V`. Why is the scaling factor `1 / sqrt(d_k)` strictly necessary?",
    "answer": "Formula:\n`Attention(Q, K, V) = softmax((Q * K^T) / sqrt(d_k)) * V`\nWhere Q: `(N, d_k)`, K: `(M, d_k)`, V: `(M, d_v)`.\nMatrix multiplication `Q * K^T` produces an `(N, M)` attention score matrix.\n\nWhy `1 / sqrt(d_k)` is strictly necessary:\nAssume components of `q` and `k` are independent random variables with mean 0 and variance 1.\nThe dot product `q \u00b7 k = sum_{i=1}^{d_k} (q_i * k_i)` has mean 0 and variance `d_k` (standard deviation `sqrt(d_k)`).\nFor large dimension `d_k` (e.g. 64 or 128), dot products grow extremely large in magnitude.\nWhen large values are fed into `softmax`, the function saturates into regions with near-zero gradients (vanishing gradient problem), stalling gradient backpropagation during training.\nDividing by `sqrt(d_k)` scales the variance back to 1, keeping softmax in a sensitive gradient regime.",
    "keyPoints": [
      "Scaling factor 1/sqrt(d_k) normalizes the dot product variance back to 1",
      "Prevents softmax saturation and vanishing gradients during backpropagation",
      "Matrix multiplication Q * K^T computes token pair similarity scores",
      "Multiplying by V yields a contextualized weighted sum of value vectors"
    ],
    "tags": [
      "Transformers",
      "Attention",
      "Deep Learning",
      "Mathematics",
      "NLP"
    ]
  },
  {
    "id": "ai-2",
    "title": "Positional Encodings: Sinusoidal vs Learned vs RoPE (Rotary Position Embedding)",
    "category": "Transformer Architecture",
    "difficulty": "Hard",
    "question": "Compare Absolute Sinusoidal, Learned, and Rotary Position Embeddings (RoPE). Why has RoPE become the standard in modern LLMs (Llama 3, Mistral, Gemma)?",
    "answer": "1. Absolute Sinusoidal (Vaswani et al. 2017):\nPrecomputed sine and cosine waves of different frequencies added to token embeddings: `PE(pos, 2i) = sin(pos / 10000^(2i/d))`. Fixed, deterministic, but doesn't naturally generalize to relative distances in inner products.\n\n2. Learned Absolute Positional Embeddings (BERT, GPT-2):\nLearnable parameter matrix `E[pos]`. Hard max length constraint (cannot extrapolate beyond max sequence length seen in pretraining).\n\n3. Rotary Position Embedding (RoPE - Su et al. 2021):\n- Represents relative position through a rotation of the Query and Key vectors in 2D complex planes.\n- For a 2D chunk of Q at position `m`, multiply by rotation matrix `R(m*theta)`: `q_m = R_theta,m * W_q * x_m`.\n- Key Property: The inner product `<q_m, k_n>` depends ONLY on the RELATIVE distance `(m - n)`: `<R_m q, R_n k> = q^T R_{n-m} k`!\n- Enables linear decay of attention with distance and natural length extrapolation (via YaRN or NTK-aware scaling).",
    "keyPoints": [
      "RoPE encodes relative token distances directly into query-key inner products",
      "Rotates 2D vector slices in the complex plane based on position index",
      "Eliminates hard sequence length boundaries of learned embeddings",
      "Standard positional encoding across Llama, Mistral, Qwen, and Gemma"
    ],
    "tags": [
      "RoPE",
      "Positional Encoding",
      "Transformers",
      "Llama",
      "Deep Learning"
    ]
  },
  {
    "id": "ai-3",
    "title": "Layer Normalization: Pre-LN vs Post-LN and RMSNorm",
    "category": "Transformer Architecture",
    "difficulty": "Medium",
    "question": "Compare Pre-LayerNorm, Post-LayerNorm, and Root Mean Square Normalization (RMSNorm). Why do modern architectures choose Pre-LN with RMSNorm?",
    "answer": "Post-LN (Original Attention is All You Need):\n`x_{t+1} = LayerNorm(x_t + SubLayer(x_t))`.\nGradients pass through the derivative of LayerNorm at each layer. For deep networks (>20 layers), gradients vanish or explode near input layers, requiring delicate warmup learning rates.\n\nPre-LN (GPT-3, Modern Standard):\n`x_{t+1} = x_t + SubLayer(LayerNorm(x_t))`.\nClean residual identity path allows gradients to flow directly from output to input without attenuation. Enables stable training of 100B+ parameter models without warmup instability.\n\nRMSNorm (Root Mean Square Normalization - Llama):\nObserves that LayerNorm's mean-centering step `(x - mu)` contributes negligibly to training stability. RMSNorm normalizes solely by root-mean-square: `x_i / sqrt(1/d * sum(x_j^2) + eps) * gamma_i`.\nCuts normalization compute by 20-30% with zero loss in training accuracy.",
    "keyPoints": [
      "Pre-LN provides an unimpeded residual skip connection stabilizing deep network gradients",
      "Post-LN suffers from vanishing gradients requiring delicate warmup schedules",
      "RMSNorm eliminates mean calculation, boosting throughput by 20-30%",
      "RMSNorm is standard across Llama, Mistral, and Gemma"
    ],
    "tags": [
      "RMSNorm",
      "LayerNorm",
      "Deep Learning",
      "Transformers",
      "Optimization"
    ]
  },
  {
    "id": "ai-4",
    "title": "Multi-Head Attention (MHA) vs Multi-Query (MQA) vs Grouped-Query Attention (GQA)",
    "category": "Transformer Architecture",
    "difficulty": "Hard",
    "question": "How does Grouped-Query Attention (GQA) reduce KV cache memory consumption during autoregressive generation while retaining Multi-Head Attention quality?",
    "answer": "The Memory Bottleneck: During autoregressive text generation, the KV Cache grows with batch size, sequence length, and number of layers, consuming dozens of gigabytes of GPU VRAM.\n\nArchitectures:\n1. Multi-Head Attention (MHA - e.g. GPT-3):\n`H` Query heads, `H` Key heads, `H` Value heads. Max expressive power, but massive KV cache memory footprint (requires caching `H` KV heads per layer).\n\n2. Multi-Query Attention (MQA - e.g. Falcon):\n`H` Query heads, but only ONE shared Key head and ONE shared Value head across all query heads! Reduces KV cache memory by factor of `H` (e.g. 32x), but suffers from quality degradation and capacity loss.\n\n3. Grouped-Query Attention (GQA - e.g. Llama 2 70B, Llama 3):\nPartitions `H` query heads into `G` groups (e.g. 8 groups of 4 heads). Each group shares 1 Key head and 1 Value head.\nGolden Mean: Delivers 99% of MHA model quality while slashing KV cache memory and memory bandwidth consumption by 4-8x!",
    "keyPoints": [
      "KV cache memory bandwidth is the primary bottleneck during LLM inference",
      "MHA uses 1 KV head per Q head (maximum memory)",
      "MQA uses 1 shared KV head for all Q heads (causes quality drops)",
      "GQA groups Q heads (e.g. 8 groups) balancing quality and inference speed"
    ],
    "tags": [
      "GQA",
      "MQA",
      "MHA",
      "KV Cache",
      "Llama",
      "Inference"
    ]
  },
  {
    "id": "ai-5",
    "title": "FlashAttention: GPU SRAM vs HBM Tiling",
    "category": "Transformer Architecture",
    "difficulty": "Hard",
    "question": "Explain how FlashAttention (Dao et al.) achieves 2-4x speedups and linear memory scaling without approximating attention math. What is GPU memory tiling?",
    "answer": "GPU Hardware Reality:\n- HBM (High Bandwidth Memory / VRAM): Large (80GB on A100), but slow (2 TB/s).\n- SRAM (On-chip Cache): Tiny (192KB per Streaming Multiprocessor), but ultra-fast (19 TB/s).\n\nStandard Attention Bottleneck:\nStandard PyTorch attention computes `S = Q * K^T` (writes N x N matrix to slow HBM), reads back to compute `P = softmax(S)` (writes to HBM), reads back to compute `O = P * V`.\nFor sequence length 8192, N x N is 67 million floats per head. Memory I/O to HBM is the bottleneck, NOT FLOPS!\n\nFlashAttention Innovation (IO-Aware Tiling):\n1. Tiling: Loads blocks of Q, K, and V into fast on-chip SRAM cache.\n2. Online Softmax (Milakov & Gimelshein): Computes softmax incrementally across blocks using running maximum and normalization sum without ever materializing the full N x N matrix in HBM!\n3. Backward Recomputation: In backward pass, recomputes attention on-the-fly in SRAM from saved output blocks rather than storing intermediate N x N attention matrices in VRAM.\nResult: Exact attention (zero approximation), O(N) memory instead of O(N\u00b2), 2-4x wall-clock speedup.",
    "keyPoints": [
      "Attention is memory-bandwidth bound (IO-bound), not compute (FLOP) bound",
      "GPU SRAM is 10x faster than HBM GPU RAM",
      "Online softmax computes attention in SRAM blocks without materializing N x N matrix",
      "Reduces memory from O(N\u00b2) to O(N) while maintaining mathematical exactness"
    ],
    "tags": [
      "FlashAttention",
      "GPU",
      "CUDA",
      "Optimization",
      "Transformers"
    ]
  },
  {
    "id": "ai-6",
    "title": "Activation Functions: ReLU vs GeLU vs SwiGLU",
    "category": "Transformer Architecture",
    "difficulty": "Medium",
    "question": "Compare ReLU, GeLU, and SwiGLU activation functions. Why do modern LLMs use SwiGLU in their Feed-Forward Network (FFN) blocks?",
    "answer": "1. ReLU: `max(0, x)`. Fast, but hard zero cutoff causes 'dying ReLU' neuron death when inputs are negative.\n2. GeLU (Gaussian Error Linear Unit - BERT, GPT-2):\n`GeLU(x) = x * Phi(x) = x * P(X <= x)` where X ~ N(0, 1).\nSmooth non-linear curve with non-zero gradient for negative values. Standard for first-generation transformers.\n\n3. SwiGLU (Swish Gated Linear Unit - Shazeer 2020 / PaLM / Llama):\nCombines Swish activation with Gated Linear Unit (GLU):\n`SwiGLU(x) = Swish(x * W_gate) * (x * W_up)` where `Swish(z) = z * sigmoid(beta * z)`.\nFFN layer projection:\n`FFN(x) = (Swish(x * W_gate) * (x * W_up)) * W_down`.\nBenefits: Multiplicative gating allows the model to dynamically suppress or amplify specific feature representations. Empirically yields lower perplexity and faster convergence across LLM benchmarks.",
    "keyPoints": [
      "SwiGLU introduces dynamic multiplicative gating to feed-forward blocks",
      "GeLU provides smooth probabilistic thresholding over hard ReLU cutoffs",
      "SwiGLU uses three weight matrices (gate, up, down) per FFN layer",
      "Adopted by Llama, Mistral, PaLM, and modern open-weights LLMs"
    ],
    "tags": [
      "SwiGLU",
      "GeLU",
      "Activation Functions",
      "Deep Learning",
      "Transformers"
    ]
  },
  {
    "id": "ai-7",
    "title": "Scaling Laws: Kaplan et al. vs Chinchilla (Hoffmann et al.)",
    "category": "Pre-Training",
    "difficulty": "Hard",
    "question": "Compare the Kaplan et al. (OpenAI 2020) and Chinchilla (DeepMind 2022) scaling laws. Why was GPT-3 severely under-trained?",
    "answer": "Kaplan et al. (2020):\nArgued that model size (parameters `N`) should scale faster than training tokens (`D`): for every 73% increase in parameters, training tokens only needed to increase by 27%.\nResult: Led to massive models trained on relatively few tokens (e.g. GPT-3: 175B parameters trained on only 300B tokens; Gopher: 280B parameters on 300B tokens).\n\nChinchilla Scaling Laws (Hoffmann et al. 2022):\nDisproved Kaplan by identifying that learning rate schedules had not been adjusted per model size. Proved that parameters `N` and tokens `D` should scale in EQUAL PROPORTION (1:1 ratio):\n`D_tokens \u2248 20 * N_parameters`.\n\nImpact:\n- For a given compute budget, models should be smaller but trained on vastly more tokens.\n- Chinchilla (70B params, 1.4T tokens) outperformed Gopher (280B params) while costing 4x less VRAM at inference.\n- Modern open models push this further (Llama 3 8B trained on 15T tokens: ~1800 tokens/param) for extreme inference efficiency.",
    "keyPoints": [
      "Kaplan favored scaling parameter count over token count",
      "Chinchilla proved parameters and tokens should scale in 1:1 proportion",
      "Compute-optimal rule: ~20 tokens per parameter during pretraining",
      "Inference economics favor over-training smaller models (Llama 3: 15T tokens on 8B)"
    ],
    "tags": [
      "Scaling Laws",
      "Chinchilla",
      "Pre-Training",
      "LLM",
      "Compute"
    ]
  },
  {
    "id": "ai-8",
    "title": "Tokenization Algorithms: BPE vs WordPiece vs SentencePiece",
    "category": "Pre-Training",
    "difficulty": "Medium",
    "question": "Compare Byte Pair Encoding (BPE), WordPiece, and SentencePiece. Why did Byte-level BPE solve the out-of-vocabulary (OOV) problem for multilingual text?",
    "answer": "1. Byte Pair Encoding (BPE - GPT-2, GPT-4, Llama):\n- Starts with character vocabulary. Iteratively counts the most frequent adjacent character pair in corpus and merges into a new token until desired vocabulary size (e.g. 32K-128K) is reached.\n- Byte-level BPE: Treats input as arbitrary UTF-8 bytes (256 base vocabulary). Any Unicode character or language can be represented as bytes, completely eliminating Out-Of-Vocabulary (OOV) `<unk>` tokens!\n\n2. WordPiece (BERT):\n- Instead of merging highest frequency pair, merges pairs that maximize the likelihood of the training data under a unigram language model. Prepends `##` to subwords.\n\n3. SentencePiece (T5, Llama):\n- Treats raw text as a sequence of characters including whitespace (represented as `_`), operating directly on raw strings without language-specific pre-tokenization rules (crucial for languages without spaces like Chinese and Japanese).",
    "keyPoints": [
      "Byte-level BPE operates on raw UTF-8 bytes eliminating OOV <unk> tokens",
      "BPE merges most frequent pairs; WordPiece maximizes corpus likelihood",
      "SentencePiece treats whitespace as a character (_) enabling uniform multilingual parsing",
      "Larger vocabulary (e.g. Llama 3 128K vs Llama 2 32K) improves token compression efficiency"
    ],
    "tags": [
      "Tokenization",
      "BPE",
      "SentencePiece",
      "Multilingual",
      "NLP"
    ]
  },
  {
    "id": "ai-9",
    "title": "Mixture of Experts (MoE): Sparse Routing and Load Balancing",
    "category": "Pre-Training",
    "difficulty": "Hard",
    "question": "Explain Mixture of Experts (MoE) architecture (Mixtral 8x7B, DeepSeek-V3). How does the gating network select Top-K experts, and what is the auxiliary load-balancing loss?",
    "answer": "Concept:\nReplaces the standard dense FFN layer with `E` independent expert FFN networks. For every token, a learned router / gating network dynamically activates only `k` experts (e.g. Top-2 of 8 experts).\n\nMath:\n`Gating score G(x) = Softmax(TopK(x * W_g, k))`\n`Output = sum_{i in TopK} G(x)_i * Expert_i(x)`.\nTotal parameters: 8x7B = ~47B params, but each token only activates 13B parameters during forward pass, delivering 47B model quality at 13B compute speed!\n\nAuxiliary Load Balancing Loss:\nProblem: Routing collapse. Gating network naturally prefers 1 or 2 favorite experts, leaving other experts untrained and creating GPU memory imbalance.\nSolution: Add auxiliary loss `L_aux = alpha * E * sum_{i=1}^E (f_i * P_i)` where `f_i` is fraction of tokens routed to expert `i` and `P_i` is average router probability assigned to expert `i`. Penalizes uneven expert allocation.",
    "keyPoints": [
      "Activates only a sparse subset (e.g. Top-2) of experts per token",
      "Delivers large parameter quality with small parameter inference compute latency",
      "Router gating network uses Softmax over Top-K linear projections",
      "Auxiliary load balancing loss prevents expert collapse"
    ],
    "tags": [
      "MoE",
      "Mixtral",
      "Sparse Models",
      "DeepSeek",
      "Transformers"
    ]
  },
  {
    "id": "ai-10",
    "title": "LoRA (Low-Rank Adaptation): Mathematical Formulation and Hyperparameters",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Hard",
    "question": "Derive the LoRA (Low-Rank Adaptation) update equation: `W = W_0 + (alpha / r) * (B * A)`. Explain rank `r`, alpha scaling, initialization, and memory savings.",
    "answer": "Mathematical Formulation:\nDuring full fine-tuning, weight matrix `W_0 in R^{d x k}` is updated by `Delta W`: `W = W_0 + Delta W`.\nHypothesis (Aghajanyan et al.): Weight updates during domain adaptation have a very low 'intrinsic rank'.\nLoRA decomposes `Delta W` into two low-rank matrices:\n`Delta W = B * A` where `A in R^{r x k}` and `B in R^{d x r}` with rank `r << min(d, k)`.\nForward pass:\n`h = W_0 * x + (alpha / r) * (B * A * x)`\n\nKey Details:\n1. Initialization: `A` is initialized with Gaussian random values `N(0, sigma^2)`; `B` is initialized to EXACT ZERO. Thus, `Delta W = 0` at training start, preserving base model weights.\n2. Alpha Scaling `alpha / r`: Acts like a learning rate multiplier. Setting `alpha = 2 * r` is standard practice; fixing alpha allows changing rank `r` without retuning learning rates.\n3. Zero Inference Latency: At deployment, merge weights: `W_new = W_0 + (alpha / r) * (B * A)` back into base weights. Zero extra latency!\n4. Memory Savings: Freezes 99.8% of weights. Cuts optimizer states (Adam momentum/variance) by over 90%.",
    "keyPoints": [
      "Decomposes weight update Delta W into low-rank matrices B * A",
      "Matrix B initialized to 0 ensures initial identity with base model",
      "alpha / r constant scaling stabilizes training across different ranks",
      "Weights can be merged back into W0 for zero inference latency overhead"
    ],
    "tags": [
      "LoRA",
      "PEFT",
      "Fine-Tuning",
      "LLM",
      "Optimization"
    ]
  },
  {
    "id": "ai-11",
    "title": "QLoRA: 4-bit NormalFloat (NF4), Double Quantization, and Paged Optimizers",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Hard",
    "question": "How does QLoRA (Dettmers et al.) enable fine-tuning a 70B parameter LLM on a single 48GB GPU? Detail NF4 quantization and Double Quantization.",
    "answer": "QLoRA combines three innovations:\n1. 4-bit NormalFloat (NF4) Data Type:\nInformation-theoretically optimal quantile quantization for normally distributed weights. Divides standard normal distribution `N(0, 1)` into 16 equal-probability bins. Outperforms standard FP4 and INT4 quantization precision.\n\n2. Double Quantization (DQ):\nQuantization requires storing quantization constants (scale factors). Standard quantization scales cost 0.5 bits per parameter. Double Quantization quantizes the quantization constants themselves from 32-bit floats to 8-bit floats, saving ~0.37 bits/param (3GB savings on a 65B model).\n\n3. Paged Optimizers (CUDA Unified Memory):\nUses NVIDIA Unified Memory to automatically page AdamW optimizer states from GPU VRAM to CPU RAM during memory spikes (e.g. processing long context sequences), preventing Out-of-Memory (OOM) crashes.\n\nResult: 65B/70B model base weights compressed to ~35GB in 4-bit VRAM; LoRA adapters trained in 16-bit BF16 on a single commodity GPU.",
    "keyPoints": [
      "NF4 is information-theoretically optimal for normally distributed weights",
      "Base weights kept in 4-bit; computations dequantized on-the-fly to BF16",
      "Double Quantization quantizes quantization constants saving memory",
      "Paged Optimizers page memory spikes to CPU RAM preventing OOMs"
    ],
    "tags": [
      "QLoRA",
      "Quantization",
      "PEFT",
      "Fine-Tuning",
      "GPU"
    ]
  },
  {
    "id": "ai-12",
    "title": "Supervised Fine-Tuning (SFT) Loss Masking on Completion Tokens",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Why must the Cross-Entropy loss in Supervised Fine-Tuning (SFT) be masked over prompt/instruction tokens? What happens if you compute loss on the prompt?",
    "answer": "In instruction datasets: `[User Prompt / Context] -> [Assistant Response]`.\n\nWhy Mask Prompt Tokens (set label to `-100` in PyTorch):\n- The goal of SFT is to teach the model HOW TO GENERATE HELPFUL RESPONSES conditioned on the prompt.\n- If you compute loss on the prompt tokens, the model wastes gradient updates trying to predict the user's prompt (learning user typing styles rather than learning how to follow instructions).\n- Loss Masking: Set `labels[i] = -100` for all prompt tokens. PyTorch `CrossEntropyLoss(ignore_index=-100)` ignores these positions, calculating loss and backpropagating gradients SOLELY on the assistant's completion tokens.",
    "keyPoints": [
      "Mask prompt token labels with -100 to exclude from cross-entropy loss",
      "Focuses gradient backpropagation entirely on instruction-following output",
      "Prevents model from overfitting to specific prompt syntax and phrasing",
      "Standard implementation in HuggingFace TRL (SFTTrainer)"
    ],
    "tags": [
      "SFT",
      "Fine-Tuning",
      "Loss Functions",
      "LLM",
      "HuggingFace"
    ]
  },
  {
    "id": "ai-13",
    "title": "Instruction Fine-Tuning vs Domain Adaptation Fine-Tuning",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Contrast Domain Adaptation (Continued Pre-training) and Instruction Fine-Tuning (SFT). How did Ajay apply this in his Master's thesis on EV sentiment analysis?",
    "answer": "1. Domain Adaptation (Continued Pre-training):\n- Objective: Teach model domain vocabulary, jargon, and syntax (e.g. EV battery specs, automotive charging protocols, German/Norwegian EV terminology).\n- Data: Unsupervised raw domain text.\n- Loss: Standard causal language modeling loss over all tokens.\n\n2. Instruction Fine-Tuning (SFT):\n- Objective: Teach model task structure and conversational behavior (e.g. 'Classify sentiment as Positive/Negative/Neutral' or 'Generate survey questions grounded in this EV review').\n- Data: High-quality curated input/output instruction pairs.\n- Loss: Cross-entropy masked to target completion tokens.\n\nAjay's Master's Thesis Pipeline:\nFine-tuned transformer LLMs on multilingual automotive reviews (EN, DE, CN, NO) for sentiment classification, followed by instruction-tuning with context grounding to generate structured consumer perception survey questions.",
    "keyPoints": [
      "Domain adaptation teaches industry vocabulary via unsupervised text",
      "Instruction tuning aligns model to follow specific output formats and tasks",
      "Multilingual sentiment analysis requires cross-lingual transfer representations",
      "Context engineering grounds generated survey questions in source reviews"
    ],
    "tags": [
      "Fine-Tuning",
      "Sentiment Analysis",
      "EV",
      "Multilingual",
      "Domain Adaptation"
    ]
  },
  {
    "id": "ai-14",
    "title": "RLHF (Reinforcement Learning from Human Feedback) with PPO",
    "category": "Alignment & RLHF",
    "difficulty": "Hard",
    "question": "Walk through the 3-step RLHF pipeline: SFT, Reward Modeling, and PPO. Why is the KL-divergence penalty critical to prevent reward hacking?",
    "answer": "3-Step RLHF Pipeline:\n1. Supervised Fine-Tuning (SFT): Train base model on high-quality demonstration prompts and answers.\n2. Reward Model Training:\n- Human annotators rank model completions: `y_w` (preferred) > `y_l` (rejected).\n- Train Reward Model `r_theta(x, y)` using Bradley-Terry preference loss:\n  `Loss = -E[log(sigmoid(r_theta(x, y_w) - r_theta(x, y_l)))]`.\n3. PPO (Proximal Policy Optimization):\n- Optimize policy `pi_phi` to maximize reward score: `max E[r_theta(x, y)]`.\n\nWhy KL-Divergence Penalty is Critical:\nWithout constraint, the policy suffers from Reward Hacking (gaming the reward model by generating repetitive punctuation, flattering phrases, or nonsensical text that scores high on the proxy reward function).\nObjective with KL penalty:\n`Reward = r_theta(x, y) - beta * D_KL(pi_phi(y|x) || pi_ref(y|x))`.\nPenalizes the policy from drifting too far from the original reference SFT model.",
    "keyPoints": [
      "Step 1: Supervised Fine-Tuning; Step 2: Reward Model; Step 3: PPO Policy Optimization",
      "Bradley-Terry loss trains reward model on pairwise human rankings",
      "KL divergence penalty prevents reward hacking and policy degeneration",
      "Maintains language fluency while aligning with human preferences"
    ],
    "tags": [
      "RLHF",
      "PPO",
      "Reward Model",
      "Alignment",
      "LLM"
    ]
  },
  {
    "id": "ai-15",
    "title": "Direct Preference Optimization (DPO) vs RLHF",
    "category": "Alignment & RLHF",
    "difficulty": "Hard",
    "question": "Derive the intuition behind Direct Preference Optimization (DPO - Rafailov et al.). How does DPO eliminate the need for training a separate reward model and running PPO?",
    "answer": "The Flaw of RLHF with PPO:\nPPO is notoriously unstable, hyperparameter-sensitive, and requires loading 4 models simultaneously into GPU memory (Actor policy, Reference policy, Critic value model, Reward model).\n\nDPO Breakthrough:\nRafailov et al. proved mathematically that the ground-truth reward function can be expressed closed-form in terms of the optimal policy `pi^*` and reference policy `pi_ref`:\n`r(x, y) = beta * log(pi(y|x) / pi_ref(y|x)) + beta * log Z(x)`.\nSubstituting this into the Bradley-Terry preference loss yields the DPO Objective:\n`L_DPO = -E_{(x, y_w, y_l)} [log sigmoid( beta * log(pi(y_w|x) / pi_ref(y_w|x)) - beta * log(pi(y_l|x) / pi_ref(y_l|x)) )]`.\n\nWhy DPO is Revolutionary:\n- Directly optimizes policy weights using standard classification cross-entropy loss!\n- Eliminates the separate reward model.\n- Eliminates PPO reinforcement learning sampling loop completely.\n- Highly stable, faster, and reproducible.",
    "keyPoints": [
      "Mathematically reparameterizes reward function in terms of policy probabilities",
      "Directly optimizes model policy on pairwise preference data (preferred vs rejected)",
      "Eliminates need for separate reward model and unstable PPO reinforcement loop",
      "Requires only Actor and frozen Reference model in memory during training"
    ],
    "tags": [
      "DPO",
      "RLHF",
      "Alignment",
      "Optimization",
      "LLM"
    ]
  },
  {
    "id": "ai-16",
    "title": "Naive RAG vs Advanced RAG: Chunking, Indexing, Retrieval, and Synthesis",
    "category": "RAG & Vector Search",
    "difficulty": "Medium",
    "question": "Compare Naive RAG with Advanced RAG. Detail chunking strategies, hybrid search, cross-encoder re-ranking, and context synthesis.",
    "answer": "Naive RAG Workflow:\nQuery -> Embed -> Vector Cosine Similarity Search -> Top-K chunks -> Concatenate into LLM prompt.\nFailure modes: Irrelevant chunks retrieved due to semantic gap; lost context across arbitrary chunk splits; hallucinations.\n\nAdvanced RAG Workflow:\n1. Pre-Retrieval:\n- Semantic / Recursive Chunking with chunk overlap (256-512 tokens with 50-token overlap).\n- Metadata extraction (title, section, dates) stored with chunks.\n- Query Rewriting: LLM expands query into multiple search variants.\n2. Retrieval (Hybrid Search):\n- Combines Dense Vector Search (semantic similarity via embeddings) with Sparse Keyword Search (BM25 for exact product names/IDs) using Reciprocal Rank Fusion (RRF).\n3. Post-Retrieval (Re-ranking):\n- Cross-Encoder re-ranks top 50 candidates down to top 5 most relevant chunks.\n4. Synthesis:\n- Grounding prompt with citation attribution: 'Answer using ONLY provided context; cite chunk IDs'.",
    "keyPoints": [
      "Naive RAG suffers from semantic mismatch and arbitrary chunk boundary cuts",
      "Hybrid search combines dense vector semantics with BM25 keyword matching",
      "Cross-Encoder re-ranker accurately scores query-passage pairs",
      "Citation attribution grounds LLM synthesis and mitigates hallucinations"
    ],
    "tags": [
      "RAG",
      "Vector Search",
      "BM25",
      "Hybrid Search",
      "Embeddings"
    ]
  },
  {
    "id": "ai-17",
    "title": "Vector Indexing: HNSW (Hierarchical Navigable Small World) vs IVFFlat",
    "category": "RAG & Vector Search",
    "difficulty": "Hard",
    "question": "How does the HNSW (Hierarchical Navigable Small World) algorithm achieve sub-10ms Approximate Nearest Neighbor (ANN) search across millions of vectors? Compare with IVFFlat.",
    "answer": "The Problem: Brute-force exact search (Flat) compares query against every vector: O(N * d). Impossible at scale (>10M vectors).\n\n1. IVFFlat (Inverted File Index):\n- Uses K-Means clustering to partition vector space into `nlist` Voronoi cells.\n- At query time: inspects only the centroids closest to query (`nprobe` cells). Fast, but lower recall on high-dimensional vectors.\n\n2. HNSW (Hierarchical Navigable Small World - Gold Standard):\n- Multi-layer graph inspired by SkipLists.\n- Top Layer: Sparse graph with long-range edges for coarse, fast navigation across vector space.\n- Lower Layers: Increasingly dense graphs with short-range edges connecting nearest neighbors.\n- Query Search: Greedy routing starts at top layer; jumps along long edges towards query vector; drops down a layer upon reaching local minimum; repeats until reaching bottom layer.\n- Complexity: O(log N) search time with 99%+ recall!\n- Used in Milvus, Pinecone, Qdrant, Weaviate, pgvector.",
    "keyPoints": [
      "HNSW uses multi-layer skip-graph structure for O(log N) nearest neighbor search",
      "Greedy graph traversal starts at coarse top layer and refines downwards",
      "IVFFlat uses K-Means Voronoi partitioning; faster indexing but lower recall",
      "HNSW provides superior recall (>99%) at sub-10ms search latencies"
    ],
    "tags": [
      "HNSW",
      "Vector Search",
      "ANN",
      "Embeddings",
      "Vector DB"
    ]
  },
  {
    "id": "ai-18",
    "title": "Hybrid Search with Reciprocal Rank Fusion (RRF)",
    "category": "RAG & Vector Search",
    "difficulty": "Medium",
    "question": "Why does pure vector search fail on exact keywords (part numbers, error codes)? How does Reciprocal Rank Fusion (RRF) combine BM25 and Dense Embeddings?",
    "answer": "Why Dense Embeddings Fail on Keywords:\nEmbedding models map semantic concepts to vectors. 'Error Code 0x80070005' and 'Error Code 0x80070002' have almost identical cosine similarity (both mean Windows error), but describe completely different bugs! Vector search cannot do exact string matching.\n\nBM25 (Sparse Keyword Search):\nComputes term frequency-inverse document frequency. Excels at exact keywords, names, part numbers.\n\nReciprocal Rank Fusion (RRF) Formula:\nCombines ranked lists from BM25 and Vector Search without needing score normalization:\n`RRF_Score(doc) = sum_{m in models} 1 / (k + rank_m(doc))`\nWhere `k` is a smoothing constant (typically 60).\nA document appearing in the top 5 of both BM25 and Vector search receives a massive composite score boost, ensuring both keyword precision and semantic breadth.",
    "keyPoints": [
      "Dense vectors fail on exact alphanumeric codes, SKU numbers, and error codes",
      "BM25 excels at exact keyword matching based on term frequency",
      "RRF fuses ranked lists without requiring score scale normalization",
      "Industry best practice across Elasticsearch, Pinecone, and Azure AI Search"
    ],
    "tags": [
      "Hybrid Search",
      "RRF",
      "BM25",
      "Vector Search",
      "RAG"
    ]
  },
  {
    "id": "ai-19",
    "title": "Re-Ranking: Cross-Encoders vs Bi-Encoders and ColBERT",
    "category": "RAG & Vector Search",
    "difficulty": "Hard",
    "question": "Compare Bi-Encoders, Cross-Encoders, and ColBERT (Late Interaction). Why is a two-tier retrieval architecture (Bi-Encoder + Cross-Encoder) optimal for production RAG?",
    "answer": "1. Bi-Encoders (e.g. OpenAI text-embedding-3, BGE, E5):\n- Encodes Query `E(Q)` and Document `E(D)` independently into fixed vectors.\n- Similarity computed via dot product: `E(Q) \u00b7 E(D)`.\n- Pros: Document embeddings precomputed and indexed in HNSW. Blazing fast retrieval (10ms).\n- Cons: No cross-attention between query words and document words (lower ranking accuracy).\n\n2. Cross-Encoders (e.g. Cohere Rerank, BGE-Reranker):\n- Feeds query AND document concatenated into transformer simultaneously: `[CLS] Query [SEP] Document [SEP]`.\n- Full cross-attention between every query token and document token!\n- Pros: Extreme ranking accuracy.\n- Cons: Slow (cannot precompute; must evaluate neural network on-the-fly for every pair).\n\nTwo-Tier Production Architecture:\n- Tier 1 (Bi-Encoder): HNSW retrieves top 50 candidates from 10 million docs in 10ms.\n- Tier 2 (Cross-Encoder): Re-ranks the 50 candidates down to top 5 in 30ms.",
    "keyPoints": [
      "Bi-encoders compute independent embeddings; fast vector retrieval",
      "Cross-encoders evaluate full cross-attention between query and passage tokens",
      "ColBERT late interaction matches token embeddings via MaxSim",
      "Two-tier retrieval achieves high throughput (Bi-Encoder) and high precision (Cross-Encoder)"
    ],
    "tags": [
      "Re-Ranking",
      "Cross-Encoder",
      "ColBERT",
      "RAG",
      "Embeddings"
    ]
  },
  {
    "id": "ai-20",
    "title": "Context Engineering: The 'Lost in the Middle' Phenomenon",
    "category": "Context Engineering",
    "difficulty": "Medium",
    "question": "Explain Liu et al.'s 'Lost in the Middle' finding in long-context LLMs. How do attention distributions degrade, and how should prompt context be engineered?",
    "answer": "The 'Lost in the Middle' Finding (Liu et al. 2023):\nLanguage models are significantly better at retrieving and reasoning over information placed at the very BEGINNING (Primacy Effect) or very END (Recency Effect) of their context window.\nPerformance plummets dramatically (up to 30-40% drop in retrieval accuracy) when critical information is placed in the middle of long contexts, even in models boasting 128K or 1M context windows!\n\nWhy It Occurs:\nSoftmax attention distribution naturally attends heavily to initial tokens (attention sinks) and recent tokens due to causal masking and relative positional bias.\n\nContext Engineering Strategies:\n1. Place system instructions and rules at the very beginning.\n2. Place the most relevant retrieved RAG passages at the beginning and end of the prompt; bury less critical background in the middle.\n3. Place the user's specific task/query at the very END of the prompt immediately preceding generation.",
    "keyPoints": [
      "Models recall information best at the start and end of prompt context",
      "Information placed in the middle experiences severe retrieval degradation",
      "Causal attention dynamics naturally favor initial and recent tokens",
      "Context engineering places query and critical RAG chunks at prompt boundaries"
    ],
    "tags": [
      "Context Engineering",
      "Prompt Engineering",
      "Attention Sinks",
      "LLM"
    ]
  },
  {
    "id": "ai-21",
    "title": "Multilingual Sentiment Analysis and Aspect-Based Sentiment Analysis (ABSA)",
    "category": "NLP & Sentiment",
    "difficulty": "Hard",
    "question": "How does Aspect-Based Sentiment Analysis (ABSA) differ from document-level sentiment classification? Detail Ajay's thesis approach on EV consumer perception across EN/DE/CN/NO.",
    "answer": "Document-Level Sentiment vs ABSA:\n- Document-Level: Assigns single label (Positive/Negative) to entire text. Problem: 'The electric motor acceleration is incredible (+), but the charging software freezes repeatedly (-)' -> Document-level classification produces noisy neutral.\n- Aspect-Based Sentiment Analysis (ABSA): Identifies specific aspects (Battery Range, Charging Speed, Infotainment, Build Quality) and assigns independent sentiment polarities to each aspect!\n\nMultilingual Pipeline (Master's Thesis Research):\n1. Multilingual Transformer Backbone: XLM-RoBERTa / fine-tuned multilingual LLM capturing cross-lingual transfer representations across English, German, Chinese, and Norwegian.\n2. Aspect Extraction: Sequence labeling (BIO tagging) or instruction-tuned JSON generation extracting `(Aspect, Sentiment, Opinion Phrase)` tuples.\n3. Grounded Question Generation: Context engineering pipeline summarizes regional consumer pain points and generates targeted survey questionnaires grounded in source review content.",
    "keyPoints": [
      "ABSA extracts fine-grained sentiment per entity feature (battery, charging, software)",
      "Document-level classification fails on mixed consumer reviews",
      "Cross-lingual transfer models (XLM-R) generalize across multiple languages",
      "Grounded generation transforms extracted sentiment aspects into survey questions"
    ],
    "tags": [
      "Sentiment Analysis",
      "ABSA",
      "Multilingual",
      "NLP",
      "Electric Vehicles"
    ]
  },
  {
    "id": "ai-22",
    "title": "Model Quantization: INT8, INT4, AWQ, and GPTQ",
    "category": "Quantization & Serving",
    "difficulty": "Hard",
    "question": "Compare Post-Training Quantization (PTQ) techniques: Weight-Only (GPTQ, AWQ) vs Weight-and-Activation (SmoothQuant, FP8). Why is AWQ superior for preservation of salient weights?",
    "answer": "Quantization Principles: Compresses 16-bit floats (FP16/BF16) into 8-bit or 4-bit integers, reducing VRAM by 2-4x and increasing inference memory-bandwidth throughput.\n\n1. GPTQ (Accurate Post-Training Quantization for GPT):\n- Second-order Taylor series approximation (Hessian matrix). Quantizes weights layer-by-layer, adjusting unquantized weights to compensate for quantization error.\n\n2. AWQ (Activation-aware Weight Quantization - SOTA Weight-Only):\n- Key Insight: Not all weights are equally important! Weights corresponding to channels with large activation magnitudes ('salient weights') contain critical knowledge.\n- Protecting just the top 1% of salient weights in full precision (or scaling them before quantization) prevents perplexity degradation in 4-bit models.\n\n3. FP8 (Floating Point 8 - H100 native):\n- E4M3 and E5M2 formats. Native hardware execution with zero accuracy loss for both inference and training.",
    "keyPoints": [
      "Quantization slashes GPU VRAM footprint and memory bandwidth bottlenecks",
      "AWQ protects top 1% salient weights based on activation magnitudes",
      "GPTQ uses Hessian error compensation across weight layers",
      "FP8 is natively accelerated on modern Hopper and Blackwell GPUs"
    ],
    "tags": [
      "Quantization",
      "AWQ",
      "GPTQ",
      "MLOps",
      "LLM Serving"
    ]
  },
  {
    "id": "ai-23",
    "title": "vLLM and PagedAttention: Eliminating KV Cache Fragmentation",
    "category": "Quantization & Serving",
    "difficulty": "Hard",
    "question": "Explain why standard KV cache allocation wastes up to 80% of GPU memory through internal and external fragmentation. How does vLLM's PagedAttention solve this?",
    "answer": "The Fragmentation Problem in Standard Serving:\nIn standard PyTorch serving (e.g. HuggingFace Transformers), KV Cache tensors must be stored in contiguous physical GPU memory. Because output token lengths are unknown in advance, systems pre-allocate contiguous memory for max sequence length (e.g. 2048 tokens).\n- Internal Fragmentation: Pre-allocated slots reserved for tokens that are never generated.\n- External Fragmentation: Variable sequence lengths leave scattered unallocatable memory gaps.\n- Up to 60-80% of GPU memory is wasted on unassigned KV cache buffers!\n\nPagedAttention (Kwon et al. 2023 - vLLM):\nInspired by Operating System Virtual Memory Paging:\n1. Divides KV cache into fixed-size physical blocks (e.g. 16 tokens per block).\n2. A Block Table maps logical token positions to physical blocks scattered non-contiguously across VRAM.\n3. Allocates physical blocks dynamically on-the-fly as new tokens are generated.\n4. Copy-on-Write (CoW): Enables multiple parallel generation branches (beam search, parallel sampling) to share identical prompt KV cache blocks safely!\nResult: Reduces wasted memory to <4%, allowing 2-4x larger batch sizes and 2-4x higher serving throughput.",
    "keyPoints": [
      "Pre-allocating contiguous KV cache memory wastes up to 80% of GPU VRAM",
      "PagedAttention mirrors OS virtual memory paging using non-contiguous block tables",
      "Allocates fixed 16-token memory blocks on-the-fly as generation proceeds",
      "Dramatically boosts serving throughput and concurrency in vLLM"
    ],
    "tags": [
      "vLLM",
      "PagedAttention",
      "KV Cache",
      "MLOps",
      "LLM Serving"
    ]
  },
  {
    "id": "ai-24",
    "title": "Transformer Encoder-Only vs Decoder-Only vs Encoder-Decoder",
    "category": "Transformer Architecture",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Transformer Encoder-Only vs Decoder-Only vs Encoder-Decoder. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Transformer Encoder-Only vs Decoder-Only vs Encoder-Decoder:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Transformer Encoder-Only vs Decoder-Only vs Encoder-Decoder",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Transformer Architecture",
      "LLM"
    ]
  },
  {
    "id": "ai-25",
    "title": "Feed-Forward Network (FFN) Dimension Expansion (4d) in Transformers",
    "category": "Transformer Architecture",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Feed-Forward Network (FFN) Dimension Expansion (4d) in Transformers. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Feed-Forward Network (FFN) Dimension Expansion (4d) in Transformers:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Feed-Forward Network (FFN) Dimension Expansion (4d) in Transformers",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Transformer Architecture",
      "LLM"
    ]
  },
  {
    "id": "ai-26",
    "title": "Residual Connections and Gradient Highway Flow in Deep Transformers",
    "category": "Transformer Architecture",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Residual Connections and Gradient Highway Flow in Deep Transformers. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Residual Connections and Gradient Highway Flow in Deep Transformers:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Residual Connections and Gradient Highway Flow in Deep Transformers",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Transformer Architecture",
      "LLM"
    ]
  },
  {
    "id": "ai-27",
    "title": "Causal Masking in Autoregressive Decoder Attention",
    "category": "Transformer Architecture",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Causal Masking in Autoregressive Decoder Attention. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Causal Masking in Autoregressive Decoder Attention:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Causal Masking in Autoregressive Decoder Attention",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Transformer Architecture",
      "LLM"
    ]
  },
  {
    "id": "ai-28",
    "title": "Cross-Attention Mechanics in Encoder-Decoder Models (T5, Whisper)",
    "category": "Transformer Architecture",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Cross-Attention Mechanics in Encoder-Decoder Models (T5, Whisper). Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Cross-Attention Mechanics in Encoder-Decoder Models (T5, Whisper):\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Cross-Attention Mechanics in Encoder-Decoder Models (T5, Whisper)",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Transformer Architecture",
      "LLM"
    ]
  },
  {
    "id": "ai-29",
    "title": "Attention Sinks in Long-Context LLMs (StreamingLLM)",
    "category": "Transformer Architecture",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Attention Sinks in Long-Context LLMs (StreamingLLM). Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Attention Sinks in Long-Context LLMs (StreamingLLM):\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Attention Sinks in Long-Context LLMs (StreamingLLM)",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Transformer Architecture",
      "LLM"
    ]
  },
  {
    "id": "ai-30",
    "title": "ALiBi (Attention with Linear Biases) vs RoPE",
    "category": "Transformer Architecture",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: ALiBi (Attention with Linear Biases) vs RoPE. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of ALiBi (Attention with Linear Biases) vs RoPE:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for ALiBi (Attention with Linear Biases) vs RoPE",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Transformer Architecture",
      "LLM"
    ]
  },
  {
    "id": "ai-31",
    "title": "KV Cache Memory Footprint Calculation Formula: 2 * 2 * n_layers * n_heads * d_head * seq_len",
    "category": "Transformer Architecture",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: KV Cache Memory Footprint Calculation Formula: 2 * 2 * n_layers * n_heads * d_head * seq_len. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of KV Cache Memory Footprint Calculation Formula: 2 * 2 * n_layers * n_heads * d_head * seq_len:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for KV Cache Memory Footprint Calculation Formula: 2 * 2 * n_layers * n_heads * d_head * seq_len",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Transformer Architecture",
      "LLM"
    ]
  },
  {
    "id": "ai-32",
    "title": "Softmax Temperature, Top-P (Nucleus Sampling), and Top-K Sampling",
    "category": "Pre-Training",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Softmax Temperature, Top-P (Nucleus Sampling), and Top-K Sampling. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Softmax Temperature, Top-P (Nucleus Sampling), and Top-K Sampling:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Softmax Temperature, Top-P (Nucleus Sampling), and Top-K Sampling",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Pre-Training",
      "LLM"
    ]
  },
  {
    "id": "ai-33",
    "title": "Repetition Penalty and Frequency/Presence Penalty in Text Generation",
    "category": "Pre-Training",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Repetition Penalty and Frequency/Presence Penalty in Text Generation. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Repetition Penalty and Frequency/Presence Penalty in Text Generation:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Repetition Penalty and Frequency/Presence Penalty in Text Generation",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Pre-Training",
      "LLM"
    ]
  },
  {
    "id": "ai-34",
    "title": "Compute-Optimal vs Inference-Optimal Training Trade-offs",
    "category": "Pre-Training",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Compute-Optimal vs Inference-Optimal Training Trade-offs. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Compute-Optimal vs Inference-Optimal Training Trade-offs:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Compute-Optimal vs Inference-Optimal Training Trade-offs",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Pre-Training",
      "LLM"
    ]
  },
  {
    "id": "ai-35",
    "title": "Data Quality vs Data Quantity: Deduplication with MinHash LSH in Pretraining",
    "category": "Pre-Training",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Data Quality vs Data Quantity: Deduplication with MinHash LSH in Pretraining. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Data Quality vs Data Quantity: Deduplication with MinHash LSH in Pretraining:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Data Quality vs Data Quantity: Deduplication with MinHash LSH in Pretraining",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Pre-Training",
      "LLM"
    ]
  },
  {
    "id": "ai-36",
    "title": "Curriculum Learning and Annealing in LLM Pre-Training",
    "category": "Pre-Training",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Curriculum Learning and Annealing in LLM Pre-Training. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Curriculum Learning and Annealing in LLM Pre-Training:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Curriculum Learning and Annealing in LLM Pre-Training",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Pre-Training",
      "LLM"
    ]
  },
  {
    "id": "ai-37",
    "title": "Catastrophic Forgetting Mitigation in Continued Pre-Training",
    "category": "Pre-Training",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Catastrophic Forgetting Mitigation in Continued Pre-Training. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Catastrophic Forgetting Mitigation in Continued Pre-Training:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Catastrophic Forgetting Mitigation in Continued Pre-Training",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Pre-Training",
      "LLM"
    ]
  },
  {
    "id": "ai-38",
    "title": "Synthetic Data Generation for Pre-Training and Fine-Tuning",
    "category": "Pre-Training",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Synthetic Data Generation for Pre-Training and Fine-Tuning. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Synthetic Data Generation for Pre-Training and Fine-Tuning:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Synthetic Data Generation for Pre-Training and Fine-Tuning",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Pre-Training",
      "LLM"
    ]
  },
  {
    "id": "ai-39",
    "title": "LoRA Rank Selection: Empirical Comparisons of r=8, r=16, r=64",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: LoRA Rank Selection: Empirical Comparisons of r=8, r=16, r=64. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of LoRA Rank Selection: Empirical Comparisons of r=8, r=16, r=64:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for LoRA Rank Selection: Empirical Comparisons of r=8, r=16, r=64",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-40",
    "title": "Prefix Tuning and Prompt Tuning: Virtual Token Embeddings",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Prefix Tuning and Prompt Tuning: Virtual Token Embeddings. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Prefix Tuning and Prompt Tuning: Virtual Token Embeddings:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Prefix Tuning and Prompt Tuning: Virtual Token Embeddings",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-41",
    "title": "Target Modules in LoRA: Query/Value only vs All Linear Layers",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Target Modules in LoRA: Query/Value only vs All Linear Layers. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Target Modules in LoRA: Query/Value only vs All Linear Layers:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Target Modules in LoRA: Query/Value only vs All Linear Layers",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-42",
    "title": "Learning Rate Schedules in Fine-Tuning: Cosine Decay with Warmup",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Learning Rate Schedules in Fine-Tuning: Cosine Decay with Warmup. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Learning Rate Schedules in Fine-Tuning: Cosine Decay with Warmup:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Learning Rate Schedules in Fine-Tuning: Cosine Decay with Warmup",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-43",
    "title": "Overfitting Indicators in LLM Fine-Tuning: Eval Loss vs Training Loss",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Overfitting Indicators in LLM Fine-Tuning: Eval Loss vs Training Loss. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Overfitting Indicators in LLM Fine-Tuning: Eval Loss vs Training Loss:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Overfitting Indicators in LLM Fine-Tuning: Eval Loss vs Training Loss",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-44",
    "title": "Multi-Task Fine-Tuning with Task Prefixes",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Multi-Task Fine-Tuning with Task Prefixes. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Multi-Task Fine-Tuning with Task Prefixes:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Multi-Task Fine-Tuning with Task Prefixes",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-45",
    "title": "Weight Decay (L2 Regularization) in AdamW vs Adam",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Weight Decay (L2 Regularization) in AdamW vs Adam. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Weight Decay (L2 Regularization) in AdamW vs Adam:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Weight Decay (L2 Regularization) in AdamW vs Adam",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-46",
    "title": "Gradient Accumulation and Effective Batch Size in GPU Training",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Gradient Accumulation and Effective Batch Size in GPU Training. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Gradient Accumulation and Effective Batch Size in GPU Training:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Gradient Accumulation and Effective Batch Size in GPU Training",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-47",
    "title": "Mixed Precision Training: FP16 vs BF16 (Bfloat16 Dynamic Range)",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Mixed Precision Training: FP16 vs BF16 (Bfloat16 Dynamic Range). Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Mixed Precision Training: FP16 vs BF16 (Bfloat16 Dynamic Range):\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Mixed Precision Training: FP16 vs BF16 (Bfloat16 Dynamic Range)",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-48",
    "title": "Kahneman-Tversky Optimization (KTO) for Binary Feedback",
    "category": "Alignment & RLHF",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Kahneman-Tversky Optimization (KTO) for Binary Feedback. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Kahneman-Tversky Optimization (KTO) for Binary Feedback:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Kahneman-Tversky Optimization (KTO) for Binary Feedback",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Alignment & RLHF",
      "LLM"
    ]
  },
  {
    "id": "ai-49",
    "title": "Identity Preference Optimization (IPO) vs DPO",
    "category": "Alignment & RLHF",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Identity Preference Optimization (IPO) vs DPO. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Identity Preference Optimization (IPO) vs DPO:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Identity Preference Optimization (IPO) vs DPO",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Alignment & RLHF",
      "LLM"
    ]
  },
  {
    "id": "ai-50",
    "title": "Constitutional AI (RLAIF): AI Feedback replacing Human Annotators",
    "category": "Alignment & RLHF",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Constitutional AI (RLAIF): AI Feedback replacing Human Annotators. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Constitutional AI (RLAIF): AI Feedback replacing Human Annotators:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Constitutional AI (RLAIF): AI Feedback replacing Human Annotators",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Alignment & RLHF",
      "LLM"
    ]
  },
  {
    "id": "ai-51",
    "title": "Jailbreak Attacks: Adversarial Suffixes and Prefix Injection",
    "category": "Alignment & RLHF",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Jailbreak Attacks: Adversarial Suffixes and Prefix Injection. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Jailbreak Attacks: Adversarial Suffixes and Prefix Injection:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Jailbreak Attacks: Adversarial Suffixes and Prefix Injection",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Alignment & RLHF",
      "LLM"
    ]
  },
  {
    "id": "ai-52",
    "title": "Guardrail Systems: Llama Guard and NeMo Guardrails",
    "category": "Alignment & RLHF",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Guardrail Systems: Llama Guard and NeMo Guardrails. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Guardrail Systems: Llama Guard and NeMo Guardrails:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Guardrail Systems: Llama Guard and NeMo Guardrails",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Alignment & RLHF",
      "LLM"
    ]
  },
  {
    "id": "ai-53",
    "title": "Hallucination Detection via Semantic Uncertainty and Logit Entropy",
    "category": "Alignment & RLHF",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Hallucination Detection via Semantic Uncertainty and Logit Entropy. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Hallucination Detection via Semantic Uncertainty and Logit Entropy:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Hallucination Detection via Semantic Uncertainty and Logit Entropy",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Alignment & RLHF",
      "LLM"
    ]
  },
  {
    "id": "ai-54",
    "title": "Self-Consistency Prompting and Majority Voting",
    "category": "Alignment & RLHF",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Self-Consistency Prompting and Majority Voting. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Self-Consistency Prompting and Majority Voting:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Self-Consistency Prompting and Majority Voting",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Alignment & RLHF",
      "LLM"
    ]
  },
  {
    "id": "ai-55",
    "title": "Document Chunking: Fixed vs Semantic vs Markdown Hierarchy",
    "category": "RAG & Vector Search",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Document Chunking: Fixed vs Semantic vs Markdown Hierarchy. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Document Chunking: Fixed vs Semantic vs Markdown Hierarchy:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Document Chunking: Fixed vs Semantic vs Markdown Hierarchy",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-56",
    "title": "Chunk Overlap Sizing and Boundary Truncation Mitigation",
    "category": "RAG & Vector Search",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Chunk Overlap Sizing and Boundary Truncation Mitigation. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Chunk Overlap Sizing and Boundary Truncation Mitigation:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Chunk Overlap Sizing and Boundary Truncation Mitigation",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-57",
    "title": "Cosine Similarity vs Dot Product on Normalized Vectors",
    "category": "RAG & Vector Search",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Cosine Similarity vs Dot Product on Normalized Vectors. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Cosine Similarity vs Dot Product on Normalized Vectors:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Cosine Similarity vs Dot Product on Normalized Vectors",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-58",
    "title": "Euclidean Distance (L2) vs Inner Product in High Dimensions",
    "category": "RAG & Vector Search",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Euclidean Distance (L2) vs Inner Product in High Dimensions. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Euclidean Distance (L2) vs Inner Product in High Dimensions:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Euclidean Distance (L2) vs Inner Product in High Dimensions",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-59",
    "title": "Vector Database Sharding and Horizontal Replication",
    "category": "RAG & Vector Search",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Vector Database Sharding and Horizontal Replication. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Vector Database Sharding and Horizontal Replication:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Vector Database Sharding and Horizontal Replication",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-60",
    "title": "Metadata Filtering in Vector Databases: Pre-Filtering vs Post-Filtering",
    "category": "RAG & Vector Search",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Metadata Filtering in Vector Databases: Pre-Filtering vs Post-Filtering. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Metadata Filtering in Vector Databases: Pre-Filtering vs Post-Filtering:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Metadata Filtering in Vector Databases: Pre-Filtering vs Post-Filtering",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-61",
    "title": "Hypothetical Document Embeddings (HyDE) in RAG",
    "category": "RAG & Vector Search",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Hypothetical Document Embeddings (HyDE) in RAG. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Hypothetical Document Embeddings (HyDE) in RAG:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Hypothetical Document Embeddings (HyDE) in RAG",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-62",
    "title": "Corrective RAG (CRAG) with Web Search Fallback",
    "category": "RAG & Vector Search",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Corrective RAG (CRAG) with Web Search Fallback. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Corrective RAG (CRAG) with Web Search Fallback:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Corrective RAG (CRAG) with Web Search Fallback",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-63",
    "title": "Self-RAG: Self-Reflective Retrieval-Augmented Generation",
    "category": "RAG & Vector Search",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Self-RAG: Self-Reflective Retrieval-Augmented Generation. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Self-RAG: Self-Reflective Retrieval-Augmented Generation:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Self-RAG: Self-Reflective Retrieval-Augmented Generation",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-64",
    "title": "Sentence Window Retrieval and Parent Document Retrieval",
    "category": "RAG & Vector Search",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Sentence Window Retrieval and Parent Document Retrieval. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Sentence Window Retrieval and Parent Document Retrieval:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Sentence Window Retrieval and Parent Document Retrieval",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-65",
    "title": "Multimodal RAG with CLIP and Vision-Language Models",
    "category": "RAG & Vector Search",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Multimodal RAG with CLIP and Vision-Language Models. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Multimodal RAG with CLIP and Vision-Language Models:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Multimodal RAG with CLIP and Vision-Language Models",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-66",
    "title": "Context Compression and Selective Context Pruning (LLMLingua)",
    "category": "RAG & Vector Search",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Context Compression and Selective Context Pruning (LLMLingua). Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Context Compression and Selective Context Pruning (LLMLingua):\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Context Compression and Selective Context Pruning (LLMLingua)",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "RAG & Vector Search",
      "LLM"
    ]
  },
  {
    "id": "ai-67",
    "title": "Chain-of-Thought (CoT) Prompting and Step-by-Step Reasoning",
    "category": "Context Engineering",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Chain-of-Thought (CoT) Prompting and Step-by-Step Reasoning. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Chain-of-Thought (CoT) Prompting and Step-by-Step Reasoning:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Chain-of-Thought (CoT) Prompting and Step-by-Step Reasoning",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Context Engineering",
      "LLM"
    ]
  },
  {
    "id": "ai-68",
    "title": "Tree-of-Thoughts (ToT) Search Algorithms (BFS/DFS on Thoughts)",
    "category": "Context Engineering",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Tree-of-Thoughts (ToT) Search Algorithms (BFS/DFS on Thoughts). Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Tree-of-Thoughts (ToT) Search Algorithms (BFS/DFS on Thoughts):\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Tree-of-Thoughts (ToT) Search Algorithms (BFS/DFS on Thoughts)",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Context Engineering",
      "LLM"
    ]
  },
  {
    "id": "ai-69",
    "title": "In-Context Learning (Few-Shot): Exemplar Selection Heuristics",
    "category": "Context Engineering",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: In-Context Learning (Few-Shot): Exemplar Selection Heuristics. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of In-Context Learning (Few-Shot): Exemplar Selection Heuristics:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for In-Context Learning (Few-Shot): Exemplar Selection Heuristics",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Context Engineering",
      "LLM"
    ]
  },
  {
    "id": "ai-70",
    "title": "System Prompt Hardening against Indirect Prompt Injections",
    "category": "Context Engineering",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: System Prompt Hardening against Indirect Prompt Injections. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of System Prompt Hardening against Indirect Prompt Injections:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for System Prompt Hardening against Indirect Prompt Injections",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Context Engineering",
      "LLM"
    ]
  },
  {
    "id": "ai-71",
    "title": "Structured JSON Extraction with Instructor and Outlines (Regex Constrained Decoding)",
    "category": "Context Engineering",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Structured JSON Extraction with Instructor and Outlines (Regex Constrained Decoding). Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Structured JSON Extraction with Instructor and Outlines (Regex Constrained Decoding):\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Structured JSON Extraction with Instructor and Outlines (Regex Constrained Decoding)",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Context Engineering",
      "LLM"
    ]
  },
  {
    "id": "ai-72",
    "title": "Function Calling / Tool Calling: OpenAPI Schemas in LLMs",
    "category": "Context Engineering",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Function Calling / Tool Calling: OpenAPI Schemas in LLMs. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Function Calling / Tool Calling: OpenAPI Schemas in LLMs:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Function Calling / Tool Calling: OpenAPI Schemas in LLMs",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Context Engineering",
      "LLM"
    ]
  },
  {
    "id": "ai-73",
    "title": "Cross-Lingual Zero-Shot Transfer in Multilingual NLP",
    "category": "NLP & Sentiment",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Cross-Lingual Zero-Shot Transfer in Multilingual NLP. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Cross-Lingual Zero-Shot Transfer in Multilingual NLP:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Cross-Lingual Zero-Shot Transfer in Multilingual NLP",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "NLP & Sentiment",
      "LLM"
    ]
  },
  {
    "id": "ai-74",
    "title": "XLM-RoBERTa vs mBERT Architecture and Pre-training Objectives",
    "category": "NLP & Sentiment",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: XLM-RoBERTa vs mBERT Architecture and Pre-training Objectives. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of XLM-RoBERTa vs mBERT Architecture and Pre-training Objectives:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for XLM-RoBERTa vs mBERT Architecture and Pre-training Objectives",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "NLP & Sentiment",
      "LLM"
    ]
  },
  {
    "id": "ai-75",
    "title": "Sentiment Lexicons vs Neural Sentiment Embeddings",
    "category": "NLP & Sentiment",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Sentiment Lexicons vs Neural Sentiment Embeddings. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Sentiment Lexicons vs Neural Sentiment Embeddings:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Sentiment Lexicons vs Neural Sentiment Embeddings",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "NLP & Sentiment",
      "LLM"
    ]
  },
  {
    "id": "ai-76",
    "title": "Survey Question Generation Pipeline: Grounding and Quality Filtering",
    "category": "NLP & Sentiment",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Survey Question Generation Pipeline: Grounding and Quality Filtering. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Survey Question Generation Pipeline: Grounding and Quality Filtering:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Survey Question Generation Pipeline: Grounding and Quality Filtering",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "NLP & Sentiment",
      "LLM"
    ]
  },
  {
    "id": "ai-77",
    "title": "Continuous Batching (Iteration-Level Scheduling) in Orca/vLLM",
    "category": "Quantization & Serving",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Continuous Batching (Iteration-Level Scheduling) in Orca/vLLM. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Continuous Batching (Iteration-Level Scheduling) in Orca/vLLM:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Continuous Batching (Iteration-Level Scheduling) in Orca/vLLM",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Quantization & Serving",
      "LLM"
    ]
  },
  {
    "id": "ai-78",
    "title": "Speculative Decoding: Small Draft Model with Fast Verification",
    "category": "Quantization & Serving",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Speculative Decoding: Small Draft Model with Fast Verification. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Speculative Decoding: Small Draft Model with Fast Verification:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Speculative Decoding: Small Draft Model with Fast Verification",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Quantization & Serving",
      "LLM"
    ]
  },
  {
    "id": "ai-79",
    "title": "GGUF Format and llama.cpp CPU Inference Acceleration",
    "category": "Quantization & Serving",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: GGUF Format and llama.cpp CPU Inference Acceleration. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of GGUF Format and llama.cpp CPU Inference Acceleration:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for GGUF Format and llama.cpp CPU Inference Acceleration",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Quantization & Serving",
      "LLM"
    ]
  },
  {
    "id": "ai-80",
    "title": "Tensor Parallelism (Megatron-LM) vs Pipeline Parallelism",
    "category": "Quantization & Serving",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Tensor Parallelism (Megatron-LM) vs Pipeline Parallelism. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Tensor Parallelism (Megatron-LM) vs Pipeline Parallelism:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Tensor Parallelism (Megatron-LM) vs Pipeline Parallelism",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Quantization & Serving",
      "LLM"
    ]
  },
  {
    "id": "ai-81",
    "title": "Fully Sharded Data Parallel (FSDP) vs DeepSpeed ZeRO-3",
    "category": "Quantization & Serving",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Fully Sharded Data Parallel (FSDP) vs DeepSpeed ZeRO-3. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Fully Sharded Data Parallel (FSDP) vs DeepSpeed ZeRO-3:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Fully Sharded Data Parallel (FSDP) vs DeepSpeed ZeRO-3",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Quantization & Serving",
      "LLM"
    ]
  },
  {
    "id": "ai-82",
    "title": "ReAct (Reason + Act) Agent Framework Loop",
    "category": "Agents & Tool Calling",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: ReAct (Reason + Act) Agent Framework Loop. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of ReAct (Reason + Act) Agent Framework Loop:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for ReAct (Reason + Act) Agent Framework Loop",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Agents & Tool Calling",
      "LLM"
    ]
  },
  {
    "id": "ai-83",
    "title": "Agent Memory Systems: Short-Term Working Memory vs Long-Term Vector Memory",
    "category": "Agents & Tool Calling",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Agent Memory Systems: Short-Term Working Memory vs Long-Term Vector Memory. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Agent Memory Systems: Short-Term Working Memory vs Long-Term Vector Memory:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Agent Memory Systems: Short-Term Working Memory vs Long-Term Vector Memory",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Agents & Tool Calling",
      "LLM"
    ]
  },
  {
    "id": "ai-84",
    "title": "Multi-Agent Orchestration: Supervisor vs Swarm Architectures",
    "category": "Agents & Tool Calling",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Multi-Agent Orchestration: Supervisor vs Swarm Architectures. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Multi-Agent Orchestration: Supervisor vs Swarm Architectures:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Multi-Agent Orchestration: Supervisor vs Swarm Architectures",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Agents & Tool Calling",
      "LLM"
    ]
  },
  {
    "id": "ai-85",
    "title": "Agent Tool Calling Error Recovery and Infinite Loop Detection",
    "category": "Agents & Tool Calling",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Agent Tool Calling Error Recovery and Infinite Loop Detection. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Agent Tool Calling Error Recovery and Infinite Loop Detection:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Agent Tool Calling Error Recovery and Infinite Loop Detection",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Agents & Tool Calling",
      "LLM"
    ]
  },
  {
    "id": "ai-86",
    "title": "Model Evaluation Metrics: Perplexity vs Cross-Entropy",
    "category": "Evaluation & MLOps",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Model Evaluation Metrics: Perplexity vs Cross-Entropy. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Model Evaluation Metrics: Perplexity vs Cross-Entropy:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Model Evaluation Metrics: Perplexity vs Cross-Entropy",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Evaluation & MLOps",
      "LLM"
    ]
  },
  {
    "id": "ai-87",
    "title": "ROUGE (1, 2, L) and BLEU Scores for Summarization and Translation",
    "category": "Evaluation & MLOps",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: ROUGE (1, 2, L) and BLEU Scores for Summarization and Translation. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of ROUGE (1, 2, L) and BLEU Scores for Summarization and Translation:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for ROUGE (1, 2, L) and BLEU Scores for Summarization and Translation",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Evaluation & MLOps",
      "LLM"
    ]
  },
  {
    "id": "ai-88",
    "title": "LLM-as-a-Judge: G-Eval and MT-Bench Evaluation Frameworks",
    "category": "Evaluation & MLOps",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: LLM-as-a-Judge: G-Eval and MT-Bench Evaluation Frameworks. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of LLM-as-a-Judge: G-Eval and MT-Bench Evaluation Frameworks:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for LLM-as-a-Judge: G-Eval and MT-Bench Evaluation Frameworks",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Evaluation & MLOps",
      "LLM"
    ]
  },
  {
    "id": "ai-89",
    "title": "MMLU, GSM8K, and HumanEval Benchmark Biases and Data Contamination",
    "category": "Evaluation & MLOps",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: MMLU, GSM8K, and HumanEval Benchmark Biases and Data Contamination. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of MMLU, GSM8K, and HumanEval Benchmark Biases and Data Contamination:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for MMLU, GSM8K, and HumanEval Benchmark Biases and Data Contamination",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Evaluation & MLOps",
      "LLM"
    ]
  },
  {
    "id": "ai-90",
    "title": "Data Drift and Concept Drift Monitoring in Production ML Models",
    "category": "Evaluation & MLOps",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Data Drift and Concept Drift Monitoring in Production ML Models. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Data Drift and Concept Drift Monitoring in Production ML Models:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Data Drift and Concept Drift Monitoring in Production ML Models",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Evaluation & MLOps",
      "LLM"
    ]
  },
  {
    "id": "ai-91",
    "title": "LLM Tracing and Observability with Langfuse, Phoenix, and OpenTelemetry",
    "category": "Evaluation & MLOps",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: LLM Tracing and Observability with Langfuse, Phoenix, and OpenTelemetry. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of LLM Tracing and Observability with Langfuse, Phoenix, and OpenTelemetry:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for LLM Tracing and Observability with Langfuse, Phoenix, and OpenTelemetry",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Evaluation & MLOps",
      "LLM"
    ]
  },
  {
    "id": "ai-92",
    "title": "Feature Stores in Machine Learning (Feast vs Hopsworks)",
    "category": "Evaluation & MLOps",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Feature Stores in Machine Learning (Feast vs Hopsworks). Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Feature Stores in Machine Learning (Feast vs Hopsworks):\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Feature Stores in Machine Learning (Feast vs Hopsworks)",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Evaluation & MLOps",
      "LLM"
    ]
  },
  {
    "id": "ai-93",
    "title": "A/B Testing and Canary Deployments for Production ML Models",
    "category": "Evaluation & MLOps",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: A/B Testing and Canary Deployments for Production ML Models. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of A/B Testing and Canary Deployments for Production ML Models:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for A/B Testing and Canary Deployments for Production ML Models",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Evaluation & MLOps",
      "LLM"
    ]
  },
  {
    "id": "ai-94",
    "title": "Cross-Entropy Loss vs Focal Loss for Imbalanced Classification",
    "category": "Deep Learning Foundations",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Cross-Entropy Loss vs Focal Loss for Imbalanced Classification. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Cross-Entropy Loss vs Focal Loss for Imbalanced Classification:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Cross-Entropy Loss vs Focal Loss for Imbalanced Classification",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-95",
    "title": "Batch Normalization vs Layer Normalization vs Group Normalization",
    "category": "Deep Learning Foundations",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Batch Normalization vs Layer Normalization vs Group Normalization. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Batch Normalization vs Layer Normalization vs Group Normalization:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Batch Normalization vs Layer Normalization vs Group Normalization",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-96",
    "title": "Vanishing and Exploding Gradients: Causes and Mitigations",
    "category": "Deep Learning Foundations",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Vanishing and Exploding Gradients: Causes and Mitigations. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Vanishing and Exploding Gradients: Causes and Mitigations:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Vanishing and Exploding Gradients: Causes and Mitigations",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-97",
    "title": "Weight Initialization Techniques: Xavier (Glorot) vs He (Kaiming)",
    "category": "Deep Learning Foundations",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Weight Initialization Techniques: Xavier (Glorot) vs He (Kaiming). Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Weight Initialization Techniques: Xavier (Glorot) vs He (Kaiming):\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Weight Initialization Techniques: Xavier (Glorot) vs He (Kaiming)",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-98",
    "title": "Dropout and DropPath (Stochastic Depth) Regularization",
    "category": "Deep Learning Foundations",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Dropout and DropPath (Stochastic Depth) Regularization. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Dropout and DropPath (Stochastic Depth) Regularization:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Dropout and DropPath (Stochastic Depth) Regularization",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-99",
    "title": "Adam vs AdamW: Decoupled Weight Decay Mechanics",
    "category": "Deep Learning Foundations",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Adam vs AdamW: Decoupled Weight Decay Mechanics. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Adam vs AdamW: Decoupled Weight Decay Mechanics:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Adam vs AdamW: Decoupled Weight Decay Mechanics",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-100",
    "title": "Cosine Annealing Learning Rate Schedule with Warm Restarts",
    "category": "Deep Learning Foundations",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Cosine Annealing Learning Rate Schedule with Warm Restarts. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Cosine Annealing Learning Rate Schedule with Warm Restarts:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Cosine Annealing Learning Rate Schedule with Warm Restarts",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-101",
    "title": "Label Smoothing Regularization in Multiclass Classification",
    "category": "Deep Learning Foundations",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Label Smoothing Regularization in Multiclass Classification. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Label Smoothing Regularization in Multiclass Classification:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Label Smoothing Regularization in Multiclass Classification",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-102",
    "title": "Gradient Clipping: Norm Clipping vs Value Clipping",
    "category": "Deep Learning Foundations",
    "difficulty": "Easy",
    "question": "Detailed AI & Machine Learning interview analysis of: Gradient Clipping: Norm Clipping vs Value Clipping. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Gradient Clipping: Norm Clipping vs Value Clipping:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Gradient Clipping: Norm Clipping vs Value Clipping",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-103",
    "title": "Autoencoders vs Variational Autoencoders (VAEs) and the Reparameterization Trick",
    "category": "Deep Learning Foundations",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Autoencoders vs Variational Autoencoders (VAEs) and the Reparameterization Trick. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Autoencoders vs Variational Autoencoders (VAEs) and the Reparameterization Trick:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Autoencoders vs Variational Autoencoders (VAEs) and the Reparameterization Trick",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-104",
    "title": "Diffusion Models: Forward Noising Process vs Reverse Denoising Process",
    "category": "Deep Learning Foundations",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Diffusion Models: Forward Noising Process vs Reverse Denoising Process. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Diffusion Models: Forward Noising Process vs Reverse Denoising Process:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Diffusion Models: Forward Noising Process vs Reverse Denoising Process",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-105",
    "title": "Contrastive Learning: SimCLR, InfoNCE Loss, and MoCo",
    "category": "Deep Learning Foundations",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: Contrastive Learning: SimCLR, InfoNCE Loss, and MoCo. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Contrastive Learning: SimCLR, InfoNCE Loss, and MoCo:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Contrastive Learning: SimCLR, InfoNCE Loss, and MoCo",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-106",
    "title": "CLIP (Contrastive Language-Image Pre-Training) Multimodal Architecture",
    "category": "Deep Learning Foundations",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: CLIP (Contrastive Language-Image Pre-Training) Multimodal Architecture. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of CLIP (Contrastive Language-Image Pre-Training) Multimodal Architecture:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for CLIP (Contrastive Language-Image Pre-Training) Multimodal Architecture",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Deep Learning Foundations",
      "LLM"
    ]
  },
  {
    "id": "ai-107",
    "title": "Prefix-Tuning vs Prompt Tuning vs LoRA Empirical Trade-offs",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Prefix-Tuning vs Prompt Tuning vs LoRA Empirical Trade-offs. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Prefix-Tuning vs Prompt Tuning vs LoRA Empirical Trade-offs:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Prefix-Tuning vs Prompt Tuning vs LoRA Empirical Trade-offs",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-108",
    "title": "DoRA (Weight-Decomposed Low-Rank Adaptation)",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: DoRA (Weight-Decomposed Low-Rank Adaptation). Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of DoRA (Weight-Decomposed Low-Rank Adaptation):\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for DoRA (Weight-Decomposed Low-Rank Adaptation)",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-109",
    "title": "LongLoRA: Efficient Fine-Tuning of Long-Context LLMs",
    "category": "Fine-Tuning & PEFT",
    "difficulty": "Hard",
    "question": "Detailed AI & Machine Learning interview analysis of: LongLoRA: Efficient Fine-Tuning of Long-Context LLMs. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of LongLoRA: Efficient Fine-Tuning of Long-Context LLMs:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for LongLoRA: Efficient Fine-Tuning of Long-Context LLMs",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Fine-Tuning & PEFT",
      "LLM"
    ]
  },
  {
    "id": "ai-110",
    "title": "Text-to-SQL Pipelines: Schema Linking and Few-Shot In-Context Grounding",
    "category": "Context Engineering",
    "difficulty": "Medium",
    "question": "Detailed AI & Machine Learning interview analysis of: Text-to-SQL Pipelines: Schema Linking and Few-Shot In-Context Grounding. Explain mathematical formulation, trade-offs, architecture, and production implementation.",
    "answer": "Comprehensive technical breakdown of Text-to-SQL Pipelines: Schema Linking and Few-Shot In-Context Grounding:\n1. Theoretical Principles: Core mathematical formulation, objective functions, and architecture.\n2. Engineering Trade-Offs: Compute complexity, VRAM memory requirements, and latency overhead.\n3. Production Implementation: Best practices, hyperparameter tuning, and framework choices (PyTorch, HuggingFace, vLLM).\n4. Evaluation & Failure Modes: Benchmarks, diagnostics, and edge case mitigation.",
    "keyPoints": [
      "Core AI/ML concept for Text-to-SQL Pipelines: Schema Linking and Few-Shot In-Context Grounding",
      "Evaluates mathematical mechanics and computational complexity",
      "Addresses VRAM efficiency and latency bottlenecks",
      "Directly applicable to LLM fine-tuning, RAG, and production serving"
    ],
    "tags": [
      "AI",
      "Machine Learning",
      "Context Engineering",
      "LLM"
    ]
  }
];
