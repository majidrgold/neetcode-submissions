# NeetCode 150 — Algorithm Cheatsheet

A reference for every core technique needed to solve the NeetCode 150, grouped by topic. For each: what it is, how to recognize when to use it, the template, and complexity.

---

## 1. Arrays & Hashing

**What it is:** Using a hash map/set for O(1) average lookup to avoid nested loops, or manipulating arrays in place.

**Recognize it when:** you need to check "have I seen this before," count frequencies, or find pairs/complements (e.g. Two Sum).

```python
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

**Complexity:** O(n) time, O(n) space.

---

## 2. Two Pointers

**What it is:** Two indices moving through a (usually sorted) structure — either converging from both ends, or one fast/one slow.

**Recognize it when:** the array is sorted, or you're looking for pairs/triplets that sum to something, or comparing from both ends (palindrome checks).

```python
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total == target:
        return [left, right]
    elif total < target:
        left += 1
    else:
        right -= 1
```

**Complexity:** O(n) time, O(1) space — beats the O(n²) brute force nested loop.

---

## 3. Sliding Window

**What it is:** A two-pointer variant where you maintain a *contiguous* range (`window`) and grow/shrink it based on a condition, instead of recomputing from scratch.

**Recognize it when:** "longest/shortest/max/min substring or subarray satisfying X" — the word **contiguous** is the tell.

```python
left = 0
window_state = {}   # or a running sum/count
best = 0
for right in range(len(s)):
    add(s[right], window_state)
    while window_is_invalid(window_state):
        remove(s[left], window_state)
        left += 1
    best = max(best, right - left + 1)
```

**Complexity:** O(n) — each pointer moves forward at most n times total (this is the "amortized" argument you should be able to explain).

---

## 4. Stack

**What it is:** LIFO structure for tracking "most recent unmatched thing" — parentheses, previous smaller/larger elements, undo history.

**Recognize it when:** matching pairs (parentheses), "next greater/smaller element," or evaluating expressions.

```python
stack = []
for char in s:
    if char in closing_to_opening:
        if not stack or stack[-1] != closing_to_opening[char]:
            return False
        stack.pop()
    else:
        stack.append(char)
return not stack
```

**Monotonic stack variant** (next greater element): keep the stack increasing/decreasing, popping while the invariant breaks.

**Complexity:** O(n) — each element pushed/popped at most once.

---

## 5. Binary Search

**What it is:** Halving a *sorted* search space each step.

**Recognize it when:** the data is sorted, OR the problem says "find minimum X such that condition holds" (binary search **on the answer**, not on an array — a huge unlock for a whole class of problems).

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

**Binary search on answer** (e.g. "minimum days to ship packages"):
```python
lo, hi = min_possible, max_possible
while lo < hi:
    mid = (lo + hi) // 2
    if feasible(mid):
        hi = mid          # mid works, try smaller
    else:
        lo = mid + 1       # mid doesn't work, need bigger
return lo
```

**Complexity:** O(log n).

---

## 6. Linked Lists

**What it is:** Pointer manipulation — no random access, so most tricks revolve around **fast/slow pointers** and carefully tracking `prev`/`curr`/`next`.

**Key patterns:**
- **Reverse a list:** walk with three pointers, flipping `.next` each step.
```python
prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
return prev
```
- **Fast/slow (Floyd's cycle detection):** `slow` moves 1 step, `fast` moves 2. If they meet, there's a cycle. Also finds the middle node.
- **Dummy head node:** simplifies edge cases when the head itself might change (merging, removing nodes).

**Complexity:** O(n) time, O(1) space (in-place pointer rewiring).

---

## 7. Trees

**What it is:** Recursive traversal (DFS) or level-by-level traversal (BFS) of a hierarchical structure.

**Recognize it when:** anything involving a binary tree/BST — depth, paths, validation, serialization.

```python
# DFS (recursive) — pick pre/in/post-order by where you process the node
def dfs(node):
    if not node:
        return
    # process(node)          # pre-order: process before children
    dfs(node.left)
    # process(node)          # in-order: process between children (gives sorted order for BST)
    dfs(node.right)
    # process(node)          # post-order: process after children

# BFS (level order)
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()
    # process(node)
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
```

**Complexity:** O(n) time (visit every node once), O(h) space for DFS recursion stack (h = height), O(w) for BFS queue (w = max width).

---

## 8. Tries (Prefix Trees)

**What it is:** A tree where each path from root spells out a prefix — built for fast prefix lookups (autocomplete, word search).

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
```

**Recognize it when:** you need to check many words against a shared set of prefixes repeatedly (Word Search II is Word Search + a Trie instead of a fixed target word).

**Complexity:** O(L) per insert/search, where L = word length — independent of how many words are stored.

---

## 9. Heap / Priority Queue

**What it is:** A structure that always gives you the min (or max) element in O(log n), instead of O(n) with a plain list scan.

**Recognize it when:** "top K," "k-th largest/smallest," "merge K sorted lists," or a running median.

```python
import heapq
heap = []
heapq.heappush(heap, val)
smallest = heapq.heappop(heap)

# Python heapq is min-heap only — for max-heap, negate values
heapq.heappush(heap, -val)
largest = -heapq.heappop(heap)

# Top K pattern: keep heap size capped at k
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)   # evicts the smallest, leaving the k largest
```

**Complexity:** O(log n) push/pop, O(n log k) for a top-K-of-n scan.

---

## 10. Backtracking

**What it is:** Build a solution incrementally; abandon (backtrack) the moment a partial solution can't work. Covered in depth above — the universal template:

```python
def backtrack(state):
    if is_complete(state):
        record_solution(state)
        return
    if is_invalid(state):
        return
    for choice in get_choices(state):
        make_choice(choice)
        backtrack(new_state)
        undo_choice(choice)
```

**The 4 decisions per problem:**
1. Does order matter? → `start_index` restriction, or a `used[]` array.
2. Can elements repeat within one answer? → recurse with `i` (reuse) vs `i+1` (no reuse).
3. Can input duplicates cause duplicate answers? → sort + skip same-depth duplicates.
4. What's the base case, and where can you prune early?

**Complexity:** exponential in the worst case (that's inherent — you're exploring a tree of choices), but pruning cuts the real-world cost dramatically.

---

## 11. Graphs

**What it is:** DFS/BFS generalized from trees to arbitrary node/edge structures (which may have cycles, so you need a `visited` set).

**Recognize it when:** grids (each cell = node, adjacency = neighbors), explicit adjacency lists, "number of islands," "course schedule" (cycle detection).

```python
# DFS on a graph/grid
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in get_neighbors(node):
        dfs(neighbor, visited)

# BFS — shortest path in unweighted graph
from collections import deque
queue = deque([start])
visited = {start}
dist = 0
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()
        if node == target:
            return dist
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    dist += 1
```

**Union-Find (Disjoint Set Union):** for connectivity questions ("are these in the same group," building a spanning tree) without repeated DFS.
```python
parent = list(range(n))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # path compression
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[ra] = rb
        return True   # newly connected
    return False      # already connected (would form a cycle)
```

**Complexity:** DFS/BFS = O(V + E). Union-Find with path compression ≈ O(α(n)) per op (effectively constant).

---

## 12. Advanced Graphs

**Topological sort** (ordering with dependencies, e.g. course prerequisites): repeatedly remove nodes with no incoming edges (Kahn's algorithm/BFS), or DFS with a post-order stack.

**Dijkstra's algorithm** (shortest path, weighted, non-negative edges): BFS with a min-heap instead of a plain queue, always expanding the currently-cheapest node.
```python
import heapq
dist = {start: 0}
heap = [(0, start)]
while heap:
    d, node = heapq.heappop(heap)
    if d > dist.get(node, float('inf')):
        continue
    for neighbor, weight in get_neighbors(node):
        nd = d + weight
        if nd < dist.get(neighbor, float('inf')):
            dist[neighbor] = nd
            heapq.heappush(heap, (nd, neighbor))
```

**Minimum Spanning Tree** (connect all nodes, minimum total edge weight): Prim's (grow one tree, heap of frontier edges) or Kruskal's (sort all edges, add via Union-Find, skip if it'd form a cycle).

**Complexity:** Topological sort O(V+E). Dijkstra O((V+E) log V) with a heap. Kruskal O(E log E) (dominated by the sort).

---

## 13. Dynamic Programming (1-D and 2-D)

**What it is:** Backtracking's sibling — when the same subproblem gets recomputed many times (overlapping subproblems + optimal substructure), cache the result instead of recomputing.

**Recognize it when:** "min/max/count ways to do X," and a brute-force recursive solution would revisit the same `(state)` repeatedly. Coin Change is structurally identical to Combination Sum — same recursion tree, but Combination Sum wants *all* the actual combinations, Coin Change only wants a *count/min*, so overlapping `(remaining_target)` states can be memoized.

```python
# Top-down (memoization) — literally backtracking + a cache
memo = {}
def dp(state):
    if state in base_cases:
        return base_case_value
    if state in memo:
        return memo[state]
    result = combine(dp(next_state) for next_state in transitions(state))
    memo[state] = result
    return result

# Bottom-up (tabulation) — build the table iteratively instead
dp_table = [base_case] * (n + 1)
for i in range(1, n + 1):
    dp_table[i] = combine(dp_table[i - j] for j in valid_transitions)
return dp_table[n]
```

**2-D DP** — same idea, but state is a pair `(i, j)` (e.g. two string indices for edit distance/LCS): `dp[i][j]` table instead of `dp[i]`.

**The one mental shift from backtracking:** ask "what's the minimal set of variables that fully describes where I am?" — that tuple is your DP state and your cache key.

**Complexity:** O(number of distinct states × work per state) — usually a massive improvement over the exponential brute force.

---

## 14. Greedy

**What it is:** Make the locally-best choice at each step and never reconsider it, trusting (and ideally being able to prove) that this leads to a globally optimal answer.

**Recognize it when:** "maximum profit," "minimum number of X," interval scheduling, jump games — and *proving* a greedy choice is always safe (exchange argument) rather than just guessing.

```python
# Example shape: process items in sorted order, greedily commit
items.sort(key=some_criterion)
result = 0
for item in items:
    if locally_best_choice_is_valid(item):
        commit(item)
```

**Complexity:** usually O(n log n) (dominated by the sort), much better than DP when a greedy proof actually holds.

---

## 15. Intervals

**What it is:** A greedy/sorting sub-pattern specifically for `[start, end]` ranges — merging overlaps, scheduling without conflicts, inserting a new interval.

**Recognize it when:** the input is a list of intervals.

```python
intervals.sort(key=lambda x: x[0])
merged = [intervals[0]]
for start, end in intervals[1:]:
    if start <= merged[-1][1]:          # overlaps with last merged interval
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
```

**Complexity:** O(n log n), dominated by sorting.

---

## 16. Bit Manipulation

**What it is:** Using bitwise operators to solve counting/uniqueness problems in O(1) space instead of a hash set.

**Key tricks:**
- `x ^ x == 0`, `x ^ 0 == x` → XOR-ing everything cancels pairs, leaving the single unpaired element (Single Number).
- `n & (n - 1)` clears the lowest set bit → used to count set bits, or check if n is a power of 2 (`n & (n-1) == 0`).
- `n & 1` checks the last bit (odd/even).
- `<<` / `>>` for multiply/divide by powers of 2.

**Complexity:** O(1) or O(bits) — typically the most efficient class of solution when it applies.

---

## 17. Math & Geometry

**What it is:** Problem-specific formulas rather than a single reusable template — but common recurring pieces:
- Matrix rotation/traversal (rotate image, spiral matrix) — careful index math, often via transpose + reverse.
- GCD/LCM (Euclidean algorithm) for divisibility problems.
- Modular arithmetic for large-number problems (avoiding overflow, "answer mod 10^9+7").

**Complexity:** varies by problem; usually O(n) or O(n²) for matrix problems.

---

## Quick-recognition table

| Signal in the problem | Likely technique |
|---|---|
| "pair/triplet sums to target," sorted array | Two Pointers |
| "longest/shortest **contiguous** substring/subarray" | Sliding Window |
| Matching brackets, "next greater element" | Stack |
| Sorted array, or "minimum X such that condition" | Binary Search |
| Reverse/detect cycle/find middle of a list | Linked List fast-slow pointers |
| Binary tree, "path," "depth," "validate" | Tree DFS/BFS |
| Many words vs. shared prefixes | Trie |
| "top K," "k-th largest," merge sorted streams | Heap |
| "find all combinations/subsets/permutations" | Backtracking |
| Grid/adjacency list, "number of islands," "can finish courses" | Graph DFS/BFS, Union-Find, Topological Sort |
| Weighted shortest path | Dijkstra |
| "min/max ways to do X," overlapping subproblems | Dynamic Programming |
| "maximum profit," interval scheduling, provably-safe local choice | Greedy |
| List of `[start, end]` ranges | Intervals |
| "single number," "power of 2," count set bits | Bit Manipulation |

---

## Suggested learning order

1. Arrays & Hashing → Two Pointers → Sliding Window → Stack *(warm-up, pattern recognition)*
2. Binary Search *(including "on the answer" variant)*
3. Linked Lists → Trees → Tries *(pointer/recursion fundamentals)*
4. Heap
5. Backtracking *(you're here)*
6. Graphs → Advanced Graphs
7. 1-D DP → 2-D DP *(the direct sequel to backtracking — memoize the recursion tree)*
8. Greedy → Intervals
9. Bit Manipulation, Math & Geometry *(smaller, can be done anytime)*
