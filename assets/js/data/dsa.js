// DSA Interview Questions Data (110 Curated Problems)
window.INTERVIEW_DATA_DSA = [
  {
    "id": "dsa-1",
    "title": "Two Sum",
    "category": "Arrays & Hashing",
    "difficulty": "Easy",
    "question": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may not use the same element twice. What is the optimal time and space complexity?",
    "answer": "Use a hash map to store each number and its index as you iterate through the array. For each element `x`, compute the complement `target - x`. Check if `complement` is already in the map; if so, return `[map[complement], currentIndex]`. Otherwise, insert `x` into the map.\n\nTime Complexity: O(N) single pass.\nSpace Complexity: O(N) for the hash map.\n\nEdge cases: Duplicates, negative numbers, large integers.",
    "keyPoints": [
      "One-pass hash table achieves O(N) time and O(N) space",
      "Lookup of complement takes O(1) average time",
      "Avoids the brute-force O(N\u00b2) nested loop approach",
      "Handles negative numbers and duplicate values cleanly"
    ],
    "tags": [
      "Array",
      "Hash Table",
      "Two Pointers"
    ]
  },
  {
    "id": "dsa-2",
    "title": "Valid Anagram",
    "category": "Arrays & Hashing",
    "difficulty": "Easy",
    "question": "Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise. How would you adapt your solution if the inputs contain Unicode characters?",
    "answer": "For ASCII lowercase letters, use a fixed-size frequency array of length 26. Increment frequency for characters in `s` and decrement for characters in `t`. If all counts end at 0, they are anagrams.\n\nIf the strings can contain arbitrary Unicode characters, replace the fixed array with a hash map (e.g., Python `Counter` or Java `HashMap<Character, Integer>`) to handle any character set without allocating excessive memory.\n\nTime Complexity: O(N)\nSpace Complexity: O(1) for fixed alphabet or O(U) where U is unique characters for Unicode.",
    "keyPoints": [
      "Fixed array of size 26 for ASCII yields O(1) auxiliary space",
      "Hash map for arbitrary Unicode code points",
      "Early exit if lengths differ",
      "Alternative: sorting both strings takes O(N log N) time"
    ],
    "tags": [
      "String",
      "Hash Table",
      "Frequency Array"
    ]
  },
  {
    "id": "dsa-3",
    "title": "Group Anagrams",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Given an array of strings `strs`, group the anagrams together. You can return the answer in any order. Compare the sorting-key vs character-frequency-tuple approaches.",
    "answer": "Two main approaches:\n1. Sorted String as Key: For each string, sort its characters to form a canonical key (e.g., 'eat' -> 'aet'). Group words in a hash map `Map<String, List<String>>`. Time: O(N * K log K), where N is number of strings and K is max length.\n2. Frequency Count Tuple as Key: Count frequencies of the 26 characters and use the tuple of counts as the map key (e.g., `(1,0,0,...,1)`). Time: O(N * K), Space: O(N * K).\n\nTrade-off: For small K, sorting is fast and simple; for large K and small alphabet, frequency counting is strictly linear with respect to string length.",
    "keyPoints": [
      "Canonical representation grouping pattern",
      "Sorting key: O(N * K log K)",
      "Character count tuple key: O(N * K)",
      "Space complexity is O(N * K) to store all strings in the map"
    ],
    "tags": [
      "Array",
      "Hash Table",
      "String",
      "Sorting"
    ]
  },
  {
    "id": "dsa-4",
    "title": "Top K Frequent Elements",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. Can you solve it in better than O(N log N) time?",
    "answer": "Two optimal methods:\n1. Bucket Sort (O(N) time & O(N) space): Count element frequencies with a hash map. Create an array of buckets where index `i` represents frequency `i` (size N+1). Place each number into bucket `bucket[freq]`. Iterate backwards from bucket `N` down to 0, collecting numbers until `k` numbers are collected.\n2. Min-Heap of size K (O(N log K) time): Maintain a min-heap of size `k` ordered by frequency. Push each unique element; if heap size exceeds `k`, pop the min. The remaining `k` elements are the answer.\n\nBucket sort achieves the optimal O(N) time complexity.",
    "keyPoints": [
      "Bucket sort achieves linear O(N) time complexity",
      "Min-heap of size K achieves O(N log K) time and O(N) space",
      "Quickselect can also achieve O(N) average time",
      "Always clarify if output can be in any order"
    ],
    "tags": [
      "Array",
      "Hash Table",
      "Bucket Sort",
      "Heap",
      "Quickselect"
    ]
  },
  {
    "id": "dsa-5",
    "title": "Product of Array Except Self",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must write an algorithm that runs in O(N) time without using the division operation, and in O(1) auxiliary space.",
    "answer": "Prefix and Postfix Products in-place:\n1. Initialize `output` array of length N.\n2. First pass (Left to Right): Store cumulative prefix products in `output[i]`. Set `output[0] = 1`, and for each `i` from 1 to N-1, `output[i] = output[i-1] * nums[i-1]`.\n3. Second pass (Right to Left): Maintain a running postfix product variable `R = 1`. For `i` from N-1 down to 0, multiply `output[i] *= R`, then update `R *= nums[i]`.\n\nTime Complexity: O(N) two passes.\nAuxiliary Space Complexity: O(1) (excluding the return array as per problem constraints).",
    "keyPoints": [
      "Prefix product and suffix product multiplication",
      "Avoids division (which fails on zeros)",
      "Achieves O(1) extra space by accumulating directly in output array",
      "Handles single zero and multiple zero cases naturally"
    ],
    "tags": [
      "Array",
      "Prefix Sum",
      "Math"
    ]
  },
  {
    "id": "dsa-6",
    "title": "Longest Consecutive Sequence",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(N) time.",
    "answer": "Insert all elements into a hash set for O(1) average lookup.\nIterate through each number `x` in the set:\n- Only start counting if `x` is the beginning of a sequence (i.e. `x - 1` is NOT in the set).\n- If it is the start, increment `x + 1, x + 2, ...` while elements exist in the set, keeping track of current streak length.\n- Update global maximum.\n\nWhy O(N)? Each number is visited at most twice: once in the outer loop, and at most once inside the `while` loop (only when part of an increasing streak starting from its head).\n\nSpace Complexity: O(N) for the set.",
    "keyPoints": [
      "Condition `!set.contains(x - 1)` ensures each streak is only checked from its origin",
      "Total operations inside inner while loop across all numbers is bounded by N",
      "Overall time is strictly O(N) average",
      "Space is O(N) to build the hash set"
    ],
    "tags": [
      "Array",
      "Hash Table",
      "Union Find"
    ]
  },
  {
    "id": "dsa-7",
    "title": "Subarray Sum Equals K",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`. Can two pointers be used here?",
    "answer": "No, two pointers / sliding window CANNOT be used if `nums` can contain negative numbers, because expanding or shrinking the window does not monotonically increase or decrease the window sum.\n\nOptimal approach: Prefix Sum + Hash Map:\n- Maintain `running_sum`.\n- At index `i`, we need the number of previous prefix sums equal to `running_sum - k`.\n- Store prefix sum frequencies in a map `prefix_counts`. Initialize with `{0: 1}` (for subarrays starting at index 0).\n- At each step: `count += prefix_counts.get(running_sum - k, 0)`, then `prefix_counts[running_sum] += 1`.\n\nTime Complexity: O(N)\nSpace Complexity: O(N)",
    "keyPoints": [
      "Two pointers fails when negative numbers are present",
      "Prefix sum difference: sum(i..j) = prefix[j] - prefix[i-1]",
      "Hash map tracks counts of seen prefix sums",
      "Must initialize map with {0: 1} to count prefix that exactly equals k"
    ],
    "tags": [
      "Array",
      "Hash Table",
      "Prefix Sum"
    ]
  },
  {
    "id": "dsa-8",
    "title": "Encode and Decode Strings",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Design an algorithm to encode a list of strings to a single string and decode that string back to the original list of strings. The strings can contain any possible ASCII/Unicode characters, including delimiters.",
    "answer": "Chunked / Length-Prefixed Encoding:\nEncode: For each string `s`, prefix it with its length followed by a non-numeric delimiter like `#`:\n`len(s) + '#' + s`.\nExample: `[\"lint\", \"code\", \"love\", \"you\"]` -> `\"4#lint4#code4#love3#you\"`.\n\nDecode:\nScan the string. Find the next `#`. The substring from the current pointer to `#` is the integer length `L`. Read `L` characters immediately following `#` as the string. Advance pointer past that string and repeat until end of encoded string.\n\nThis handles any delimiter or special characters inside strings (including `#`, newlines, null bytes) because length tells exactly how many bytes to read.",
    "keyPoints": [
      "Length-prefixing avoids delimiter collision attacks and escaping bugs",
      "Linear time O(N) encode and decode",
      "Stateless and streaming friendly",
      "Foundation for network protocol framing (e.g. HTTP chunking, TLV)"
    ],
    "tags": [
      "String",
      "Design",
      "Encoding"
    ]
  },
  {
    "id": "dsa-9",
    "title": "3Sum",
    "category": "Two Pointers",
    "difficulty": "Medium",
    "question": "Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.",
    "answer": "Sort the array first in O(N log N). Iterate `i` from 0 to N-3:\n- If `nums[i] > 0`, break early (sum of 3 positive numbers can never be 0).\n- If `i > 0` and `nums[i] == nums[i-1]`, skip to avoid duplicate triplets.\n- Set two pointers: `left = i + 1`, `right = N - 1`. While `left < right`:\n  - `sum = nums[i] + nums[left] + nums[right]`.\n  - If `sum == 0`, record triplet, then advance `left` skipping duplicates (`nums[left] == nums[left+1]`) and decrement `right` skipping duplicates (`nums[right] == nums[right-1]`). Move both inwards.\n  - If `sum < 0`, `left++`.\n  - If `sum > 0`, `right--`.\n\nTime: O(N\u00b2), Space: O(1) or O(N) depending on sorting implementation.",
    "keyPoints": [
      "Sort first to enable two-pointer convergence",
      "Skip duplicates at outer loop and both inner pointer steps",
      "Early termination when nums[i] > 0",
      "Time complexity O(N\u00b2), space O(1) auxiliary"
    ],
    "tags": [
      "Array",
      "Two Pointers",
      "Sorting"
    ]
  },
  {
    "id": "dsa-10",
    "title": "Container With Most Water",
    "category": "Two Pointers",
    "difficulty": "Medium",
    "question": "Given `n` non-negative integers `height` where each represents a point at coordinate `(i, height[i])`, find two lines that together with the x-axis form a container that contains the most water. Prove why the two-pointer greedy choice is optimal.",
    "answer": "Place two pointers at the ends: `left = 0`, `right = n - 1`.\nArea = `min(height[left], height[right]) * (right - left)`.\nAt each step, move the pointer pointing to the shorter line inward (`if height[left] < height[right]: left++ else right--`).\n\nProof of Optimality: The width `(right - left)` strictly decreases at every step. If we moved the taller bar inward, the width decreases, but the bottleneck height can never exceed the shorter bar we kept. Thus, no pair with the shorter bar and any interior index can ever produce a larger area than the current pair. Eliminating the shorter bar discards only sub-optimal configurations without missing the global maximum.\n\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "Greedy two-pointer approach shrinks width while hunting for greater height",
      "Always move the pointer with the smaller height",
      "Rigorous proof based on area bounded by min(h[l], h[r])",
      "O(N) time and O(1) space"
    ],
    "tags": [
      "Array",
      "Two Pointers",
      "Greedy"
    ]
  },
  {
    "id": "dsa-11",
    "title": "Trapping Rain Water",
    "category": "Two Pointers",
    "difficulty": "Hard",
    "question": "Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining. Compare the dynamic programming, monotonic stack, and two-pointer approaches.",
    "answer": "Approaches:\n1. Two Pointers (Optimal: O(N) time, O(1) space):\nMaintain `left = 0, right = n-1`, `left_max = 0, right_max = 0`.\nWhile `left < right`:\n- If `height[left] <= height[right]`:\n  - If `height[left] >= left_max`, `left_max = height[left]`.\n  - Else `water += left_max - height[left]`.\n  - `left++`.\n- Else:\n  - If `height[right] >= right_max`, `right_max = height[right]`.\n  - Else `water += right_max - height[right]`.\n  - `right--`.\n2. Monotonic Decreasing Stack: O(N) time & O(N) space. Good for calculating trapped water layer-by-layer horizontally.\n3. DP (Prefix max + Suffix max arrays): O(N) time & O(N) space.",
    "keyPoints": [
      "Two pointers reduces auxiliary space to O(1)",
      "Water trapped at i is min(left_max, right_max) - height[i]",
      "Monotonic stack calculates volume horizontally row by row",
      "Two pointers calculates volume vertically column by column"
    ],
    "tags": [
      "Array",
      "Two Pointers",
      "Monotonic Stack",
      "Dynamic Programming"
    ]
  },
  {
    "id": "dsa-12",
    "title": "Longest Substring Without Repeating Characters",
    "category": "Sliding Window",
    "difficulty": "Medium",
    "question": "Given a string `s`, find the length of the longest substring without repeating characters. What is the optimal sliding window implementation?",
    "answer": "Sliding Window with Last-Seen Index Map:\nMaintain a hash map `last_seen` that maps each character to its most recent index. Maintain window `[left, right]`.\nFor `right` from 0 to `len(s) - 1`:\n- Character `c = s[right]`.\n- If `c` is in `last_seen` and `last_seen[c] >= left`:\n  - Jump `left = last_seen[c] + 1`.\n- Update `last_seen[c] = right`.\n- `max_len = max(max_len, right - left + 1)`.\n\nTime Complexity: O(N) single pass (left pointer jumps directly rather than incrementing one-by-one).\nSpace Complexity: O(min(N, M)) where M is alphabet size.",
    "keyPoints": [
      "Hash map storing character indices allows O(1) jump of left pointer",
      "Condition `last_seen[c] >= left` prevents moving left backwards",
      "Single pass O(N) time complexity",
      "Space bounded by charset size (e.g. 128 for ASCII)"
    ],
    "tags": [
      "String",
      "Sliding Window",
      "Hash Table"
    ]
  },
  {
    "id": "dsa-13",
    "title": "Minimum Window Substring",
    "category": "Sliding Window",
    "difficulty": "Hard",
    "question": "Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string.",
    "answer": "Sliding Window with Character Frequency Counts:\n1. Count character frequencies of `t` in `target_map`. Count required unique characters `required = len(target_map)`.\n2. Maintain `window_map` and `formed = 0` (number of unique characters meeting target count in current window).\n3. Expand `right` pointer:\n   - Add `s[right]` to `window_map`.\n   - If `window_map[c] == target_map[c]`, `formed++`.\n4. When `formed == required`, contract from `left`:\n   - Record window if shorter than previous best.\n   - Decrement `window_map[s[left]]`.\n   - If `window_map[s[left]] < target_map[s[left]]`, `formed--`.\n   - `left++`.\n5. Repeat until `right` reaches end of `s`.\n\nTime Complexity: O(|S| + |T|).\nSpace Complexity: O(|S| + |T|).",
    "keyPoints": [
      "Two frequency maps and a 'formed' count avoid full map comparison on every step",
      "Contract window from left as much as possible once condition is satisfied",
      "Time is O(|S| + |T|), each character visited at most twice",
      "Tracks start index and min length to slice final answer once"
    ],
    "tags": [
      "String",
      "Sliding Window",
      "Hash Table"
    ]
  },
  {
    "id": "dsa-14",
    "title": "Sliding Window Maximum",
    "category": "Sliding Window",
    "difficulty": "Hard",
    "question": "You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. Return the max sliding window. Can you achieve O(N) time?",
    "answer": "Monotonic Decreasing Deque:\nMaintain a double-ended queue `deque` storing *indices* of elements in monotonically decreasing order of their values:\n1. Before inserting index `i`, remove indices from the front that fall outside the window: `while deque and deque[0] < i - k + 1: deque.popleft()`.\n2. Maintain monotonic property: remove elements from the back that are smaller than `nums[i]`: `while deque and nums[deque[-1]] < nums[i]: deque.pop()`.\n3. Append index `i` to the back.\n4. Once `i >= k - 1`, `nums[deque[0]]` is the maximum for the current window.\n\nTime Complexity: O(N) because each element index is pushed and popped from the deque at most once.\nSpace Complexity: O(k) for the deque.",
    "keyPoints": [
      "Monotonic decreasing deque stores candidate maximums",
      "Store indices instead of values to verify window expiry",
      "Each element pushed and popped at most once -> strictly O(N)",
      "Deque front always holds the index of maximum element in window"
    ],
    "tags": [
      "Array",
      "Sliding Window",
      "Monotonic Queue",
      "Deque"
    ]
  },
  {
    "id": "dsa-15",
    "title": "Reverse a Linked List (Iterative & Recursive)",
    "category": "Linked List",
    "difficulty": "Easy",
    "question": "Given the `head` of a singly linked list, reverse the list, and return the reversed list. Explain both iterative and recursive implementations with their space complexities.",
    "answer": "Iterative:\nMaintain three pointers: `prev = null`, `curr = head`, `next = null`.\nWhile `curr != null`:\n  `next = curr.next`\n  `curr.next = prev`\n  `prev = curr`\n  `curr = next`\nReturn `prev`.\nTime: O(N), Space: O(1).\n\nRecursive:\nBase case: `if head == null or head.next == null: return head`.\nRecursively reverse the rest: `new_head = reverseList(head.next)`.\nAttach current node to the end of reversed sublist: `head.next.next = head`, `head.next = null`.\nReturn `new_head`.\nTime: O(N), Space: O(N) call stack.",
    "keyPoints": [
      "Iterative requires 3 pointers and runs in O(1) space",
      "Recursive uses O(N) call stack space",
      "Crucial line in recursion: head.next.next = head, then head.next = null",
      "Common base building block for complex list operations"
    ],
    "tags": [
      "Linked List",
      "Recursion"
    ]
  },
  {
    "id": "dsa-16",
    "title": "Merge Two Sorted Lists",
    "category": "Linked List",
    "difficulty": "Easy",
    "question": "You are given the heads of two sorted linked lists `list1` and `list2`. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.",
    "answer": "Use a dummy head node to simplify edge cases.\nMaintain a pointer `tail = dummy`.\nWhile both `l1` and `l2` are non-null:\n- If `l1.val <= l2.val`: `tail.next = l1; l1 = l1.next`\n- Else: `tail.next = l2; l2 = l2.next`\n- `tail = tail.next`\nAfter the loop, attach the remaining non-null list: `tail.next = l1 if l1 else l2`.\nReturn `dummy.next`.\n\nTime Complexity: O(N + M)\nSpace Complexity: O(1) iterative.",
    "keyPoints": [
      "Dummy head node eliminates null checks for the new head",
      "Splices existing nodes without allocating new nodes",
      "Directly appends remaining non-empty list in O(1)",
      "O(N + M) time and O(1) auxiliary space"
    ],
    "tags": [
      "Linked List",
      "Two Pointers"
    ]
  },
  {
    "id": "dsa-17",
    "title": "Linked List Cycle & Finding Cycle Start",
    "category": "Linked List",
    "difficulty": "Medium",
    "question": "Given the `head` of a linked list, return `true` if there is a cycle, and find the node where the cycle begins. Prove Floyd's Cycle-Finding Algorithm (Tortoise and Hare).",
    "answer": "Floyd's Algorithm:\nPhase 1 (Detection):\n`slow = head, fast = head`.\nAdvance `slow` by 1 step (`slow = slow.next`) and `fast` by 2 steps (`fast = fast.next.next`). If `fast` or `fast.next` reaches null, no cycle. If `slow == fast`, cycle exists.\n\nPhase 2 (Start Node):\nReset `slow = head`, leave `fast` at intersection point. Advance both 1 step at a time (`slow = slow.next`, `fast = fast.next`). The node where they meet is the start of the cycle.\n\nProof: Let distance from head to cycle entrance be `L`, distance from entrance to meeting point be `d`, and cycle length be `C`.\n`dist(slow) = L + d`\n`dist(fast) = L + d + k*C`\nSince fast moves twice as fast: `2(L + d) = L + d + k*C` => `L + d = k*C` => `L = k*C - d`.\nThus, moving `L` steps from head and `L` steps from meeting point brings both pointers to the cycle entrance.\n\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "Floyd's Tortoise and Hare detects cycle in O(N) time and O(1) space",
      "Mathematical proof establishes L = k*C - d",
      "Phase 2 advances both pointers at speed 1 to find entry node",
      "Works without modifying node values or using hash set"
    ],
    "tags": [
      "Linked List",
      "Two Pointers",
      "Floyd Cycle"
    ]
  },
  {
    "id": "dsa-18",
    "title": "LRU Cache Implementation",
    "category": "Linked List",
    "difficulty": "Medium",
    "question": "Design a data structure that follows the constraints of a Least Recently Used (LRU) cache. Implement `get(key)` and `put(key, value)` both running in O(1) average time complexity.",
    "answer": "Data Structure: Hash Map + Doubly Linked List with dummy `head` and `tail`.\n- Hash Map: Maps `key -> Node` for O(1) lookups.\n- Doubly Linked List: Maintains usage order. Most recently used at `head`, least recently used at `tail`.\n\nOperations:\n`get(key)`:\n- If `key` not in map, return -1.\n- Retrieve `node = map[key]`. Move `node` to front of list (remove from current position, insert after `head`).\n- Return `node.val`.\n\n`put(key, value)`:\n- If `key` exists: update `node.val`, move `node` to front.\n- If `key` is new:\n  - If `len(map) == capacity`: remove node before `tail` (`lru_node = tail.prev`), delete `map[lru_node.key]`.\n  - Create new `Node(key, value)`, insert after `head`, add to map.\n\nAll operations execute in O(1) time.",
    "keyPoints": [
      "Doubly linked list allows O(1) node removal and insertion",
      "Hash map allows O(1) node lookup",
      "Dummy head and tail sentinels eliminate edge case null checks",
      "Fundamental system design building block for caching tiers"
    ],
    "tags": [
      "Linked List",
      "Hash Table",
      "Design",
      "LRU Cache"
    ]
  },
  {
    "id": "dsa-19",
    "title": "Merge K Sorted Lists",
    "category": "Linked List",
    "difficulty": "Hard",
    "question": "You are given an array of `k` linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and analyze the time complexity.",
    "answer": "Two primary optimal approaches:\n\n1. Min-Heap (Priority Queue):\nPush the head node of each of the `k` lists into a min-heap: `(node.val, i, node)`. While heap is not empty, pop the smallest node, append to output list, and if `node.next` exists, push `node.next` into heap.\nTime: O(N log k) where N is total number of nodes across all lists.\nSpace: O(k) for the heap.\n\n2. Divide and Conquer (Pairwise Merge):\nMerge pairs of lists iteratively using standard `mergeTwoLists` until only 1 list remains (like Merge Sort bottom-up).\nAt step 1: k/2 merges of length 2N/k.\nAt step 2: k/4 merges of length 4N/k.\nTotal levels = log\u2082 k. Each level processes all N nodes.\nTime: O(N log k).\nAuxiliary Space: O(1) iterative pairwise merge.\n\nDivide and conquer achieves O(1) auxiliary space without heap allocation.",
    "keyPoints": [
      "Min-Heap: O(N log k) time and O(k) space",
      "Divide & Conquer: O(N log k) time and O(1) auxiliary space",
      "Brute-force collecting and sorting is O(N log N)",
      "Sequential pairwise merge is O(k N) - sub-optimal"
    ],
    "tags": [
      "Linked List",
      "Divide and Conquer",
      "Heap",
      "Priority Queue"
    ]
  },
  {
    "id": "dsa-20",
    "title": "Reverse Nodes in k-Group",
    "category": "Linked List",
    "difficulty": "Hard",
    "question": "Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is. You must solve it in O(1) extra memory.",
    "answer": "Iterative Solution in O(1) space:\n1. Use a dummy node pointing to head: `dummy.next = head`. Set `group_prev = dummy`.\n2. While true:\n   - Find the `k-th` node from `group_prev`. If fewer than `k` nodes remain, break.\n   - Store `group_next = kth.next`.\n   - Reverse `k` nodes between `group_prev` and `group_next` using 3 pointers (`prev = group_next, curr = group_prev.next`).\n   - Connect reversed group: `temp = group_prev.next; group_prev.next = kth; group_prev = temp`.\n3. Return `dummy.next`.\n\nTime Complexity: O(N) single pass over all nodes.\nSpace Complexity: O(1) in-place pointer adjustments.",
    "keyPoints": [
      "Check for existence of k nodes before reversing",
      "Preserves tail nodes that form an incomplete group",
      "Sub-procedure reverses exactly k nodes in-place",
      "Maintains group_prev and group_next pointers to stitch groups"
    ],
    "tags": [
      "Linked List",
      "Recursion",
      "In-Place"
    ]
  },
  {
    "id": "dsa-21",
    "title": "Valid Parentheses",
    "category": "Stack",
    "difficulty": "Easy",
    "question": "Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. How do you handle scalability for custom bracket pairs?",
    "answer": "Stack with Hash Map:\nCreate a map of closing brackets to opening brackets: `{')': '(', '}': '{', ']': '['}`.\nInitialize an empty stack.\nFor char `c` in `s`:\n- If `c` is a closing bracket:\n  - If stack is empty or `stack.pop() != map[c]`, return `false`.\n- Else (opening bracket):\n  - Push `c` onto stack.\nReturn `stack.isEmpty()`.\n\nScalability: Mapping bracket pairs in a dictionary allows easy extension to custom delimiters without hardcoding multiple `if-else` branches.\n\nTime: O(N), Space: O(N).",
    "keyPoints": [
      "LIFO stack matches innermost brackets first",
      "Dictionary mapping closing to opening simplifies logic",
      "Must verify stack is empty at the end",
      "O(N) time and O(N) space"
    ],
    "tags": [
      "String",
      "Stack"
    ]
  },
  {
    "id": "dsa-22",
    "title": "Min Stack with O(1) Operations",
    "category": "Stack",
    "difficulty": "Medium",
    "question": "Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time O(1). Can you do this without using a secondary stack?",
    "answer": "Method 1: Two Stacks (or Stack of Pairs):\nMain stack stores values. Secondary stack stores running minimums. When pushing `val`, push `min(val, min_stack.peek())` to `min_stack`.\n\nMethod 2: Single Stack with Value Difference (O(1) extra space):\nStore the difference `val - current_min` on the stack.\n- When pushing `val`: if stack is empty, set `min = val`, push 0. Else, push `diff = val - min`. If `diff < 0`, update `min = val`.\n- When popping: if top `diff < 0`, the popped value was the min, restore previous min: `min = min - diff`.\n- `top()`: if top `diff < 0`, return `min`, else return `min + diff`.\n\nBoth methods provide O(1) for all operations.",
    "keyPoints": [
      "Two stacks / pair stack is clean and avoids integer overflow",
      "Difference encoding achieves strictly O(1) auxiliary space",
      "All operations push, pop, top, getMin are O(1) time",
      "Must guard against integer overflow in languages with fixed-width integers"
    ],
    "tags": [
      "Stack",
      "Design"
    ]
  },
  {
    "id": "dsa-23",
    "title": "Daily Temperatures (Monotonic Stack)",
    "category": "Stack",
    "difficulty": "Medium",
    "question": "Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature. If there is no future day, keep `answer[i] == 0`.",
    "answer": "Monotonic Decreasing Stack:\nMaintain a stack storing indices of days with temperatures in decreasing order.\nInitialize `res = [0] * n`.\nFor `i, temp` in enumerate(temperatures):\n- While stack is non-empty and `temp > temperatures[stack[-1]]`:\n  - `prev_day = stack.pop()`\n  - `res[prev_day] = i - prev_day`\n- `stack.append(i)`\n\nEach index is pushed and popped at most once.\nTime Complexity: O(N).\nSpace Complexity: O(N).",
    "keyPoints": [
      "Monotonic decreasing stack pattern for 'next greater element'",
      "Stores indices so distance can be calculated directly",
      "Each index pushed and popped at most once -> O(N)",
      "Unresolved indices remain 0 as required"
    ],
    "tags": [
      "Array",
      "Stack",
      "Monotonic Stack"
    ]
  },
  {
    "id": "dsa-24",
    "title": "Largest Rectangle in Histogram",
    "category": "Stack",
    "difficulty": "Hard",
    "question": "Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.",
    "answer": "Monotonic Increasing Stack:\nMaintain a stack of pairs `(index, height)`.\nFor each bar `(i, h)`:\n- `start = i`\n- While stack has taller bar `stack[-1].height > h`:\n  - `prev_index, prev_h = stack.pop()`\n  - `max_area = max(max_area, prev_h * (i - prev_index))`\n  - `start = prev_index` (the current shorter bar can extend backwards to `prev_index`)\n- `stack.append((start, h))`\n\nAfter iterating through all bars, process remaining bars extending to end of array `n`:\n- For `(start, h)` in stack: `max_area = max(max_area, h * (n - start))`.\n\nTime Complexity: O(N).\nSpace Complexity: O(N).",
    "keyPoints": [
      "Monotonic increasing stack tracks left boundary where current height could extend",
      "Pop triggers area calculation with height as bottleneck",
      "Width is determined by current index minus popped bar start index",
      "Single pass O(N) time and O(N) space"
    ],
    "tags": [
      "Array",
      "Stack",
      "Monotonic Stack"
    ]
  },
  {
    "id": "dsa-25",
    "title": "Search in Rotated Sorted Array",
    "category": "Binary Search",
    "difficulty": "Medium",
    "question": "Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not. You must write an algorithm with O(log n) runtime complexity.",
    "answer": "Binary Search with Sorted Half Identification:\n`left = 0, right = n - 1`.\nWhile `left <= right`:\n- `mid = (left + right) // 2`\n- If `nums[mid] == target`, return `mid`.\n- Determine which half is sorted:\n  - Left half sorted (`nums[left] <= nums[mid]`):\n    - If `nums[left] <= target < nums[mid]`, search left: `right = mid - 1`.\n    - Else search right: `left = mid + 1`.\n  - Right half sorted (`nums[mid] < nums[left]`):\n    - If `nums[mid] < target <= nums[right]`, search right: `left = mid + 1`.\n    - Else search left: `right = mid - 1`.\nReturn -1 if not found.\n\nTime: O(log N), Space: O(1).",
    "keyPoints": [
      "At least one half is always sorted in a rotated array",
      "Check if target lies inside the sorted half to discard the other half",
      "Condition `nums[left] <= nums[mid]` identifies sorted left half",
      "O(log N) time and O(1) space"
    ],
    "tags": [
      "Array",
      "Binary Search"
    ]
  },
  {
    "id": "dsa-26",
    "title": "Find Minimum in Rotated Sorted Array",
    "category": "Binary Search",
    "difficulty": "Medium",
    "question": "Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times. Given the sorted rotated array `nums` of unique elements, return the minimum element of this array in O(log n) time.",
    "answer": "`left = 0, right = n - 1`.\nWhile `left < right`:\n- If `nums[left] < nums[right]`: array is already sorted, return `nums[left]`.\n- `mid = (left + right) // 2`.\n- If `nums[mid] > nums[right]`:\n  - The inflection point (minimum) must be strictly to the right of `mid`: `left = mid + 1`.\n- Else (`nums[mid] <= nums[right]`):\n  - The minimum could be `mid` or to its left: `right = mid`.\nReturn `nums[left]`.\n\nTime: O(log N), Space: O(1).",
    "keyPoints": [
      "Compare nums[mid] with nums[right] rather than nums[left]",
      "If nums[mid] > nums[right], minimum must lie in right half",
      "Loop condition `left < right` with `right = mid` prevents infinite loop",
      "O(log N) time and O(1) space"
    ],
    "tags": [
      "Array",
      "Binary Search"
    ]
  },
  {
    "id": "dsa-27",
    "title": "Koko Eating Bananas (Binary Search on Answer)",
    "category": "Binary Search",
    "difficulty": "Medium",
    "question": "Koko loves to eat bananas. There are `n` piles of bananas. She can decide her eating speed `k` (bananas/hour). Return the minimum integer `k` such that she can eat all the bananas within `h` hours.",
    "answer": "Binary Search on Value Range `[1, max(piles)]`:\nDefine feasible predicate `canFinish(speed)`:\n- Total hours = `sum(ceil(pile / speed) for pile in piles)`.\n- Return `total_hours <= h`.\n\nSearch range:\n`left = 1, right = max(piles)`.\nWhile `left < right`:\n- `mid = (left + right) // 2`\n- If `canFinish(mid)`:\n  - Valid speed, try smaller: `right = mid`.\n- Else:\n  - Too slow: `left = mid + 1`.\nReturn `left`.\n\nTime Complexity: O(N * log(max(piles))).\nSpace Complexity: O(1).",
    "keyPoints": [
      "Binary search on monotonic answer space",
      "Ceil division without floats: (pile + speed - 1) // speed",
      "Predicate function canFinish runs in O(N)",
      "Classic pattern for capacity, throughput, and optimization questions"
    ],
    "tags": [
      "Array",
      "Binary Search",
      "Optimization"
    ]
  },
  {
    "id": "dsa-28",
    "title": "Median of Two Sorted Arrays",
    "category": "Binary Search",
    "difficulty": "Hard",
    "question": "Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).",
    "answer": "Binary Search on Partition of the Shorter Array:\nEnsure `len(A) <= len(B)`. Total elements `total = m + n`, half = `(total + 1) // 2`.\nBinary search on partition `A`: `left = 0, right = m`.\nWhile `left <= right`:\n- `i = (left + right) // 2` (elements from A)\n- `j = half - i` (elements from B)\n- `A_left = A[i-1]` if `i > 0` else `-inf`\n- `A_right = A[i]` if `i < m` else `inf`\n- `B_left = B[j-1]` if `j > 0` else `-inf`\n- `B_right = B[j]` if `j < n` else `inf`\n- Check partition validity: `A_left <= B_right` and `B_left <= A_right`:\n  - If valid: if `total % 2 != 0`, return `max(A_left, B_left)`. Else return `(max(A_left, B_left) + min(A_right, B_right)) / 2.0`.\n  - Else if `A_left > B_right`: move partition left `right = i - 1`.\n  - Else: move partition right `left = i + 1`.\n\nTime Complexity: O(log(min(m, n))).\nSpace Complexity: O(1).",
    "keyPoints": [
      "Partitions both arrays such that left half has same size as right half",
      "Binary search on shorter array ensures O(log(min(m, n))) complexity",
      "Guard boundaries with -infinity and +infinity",
      "Returns exact median without allocating merged array"
    ],
    "tags": [
      "Array",
      "Binary Search",
      "Divide and Conquer"
    ]
  },
  {
    "id": "dsa-29",
    "title": "Invert / Flip Binary Tree",
    "category": "Trees",
    "difficulty": "Easy",
    "question": "Given the `root` of a binary tree, invert the tree, and return its root. Discuss both recursive and iterative level-order solutions.",
    "answer": "Recursive (DFS):\nBase case: `if not root: return None`.\nSwap children: `root.left, root.right = invertTree(root.right), invertTree(root.left)`.\nReturn `root`.\n\nIterative (BFS with Queue):\nInitialize `queue = deque([root])`.\nWhile queue is not empty:\n- `node = queue.popleft()`\n- Swap: `node.left, node.right = node.right, node.left`\n- If `node.left`: `queue.append(node.left)`\n- If `node.right`: `queue.append(node.right)`\nReturn `root`.\n\nTime Complexity: O(N) visits every node once.\nSpace Complexity: O(H) recursion stack for DFS (O(N) worst, O(log N) balanced) or O(W) queue width for BFS.",
    "keyPoints": [
      "Swaps left and right pointers at every node",
      "DFS recursion uses O(H) stack frames",
      "BFS queue uses O(W) space where W is max width of tree",
      "Linear time O(N)"
    ],
    "tags": [
      "Tree",
      "Depth-First Search",
      "Breadth-First Search"
    ]
  },
  {
    "id": "dsa-30",
    "title": "Maximum Depth of Binary Tree",
    "category": "Trees",
    "difficulty": "Easy",
    "question": "Given the `root` of a binary tree, return its maximum depth. Compare recursive DFS, iterative DFS with stack, and iterative BFS.",
    "answer": "1. Recursive DFS: `if not root: return 0; return 1 + max(maxDepth(root.left), maxDepth(root.right))`.\n2. Iterative BFS: Level-order traversal with queue. Increment `depth` after consuming each complete level.\n3. Iterative DFS: Stack storing `(node, current_depth)`. Maintain global `max_depth`.\n\nTime: O(N) for all.\nSpace: O(H) for DFS, O(W) for BFS.",
    "keyPoints": [
      "Recursive DFS is elegant and concise",
      "BFS processes level by level using queue size snapshot",
      "Time is strictly O(N) visiting each node once",
      "Space depends on height H (DFS) vs max width W (BFS)"
    ],
    "tags": [
      "Tree",
      "DFS",
      "BFS"
    ]
  },
  {
    "id": "dsa-31",
    "title": "Diameter of Binary Tree",
    "category": "Trees",
    "difficulty": "Easy",
    "question": "Given the `root` of a binary tree, return the length of the diameter of the tree. The diameter is the length of the longest path between any two nodes. This path may or may not pass through the root.",
    "answer": "Post-Order DFS with Global Maximum:\nMaintain `max_diameter = 0`.\nHelper function `height(node)` returns height of subtree:\n- Base case: `if not node: return 0`.\n- `left_h = height(node.left)`\n- `right_h = height(node.right)`\n- Path through current node: `left_h + right_h` edges.\n- `max_diameter = max(max_diameter, left_h + right_h)`.\n- Return `1 + max(left_h, right_h)` to parent.\n\nTime Complexity: O(N) single traversal.\nSpace Complexity: O(H) call stack.",
    "keyPoints": [
      "Post-order traversal computes heights from bottom-up",
      "Diameter at node = left_height + right_height",
      "Diameter path might not pass through root",
      "O(N) time and O(H) space"
    ],
    "tags": [
      "Tree",
      "DFS"
    ]
  },
  {
    "id": "dsa-32",
    "title": "Lowest Common Ancestor (LCA) in Binary Tree & BST",
    "category": "Trees",
    "difficulty": "Medium",
    "question": "Given a binary tree and two nodes `p` and `q`, find their lowest common ancestor. How does the solution differ between a general Binary Tree and a Binary Search Tree (BST)?",
    "answer": "General Binary Tree:\nPost-order DFS:\n- Base cases: if `root is None` or `root == p` or `root == q`, return `root`.\n- `left = LCA(root.left, p, q)`\n- `right = LCA(root.right, p, q)`\n- If both `left` and `right` are non-null, `root` is the LCA!\n- If only one is non-null, return that non-null node.\nTime: O(N), Space: O(H).\n\nBinary Search Tree (BST):\nTake advantage of BST ordering:\n- If both `p.val` and `q.val` < `root.val`, LCA must be in `root.left`.\n- If both `p.val` and `q.val` > `root.val`, LCA must be in `root.right`.\n- If `p` and `q` split across `root` (or one equals `root`), `root` is the split point and hence LCA!\nTime: O(H) = O(log N) on average, Space: O(1) iterative.",
    "keyPoints": [
      "BST allows O(log N) decision at each step by comparing values",
      "General tree requires post-order traversal O(N)",
      "Split condition in BST immediately identifies LCA",
      "Iterative BST LCA achieves O(1) extra space"
    ],
    "tags": [
      "Tree",
      "BST",
      "DFS",
      "Binary Search Tree"
    ]
  },
  {
    "id": "dsa-33",
    "title": "Binary Tree Level Order Traversal",
    "category": "Trees",
    "difficulty": "Medium",
    "question": "Given the `root` of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).",
    "answer": "Queue-based BFS with Level Size Snapshot:\nIf `not root: return []`.\n`result = []`, `queue = deque([root])`.\nWhile `queue` is not empty:\n- `level_size = len(queue)`\n- `current_level = []`\n- Loop `level_size` times:\n  - `node = queue.popleft()`\n  - `current_level.append(node.val)`\n  - If `node.left`: `queue.append(node.left)`\n  - If `node.right`: `queue.append(node.right)`\n- `result.append(current_level)`\nReturn `result`.\n\nTime Complexity: O(N).\nSpace Complexity: O(N) max width queue.",
    "keyPoints": [
      "Capturing len(queue) at start of while loop defines level boundary",
      "Standard pattern for Zigzag traversal, Right Side View, Level Averages",
      "FIFO queue guarantees top-to-bottom left-to-right order",
      "O(N) time and O(W) auxiliary space"
    ],
    "tags": [
      "Tree",
      "BFS",
      "Queue"
    ]
  },
  {
    "id": "dsa-34",
    "title": "Validate Binary Search Tree",
    "category": "Trees",
    "difficulty": "Medium",
    "question": "Given the `root` of a binary tree, determine if it is a valid binary search tree (BST). Explain why checking `node.left.val < node.val < node.right.val` locally is insufficient.",
    "answer": "Local check is insufficient because ALL nodes in the left subtree must be less than `node.val`, and all nodes in right subtree must be greater.\nExample: `[10, 5, 15, null, null, 6, 20]`: 6 is < 15, but 6 is in the right subtree of 10, violating BST property!\n\nCorrect Methods:\n1. Range Validation DFS: Pass allowed `(low, high)` bounds.\n`def validate(node, low, high):`\n  `if not node: return True`\n  `if not (low < node.val < high): return False`\n  `return validate(node.left, low, node.val) and validate(node.right, node.val, high)`\nCall `validate(root, -inf, inf)`.\n\n2. In-Order Traversal: In-order traversal of a valid BST must yield strictly ascending values. Track `prev_val` and verify `node.val > prev_val`.\n\nTime: O(N), Space: O(H).",
    "keyPoints": [
      "Every node must satisfy global (min, max) boundary conditions",
      "In-order traversal of BST produces strictly increasing sequence",
      "Local parent-child checks miss ancestral violations",
      "O(N) time and O(H) space"
    ],
    "tags": [
      "Tree",
      "BST",
      "DFS"
    ]
  },
  {
    "id": "dsa-35",
    "title": "Construct Binary Tree from Preorder and Inorder Traversal",
    "category": "Trees",
    "difficulty": "Medium",
    "question": "Given two integer arrays `preorder` and `inorder`, construct and return the binary tree. Optimize node lookup using a hash map.",
    "answer": "Properties:\n- `preorder[0]` is always the root of the current subtree.\n- Locating root value in `inorder` splits it into `left_inorder` and `right_inorder`.\n- Number of nodes in left subtree = `mid - in_start`.\n\nAlgorithm with Hash Map:\n1. Build `inorder_map = {val: idx for idx, val in enumerate(inorder)}` for O(1) index lookup.\n2. Maintain `pre_idx` pointer.\n3. Helper `build(in_start, in_end)`:\n   - If `in_start > in_end: return None`.\n   - `root_val = preorder[pre_idx]; pre_idx += 1`.\n   - `mid = inorder_map[root_val]`.\n   - `root = TreeNode(root_val)`.\n   - `root.left = build(in_start, mid - 1)`.\n   - `root.right = build(mid + 1, in_end)`.\n   - Return `root`.\n\nTime Complexity: O(N) (hash map eliminates O(N) search per node).\nSpace Complexity: O(N) map and recursion stack.",
    "keyPoints": [
      "Preorder determines root node; Inorder partitions left and right subtrees",
      "Hash map of inorder indices reduces complexity from O(N\u00b2) to O(N)",
      "Must construct left child before right child when incrementing preorder index",
      "Linear time O(N) and linear space O(N)"
    ],
    "tags": [
      "Tree",
      "Array",
      "Divide and Conquer",
      "DFS"
    ]
  },
  {
    "id": "dsa-36",
    "title": "Binary Tree Maximum Path Sum",
    "category": "Trees",
    "difficulty": "Hard",
    "question": "A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. A node can only appear at most once. Return the maximum path sum of any non-empty path.",
    "answer": "Post-Order DFS with Subtree Contribution:\nMaintain `max_sum = -inf`.\nHelper function `max_gain(node)` returns the maximum sum of a path starting at `node` and extending down one branch:\n- If `not node: return 0`.\n- `left_gain = max(max_gain(node.left), 0)` (ignore negative sums by taking 0).\n- `right_gain = max(max_gain(node.right), 0)`.\n- Price of new path through current node: `price_newpath = node.val + left_gain + right_gain`.\n- Update global: `max_sum = max(max_sum, price_newpath)`.\n- Return to parent: `node.val + max(left_gain, right_gain)` (can only choose one branch to continue path upward).\n\nTime Complexity: O(N).\nSpace Complexity: O(H).",
    "keyPoints": [
      "Ignore negative subtree contributions using max(gain, 0)",
      "Path turning point combines both left and right gains at current node",
      "Return value to parent can only choose one branch (left or right)",
      "O(N) time and O(H) space"
    ],
    "tags": [
      "Tree",
      "DFS",
      "Dynamic Programming"
    ]
  },
  {
    "id": "dsa-37",
    "title": "Serialize and Deserialize Binary Tree",
    "category": "Trees",
    "difficulty": "Hard",
    "question": "Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.",
    "answer": "Pre-Order DFS with Delimiter and Null Markers:\nSerialize:\n- Pre-order traversal.\n- If node is null, append `'N,'`.\n- Else append `str(node.val) + ','`, then recurse left and right.\nExample: `1,2,N,N,3,4,N,N,5,N,N`.\n\nDeserialize:\n- Split serialized string by `,` into a queue or list iterator of tokens.\n- Helper `build()`:\n  - Pop token from queue.\n  - If token == `'N'`: return `None`.\n  - `node = TreeNode(int(token))`.\n  - `node.left = build()`.\n  - `node.right = build()`.\n  - Return `node`.\n\nTime Complexity: O(N) for both serialize and deserialize.\nSpace Complexity: O(N) string storage and recursion stack.",
    "keyPoints": [
      "Preorder traversal with explicit null markers encodes tree uniquely",
      "No need for both preorder and inorder if nulls are preserved",
      "Queue of tokens makes deserialization clean and linear O(N)",
      "Alternative: Level-order BFS with queue"
    ],
    "tags": [
      "Tree",
      "Design",
      "DFS",
      "BFS"
    ]
  },
  {
    "id": "dsa-38",
    "title": "Implement Trie (Prefix Tree)",
    "category": "Trie",
    "difficulty": "Medium",
    "question": "Implement a Trie with `insert`, `search`, and `startsWith` methods. What are the time and space trade-offs compared to a Hash Table?",
    "answer": "Trie Node structure:\n`class TrieNode:`\n  `children = {}` (or array of size 26)\n  `is_end_of_word = False`\n\nMethods:\n- `insert(word)`: Traverse character by character, creating child `TrieNode` if not present. Mark last node `is_end_of_word = True`. Time: O(L).\n- `search(word)`: Traverse character by character. If child missing, return `false`. Return `curr.is_end_of_word`. Time: O(L).\n- `startsWith(prefix)`: Traverse prefix. If all characters exist, return `true`. Time: O(P).\n\nTrade-off vs Hash Table:\n- Hash Table: O(L) hash computation, but cannot perform prefix matching (`startsWith`) or wildcard search efficiently without full scan.\n- Trie: Efficient prefix searches, auto-complete, common prefix extraction, memory sharing for common prefixes, but higher node pointer overhead.",
    "keyPoints": [
      "O(L) operations where L is string length, independent of total words N",
      "Enables prefix queries and auto-completion",
      "Array of 26 pointers vs HashMap children trade-off",
      "Essential for IP routing tables, spellcheckers, and search engines"
    ],
    "tags": [
      "Trie",
      "Design",
      "Hash Table"
    ]
  },
  {
    "id": "dsa-39",
    "title": "Word Search II (Boggle with Trie & Backtracking)",
    "category": "Trie",
    "difficulty": "Hard",
    "question": "Given an `m x n` board of characters and a list of strings `words`, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells (horizontal or vertical). You cannot revisit cells in a single word.",
    "answer": "Trie + 2D Backtracking DFS:\n1. Build a Trie containing all `words`. Store the complete word string directly in the leaf node `node.word = word` to avoid rebuilding string during DFS.\n2. DFS from each cell `(r, c)`:\n   - Base cases: out of bounds or visited marker `#`.\n   - Check if `char` exists in current `trie_node.children`. If not, return.\n   - Move to child node `curr = curr.children[char]`.\n   - If `curr.word`: record word in `result`, set `curr.word = None` to avoid duplicates.\n   - Mark cell visited: `board[r][c] = '#'`.\n   - Recurse in 4 directions.\n   - Backtrack: restore `board[r][c] = char`.\n3. Optimization (Trie Pruning): When a leaf node has no children left after word extraction, delete it from parent to prune fruitless search branches early.\n\nTime Complexity: O(M * N * 4 * 3^(L-1)) where L is maximum word length.",
    "keyPoints": [
      "Trie allows searching all words simultaneously in single board traversal",
      "Storing full word at Trie leaf avoids string concatenation in recursion",
      "Pruning dead Trie branches dramatically accelerates execution",
      "In-place board mutation board[r][c]='#' achieves O(1) visited memory"
    ],
    "tags": [
      "Trie",
      "Backtracking",
      "Matrix",
      "DFS"
    ]
  },
  {
    "id": "dsa-40",
    "title": "Kth Largest Element in an Array (Quickselect vs Min-Heap)",
    "category": "Heap",
    "difficulty": "Medium",
    "question": "Given an integer array `nums` and an integer `k`, return the `k-th` largest element in the array. Compare Min-Heap and Quickselect solutions.",
    "answer": "1. Min-Heap of size K:\nMaintain a min-heap. Push each element. If `len(heap) > k`, pop the smallest. The root at the end is the k-th largest element.\nTime: O(N log k), Space: O(k).\n\n2. Quickselect (Hoare's Selection Algorithm):\nFind element at index `target = len(nums) - k`.\nPartition array around a random pivot (Lomuto or Hoare):\n- Elements < pivot go left, > pivot go right.\n- If `pivot_idx == target`: return `nums[pivot_idx]`.\n- If `pivot_idx < target`: search right half.\n- Else: search left half.\nAverage Time: O(N) because N + N/2 + N/4 + ... = 2N.\nWorst Time: O(N\u00b2) (mitigated with random pivot).\nSpace: O(1) iterative.",
    "keyPoints": [
      "Quickselect achieves O(N) average time and O(1) space",
      "Min-Heap achieves O(N log K) time and O(K) space (ideal for streaming data)",
      "Random pivot avoids O(N\u00b2) worst-case on pre-sorted arrays",
      "Quickselect modifies input array in-place"
    ],
    "tags": [
      "Array",
      "Heap",
      "Quickselect",
      "Divide and Conquer"
    ]
  },
  {
    "id": "dsa-41",
    "title": "Find Median from Data Stream",
    "category": "Heap",
    "difficulty": "Hard",
    "question": "The median is the middle value in an ordered integer list. Implement the `MedianFinder` class with `addNum(int num)` and `findMedian()` in O(log n) and O(1) time respectively.",
    "answer": "Two Balanced Heaps (Max-Heap + Min-Heap):\n- `small`: Max-heap storing lower half of numbers (inverted signs in Python).\n- `large`: Min-heap storing upper half of numbers.\n\nInvariants to maintain:\n1. Every element in `small` <= every element in `large`.\n2. Size property: `len(small) == len(large)` or `len(small) == len(large) + 1`.\n\n`addNum(num)`:\n- Push to `small`.\n- Pop max from `small` and push to `large` to enforce order.\n- If `len(large) > len(small)`: pop min from `large` and push to `small` to balance size.\nTime: O(log N).\n\n`findMedian()`:\n- If `len(small) > len(large)`: return `small.peek()`.\n- Else: return `(small.peek() + large.peek()) / 2.0`.\nTime: O(1).",
    "keyPoints": [
      "Two heaps divide data stream into lower and upper halves",
      "addNum runs in O(log N) time",
      "findMedian runs in O(1) time",
      "Carefully balance heap sizes after every insertion"
    ],
    "tags": [
      "Heap",
      "Design",
      "Data Stream"
    ]
  },
  {
    "id": "dsa-42",
    "title": "Task Scheduler (CPU Cooling Period)",
    "category": "Heap",
    "difficulty": "Medium",
    "question": "Given a characters array `tasks`, representing CPU tasks, and an integer `n` as cooling period between same tasks, return the minimum units of time required to complete all tasks.",
    "answer": "Greedy / Math Approach:\n1. Count task frequencies. Let `max_freq` be the maximum frequency of any task, and `max_count` be the number of tasks that share `max_freq`.\n2. Formula:\n   - There are `max_freq - 1` complete chunks.\n   - Each chunk has length `n + 1` (the task plus `n` cooling slots).\n   - The final chunk contains only the tasks with `max_freq`.\n   - Minimum time = `(max_freq - 1) * (n + 1) + max_count`.\n3. However, if there are so many distinct tasks that cooling slots are naturally filled with other tasks, the answer is simply the total number of tasks `len(tasks)`.\nResult = `max(len(tasks), (max_freq - 1) * (n + 1) + max_count)`.\n\nTime Complexity: O(N) single pass to count frequencies.\nSpace Complexity: O(1) 26 uppercase letters.",
    "keyPoints": [
      "Mathematical chunk formula resolves idle slots in O(N) time and O(1) space",
      "Alternative: Max-Heap with cooling wait queue runs in O(T log 26)",
      "Bottleneck is always the most frequent task",
      "Formula handles under-saturation and over-saturation cleanly"
    ],
    "tags": [
      "Array",
      "Hash Table",
      "Greedy",
      "Heap",
      "Math"
    ]
  },
  {
    "id": "dsa-43",
    "title": "Number of Islands",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands. Compare BFS, DFS, and Disjoint Set (Union-Find).",
    "answer": "1. DFS / BFS (In-place):\nIterate through each cell `(r, c)`.\nWhen `grid[r][c] == '1'`:\n- Increment `islands_count`.\n- Run DFS or BFS to sink the entire island by marking visited cells as `'0'`.\n- Explore 4 orthogonal neighbors.\nTime: O(M * N), Space: O(M * N) recursion stack / queue.\n\n2. Disjoint Set Union (Union-Find):\n- Initialize DSU with count = total '1' cells.\n- Iterate through grid; for each '1', union with adjacent '1's (right and down).\n- Each successful union decrements island count.\n- Time: O(M * N * \u03b1(MN)), Space: O(M * N).\n\nTrade-off: DFS/BFS in-place uses O(1) auxiliary heap memory if grid mutation is permitted.",
    "keyPoints": [
      "Sinking visited land to '0' avoids extra visited set memory",
      "DFS or BFS both visit each cell at most twice -> O(M * N)",
      "Union-Find is excellent for dynamic streaming connectivity",
      "Handle grid boundaries and edge cases"
    ],
    "tags": [
      "Array",
      "DFS",
      "BFS",
      "Union Find",
      "Matrix"
    ]
  },
  {
    "id": "dsa-44",
    "title": "Course Schedule I & II (Cycle Detection & Topological Sort)",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "There are `numCourses` labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [a, b]` indicates you must take `b` before `a`. Can you finish all courses? If yes, return the valid course order. Discuss Kahn's Algorithm and DFS 3-coloring.",
    "answer": "1. Kahn's Algorithm (BFS Topological Sort):\n- Build adjacency list `adj` and calculate in-degree for every course.\n- Initialize `queue` with all courses having `in_degree == 0`.\n- `order = []`.\n- While queue not empty:\n  - `curr = queue.popleft()`\n  - `order.append(curr)`\n  - For neighbor in `adj[curr]`:\n    - `in_degree[neighbor] -= 1`\n    - If `in_degree[neighbor] == 0`: `queue.append(neighbor)`\n- If `len(order) == numCourses`, return `order` (valid DAG). Else, cycle exists!\n\n2. DFS 3-Coloring:\nState 0 = Unvisited, 1 = Visiting (in current recursion path), 2 = Visited.\nIf DFS encounters a node with State 1, a back-edge (cycle) is detected.\n\nTime Complexity: O(V + E).\nSpace Complexity: O(V + E).",
    "keyPoints": [
      "Kahn's BFS algorithm tracks in-degrees and uses a queue",
      "Cycle exists if topologically sorted list length < total courses",
      "DFS 3-state coloring detects back-edges in directed graphs",
      "O(V + E) time and O(V + E) space"
    ],
    "tags": [
      "Graph",
      "BFS",
      "DFS",
      "Topological Sort"
    ]
  },
  {
    "id": "dsa-45",
    "title": "Clone Graph",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. How do you handle cycles during traversal?",
    "answer": "Hash Map Tracking Visited/Cloned Nodes:\nUse a map `visited = {}` mapping `original_node -> cloned_node` to avoid infinite loops caused by cycles.\n\nDFS Approach:\n`def clone(node):`\n  `if not node: return None`\n  `if node in visited: return visited[node]`\n  `copy = Node(node.val)`\n  `visited[node] = copy`\n  `for neighbor in node.neighbors:`\n    `copy.neighbors.append(clone(neighbor))`\n  `return copy`\n\nBFS Approach:\nInitialize queue with start node, create its copy and store in `visited`. While queue not empty, dequeue node, iterate neighbors: if neighbor not visited, copy it, store in map, and enqueue. Append copied neighbor to copied node's neighbors.\n\nTime: O(V + E), Space: O(V) hash map and call stack.",
    "keyPoints": [
      "Map of original_node -> cloned_node prevents infinite cycles",
      "DFS or BFS both visit each node and edge exactly once",
      "Creates clone node BEFORE recursing on neighbors",
      "O(V + E) time and O(V) space"
    ],
    "tags": [
      "Hash Table",
      "DFS",
      "BFS",
      "Graph"
    ]
  },
  {
    "id": "dsa-46",
    "title": "Word Ladder (Shortest Transformation Sequence)",
    "category": "Graphs",
    "difficulty": "Hard",
    "question": "Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, where each step changes exactly one letter. Compare bidirectional BFS with standard BFS.",
    "answer": "1. Standard BFS:\nConvert `wordList` to a set for O(1) lookup. Initialize `queue = deque([(beginWord, 1)])`.\nWhile queue is not empty:\n- `word, length = queue.popleft()`\n- If `word == endWord: return length`.\n- For each char position `i` in word (len L):\n  - Try replacing with 'a' through 'z' (26 variations).\n  - If new word in set: remove from set (marks visited) and `queue.append((new_word, length + 1))`.\nIf queue exhausts, return 0.\nTime: O(M * 26 * L\u00b2) where M is word list size and L is word length.\n\n2. Bidirectional BFS:\nSearch simultaneously from `beginWord` and `endWord`. Expand the smaller set at each step. Greatly reduces the search branching tree from O(b^d) to O(b^(d/2)).",
    "keyPoints": [
      "BFS guarantees shortest transformation path in unweighted graph",
      "Generate 26*L mutations rather than comparing against all words in dictionary",
      "Removing word from set upon discovery eliminates separate visited set",
      "Bidirectional BFS cuts branching factor exponentially"
    ],
    "tags": [
      "Hash Table",
      "String",
      "BFS",
      "Graph"
    ]
  },
  {
    "id": "dsa-47",
    "title": "Network Delay Time (Dijkstra's Algorithm)",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "You are given a network of `n` nodes labeled from 1 to `n` and a list of travel times directed edges `times[i] = (u, v, w)`. How long will it take for all nodes to receive a signal sent from node `k`? If impossible, return -1.",
    "answer": "Dijkstra's Algorithm with Min-Heap:\n1. Build adjacency list: `adj[u] = [(v, w)]`.\n2. Maintain `min_dist = {}`, `heap = [(0, k)]` (stores `(cost, node)`).\n3. While heap is not empty:\n   - `cost, u = heapq.heappop(heap)`\n   - If `u` already in `min_dist`: continue (already found shorter path).\n   - `min_dist[u] = cost`\n   - For `(v, w)` in `adj[u]`:\n     - If `v` not in `min_dist`:\n       - `heapq.heappush(heap, (cost + w, v))`\n4. If `len(min_dist) == n`: return `max(min_dist.values())`. Else return -1.\n\nTime Complexity: O(E log V) with binary heap.\nSpace Complexity: O(V + E).",
    "keyPoints": [
      "Dijkstra handles non-negative weighted graphs optimally",
      "Min-heap extracts currently shortest path vertex in O(log V)",
      "Early skipping of already finalized nodes avoids stale heap entries",
      "Returns max time among all nodes, or -1 if unreachable"
    ],
    "tags": [
      "Graph",
      "Heap",
      "Shortest Path",
      "Dijkstra"
    ]
  },
  {
    "id": "dsa-48",
    "title": "Cheapest Flights Within K Stops (Bellman-Ford / Modified Dijkstra)",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "There are `n` cities and `flights` where `flights[i] = [from, to, price]`. Find the cheapest price from `src` to `dst` with at most `k` stops. Why does standard Dijkstra fail without modifications?",
    "answer": "Standard Dijkstra fails because it eagerly prunes paths with higher costs, but a path with higher cost might have fewer stops and be the only one that reaches within `k` stops!\n\nApproach 1: Bellman-Ford (k+1 iterations):\nInitialize `prices = [inf] * n; prices[src] = 0`.\nRun `k + 1` rounds:\n- Make a copy `temp = prices.copy()`.\n- For `u, v, w` in `flights`:\n  - If `prices[u] != inf and prices[u] + w < temp[v]`:\n    - `temp[v] = prices[u] + w`\n- `prices = temp`\nReturn `prices[dst]` if != inf else -1.\nTime: O(K * E), Space: O(V).\n\nApproach 2: Modified Dijkstra storing `(cost, node, stops)` in priority queue and maintaining `stops_table`.",
    "keyPoints": [
      "Bellman-Ford with k+1 relaxation rounds naturally enforces at most k stops",
      "Must use previous round copy (temp) to prevent propagating multiple edges in 1 step",
      "Standard Dijkstra fails because cost optimality does not equal stop optimality",
      "Time O(K * E) and Space O(V)"
    ],
    "tags": [
      "Dynamic Programming",
      "Graph",
      "Shortest Path",
      "Bellman-Ford"
    ]
  },
  {
    "id": "dsa-49",
    "title": "Alien Dictionary (Topological Sort on Directed Graph)",
    "category": "Graphs",
    "difficulty": "Hard",
    "question": "There is a new alien language that uses the English alphabet. You are given a list of words from the dictionary, where words are claimed to be sorted lexicographically by the rules of this new language. Derive the order of letters in this language. Handle invalid ordering cases.",
    "answer": "Graph Construction + Topological Sort:\n1. Nodes: Every unique character in `words`.\n2. Directed Edges: Compare adjacent words `w1` and `w2`:\n   - Find first mismatching character `c1 != c2`: add directed edge `c1 -> c2` (`c1` precedes `c2`), break.\n   - Edge Case (Invalid prefix): If `len(w1) > len(w2)` and `w1.startswith(w2)`, dictionary order is invalid! Return `\"\"` immediately (e.g. `[\"apple\", \"app\"]` is invalid).\n3. Topological Sort (Post-Order DFS or Kahn's BFS):\n   - Run cycle detection.\n   - If a cycle exists, return `\"\"`.\n   - Otherwise, return topologically sorted characters.\n\nTime Complexity: O(C) where C is total length of all words in the input.\nSpace Complexity: O(V + E) = O(1) since English alphabet has at most 26 characters.",
    "keyPoints": [
      "Lexicographical order is determined by first differing character",
      "Detect prefix anomaly (longer word preceding its own prefix is invalid)",
      "Cycle detection identifies impossible ordering constraints",
      "Topological sort generates valid total or partial character sequence"
    ],
    "tags": [
      "Graph",
      "Topological Sort",
      "DFS",
      "String"
    ]
  },
  {
    "id": "dsa-50",
    "title": "Tarjan's Algorithm: Critical Connections in a Network",
    "category": "Graphs",
    "difficulty": "Hard",
    "question": "An edge in an undirected connected graph is a bridge (critical connection) if removing it disconnects the graph. Find all bridges in O(V + E) time using Tarjan's Bridge-Finding Algorithm.",
    "answer": "Tarjan's DFS with Discovery and Low-link Times:\n- `disc[u]`: Discovery time of vertex `u`.\n- `low[u]`: Lowest discovery time reachable from `u` using back-edges.\n- `time = 0`.\n\nDFS(u, parent):\n- `disc[u] = low[u] = time; time += 1`\n- For `v` in `adj[u]`:\n  - If `v == parent`: continue (do not traverse bidirectional edge back immediately).\n  - If `disc[v] != -1` (already visited -> back-edge):\n    - `low[u] = min(low[u], disc[v])`\n  - Else (unvisited tree-edge):\n    - `DFS(v, u)`\n    - `low[u] = min(low[u], low[v])`\n    - Bridge Condition: If `low[v] > disc[u]`:\n      - Edge `(u, v)` is a bridge! Because `v` has no back-edge to reach `u` or any ancestor of `u`.\n\nTime Complexity: O(V + E) single DFS.\nSpace Complexity: O(V + E) graph and call stack.",
    "keyPoints": [
      "low[v] > disc[u] means no back-edge from subtree v to u or higher",
      "Finds all network bridges in a single DFS pass",
      "Essential for distributed systems fault tolerance and network redundancy",
      "Linear time O(V + E)"
    ],
    "tags": [
      "Graph",
      "DFS",
      "Tarjan",
      "Bridges"
    ]
  },
  {
    "id": "dsa-51",
    "title": "Climbing Stairs (Fibonacci DP)",
    "category": "Dynamic Programming",
    "difficulty": "Easy",
    "question": "You are climbing a staircase. It takes `n` steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? Reduce space to O(1).",
    "answer": "Recurrence Relation:\nTo reach step `n`, you either step from `n-1` (1 step) or from `n-2` (2 steps).\n`dp[n] = dp[n-1] + dp[n-2]` with base cases `dp[1] = 1, dp[2] = 2`.\n\nSpace Optimization to O(1):\n`a = 1, b = 2`.\nFor `i` from 3 to `n`:\n  `c = a + b`\n  `a = b`\n  `b = c`\nReturn `b`.\n\nTime: O(N), Space: O(1).\n(Matrix exponentiation can further achieve O(log N)).",
    "keyPoints": [
      "Exact Fibonacci sequence with offset base cases",
      "State dp[i] depends only on previous two states",
      "Space optimized from O(N) to O(1)",
      "Can be solved in O(log N) using matrix exponentiation"
    ],
    "tags": [
      "Dynamic Programming",
      "Math"
    ]
  },
  {
    "id": "dsa-52",
    "title": "Coin Change (Minimum Coins)",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "You are given an integer array `coins` representing coins of different denominations and an integer `amount`. Return the fewest number of coins that you need to make up that amount. If that amount cannot be made up, return -1.",
    "answer": "Bottom-Up Unbounded Knapsack DP:\nLet `dp[i]` be minimum coins needed to make amount `i`.\nInitialize `dp = [inf] * (amount + 1)`, `dp[0] = 0`.\nFor `a` from 1 to `amount`:\n  For `c` in `coins`:\n    If `a - c >= 0`:\n      `dp[a] = min(dp[a], 1 + dp[a - c])`\nReturn `dp[amount]` if != inf else -1.\n\nTime Complexity: O(amount * len(coins)).\nSpace Complexity: O(amount).\n\nBFS Alternative: Shortest path in graph where each level subtracts coin denominations.",
    "keyPoints": [
      "Unbounded knapsack sub-problem",
      "State: dp[a] = min(dp[a], 1 + dp[a - coin])",
      "Initialize array with infinity and dp[0] = 0",
      "Time O(Amount * Coins) and Space O(Amount)"
    ],
    "tags": [
      "Dynamic Programming",
      "Knapsack",
      "BFS"
    ]
  },
  {
    "id": "dsa-53",
    "title": "Coin Change II (Number of Combinations)",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "You are given an integer array `coins` and an integer `amount`. Return the number of combinations that make up that amount. Why must the outer loop iterate over coins rather than amounts?",
    "answer": "Outer Loop must iterate over COINS to prevent counting permutations:\nIf outer loop is `coins`:\nEach coin is considered sequentially. We only form combinations where coins are in non-decreasing order of denomination, avoiding counting `[1, 2]` and `[2, 1]` as separate ways.\n\nAlgorithm:\n`dp = [0] * (amount + 1); dp[0] = 1`\nFor `c` in `coins`:\n  For `a` from `c` to `amount`:\n    `dp[a] += dp[a - c]`\nReturn `dp[amount]`.\n\nTime Complexity: O(amount * len(coins)).\nSpace Complexity: O(amount).",
    "keyPoints": [
      "Outer loop over coins enforces combination order (no duplicates)",
      "Inner loop from coin to amount handles unbounded supply",
      "dp[0] = 1 represents 1 way to make 0 amount (empty set)",
      "Time O(Amount * Coins), Space O(Amount)"
    ],
    "tags": [
      "Dynamic Programming",
      "Combinatorics"
    ]
  },
  {
    "id": "dsa-54",
    "title": "Longest Increasing Subsequence (Patience Sorting O(N log N))",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "Given an integer array `nums`, return the length of the longest strictly increasing subsequence. Optimize from the classic O(N\u00b2) DP to O(N log N) using Patience Sorting / Binary Search.",
    "answer": "Patience Sorting / Tails Array:\nMaintain an array `tails` where `tails[i]` stores the smallest tail of all increasing subsequences of length `i + 1` found so far.\nFor `x` in `nums`:\n- Binary search `idx` in `tails` for first element >= `x` (e.g. `bisect_left(tails, x)`).\n- If `idx == len(tails)`:\n  - `x` is greater than all existing tails -> extends the longest subsequence: `tails.append(x)`.\n- Else:\n  - `tails[idx] = x` (updating with a smaller tail value improves future extension possibilities).\nLength of `tails` at the end is the length of LIS!\n\nTime Complexity: O(N log N) (N elements, binary search takes log N).\nSpace Complexity: O(N).",
    "keyPoints": [
      "tails array is always strictly sorted, enabling binary search",
      "Replaces first element >= x to minimize tail value greedily",
      "Length of tails array equals LIS length",
      "Reduces runtime from O(N\u00b2) to O(N log N)"
    ],
    "tags": [
      "Array",
      "Binary Search",
      "Dynamic Programming"
    ]
  },
  {
    "id": "dsa-55",
    "title": "House Robber I & II (Linear vs Circular)",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "You are a professional robber planning to rob houses along a street. Adjacent houses have security systems connected. In House Robber I, houses are in a line. In House Robber II, houses are arranged in a circle. Solve both in O(N) time and O(1) space.",
    "answer": "House Robber I (Linear):\nAt house `i`, either rob it (gain `nums[i] + rob[i-2]`) or skip it (keep `rob[i-1]`).\n`rob1 = 0, rob2 = 0`\nFor `n` in `nums`:\n  `new_rob = max(rob2, rob1 + n)`\n  `rob1 = rob2`\n  `rob2 = new_rob`\nReturn `rob2`.\n\nHouse Robber II (Circular):\nFirst and last houses are neighbors. You cannot rob both.\nTwo independent sub-problems:\n1. Rob houses from index `0` to `n-2` (exclude last house).\n2. Rob houses from index `1` to `n-1` (exclude first house).\nAnswer is `max(nums[0], robLinear(nums[:-1]), robLinear(nums[1:]))`.\n\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "State transition: dp[i] = max(dp[i-1], dp[i-2] + nums[i])",
      "O(1) space using two rolling variables",
      "Circular constraint split into two linear passes: [0..n-2] and [1..n-1]",
      "Clean decomposition of cyclic dependency"
    ],
    "tags": [
      "Dynamic Programming",
      "Array"
    ]
  },
  {
    "id": "dsa-56",
    "title": "Word Break I & II",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of dictionary words. What if you need to return all valid sentences (Word Break II)?",
    "answer": "Word Break I (Boolean DP):\n`dp[i]` is True if `s[0...i-1]` can be segmented.\nInitialize `dp = [False] * (len(s) + 1)`, `dp[0] = True`.\nFor `i` from 1 to `len(s)`:\n  For `w` in `wordDict`:\n    If `i >= len(w)` and `dp[i - len(w)]` and `s[i - len(w) : i] == w`:\n      `dp[i] = True; break`\nTime: O(N * M * K) where N=len(s), M=words, K=word length.\nSpace: O(N).\n\nWord Break II (All Sentences):\nMemoized Backtracking (DFS with cache):\nFor substring `s[start:]`, iterate each word in dictionary. If `s` starts with word, recursively get sentences for remainder `s[start + len(word):]`, and join.",
    "keyPoints": [
      "dp[i] represents valid segmentation of prefix s[0..i]",
      "Lookback window matches dictionary word lengths",
      "Word Break II requires memoized DFS backtracking",
      "Set lookup for dictionary words provides O(1) matching"
    ],
    "tags": [
      "Dynamic Programming",
      "Backtracking",
      "String"
    ]
  },
  {
    "id": "dsa-57",
    "title": "Maximum Product Subarray",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "Given an integer array `nums`, find a subarray that has the largest product, and return the product. How do negative numbers and zeros affect state tracking?",
    "answer": "Track both Current Min and Current Max:\nBecause multiplying by a negative number can turn a minimum (large negative) into a maximum (large positive)!\n\nAlgorithm in O(1) space:\n`res = max(nums)`\n`cur_min = 1, cur_max = 1`\nFor `n` in `nums`:\n  If `n == 0`:\n    `cur_min = 1, cur_max = 1`\n    Continue\n  `tmp = cur_max * n`\n  `cur_max = max(n * cur_max, n * cur_min, n)`\n  `cur_min = min(tmp, n * cur_min, n)`\n  `res = max(res, cur_max)`\nReturn `res`.\n\nTime Complexity: O(N).\nSpace Complexity: O(1).",
    "keyPoints": [
      "Must track both max and min product at each step",
      "Negative times negative yields positive",
      "Reset running products to 1 when hitting 0",
      "O(N) time and O(1) space"
    ],
    "tags": [
      "Array",
      "Dynamic Programming"
    ]
  },
  {
    "id": "dsa-58",
    "title": "Partition Equal Subset Sum (0/1 Knapsack)",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "Given an integer array `nums`, return `true` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal.",
    "answer": "Reduction to 0/1 Knapsack:\nTotal sum `S = sum(nums)`.\nIf `S % 2 != 0`: impossible, return `false`.\nTarget subset sum `target = S // 2`.\nProblem becomes: can we find a subset of numbers whose sum equals `target`?\n\nBitset / 1D DP Array:\n`dp = [False] * (target + 1); dp[0] = True`\nFor `num` in `nums`:\n  For `j` from `target` down to `num`: (must iterate BACKWARDS to use each element at most once)\n    `dp[j] = dp[j] or dp[j - num]`\nReturn `dp[target]`.\n\nPython bitset optimization: `bits = 1; for n in nums: bits |= (bits << n); return bool((bits >> target) & 1)`.\n\nTime: O(N * target), Space: O(target).",
    "keyPoints": [
      "Target is sum(nums) / 2; odd sum immediately returns false",
      "Iterating backwards in 1D array enforces 0/1 knapsack constraint",
      "Bit manipulation bits |= (bits << n) provides 64x hardware acceleration",
      "Time O(N * S) and Space O(S)"
    ],
    "tags": [
      "Array",
      "Dynamic Programming",
      "Knapsack",
      "Bit Manipulation"
    ]
  },
  {
    "id": "dsa-59",
    "title": "Longest Common Subsequence (LCS)",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "Given two strings `text1` and `text2`, return the length of their longest common subsequence. What is the state transition and how can memory be optimized to O(min(M, N))?",
    "answer": "State Definition:\n`dp[i][j]` = length of LCS of `text1[0...i-1]` and `text2[0...j-1]`.\n\nTransition:\n- If `text1[i-1] == text2[j-1]`: `dp[i][j] = 1 + dp[i-1][j-1]`\n- Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`\n\nSpace Optimization to O(N):\nNotice `dp[i]` only depends on row `dp[i-1]`. Maintain two rolling rows `prev` and `curr` of length `len(text2) + 1`.\n\nTime Complexity: O(M * N).\nSpace Complexity: O(min(M, N)) by choosing shorter string for columns.",
    "keyPoints": [
      "Matching character takes diagonal + 1",
      "Mismatching character takes max(top, left)",
      "Two rolling rows reduces space from O(M*N) to O(min(M,N))",
      "Foundation for diff tools and bioinformatics sequence alignment"
    ],
    "tags": [
      "Dynamic Programming",
      "String"
    ]
  },
  {
    "id": "dsa-60",
    "title": "Edit Distance (Levenshtein Distance)",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "Given two strings `word1` and `word2`, return the minimum number of operations required to convert `word1` to `word2` (insert, delete, or replace a character).",
    "answer": "2D DP Table:\n`dp[i][j]` is min edits to transform `word1[0...i-1]` to `word2[0...j-1]`.\nBase cases:\n- `dp[i][0] = i` (delete all `i` characters)\n- `dp[0][j] = j` (insert all `j` characters)\n\nTransitions:\nIf `word1[i-1] == word2[j-1]`:\n  `dp[i][j] = dp[i-1][j-1]` (no operation needed)\nElse:\n  `dp[i][j] = 1 + min(`\n    `dp[i-1][j],`    # Delete\n    `dp[i][j-1],`    # Insert\n    `dp[i-1][j-1]`   # Replace\n  `)\n\nTime Complexity: O(M * N).\nSpace Complexity: O(min(M, N)) with rolling row.",
    "keyPoints": [
      "3 operations correspond to top (delete), left (insert), diagonal (replace)",
      "Matching character inherits diagonal cost with 0 penalty",
      "Space optimized to O(min(M, N)) using two 1D arrays",
      "Core algorithm for fuzzy search and autocorrect"
    ],
    "tags": [
      "String",
      "Dynamic Programming"
    ]
  },
  {
    "id": "dsa-61",
    "title": "Burst Balloons (Matrix Chain Multiplication DP)",
    "category": "Dynamic Programming",
    "difficulty": "Hard",
    "question": "You are given `n` balloons indexed from 0 to `n - 1`, each with a number. If you burst balloon `i` you get `nums[i-1] * nums[i] * nums[i+1]` coins. Find the maximum coins you can collect. Why does choosing the FIRST balloon to burst fail, while choosing the LAST balloon succeeds?",
    "answer": "Why 'Last Balloon' to burst works:\nIf you pick which balloon to burst *first*, the subproblems are dependent because neighboring balloons merge, altering boundaries.\nIf you pick balloon `k` as the *LAST* balloon to burst in interval `(i, j)`:\n- Subproblems `(i, k)` and `(k, j)` are completely independent because balloon `k` remains intact as their boundary!\n- When `k` bursts last, its coins are `nums[i] * nums[k] * nums[j]`.\n\nRecurrence:\nPad `nums` with 1 at both ends.\n`dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])` for all `k` in `(i, j)`.\nIterate interval length `len` from 1 to `n`.\n\nTime Complexity: O(N\u00b3).\nSpace Complexity: O(N\u00b2).",
    "keyPoints": [
      "Choosing the last balloon preserves subproblem independence",
      "Interval DP pattern: iterate window length from 1 to N",
      "Pad array with 1 at both ends to eliminate edge case conditions",
      "Time O(N\u00b3) and Space O(N\u00b2)"
    ],
    "tags": [
      "Array",
      "Dynamic Programming",
      "Interval DP"
    ]
  },
  {
    "id": "dsa-62",
    "title": "Best Time to Buy and Sell Stock with Cooldown",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day. After you sell your stock, you cannot buy stock on the next day (i.e., 1 day cooldown). Find the maximum profit in O(N) time and O(1) space.",
    "answer": "State Machine DP:\nThree states for each day:\n1. `held`: Currently holding a stock.\n   `held = max(held, rest - price)`\n2. `sold`: Just sold a stock today.\n   `sold = prev_held + price`\n3. `rest`: In cooldown or doing nothing.\n   `rest = max(rest, prev_sold)`\n\nInitialize: `held = -inf, sold = 0, rest = 0`.\nIterate through each price and update states simultaneously.\nResult = `max(sold, rest)`.\n\nTime Complexity: O(N).\nSpace Complexity: O(1).",
    "keyPoints": [
      "State machine transitions: held, sold, cooldown/rest",
      "Cooldown enforces buying only from rest state",
      "O(1) space using three state variables",
      "Generalizes to transaction fees and k-transaction variants"
    ],
    "tags": [
      "Array",
      "Dynamic Programming",
      "State Machine"
    ]
  },
  {
    "id": "dsa-63",
    "title": "Subsets I & II (With Duplicates)",
    "category": "Backtracking",
    "difficulty": "Medium",
    "question": "Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.",
    "answer": "Sort Array + Backtracking with Skip Duplicates:\n1. Sort `nums` first so duplicates are adjacent.\n2. Backtracking function `backtrack(start, current_path)`:\n   - `result.append(list(current_path))` (every node in recursion tree is a valid subset).\n   - For `i` from `start` to `len(nums) - 1`:\n     - If `i > start` and `nums[i] == nums[i-1]`: skip (prevents duplicate subsets at same tree depth).\n     - `current_path.append(nums[i])`\n     - `backtrack(i + 1, current_path)`\n     - `current_path.pop()` (backtrack)\n\nTime Complexity: O(N * 2^N).\nSpace Complexity: O(N) recursion stack.",
    "keyPoints": [
      "Sort first to place identical elements adjacently",
      "Condition i > start and nums[i] == nums[i-1] skips sibling duplicates",
      "Every recursive state is added to results (unlike permutations)",
      "Time O(N * 2^N) generating all subsets"
    ],
    "tags": [
      "Array",
      "Backtracking",
      "Bit Manipulation"
    ]
  },
  {
    "id": "dsa-64",
    "title": "Permutations I & II (With Duplicates)",
    "category": "Backtracking",
    "difficulty": "Medium",
    "question": "Given an array `nums` of numbers that might contain duplicates, return all possible unique permutations in any order.",
    "answer": "Sort + Frequency Map / Used Array:\n1. Sort `nums`.\n2. Maintain `used = [False] * n` and `current = []`.\n3. Backtrack():\n   - If `len(current) == len(nums)`: `result.append(list(current)); return`.\n   - For `i` from 0 to `len(nums) - 1`:\n     - If `used[i]`: continue.\n     - If `i > 0 and nums[i] == nums[i-1] and not used[i-1]`:\n       - Skip! (If the duplicate neighbor was NOT used in the current branch, using `nums[i]` would generate identical duplicate branch).\n     - `used[i] = True; current.append(nums[i])`\n     - `backtrack()`\n     - `used[i] = False; current.pop()`\n\nTime Complexity: O(N * N!).\nSpace Complexity: O(N).",
    "keyPoints": [
      "used boolean array tracks elements in current permutation",
      "Condition nums[i] == nums[i-1] and not used[i-1] prunes duplicate permutations",
      "Generates exactly N! unique leaves",
      "O(N * N!) time complexity"
    ],
    "tags": [
      "Array",
      "Backtracking"
    ]
  },
  {
    "id": "dsa-65",
    "title": "N-Queens I & II",
    "category": "Backtracking",
    "difficulty": "Hard",
    "question": "The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. Find all distinct solutions and count total solutions.",
    "answer": "Row-by-Row Backtracking with Diagonal Sets:\nPlace one queen per row `r`. We need to ensure no conflicts in:\n1. Columns: set `cols`.\n2. Positive diagonals `r + c`: set `pos_diag` (top-right to bottom-left).\n3. Negative diagonals `r - c`: set `neg_diag` (top-left to bottom-right).\n\nBacktrack(r):\n- If `r == n`: board complete! Record formatted board in `result`.\n- For `c` from 0 to `n - 1`:\n  - If `c in cols` or `(r + c) in pos_diag` or `(r - c) in neg_diag`: continue.\n  - Place queen: add `c`, `r+c`, `r-c` to sets.\n  - `backtrack(r + 1)`\n  - Remove from sets (backtrack).\n\nTime Complexity: O(N!).\nSpace Complexity: O(N) sets and board.",
    "keyPoints": [
      "r + c uniquely identifies positive diagonals",
      "r - c uniquely identifies negative diagonals",
      "Sets allow O(1) conflict validation without scanning board",
      "Time complexity bounded by O(N!)"
    ],
    "tags": [
      "Backtracking",
      "Design"
    ]
  },
  {
    "id": "dsa-66",
    "title": "Word Search (Grid Backtracking)",
    "category": "Backtracking",
    "difficulty": "Medium",
    "question": "Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid. The word can be constructed from sequentially adjacent cells. Can you prune the search if character frequencies don't match?",
    "answer": "DFS Backtracking with Early Pruning:\n1. Frequency Pruning: Check if letter counts of `word` can be satisfied by letter counts in `board`. If not, return `false` immediately.\n2. Reverse Word Optimization: If frequency of `word[0]` > frequency of `word[-1]`, search for `word[::-1]` instead (drastically prunes initial search tree).\n3. DFS from each cell `(r, c)`:\n   - Base case: `if idx == len(word): return True`.\n   - Bounds & match check: `if out of bounds or board[r][c] != word[idx]: return False`.\n   - Mark visited in-place: `temp = board[r][c]; board[r][c] = '#'`.\n   - Recurse in 4 directions: `res = dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or ...`\n   - Backtrack: `board[r][c] = temp`.\n   - Return `res`.\n\nTime: O(M * N * 3^L) where L is word length.",
    "keyPoints": [
      "Reverse word if suffix is rarer than prefix to prune branching early",
      "In-place grid modification board[r][c]='#' avoids visited set overhead",
      "Backtracking restores cell value after all 4 directions explore",
      "Time O(M * N * 3^L)"
    ],
    "tags": [
      "Array",
      "Backtracking",
      "Matrix"
    ]
  },
  {
    "id": "dsa-67",
    "title": "Single Number (XOR Trick)",
    "category": "Bit Manipulation",
    "difficulty": "Easy",
    "question": "Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one in O(N) time and O(1) space.",
    "answer": "XOR Properties:\n1. `x ^ x = 0` (any number XORed with itself cancels out).\n2. `x ^ 0 = x`.\n3. XOR is commutative and associative: order does not matter.\n\nAlgorithm:\nInitialize `res = 0`.\nFor `n` in `nums`: `res ^= n`.\nAll pairs cancel to 0, leaving only the single number!\n\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "x ^ x = 0 and x ^ 0 = x",
      "Commutative property guarantees pairs cancel regardless of order",
      "O(N) time with O(1) extra space",
      "Universal bitwise trick for pairing problems"
    ],
    "tags": [
      "Array",
      "Bit Manipulation"
    ]
  },
  {
    "id": "dsa-68",
    "title": "Number of 1 Bits (Brian Kernighan's Algorithm)",
    "category": "Bit Manipulation",
    "difficulty": "Easy",
    "question": "Write a function that takes the binary representation of a positive integer and returns the number of set bits ('1' bits). Optimize so the loop runs only as many times as there are 1 bits.",
    "answer": "Brian Kernighan's Bit Trick `n & (n - 1)`:\nSubtracting 1 from `n` flips the least significant set bit and all trailing zeros to 1.\nBitwise AND `n & (n - 1)` clears the lowest set bit of `n` to 0!\n\nAlgorithm:\n`count = 0`\nWhile `n > 0`:\n  `n &= (n - 1)`\n  `count += 1`\nReturn `count`.\n\nInstead of 32 iterations for a 32-bit integer, this loop executes exactly `k` times, where `k` is the number of set bits (Hamming weight).\nTime: O(k), Space: O(1).",
    "keyPoints": [
      "n & (n - 1) clears the lowest set bit",
      "Runs in O(k) iterations where k is number of 1s",
      "Faster than testing all 32 bits individually",
      "Core bit manipulation primitive"
    ],
    "tags": [
      "Bit Manipulation"
    ]
  },
  {
    "id": "dsa-69",
    "title": "Counting Bits (DP with Bitwise Offset)",
    "category": "Bit Manipulation",
    "difficulty": "Easy",
    "question": "Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (0 <= i <= n), `ans[i]` is the number of 1's in the binary representation of `i`. Solve it in linear time O(N).",
    "answer": "Dynamic Programming with Bit Manipulation:\nNotice:\n- If `i` is even: `i` has the exact same number of 1 bits as `i // 2` (`i >> 1`), because shifting right simply drops the trailing 0.\n- If `i` is odd: `i` has 1 more set bit than `i // 2`.\n\nUnified Recurrence:\n`dp[i] = dp[i >> 1] + (i & 1)`\n\nAlgorithm:\n`dp = [0] * (n + 1)`\nFor `i` from 1 to `n`:\n  `dp[i] = dp[i >> 1] + (i & 1)`\nReturn `dp`.\n\nTime Complexity: O(N) single pass.\nSpace Complexity: O(N) output array.",
    "keyPoints": [
      "dp[i] = dp[i >> 1] + (i & 1)",
      "Reuses previously computed bit count of i / 2",
      "Strictly O(N) time without calling popcount function",
      "O(1) extra space beyond return array"
    ],
    "tags": [
      "Dynamic Programming",
      "Bit Manipulation"
    ]
  },
  {
    "id": "dsa-70",
    "title": "Reverse Bits",
    "category": "Bit Manipulation",
    "difficulty": "Easy",
    "question": "Reverse bits of a given 32 bits unsigned integer. How would you optimize this if the function is called millions of times?",
    "answer": "1. Bit-by-Bit (32 steps):\n`res = 0`\nFor `i` in range(32):\n  `bit = (n >> i) & 1`\n  `res |= (bit << (31 - i))`\nReturn `res`.\n\n2. Repeated Call Optimization (Byte Lookup Table):\nPrecompute bit-reversal for all 256 possible bytes (0 to 255) in a table `lookup`.\nFor any 32-bit integer, reverse each of its 4 bytes using the table:\n`return (lookup[n & 0xff] << 24) | (lookup[(n >> 8) & 0xff] << 16) | (lookup[(n >> 16) & 0xff] << 8) | lookup[(n >> 24) & 0xff]`.\nRuns in O(1) time with only 4 table lookups!",
    "keyPoints": [
      "Bit-by-bit reversal takes 32 iterations",
      "Lookup table for 8-bit bytes (256 entries) reduces 32 iterations to 4 lookups",
      "Massive speedup for high-frequency low-latency systems",
      "Bitwise mask and shift operations"
    ],
    "tags": [
      "Bit Manipulation",
      "Optimization"
    ]
  },
  {
    "id": "dsa-71",
    "title": "Merge Intervals",
    "category": "Intervals",
    "difficulty": "Medium",
    "question": "Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.",
    "answer": "Sort by Start Time + Single Pass Merge:\n1. Sort `intervals` by `start` time in O(N log N).\n2. Initialize `merged = [intervals[0]]`.\n3. For each `current` interval `[start, end]` in `intervals[1:]`:\n   - `prev_start, prev_end = merged[-1]`\n   - If `start <= prev_end`: (overlapping)\n     - Extend end: `merged[-1][1] = max(prev_end, end)`\n   - Else: (disjoint)\n     - `merged.append(current)`\n4. Return `merged`.\n\nTime Complexity: O(N log N) sorting.\nSpace Complexity: O(N) or O(1) depending on in-place sort.",
    "keyPoints": [
      "Sort by interval start time guarantees adjacent overlaps",
      "Condition current.start <= prev.end indicates overlap",
      "Update merged[-1].end with max(prev.end, current.end)",
      "O(N log N) time and O(N) space"
    ],
    "tags": [
      "Array",
      "Sorting",
      "Intervals"
    ]
  },
  {
    "id": "dsa-72",
    "title": "Insert Interval",
    "category": "Intervals",
    "difficulty": "Medium",
    "question": "You are given an array of non-overlapping intervals `intervals` sorted by `start_i` in ascending order. Insert `newInterval` into `intervals` such that `intervals` is still sorted and non-overlapping. Solve in O(N) time without re-sorting.",
    "answer": "Three-Phase Linear Scan:\nInitialize `res = []`.\nPhase 1: Add all intervals ending before `newInterval` starts:\n- While `i < n and intervals[i][1] < newInterval[0]`:\n  - `res.append(intervals[i]); i += 1`\n\nPhase 2: Merge all overlapping intervals with `newInterval`:\n- While `i < n and intervals[i][0] <= newInterval[1]`:\n  - `newInterval[0] = min(newInterval[0], intervals[i][0])`\n  - `newInterval[1] = max(newInterval[1], intervals[i][1])`\n  - `i += 1`\n- `res.append(newInterval)`\n\nPhase 3: Add all remaining intervals starting after `newInterval` ends:\n- While `i < n`: `res.append(intervals[i]); i += 1`\n\nTime Complexity: O(N) single pass.\nSpace Complexity: O(N).",
    "keyPoints": [
      "Three phases: before, overlapping/merged, after",
      "Does not require re-sorting existing intervals",
      "Runs in strictly linear O(N) time",
      "O(1) auxiliary space beyond result list"
    ],
    "tags": [
      "Array",
      "Intervals"
    ]
  },
  {
    "id": "dsa-73",
    "title": "Non-overlapping Intervals (Interval Scheduling Greedy)",
    "category": "Intervals",
    "difficulty": "Medium",
    "question": "Given an array of intervals `intervals`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping. Prove why sorting by END time is optimal.",
    "answer": "Greedy Choice: Sort by END Time:\nTo maximize the number of non-overlapping intervals that can fit, we should always pick the interval that finishes earliest (smallest `end` time), leaving maximum room for future intervals.\n\nAlgorithm:\n1. Sort `intervals` by `end` time: `intervals.sort(key=lambda x: x[1])`.\n2. `count_removed = 0`.\n3. `prev_end = intervals[0][1]`.\n4. For `start, end` in `intervals[1:]`:\n   - If `start < prev_end`: (conflict)\n     - Must remove this interval: `count_removed += 1`\n   - Else: (no conflict)\n     - Update `prev_end = end`\n5. Return `count_removed`.\n\nTime: O(N log N), Space: O(1).",
    "keyPoints": [
      "Classic Interval Scheduling Theorem: sort by finish/end time",
      "Always preserve interval that finishes earliest to maximize available timeline",
      "Count conflicts as intervals to remove",
      "Time O(N log N) and Space O(1)"
    ],
    "tags": [
      "Array",
      "Greedy",
      "Sorting",
      "Intervals"
    ]
  },
  {
    "id": "dsa-74",
    "title": "Meeting Rooms II (Min Conference Rooms)",
    "category": "Intervals",
    "difficulty": "Medium",
    "question": "Given an array of meeting time intervals `intervals` where `intervals[i] = [start_i, end_i]`, return the minimum number of conference rooms required. Compare Min-Heap and Two-Pointer approaches.",
    "answer": "1. Two Pointers / Chronological Scan (Optimal):\nSeparate and sort starts and ends independently:\n`starts = sorted([i[0] for i in intervals])`\n`ends = sorted([i[1] for i in intervals])`\n`rooms = 0, end_ptr = 0`\nFor `s` in `starts`:\n  If `s < ends[end_ptr]`: (meeting starts before earliest meeting ends -> need new room)\n    `rooms += 1`\n  Else: (a meeting ended, room recycled)\n    `end_ptr += 1`\nReturn `rooms`.\n\n2. Min-Heap:\nSort intervals by start. Min-heap stores end times of active meetings. If `curr.start >= heap[0]`, pop room (reused). Push `curr.end`. Max heap size is answer.\n\nBoth take O(N log N) time and O(N) space.",
    "keyPoints": [
      "Chronological sweep-line pattern",
      "Separate starts and ends sorting avoids heap overhead",
      "Increment rooms when start < earliest end; advance end pointer when recycled",
      "O(N log N) time and O(N) space"
    ],
    "tags": [
      "Array",
      "Two Pointers",
      "Sorting",
      "Heap",
      "Intervals"
    ]
  },
  {
    "id": "dsa-75",
    "title": "Subarray with Given XOR",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Given an array of integers `A` and an integer `B`, find the total number of subarrays having bitwise XOR equal to `B`.",
    "answer": "Prefix XOR + Hash Map:\nLet `prefix_xor` be running XOR from index 0 to `i`. We need previous prefix XOR `Y` such that `Y ^ prefix_xor = B` => `Y = prefix_xor ^ B`. Store frequency of seen prefix XORs in a hash map. Time: O(N), Space: O(N).",
    "keyPoints": [
      "Analogous to prefix sum with target difference",
      "Y ^ prefix_xor = B implies Y = prefix_xor ^ B",
      "Hash map stores counts of seen prefix XOR values",
      "O(N) time and O(N) space"
    ],
    "tags": [
      "Array",
      "Hash Table",
      "Bit Manipulation"
    ]
  },
  {
    "id": "dsa-76",
    "title": "Majority Element (Boyer-Moore Voting)",
    "category": "Arrays & Hashing",
    "difficulty": "Easy",
    "question": "Given an array `nums` of size `n`, return the majority element (appears > n/2 times). Can you solve it in O(N) time and O(1) space?",
    "answer": "Boyer-Moore Voting Algorithm:\nMaintain `candidate` and `count = 0`.\nFor `x` in `nums`:\n- If `count == 0`: `candidate = x`\n- `count += (1 if x == candidate else -1)`\nReturn `candidate`.\nSince majority element occurs > n/2 times, its count will withstand all other elements canceling it out.\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "Boyer-Moore voting algorithm cancels non-matching elements",
      "Guaranteed to identify majority element when one exists (> n/2)",
      "Strictly O(N) time and O(1) space",
      "Extendable to n/3 majority using two candidates"
    ],
    "tags": [
      "Array",
      "Counting"
    ]
  },
  {
    "id": "dsa-77",
    "title": "Next Permutation",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers in-place.",
    "answer": "Three-Step In-Place Algorithm:\n1. Find the first decreasing element from the right: find largest index `i` such that `nums[i] < nums[i+1]`. If none exists, reverse whole array (already largest).\n2. Find element to swap: find largest index `j > i` such that `nums[j] > nums[i]`. Swap `nums[i]` and `nums[j]`.\n3. Reverse the suffix: reverse elements from `i+1` to end of array to make suffix as small as possible.\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "Find first inflection point from right where nums[i] < nums[i+1]",
      "Swap with smallest element on right that is greater than nums[i]",
      "Reverse suffix from i+1 to end to minimize suffix value",
      "In-place O(N) time and O(1) space"
    ],
    "tags": [
      "Array",
      "Two Pointers"
    ]
  },
  {
    "id": "dsa-78",
    "title": "Spiral Matrix Traversal",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Given an `m x n` matrix, return all elements of the matrix in spiral order.",
    "answer": "Boundary Simulation:\nMaintain 4 boundaries: `top = 0, bottom = m - 1, left = 0, right = n - 1`.\nWhile `top <= bottom and left <= right`:\n1. Traverse right: `left` to `right` along `top`; `top += 1`.\n2. Traverse down: `top` to `bottom` along `right`; `right -= 1`.\n3. If `top <= bottom`: traverse left: `right` to `left` along `bottom`; `bottom -= 1`.\n4. If `left <= right`: traverse up: `bottom` to `top` along `left`; `left += 1`.\nTime: O(M * N), Space: O(1) auxiliary.",
    "keyPoints": [
      "Maintain top, bottom, left, right bounds",
      "Shrink boundary after each directional sweep",
      "Check top <= bottom and left <= right before reverse passes",
      "Linear time O(M * N)"
    ],
    "tags": [
      "Matrix",
      "Simulation"
    ]
  },
  {
    "id": "dsa-79",
    "title": "Rotate Image (In-Place Matrix Rotation)",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "You are given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees (clockwise) in-place.",
    "answer": "Transpose + Reverse Rows:\n1. Transpose the matrix: swap `matrix[i][j]` with `matrix[j][i]` for `i < j`.\n2. Reverse each row: reverse `matrix[i]` left to right.\nMathematically, Transpose + Horizontal Reflection = 90 degree clockwise rotation!\nTime: O(N\u00b2), Space: O(1) in-place.",
    "keyPoints": [
      "Transpose matrix swapping elements across main diagonal",
      "Reverse each row horizontally to complete 90-degree clockwise turn",
      "To rotate 90-deg counter-clockwise: reverse rows first, then transpose",
      "O(N\u00b2) time and strictly O(1) space"
    ],
    "tags": [
      "Matrix",
      "Math"
    ]
  },
  {
    "id": "dsa-80",
    "title": "Set Matrix Zeroes",
    "category": "Arrays & Hashing",
    "difficulty": "Medium",
    "question": "Given an `m x n` integer matrix, if an element is 0, set its entire row and column to 0's in-place with O(1) space.",
    "answer": "First Row & Column as Storage Markers:\n1. Use variables `first_row_zero` and `first_col_zero` boolean flags.\n2. Check if first row/col has zeros initially.\n3. Iterate interior cells `(1..m, 1..n)`: if `matrix[i][j] == 0`, set `matrix[i][0] = 0` and `matrix[0][j] = 0`.\n4. Iterate interior again, setting `matrix[i][j] = 0` if its row marker or col marker is 0.\n5. Zero out first row/col if their flags were true.\nTime: O(M * N), Space: O(1).",
    "keyPoints": [
      "Uses matrix's own first row and column as marker arrays",
      "Dedicated flags preserve original zero status of row 0 and col 0",
      "Two-pass in-place update",
      "Achieves O(1) auxiliary space"
    ],
    "tags": [
      "Matrix",
      "Array"
    ]
  },
  {
    "id": "dsa-81",
    "title": "Longest Repeating Character Replacement",
    "category": "Sliding Window",
    "difficulty": "Medium",
    "question": "You are given a string `s` and an integer `k`. You can choose any character and change it to any other uppercase English character at most `k` times. Return the length of the longest substring containing the same letter.",
    "answer": "Sliding Window with Max Frequency:\nMaintain frequency count of characters in window and `max_freq`.\nFor `right` from 0 to N-1:\n- Increment frequency of `s[right]`.\n- `max_freq = max(max_freq, count[s[right]])`.\n- Window condition: `(right - left + 1) - max_freq > k` (more than `k` replacements needed):\n  - Decrement `count[s[left]]`; `left += 1`.\n- `max_len = max(max_len, right - left + 1)`.\nNotice we don't need to decrement `max_freq` when shrinking because window size only grows when a larger `max_freq` is encountered!\nTime: O(N), Space: O(1) 26 letters.",
    "keyPoints": [
      "Window invalid when length - max_freq > k",
      "max_freq doesn't need recomputing when shrinking window",
      "Window size never decreases, sliding forward monotonically",
      "O(N) time and O(1) space"
    ],
    "tags": [
      "String",
      "Sliding Window",
      "Hash Table"
    ]
  },
  {
    "id": "dsa-82",
    "title": "Permutation in String",
    "category": "Sliding Window",
    "difficulty": "Medium",
    "question": "Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.",
    "answer": "Fixed-Size Sliding Window of length len(s1):\nMaintain frequency array of size 26 for `s1` and for current window in `s2`. Maintain `matches` count (number of characters with equal frequency, out of 26). Slide window across `s2` updating `matches` on entry and exit. When `matches == 26`, return `true`.\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "Fixed window size equal to s1 length",
      "Track number of matching character counts (0..26)",
      "O(1) update per character slide instead of comparing full maps",
      "Strictly O(N) time and O(1) space"
    ],
    "tags": [
      "String",
      "Sliding Window",
      "Hash Table"
    ]
  },
  {
    "id": "dsa-83",
    "title": "Reorder List",
    "category": "Linked List",
    "difficulty": "Medium",
    "question": "You are given the head of a singly linked-list: `L0 \u2192 L1 \u2192 \u2026 \u2192 Ln - 1 \u2192 Ln`. Reorder it to: `L0 \u2192 Ln \u2192 L1 \u2192 Ln - 1 \u2192 L2 \u2192 Ln - 2 \u2192 \u2026` in-place.",
    "answer": "Three Steps in O(N) time and O(1) space:\n1. Find middle of list using slow and fast pointers (`slow = slow.next, fast = fast.next.next`).\n2. Reverse second half of list (`head2 = reverse(slow.next); slow.next = None`).\n3. Merge two halves alternating nodes (`l1_next = l1.next; l2_next = l2.next; l1.next = l2; l2.next = l1_next`).",
    "keyPoints": [
      "Find midpoint using fast/slow runners",
      "Reverse second half in-place",
      "Interleave nodes alternating from first and reversed second half",
      "O(N) time and strictly O(1) space"
    ],
    "tags": [
      "Linked List",
      "Two Pointers"
    ]
  },
  {
    "id": "dsa-84",
    "title": "Remove Nth Node From End of List",
    "category": "Linked List",
    "difficulty": "Medium",
    "question": "Given the head of a linked list, remove the `n-th` node from the end of the list and return its head in one pass.",
    "answer": "Two Pointers with N-Gap:\nCreate dummy node pointing to head. Advance `fast` pointer `n + 1` steps ahead of `slow`. Then move both `slow` and `fast` one step at a time until `fast` reaches `null`. `slow.next` is the node to delete! Set `slow.next = slow.next.next`.\nTime: O(N) single pass, Space: O(1).",
    "keyPoints": [
      "Two pointers separated by n steps",
      "Dummy node simplifies removing the original head node",
      "Single pass O(N) time complexity",
      "O(1) auxiliary space"
    ],
    "tags": [
      "Linked List",
      "Two Pointers"
    ]
  },
  {
    "id": "dsa-85",
    "title": "Copy List with Random Pointer",
    "category": "Linked List",
    "difficulty": "Medium",
    "question": "Construct a deep copy of a linked list where each node contains an additional `random` pointer. Can you solve it in O(1) extra space without a hash map?",
    "answer": "Interweaving Nodes In-Place:\nPass 1: Duplicate each node in-place: `curr.next = Node(curr.val, curr.next)` (original list: A->A'->B->B').\nPass 2: Set random pointers: `curr.next.random = curr.random.next` (if `curr.random` exists).\nPass 3: Unweave the lists: separate cloned nodes from original nodes restoring original list.\nTime: O(N), Space: O(1) extra memory.",
    "keyPoints": [
      "Interweave cloned nodes directly next to originals",
      "Cloned random pointer equals original.random.next",
      "Separate interleaved lists in third pass",
      "Achieves O(1) auxiliary space"
    ],
    "tags": [
      "Linked List",
      "Hash Table"
    ]
  },
  {
    "id": "dsa-86",
    "title": "Flatten a Multilevel Doubly Linked List",
    "category": "Linked List",
    "difficulty": "Medium",
    "question": "You are given a doubly linked list, which in addition to the next and previous pointers, it could have a child pointer. Flatten the list so that all the nodes appear in a single-level doubly linked list.",
    "answer": "Iterative Stack / Pointer Splicing:\nIterate through list with `curr`. When `curr.child` is non-null:\n- If `curr.next` exists, find the tail of child list.\n- Connect child tail's `next` to `curr.next`, and `curr.next.prev` to child tail.\n- Connect `curr.next` to `curr.child`, and `curr.child.prev` to `curr`.\n- Set `curr.child = None`.\n- Advance `curr`.\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "Slices child list between curr and curr.next in-place",
      "Updates 4 pointer references per child list",
      "Clears child pointer to null",
      "O(N) time and O(1) space"
    ],
    "tags": [
      "Linked List",
      "Doubly Linked List",
      "DFS"
    ]
  },
  {
    "id": "dsa-87",
    "title": "Evaluate Reverse Polish Notation",
    "category": "Stack",
    "difficulty": "Medium",
    "question": "Evaluate the value of an arithmetic expression in Reverse Polish Notation (Postfix). Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.",
    "answer": "Stack Evaluation:\nMaintain an operand stack.\nFor token in tokens:\n- If token is operator: pop `b`, pop `a`. Compute `res = a op b` (careful with integer division truncating toward zero: `int(a / b)` in Python). Push `res` back to stack.\n- Else: parse int and push to stack.\nReturn `stack.pop()`.\nTime: O(N), Space: O(N).",
    "keyPoints": [
      "Postfix notation needs no parentheses",
      "Binary operator consumes top two elements from stack",
      "Note operand order: a = first popped is b, second is a (a / b)",
      "Trunaction toward zero for negative numbers: int(a / b)"
    ],
    "tags": [
      "Stack",
      "Math"
    ]
  },
  {
    "id": "dsa-88",
    "title": "Basic Calculator II (No Parentheses, +, -, *, /)",
    "category": "Stack",
    "difficulty": "Medium",
    "question": "Given a string `s` which represents an expression, evaluate this expression without using `eval()`. Follow operator precedence where `*` and `/` have higher precedence than `+` and `-`.",
    "answer": "Single Pass Stack or O(1) Rolling Variables:\nMaintain `last_sign = '+'` and `curr_num = 0`.\nIterate chars: if digit, accumulate `curr_num`.\nWhen reaching operator or end of string:\n- If `last_sign == '+'`: `stack.append(curr_num)`\n- If `last_sign == '-'`: `stack.append(-curr_num)`\n- If `last_sign == '*'`: `stack.append(stack.pop() * curr_num)`\n- If `last_sign == '/'`: `stack.append(int(stack.pop() / curr_num))`\n- `last_sign = char; curr_num = 0`.\nReturn `sum(stack)`.\nTime: O(N), Space: O(N) or O(1).",
    "keyPoints": [
      "Multiply and divide evaluated immediately against stack top",
      "Add and subtract pushed to stack for deferred evaluation",
      "Handles multi-digit numbers and whitespace",
      "Time O(N) single pass"
    ],
    "tags": [
      "Stack",
      "Math",
      "String"
    ]
  },
  {
    "id": "dsa-89",
    "title": "Search a 2D Matrix I & II",
    "category": "Binary Search",
    "difficulty": "Medium",
    "question": "In Matrix I, each row is sorted and first integer of each row > last of previous. In Matrix II, rows and columns are sorted independently. Compare the binary search strategies.",
    "answer": "Matrix I: Treat as flat 1D array of size `M * N`. Run standard binary search on `[0, M*N - 1]`. Convert `mid` to coordinates: `row = mid // N, col = mid % N`. Time: O(log(MN)).\n\nMatrix II: Start at top-right corner `(r=0, c=N-1)`:\n- If `matrix[r][c] == target`: return `True`.\n- If `matrix[r][c] > target`: eliminate column `c -= 1`.\n- If `matrix[r][c] < target`: eliminate row `r += 1`.\nTime: O(M + N), Space: O(1).",
    "keyPoints": [
      "Matrix I: 1D mapping mid // cols, mid % cols yields O(log(MN))",
      "Matrix II: Top-right corner traversal eliminates 1 row or col per step in O(M + N)",
      "Bottom-left corner works identically for Matrix II",
      "Space complexity O(1)"
    ],
    "tags": [
      "Array",
      "Binary Search",
      "Matrix"
    ]
  },
  {
    "id": "dsa-90",
    "title": "Find Peak Element",
    "category": "Binary Search",
    "difficulty": "Medium",
    "question": "A peak element is an element that is strictly greater than its neighbors. Given an integer array `nums`, find a peak element, and return its index in O(log n) time.",
    "answer": "Binary Search on Gradient:\n`left = 0, right = n - 1`.\nWhile `left < right`:\n- `mid = (left + right) // 2`.\n- If `nums[mid] < nums[mid + 1]`:\n  - Rising slope: a peak is guaranteed to exist to the right: `left = mid + 1`.\n- Else (`nums[mid] > nums[mid + 1]`):\n  - Falling slope or peak itself: search left including `mid`: `right = mid`.\nReturn `left`.\nTime: O(log N), Space: O(1).",
    "keyPoints": [
      "Follow ascending gradient to guarantee finding a local maximum",
      "Works even in unsorted arrays",
      "Condition nums[mid] < nums[mid+1] safely checks right neighbor",
      "O(log N) time and O(1) space"
    ],
    "tags": [
      "Array",
      "Binary Search"
    ]
  },
  {
    "id": "dsa-91",
    "title": "Subtree of Another Tree",
    "category": "Trees",
    "difficulty": "Easy",
    "question": "Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot`.",
    "answer": "Recursive Tree Traversal + Same Tree Helper:\n`isSubtree(root, subRoot)`:\n- Base case: `if not root: return False`.\n- If `isSameTree(root, subRoot): return True`.\n- Return `isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)`.\n\nHelper `isSameTree(s, t)`:\n- If both null: return True.\n- If one null or `s.val != t.val`: return False.\n- Return `isSameTree(s.left, t.left) and isSameTree(s.right, t.right)`.\nTime: O(M * N) worst case, or O(M + N) using Merkle Tree hashing / KMP on serialized strings.",
    "keyPoints": [
      "Subtree requires identical values and null leaf structures",
      "Helper isSameTree compares two subtrees simultaneously",
      "Worst case O(M * N), average case much faster",
      "Can optimize to O(M + N) with Merkle tree hashing"
    ],
    "tags": [
      "Tree",
      "DFS",
      "String Matching"
    ]
  },
  {
    "id": "dsa-92",
    "title": "Binary Tree Right Side View",
    "category": "Trees",
    "difficulty": "Medium",
    "question": "Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.",
    "answer": "Level-Order BFS or Reverse Pre-Order DFS:\n1. BFS: At each level, the last node processed in that level's queue snapshot is added to result.\n2. DFS: Traverse `root -> right -> left`. Pass `depth`. If `depth == len(result)`, append `node.val` (first node encountered at this depth is guaranteed to be rightmost).\nTime: O(N), Space: O(H) for DFS or O(W) for BFS.",
    "keyPoints": [
      "BFS picks last node at each level",
      "DFS (root, right, left) visits rightmost node at each depth first",
      "Condition depth == len(result) records exactly one node per level",
      "O(N) time and O(H) space"
    ],
    "tags": [
      "Tree",
      "DFS",
      "BFS"
    ]
  },
  {
    "id": "dsa-93",
    "title": "Count Good Nodes in Binary Tree",
    "category": "Trees",
    "difficulty": "Medium",
    "question": "Given a binary tree `root`, a node `X` in the tree is named good if in the path from root to `X` there are no nodes with a value greater than `X`. Return the number of good nodes in the binary tree.",
    "answer": "Pre-Order DFS tracking Maximum Value so far:\n`def dfs(node, max_val):`\n  `if not node: return 0`\n  `good = 1 if node.val >= max_val else 0`\n  `new_max = max(max_val, node.val)`\n  `return good + dfs(node.left, new_max) + dfs(node.right, new_max)`\nCall `dfs(root, root.val)`.\nTime: O(N), Space: O(H).",
    "keyPoints": [
      "Pass maximum value seen along path down recursive calls",
      "Node is good if node.val >= max_val",
      "Update max_val = max(max_val, node.val)",
      "O(N) time and O(H) space"
    ],
    "tags": [
      "Tree",
      "DFS",
      "BFS"
    ]
  },
  {
    "id": "dsa-94",
    "title": "Kth Smallest Element in a BST",
    "category": "Trees",
    "difficulty": "Medium",
    "question": "Given the `root` of a binary search tree, and an integer `k`, return the `k-th` smallest value (1-indexed) of all the values of the nodes in the tree.",
    "answer": "Iterative In-Order Traversal with Stack:\nIn-order traversal visits BST nodes in strictly ascending order.\nMaintain stack. Traverse down left branch pushing nodes.\nWhen left exhausts, pop node, decrement `k -= 1`. If `k == 0`, return `node.val`.\nMove to `node.right`.\nTime: O(H + k), Space: O(H).",
    "keyPoints": [
      "In-order traversal of BST yields sorted values",
      "Iterative stack enables early return once k-th node is popped",
      "Time O(H + k) without visiting unnecessary nodes",
      "Space O(H) stack depth"
    ],
    "tags": [
      "Tree",
      "BST",
      "DFS"
    ]
  },
  {
    "id": "dsa-95",
    "title": "Path Sum III (Prefix Sum on Trees)",
    "category": "Trees",
    "difficulty": "Medium",
    "question": "Given the root of a binary tree and an integer `targetSum`, return the number of paths where the sum of the values in the path equals `targetSum`. The path does not need to start or end at the root or a leaf.",
    "answer": "Prefix Sum Map + DFS Backtracking:\nMaintain a hash map `prefix_map` storing counts of prefix sums along current root-to-node path. Initialize with `{0: 1}`.\nAt `node`:\n- `curr_sum += node.val`\n- `count += prefix_map.get(curr_sum - targetSum, 0)`\n- `prefix_map[curr_sum] += 1`\n- Recurse on `node.left` and `node.right`\n- Backtrack: `prefix_map[curr_sum] -= 1` (remove current sum so it doesn't affect sibling branches).\nTime: O(N) single pass, Space: O(H).",
    "keyPoints": [
      "Applies subarray sum equals k to binary trees",
      "Backtracking removes current node's prefix sum upon returning",
      "Reduces brute-force O(N\u00b2) to optimal O(N) time",
      "Space O(H) call stack and map"
    ],
    "tags": [
      "Tree",
      "DFS",
      "Prefix Sum"
    ]
  },
  {
    "id": "dsa-96",
    "title": "Rotting Oranges (Multi-Source BFS)",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "You are given an `m x n` grid where each cell has 0 (empty), 1 (fresh), or 2 (rotten). Every minute, any fresh orange 4-directionally adjacent to a rotten orange becomes rotten. Return minimum minutes until no fresh orange remains, or -1.",
    "answer": "Multi-Source BFS:\n1. Count total `fresh` oranges. Enqueue all initial rotten oranges `(r, c)` into BFS queue.\n2. `minutes = 0`.\n3. While queue non-empty and `fresh > 0`:\n   - Loop for `len(queue)` rotten oranges:\n     - For 4 neighbors: if fresh `grid[nr][nc] == 1`:\n       - Make rotten `grid[nr][nc] = 2`\n       - `fresh -= 1`\n       - `queue.append((nr, nc))`\n   - `minutes += 1`\n4. Return `minutes` if `fresh == 0` else -1.\nTime: O(M * N), Space: O(M * N).",
    "keyPoints": [
      "Enqueue all initial rotten oranges simultaneously (multi-source BFS)",
      "Only increment minutes if at least one fresh orange was infected",
      "Decrements fresh count to check feasibility without final scan",
      "O(M * N) time and O(M * N) space"
    ],
    "tags": [
      "Array",
      "BFS",
      "Matrix"
    ]
  },
  {
    "id": "dsa-97",
    "title": "Pacific Atlantic Water Flow",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "An `m x n` matrix of island borders Pacific (top & left) and Atlantic (bottom & right) oceans. Water flows from a cell to adjacent cell of equal or lower height. Return all grid coordinates where water can reach both oceans.",
    "answer": "Reverse Reachability DFS/BFS from Ocean Borders:\nInstead of starting from interior cells, start from ocean borders and climb uphill (water flows downhill => reachability flows uphill!):\n- Set `pacific_visited`: run DFS from all cells in row 0 and col 0.\n- Set `atlantic_visited`: run DFS from all cells in row `m-1` and col `n-1`.\n- In DFS: only traverse to neighbor if `height[nr][nc] >= height[r][c]`.\n- Result: intersection `pacific_visited & atlantic_visited`.\nTime: O(M * N), Space: O(M * N).",
    "keyPoints": [
      "Reverse direction: search uphill from ocean edges",
      "Intersection of two reachability sets gives the answer",
      "Avoids redundant DFS from every internal cell",
      "O(M * N) time and O(M * N) space"
    ],
    "tags": [
      "Array",
      "DFS",
      "BFS",
      "Matrix"
    ]
  },
  {
    "id": "dsa-98",
    "title": "Redundant Connection (Disjoint Set Union)",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "In this problem, a tree is an undirected graph that is connected and has no cycles. You are given a graph that started as a tree with `n` nodes, with one additional edge added. Find that edge which can be removed so the graph is a tree.",
    "answer": "Union-Find with Path Compression & Union by Rank:\nInitialize DSU with `n` nodes.\nFor `u, v` in `edges`:\n- If `find(u) == find(v)`: `u` and `v` are already in the same connected component! Adding edge `(u, v)` creates a cycle. This is the redundant edge! Return `[u, v]`.\n- Else: `union(u, v)`.\nTime: O(E * \u03b1(V)) \u2248 O(E) nearly linear.\nSpace: O(V) parent and rank arrays.",
    "keyPoints": [
      "Union-Find tracks connected components",
      "If find(u) == find(v), edge forms a cycle",
      "Near-linear time O(N * \u03b1(N)) using path compression and union by rank",
      "Returns the exact duplicate edge in order of appearance"
    ],
    "tags": [
      "Graph",
      "Union Find"
    ]
  },
  {
    "id": "dsa-99",
    "title": "Min Cost to Connect All Points (Prim's / Kruskal's MST)",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "You are given an array `points` representing integer coordinates on a 2D plane. Cost between points `(xi, yi)` and `(xj, yj)` is Manhattan distance `|xi - xj| + |yi - yj|`. Return minimum cost to connect all points.",
    "answer": "Prim's Minimum Spanning Tree (MST) with Min-Heap:\n1. Maintain `visited = set()`, `min_heap = [(0, 0)]` (stores `(cost, point_index)`), `total_cost = 0`.\n2. While `len(visited) < n`:\n   - `cost, u = heappop(min_heap)`\n   - If `u in visited`: continue\n   - `visited.add(u); total_cost += cost`\n   - For each unvisited point `v`:\n     - Compute Manhattan distance `d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])`\n     - `heappush(min_heap, (d, v))`\n3. Return `total_cost`.\nTime: O(N\u00b2 log N) with heap or O(N\u00b2) optimized Prim's without heap. Space: O(N).",
    "keyPoints": [
      "Minimum Spanning Tree connects all nodes with minimum total edge weight",
      "Prim's algorithm grows MST greedily from arbitrary starting node",
      "Dense graph (all pairs connected) makes Prim's preferable to Kruskal's",
      "Time O(N\u00b2 log N) and space O(N)"
    ],
    "tags": [
      "Array",
      "Graph",
      "Minimum Spanning Tree",
      "Heap"
    ]
  },
  {
    "id": "dsa-100",
    "title": "Shortest Path in Binary Matrix",
    "category": "Graphs",
    "difficulty": "Medium",
    "question": "Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix from `(0, 0)` to `(n-1, n-1)` moving in 8 directions. If no clear path exists, return -1.",
    "answer": "8-Directional BFS:\nIf `grid[0][0] != 0` or `grid[n-1][n-1] != 0`: return -1.\nQueue = `deque([(0, 0, 1)])` (stores `(r, c, distance)`). Mark `grid[0][0] = 1` as visited.\nWhile queue non-empty:\n- `r, c, d = queue.popleft()`\n- If `r == n-1 and c == n-1`: return `d`.\n- For `dr, dc` in 8 directions:\n  - `nr, nc = r + dr, c + dc`\n  - If `0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0`:\n    - `grid[nr][nc] = 1` (mark visited immediately upon enqueuing)\n    - `queue.append((nr, nc, d + 1))`\nReturn -1.\nTime: O(N\u00b2), Space: O(N\u00b2).",
    "keyPoints": [
      "8-directional neighbor exploration",
      "Mark cell visited immediately upon enqueuing to prevent duplicate queue entries",
      "BFS guarantees shortest path in unweighted graph",
      "O(N\u00b2) time and O(N\u00b2) space"
    ],
    "tags": [
      "Array",
      "BFS",
      "Matrix"
    ]
  },
  {
    "id": "dsa-101",
    "title": "Decode Ways",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "A message containing letters from A-Z is being encoded to numbers ('A' -> 1, 'Z' -> 26). Given a string `s` containing only digits, return the number of ways to decode it.",
    "answer": "1D DP with Lookback of 1 and 2 digits:\n`dp[i]` = ways to decode prefix `s[0...i-1]`.\nBase case: `dp[0] = 1`.\nFor `i` from 1 to `len(s)`:\n- Single digit: if `s[i-1] != '0'`: `dp[i] += dp[i-1]`.\n- Two digits: if `10 <= int(s[i-2:i]) <= 26`: `dp[i] += dp[i-2]`.\nCan be space-optimized to O(1) using two variables `prev1` and `prev2`.\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "Valid 1-digit code: '1' through '9'",
      "Valid 2-digit code: '10' through '26'",
      "Leading '0' cannot be decoded standalone",
      "Space optimized from O(N) to O(1)"
    ],
    "tags": [
      "String",
      "Dynamic Programming"
    ]
  },
  {
    "id": "dsa-102",
    "title": "Unique Paths I & II (With Obstacles)",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "A robot is located at top-left corner of `m x n` grid. The robot can only move down or right. Find the number of possible unique paths to bottom-right corner. Handle obstacle grid.",
    "answer": "2D DP Table or 1D Rolling Row:\nWithout obstacles: `dp[j] = dp[j] + dp[j-1]` (or math combinations `(m+n-2) choose (m-1)`).\nWith obstacles `grid`:\nInitialize `dp = [0] * n; dp[0] = 1 if grid[0][0] == 0 else 0`.\nFor `r` in range(m):\n  For `c` in range(n):\n    If `grid[r][c] == 1`: `dp[c] = 0` (blocked)\n    Elif `c > 0`: `dp[c] += dp[c-1]`\nReturn `dp[n-1]`.\nTime: O(M * N), Space: O(N).",
    "keyPoints": [
      "dp[r][c] = dp[r-1][c] + dp[r][c-1]",
      "Obstacle resets cell path count to 0",
      "Space optimized to single 1D array of width n",
      "O(M * N) time and O(N) space"
    ],
    "tags": [
      "Array",
      "Dynamic Programming",
      "Matrix"
    ]
  },
  {
    "id": "dsa-103",
    "title": "Maximal Square",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "Given an `m x n` binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.",
    "answer": "2D DP Transition:\n`dp[i][j]` represents length of largest square whose bottom-right corner is `(i, j)`.\nIf `matrix[i][j] == '1'`:\n- `dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])` (bounded by minimum of top, left, and diagonal squares!).\n- `max_side = max(max_side, dp[i][j])`.\nReturn `max_side * max_side`.\nTime: O(M * N), Space: O(N) rolling row.",
    "keyPoints": [
      "Square size constrained by min(top, left, diagonal) + 1",
      "Requires only previous row and current row -> O(N) space",
      "Result is max_side\u00b2 (area)",
      "O(M * N) time and O(N) space"
    ],
    "tags": [
      "Array",
      "Dynamic Programming",
      "Matrix"
    ]
  },
  {
    "id": "dsa-104",
    "title": "Target Sum",
    "category": "Dynamic Programming",
    "difficulty": "Medium",
    "question": "You are given an integer array `nums` and an integer `target`. Build expression by adding '+' or '-' before each integer. Return the number of different expressions that evaluate to `target`.",
    "answer": "Math Reduction to Subset Sum:\nLet `P` be positive subset and `N` be negative subset:\n`sum(P) - sum(N) = target`\n`sum(P) + sum(N) = sum(nums)`\nAdding equations: `2 * sum(P) = target + sum(nums)` => `sum(P) = (target + sum(nums)) / 2`.\nIf `target + sum(nums)` is odd or negative: return 0.\nReduces to finding number of subsets summing to `(target + sum(nums)) // 2` (Subset Sum DP!).\nTime: O(N * S), Space: O(S).",
    "keyPoints": [
      "Mathematical reformulation converts +/- problem into subset sum",
      "target + sum(nums) must be even and non-negative",
      "Solved with standard 0/1 knapsack combination DP",
      "O(N * S) time and O(S) space"
    ],
    "tags": [
      "Array",
      "Dynamic Programming"
    ]
  },
  {
    "id": "dsa-105",
    "title": "Combination Sum I & II",
    "category": "Backtracking",
    "difficulty": "Medium",
    "question": "In Combination Sum I, elements can be chosen unlimited times to sum to target. In Combination Sum II, each number may be used only once, and candidate numbers contain duplicates. Compare backtracking trees.",
    "answer": "Sum I: `backtrack(idx, target, path)`: When choosing `candidates[i]`, recursive call keeps same index `i` (unlimited reuse). Time: O(2^T).\n\nSum II: Sort array first. Recursive call advances index `i + 1`. Skip duplicates among siblings: `if i > start and candidates[i] == candidates[i-1]: continue`. Time: O(2^N).",
    "keyPoints": [
      "Sum I allows re-using current element (recurse with i)",
      "Sum II enforces single use (recurse with i + 1)",
      "Sum II skips duplicate siblings to prevent identical combinations",
      "Early termination when candidate exceeds remaining target"
    ],
    "tags": [
      "Array",
      "Backtracking"
    ]
  },
  {
    "id": "dsa-106",
    "title": "Letter Combinations of a Phone Number",
    "category": "Backtracking",
    "difficulty": "Medium",
    "question": "Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent according to telephone buttons.",
    "answer": "Backtracking / BFS Cartesion Product:\nMap digits to letter strings: `{'2': 'abc', '3': 'def', ...}`.\nRecursive helper `backtrack(idx, current_str)`:\n- If `idx == len(digits)`: `res.append(current_str); return`.\n- For `letter` in `phone_map[digits[idx]]`:\n  - `backtrack(idx + 1, current_str + letter)`\nTime: O(4^N * N) where N is number of digits (each digit has at most 4 letters).\nSpace: O(N) recursion depth.",
    "keyPoints": [
      "Digit-to-letters mapping table",
      "Tree depth equals length of digits string",
      "Branching factor 3 or 4 per level",
      "Time O(4^N * N) generating all combinations"
    ],
    "tags": [
      "String",
      "Backtracking"
    ]
  },
  {
    "id": "dsa-107",
    "title": "Sudoku Solver",
    "category": "Backtracking",
    "difficulty": "Hard",
    "question": "Write a program to solve a Sudoku puzzle by filling the empty cells. Optimize board verification using bitmasks.",
    "answer": "Backtracking with Bitmasks for Rows, Cols, and 3x3 Boxes:\nMaintain 9-bit bitmask for each row, column, and 3x3 box (`box_idx = (r // 3) * 3 + (c // 3)`).\nAt empty cell `(r, c)`:\n- Available numbers: `~(rows[r] | cols[c] | boxes[box_idx]) & 0x1ff`.\n- Iterate through available bits.\n- Set bit in row, col, box masks, place digit on board, recurse.\n- If recursion succeeds, return True.\n- Else backtrack: clear bit, reset cell to `.`.\nOptimization: Minimum Remaining Values (MRV) heuristic chooses cell with fewest valid candidate numbers first.",
    "keyPoints": [
      "Bitmask representation allows O(1) candidate number calculation",
      "MRV (Minimum Remaining Values) heuristic speeds up solving by 100x",
      "3x3 sub-box index = (r // 3) * 3 + (c // 3)",
      "Classic constraint satisfaction backtracking"
    ],
    "tags": [
      "Array",
      "Backtracking",
      "Matrix"
    ]
  },
  {
    "id": "dsa-108",
    "title": "Pow(x, n) (Fast Exponentiation / Binary Exponentiation)",
    "category": "Bit Manipulation",
    "difficulty": "Medium",
    "question": "Implement `pow(x, n)`, which calculates `x` raised to the power `n` in O(log n) time.",
    "answer": "Binary Exponentiation (Divide and Conquer):\nIf `n < 0`: `x = 1 / x; n = -n`.\n`res = 1`\nWhile `n > 0`:\n- If `n % 2 == 1` (`n & 1`): `res *= x`\n- `x *= x` (square the base)\n- `n //= 2` (`n >>= 1`)\nReturn `res`.\n\nInstead of multiplying `x` `n` times in O(N), we square the base at each step, halving `n`.\nTime: O(log N), Space: O(1).",
    "keyPoints": [
      "x^n = (x^2)^(n/2) for even n; x * (x^2)^((n-1)/2) for odd n",
      "Reduces multiplications from N to log2(N)",
      "Handles negative exponents by inverting base x = 1/x",
      "Handles INT_MIN overflow in C++/Java"
    ],
    "tags": [
      "Math",
      "Recursion",
      "Binary Exponentiation"
    ]
  },
  {
    "id": "dsa-109",
    "title": "Subsets with Bitmasking",
    "category": "Bit Manipulation",
    "difficulty": "Medium",
    "question": "Generate all 2^N subsets of an array `nums` without using recursion or backtracking.",
    "answer": "Iterate from `0` to `(1 << n) - 1`:\nEach integer `mask` from `0` to `2^n - 1` has a unique binary pattern of length `n`.\nBit `i` in `mask` being 1 means include `nums[i]` in current subset.\n`res = []`\nFor `mask` from 0 to `(1 << n) - 1`:\n  `subset = [nums[i] for i in range(n) if (mask & (1 << i))]`\n  `res.append(subset)`\nReturn `res`.\nTime: O(N * 2^N), Space: O(1) auxiliary.",
    "keyPoints": [
      "Binary representation of 0..2^N-1 maps directly to all combinations",
      "Bit i is 1 if nums[i] is selected",
      "Clean iterative approach without recursion stack",
      "Runs in O(N * 2^N) time"
    ],
    "tags": [
      "Array",
      "Bit Manipulation"
    ]
  },
  {
    "id": "dsa-110",
    "title": "Single Number II (Element Appears Once, Others Three Times)",
    "category": "Bit Manipulation",
    "difficulty": "Medium",
    "question": "Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element in O(N) time and O(1) space.",
    "answer": "Bitwise State Machine (Modulo 3 Counter):\nMaintain two bitmasks `ones` and `twos`:\n- `ones`: bits that have appeared 1 time (mod 3).\n- `twos`: bits that have appeared 2 times (mod 3).\nFor `x` in `nums`:\n  `ones = (ones ^ x) & ~twos`\n  `twos = (twos ^ x) & ~ones`\nBits appearing 3 times reset both masks to 0.\nReturn `ones`.\nTime: O(N), Space: O(1).",
    "keyPoints": [
      "Bitwise finite state machine for mod-3 counters",
      "ones and twos hold bit frequencies modulo 3",
      "Clears bits when frequency hits 3",
      "Time O(N) and auxiliary space O(1)"
    ],
    "tags": [
      "Array",
      "Bit Manipulation"
    ]
  }
];
