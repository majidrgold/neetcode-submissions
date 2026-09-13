# The 18 Patterns Behind ~150 Coding Interview Problems

How to use this doc: for each pattern, read the idea, study the template, then solve the problems in order (easy → hard). Don't move to the next pattern until you can explain *why* that pattern fits a problem just from reading it — that recognition is the real skill.

---

## 1. Arrays & Hashing

**Idea:** Trade space for time. A hash map/set gives O(1) average lookup, letting you avoid nested loops.

**Recognize it when:** you need to check "have I seen this before," count frequencies, or find complements/pairs.

**Template:**
```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
```

**Problems:** Two Sum · Contains Duplicate · Valid Anagram · Group Anagrams · Top K Frequent Elements · Product of Array Except Self · Valid Sudoku · Longest Consecutive Sequence

**Complexity:** O(n) time, O(n) space typically.

---

## 2. Two Pointers

**Idea:** Use two indices moving toward each other (or same direction) to avoid nested loops — usually on sorted data.

**Recognize it when:** array is sorted, or you're comparing pairs/triplets from opposite ends.

**Template:**
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
```

**Problems:** Valid Palindrome · Two Sum II · 3Sum · Container With Most Water · Trapping Rain Water

**Complexity:** O(n) time, O(1) space — big upgrade from the O(n²) brute force.

---

## 3. Sliding Window

**Idea:** Maintain a window [left, right] over a sequence; expand right, shrink left when a condition breaks.

**Recognize it when:** "longest/shortest/max/min substring or subarray satisfying X."

**Template:**
```python
def longest_substring_no_repeat(s):
    seen = set()
    left = max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

**Problems:** Best Time to Buy/Sell Stock · Longest Substring Without Repeating Characters · Longest Repeating Character Replacement · Permutation in String · Minimum Window Substring · Sliding Window Maximum

**Complexity:** O(n) time — each pointer moves forward at most n times.

---

## 4. Stack

**Idea:** LIFO structure for matching, nesting, and "next greater/smaller element" problems.

**Recognize it when:** parentheses/brackets, undo operations, or needing to remember state until a later condition resolves it.

**Template (monotonic stack):**
```python
def daily_temperatures(temps):
    res = [0] * len(temps)
    stack = []  # indices
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)
    return res
```

**Problems:** Valid Parentheses · Min Stack · Evaluate Reverse Polish Notation · Generate Parentheses · Daily Temperatures · Car Fleet · Largest Rectangle in Histogram

**Complexity:** O(n) time — each element pushed/popped once.

---

## 5. Binary Search

**Idea:** Halve the search space each step. Works on sorted arrays *and* on "search on the answer" problems (monotonic predicate).

**Recognize it when:** sorted data, or a question like "minimum X such that condition holds" — even without an explicit array.

**Template:**
```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Problems:** Binary Search · Search a 2D Matrix · Koko Eating Bananas · Search in Rotated Sorted Array · Find Minimum in Rotated Sorted Array · Time Based Key-Value Store · Median of Two Sorted Arrays

**Complexity:** O(log n) time.

---

## 6. Linked List

**Idea:** Fast/slow pointers, dummy head nodes, and careful pointer rewiring.

**Recognize it when:** reversing, detecting cycles, merging, or reordering a linked list.

**Template (reverse):**
```python
def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev
```

**Template (fast/slow — cycle detection):**
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Problems:** Reverse Linked List · Merge Two Sorted Lists · Reorder List · Remove Nth Node From End · Copy List with Random Pointer · Add Two Numbers · Linked List Cycle · Find Duplicate Number · LRU Cache · Merge K Sorted Lists · Reverse Nodes in K-Group

**Complexity:** O(n) time, O(1) space (usually).

---

## 7. Trees

**Idea:** Recursive DFS (preorder/inorder/postorder) or level-by-level BFS.

**Recognize it when:** anything involving a binary tree/BST — depth, paths, comparisons, construction.

**Template (DFS):**
```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

**Template (BFS):**
```python
from collections import deque
def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
```

**Problems:** Invert Binary Tree · Same Tree · Subtree of Another Tree · Lowest Common Ancestor of a BST · Binary Tree Level Order Traversal · Validate BST · Kth Smallest Element in a BST · Construct Binary Tree from Preorder/Inorder · Binary Tree Max Path Sum · Serialize/Deserialize Binary Tree

**Complexity:** O(n) time, O(h) space where h is tree height (recursion stack).

---

## 8. Tries (Prefix Trees)

**Idea:** Nested hash maps where each level represents one character — enables fast prefix search.

**Recognize it when:** "starts with," autocomplete, or word search with a dictionary.

**Template:**
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

**Problems:** Implement Trie · Design Add and Search Words Data Structure · Word Search II

**Complexity:** O(L) per insert/search, where L is word length.

---

## 9. Heap / Priority Queue

**Idea:** Binary heap gives O(log n) insert and O(1) access to min/max — perfect for "top K" or "merge sorted things."

**Recognize it when:** "kth largest/smallest," scheduling, or continuously needing the current min/max.

**Template:**
```python
import heapq
def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    for n in nums[k:]:
        if n > heap[0]:
            heapq.heapreplace(heap, n)
    return heap[0]
```

**Problems:** Kth Largest Element in a Stream · Last Stone Weight · K Closest Points to Origin · Kth Largest Element in an Array · Task Scheduler · Design Twitter · Find Median from Data Stream · Merge K Sorted Lists

**Complexity:** O(n log k) for top-K style problems.

---

## 10. Backtracking

**Idea:** Recursive "try a choice → recurse → undo (backtrack)" to explore all valid combinations/paths.

**Recognize it when:** "all possible," "generate all," combinations/permutations/subsets, constraint satisfaction (N-Queens, Sudoku).

**Template:**
```python
def subsets(nums):
    res = []
    path = []
    def backtrack(start):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
    backtrack(0)
    return res
```

**Problems:** Subsets · Combination Sum · Permutations · Subsets II · Combination Sum II · Word Search · Palindrome Partitioning · Letter Combinations of a Phone Number · N-Queens

**Complexity:** Often exponential (O(2ⁿ) or O(n!)) — that's expected, the goal is correctness and pruning.

---

## 11. Graphs

**Idea:** Represent as adjacency list; traverse with DFS/BFS; use Union-Find for connectivity questions.

**Recognize it when:** grids (island counting), networks, dependencies, connectivity.

**Template (DFS on grid):**
```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols
                or grid[r][c] == '0' or (r, c) in visited):
            return
        visited.add((r, c))
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(r+dr, c+dc)

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                count += 1
    return count
```

**Problems:** Number of Islands · Clone Graph · Max Area of Island · Pacific Atlantic Water Flow · Surrounded Regions · Rotting Oranges · Walls and Gates · Course Schedule · Course Schedule II · Redundant Connection · Number of Connected Components · Graph Valid Tree · Word Ladder

**Complexity:** O(V + E) for DFS/BFS.

---

## 12. Advanced Graphs

**Idea:** Weighted graph algorithms — shortest path, minimum spanning tree, topological ordering.

**Recognize it when:** edge weights matter, "cheapest," "minimum cost to connect," or ordering with dependencies.

**Template (Dijkstra):**
```python
import heapq
def dijkstra(graph, start):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float('inf')):
            continue
        for neighbor, weight in graph[node]:
            nd = d + weight
            if nd < dist.get(neighbor, float('inf')):
                dist[neighbor] = nd
                heapq.heappush(heap, (nd, neighbor))
    return dist
```

**Problems:** Network Delay Time · Reconstruct Itinerary · Min Cost to Connect All Points · Swim in Rising Water · Alien Dictionary · Cheapest Flights Within K Stops

**Complexity:** O(E log V) for Dijkstra with a heap.

---

## 13. 1-D Dynamic Programming

**Idea:** Break a problem into subproblems where state depends on a linear sequence of prior states. Bottom-up (tabulation) or top-down (memoization).

**Recognize it when:** "number of ways," "min/max cost," and the answer for `n` depends on smaller `n`.

**Template:**
```python
def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
```

**Problems:** Climbing Stairs · Min Cost Climbing Stairs · House Robber · House Robber II · Longest Palindromic Substring · Palindromic Substrings · Decode Ways · Coin Change · Maximum Product Subarray · Word Break · Longest Increasing Subsequence · Partition Equal Subset Sum

**Complexity:** O(n) time/space typically (often O(1) space with rolling variables).

---

## 14. 2-D Dynamic Programming

**Idea:** State depends on two dimensions — usually two strings, or a grid.

**Recognize it when:** comparing two sequences, grid path counting, or subsequence/substring matching.

**Template (Longest Common Subsequence):**
```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
```

**Problems:** Unique Paths · Longest Common Subsequence · Best Time to Buy/Sell Stock with Cooldown · Coin Change II · Target Sum · Interleaving String · Edit Distance · Burst Balloons · Regular Expression Matching

**Complexity:** O(m·n) time and space (space often optimizable to O(n)).

---

## 15. Greedy

**Idea:** Make the locally optimal choice at each step and prove (or trust) it leads to a global optimum.

**Recognize it when:** "maximize/minimize" with a simple, provable local rule — no need to explore all options like backtracking.

**Template:**
```python
def can_jump(nums):
    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0
```

**Problems:** Maximum Subarray · Jump Game · Jump Game II · Gas Station · Hand of Straights · Merge Triplets to Form Target Triplet · Partition Labels · Valid Parenthesis String

**Complexity:** Usually O(n) or O(n log n) if sorting is involved.

---

## 16. Intervals

**Idea:** Sort by start (or end) time, then sweep through comparing overlaps.

**Recognize it when:** meeting rooms, merging ranges, scheduling.

**Template:**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

**Problems:** Insert Interval · Merge Intervals · Non-overlapping Intervals · Meeting Rooms · Meeting Rooms II · Minimum Interval to Include Each Query

**Complexity:** O(n log n) — dominated by the sort.

---

## 17. Math & Geometry

**Idea:** Problem-specific tricks — modular arithmetic, matrix manipulation, coordinate geometry.

**Recognize it when:** rotating/transposing matrices, powers, or geometric properties (collinearity, spirals).

**Template (matrix rotation in place):**
```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
```

**Problems:** Rotate Image · Spiral Matrix · Set Matrix Zeroes · Happy Number · Plus One · Pow(x, n) · Multiply Strings · Detect Squares

**Complexity:** Varies by problem; often O(n²) for matrix problems, O(log n) for fast exponentiation.

---

## 18. Bit Manipulation

**Idea:** Use XOR, AND, OR, and shifts for O(1) tricks — often replaces a full pass with a single arithmetic trick.

**Recognize it when:** "without using extra space," finding a unique element, or counting bits.

**Template (XOR to find single number):**
```python
def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result
```

**Problems:** Single Number · Number of 1 Bits · Counting Bits · Reverse Bits · Missing Number · Sum of Two Integers · Reverse Integer

**Complexity:** O(n) time, O(1) space.

---

## Suggested order to learn these

1. Arrays & Hashing → Two Pointers → Sliding Window → Stack *(warm-up, builds intuition for the rest)*
2. Binary Search → Linked List → Trees → Tries *(structure-focused)*
3. Heap → Backtracking → Graphs → Advanced Graphs *(search/traversal)*
4. 1-D DP → 2-D DP → Greedy → Intervals *(optimization — hardest conceptually)*
5. Math & Geometry → Bit Manipulation *(quick wins, can be done anytime)*

**Practice rule of thumb:** 3–5 problems per pattern, spaced with review. When stuck for >20 minutes on a new pattern, read the approach (not the code), re-derive it yourself, then code it from scratch a day later.
