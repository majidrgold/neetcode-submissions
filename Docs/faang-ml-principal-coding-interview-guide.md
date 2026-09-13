# FAANG coding interviews for Lead/Principal AI/ML Engineers

Standard DSA (NeetCode 150) is necessary but not sufficient at this level. This covers what's *additionally* expected: ML-specific coding rounds, the communication bar that changes at senior levels, and the adjacent knowledge interviewers assume you have.

---

## 1. What actually changes at Lead/Principal level

The problems aren't necessarily harder — the bar for *how* you solve them is higher. Interviewers are evaluating:

- **You clarify before coding.** Junior candidates jump to code. Senior candidates restate the problem, ask about scale/constraints/edge cases, and propose an approach *before* writing anything. Silence while typing is a red flag at this level — narrate your reasoning.
- **You discuss trade-offs unprompted.** "I'll use a hash map here — O(n) time, O(n) space — versus sorting first for O(n log n) time, O(1) space. Given we care more about latency than memory here, I'll go with the hash map." That sentence alone signals seniority more than the code does.
- **You write production-quality code, not contest code.** Meaningful variable names, no magic numbers, functions that do one thing. At Principal level, some interviewers will explicitly ask "how would you make this production-ready" — think input validation, logging hooks, type hints.
- **You test your own code out loud.** Walk through at least one normal case and one edge case (empty input, single element, all-duplicates, negative numbers) without being asked.
- **You're expected to know when to stop optimizing.** Senior candidates recognize when O(n²) is *fine* (small, bounded n) rather than reflexively over-engineering — and can articulate why.
- **ML coding rounds replace or supplement pure DSA.** Many FAANG ML-track loops (Meta, Google DeepMind/Research, Amazon AWS AI, Apple ML) include a round where you implement an ML algorithm from scratch in NumPy/Python — no sklearn, no PyTorch autograd.

---

## 2. Communication framework for every coding round

A structured loop to run through out loud, every time:

1. **Restate** the problem in your own words. Confirms you understood it.
2. **Clarify** — ask about input size, data types, duplicates, sorted-ness, negative numbers, what to return on invalid input.
3. **Propose** a brute-force approach first, state its complexity, *then* propose the optimization. Don't skip straight to optimal — it shows your reasoning process.
4. **Code**, narrating non-obvious decisions as you write.
5. **Test** — trace through a normal example, then explicitly call out 1-2 edge cases.
6. **Analyze** final time/space complexity out loud, unprompted.

This is sometimes called UMPIRE (Understand, Match, Plan, Implement, Review, Evaluate) — same idea under a different name. Pick a version and drill it until it's automatic.

---

## 3. ML-from-scratch implementations you must be able to write cold

These show up directly as coding questions ("implement k-means," "implement logistic regression") at Meta, Google, Amazon, and most AI-lab interviews. You should be able to write each of these in under 15 minutes with correct vectorized NumPy, not toy loops.

### Linear regression (closed-form + gradient descent)
```python
import numpy as np

def linear_regression_gd(X, y, lr=0.01, epochs=1000):
    n, d = X.shape
    w = np.zeros(d)
    b = 0.0
    for _ in range(epochs):
        y_pred = X @ w + b
        error = y_pred - y
        dw = (2 / n) * X.T @ error
        db = (2 / n) * np.sum(error)
        w -= lr * dw
        b -= lr * db
    return w, b
```

### Logistic regression (with sigmoid + binary cross-entropy)
```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def logistic_regression_gd(X, y, lr=0.01, epochs=1000):
    n, d = X.shape
    w = np.zeros(d)
    b = 0.0
    for _ in range(epochs):
        z = X @ w + b
        y_pred = sigmoid(z)
        dw = (1 / n) * X.T @ (y_pred - y)
        db = (1 / n) * np.sum(y_pred - y)
        w -= lr * dw
        b -= lr * db
    return w, b
```

### k-means clustering
```python
def kmeans(X, k, epochs=100):
    n, d = X.shape
    centroids = X[np.random.choice(n, k, replace=False)]
    for _ in range(epochs):
        dists = np.linalg.norm(X[:, None] - centroids[None, :], axis=2)  # (n, k)
        labels = np.argmin(dists, axis=1)
        new_centroids = np.array([
            X[labels == i].mean(axis=0) if np.any(labels == i) else centroids[i]
            for i in range(k)
        ])
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return centroids, labels
```

### k-nearest neighbors
```python
def knn_predict(X_train, y_train, x_query, k):
    dists = np.linalg.norm(X_train - x_query, axis=1)
    nearest_idx = np.argsort(dists)[:k]
    nearest_labels = y_train[nearest_idx]
    values, counts = np.unique(nearest_labels, return_counts=True)
    return values[np.argmax(counts)]
```

### Softmax + cross-entropy (numerically stable)
```python
def softmax(z):
    z = z - np.max(z, axis=-1, keepdims=True)   # subtract max: prevents overflow
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z, axis=-1, keepdims=True)

def cross_entropy(y_true_onehot, y_pred_probs, eps=1e-12):
    y_pred_probs = np.clip(y_pred_probs, eps, 1 - eps)  # prevent log(0)
    return -np.mean(np.sum(y_true_onehot * np.log(y_pred_probs), axis=-1))
```

### A single neural network layer, forward + backward pass by hand
```python
class DenseLayer:
    def __init__(self, in_dim, out_dim):
        self.W = np.random.randn(in_dim, out_dim) * 0.01
        self.b = np.zeros(out_dim)

    def forward(self, X):
        self.X = X                    # cache for backward
        return X @ self.W + self.b

    def backward(self, dout, lr):
        dW = self.X.T @ dout
        db = np.sum(dout, axis=0)
        dX = dout @ self.W.T
        self.W -= lr * dW
        self.b -= lr * db
        return dX
```
Interviewers frequently probe: "what does `dX` represent, and why do you return it?" — the answer is that it's the gradient flowing to the *previous* layer, which is the entire mechanism of backprop (chain rule, layer by layer).

### Scaled dot-product attention (increasingly common given LLM prevalence)
```python
def attention(Q, K, V, mask=None):
    d_k = Q.shape[-1]
    scores = Q @ K.transpose(-2, -1) / np.sqrt(d_k)   # scale by sqrt(d_k) for stability
    if mask is not None:
        scores = np.where(mask, scores, -np.inf)
    weights = softmax(scores)
    return weights @ V
```
Know *why* the `sqrt(d_k)` scaling exists (keeps dot products from growing large with dimension, which would push softmax into saturated/near-zero-gradient regions) — that reasoning is often the actual follow-up question.

### Decision tree split (Gini impurity)
```python
def gini(y):
    _, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    return 1 - np.sum(probs ** 2)

def best_split(X, y):
    best_gain, best_feat, best_thresh = -1, None, None
    parent_gini = gini(y)
    for feat in range(X.shape[1]):
        for thresh in np.unique(X[:, feat]):
            left = y[X[:, feat] <= thresh]
            right = y[X[:, feat] > thresh]
            if len(left) == 0 or len(right) == 0:
                continue
            weighted_gini = (len(left) * gini(left) + len(right) * gini(right)) / len(y)
            gain = parent_gini - weighted_gini
            if gain > best_gain:
                best_gain, best_feat, best_thresh = gain, feat, thresh
    return best_feat, best_thresh
```

**Others worth being able to sketch on request (lower frequency but do come up):** PCA (via SVD or eigendecomposition of the covariance matrix), naive Bayes, a basic recommendation system (matrix factorization via SGD), batch normalization forward pass, an LSTM/GRU cell's equations, non-max suppression (for CV roles), beam search decoding (for NLP/LLM roles).

---

## 4. NumPy / Python fluency specifically for ML coding rounds

Interviewers penalize loop-based implementations when a vectorized one is expected — "can you vectorize that?" is one of the most common follow-ups.

- **Broadcasting rules**: know exactly how shapes align (trailing dimensions must match or be 1) — this is where most live-coding bugs happen (`X[:, None]` vs `X[None, :]` mistakes, as in the k-means example above).
- **Avoid Python loops over rows/columns** whenever a matrix operation exists: `X @ W` instead of nested loops, `np.sum(axis=...)` instead of manual accumulation.
- **Numerical stability idioms**: subtract the max before `exp()` (softmax), clip before `log()` (cross-entropy), use `log-sum-exp` trick for log-likelihoods.
- **Shape discipline**: state tensor shapes out loud at each step (`X: (n, d)`, `W: (d, k)`, `scores: (n, k)`) — this catches bugs before you run the code and reads as senior-level rigor.
- **`np.random.seed()`** for reproducibility when asked to demo output.

---

## 5. Statistics & probability, in coding form

These often appear as short coding exercises, not whiteboard theory:

- Implement a function to compute mean/variance/standard deviation without `np.var` (shows you understand the formula, not just the API).
- Sample from a distribution given only `random.random()` (e.g., implement `np.random.choice` with weighted probabilities via cumulative sum + binary search).
- Compute a confidence interval or run a basic A/B test significance calculation (z-test/t-test) in code.
- Reservoir sampling — sample k items from a stream of unknown length with uniform probability, O(1) space per item:
```python
import random
def reservoir_sample(stream, k):
    reservoir = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir
```

---

## 6. Beyond pure coding: what Lead/Principal loops add

A Principal-level loop is rarely *just* DSA + ML coding. Expect some subset of:

- **ML system design round** — distinct from software system design. Practice framing: problem formulation → data collection/labeling → feature engineering → model choice & justification → training infra (data/model parallelism) → offline eval metrics → online eval (A/B testing) → deployment/serving → monitoring for drift/degradation → retraining loop. Common prompts: "design a feed ranking system," "design a fraud detection system," "design a search relevance model."
- **Behavioral rounds weighted toward leadership**, not just individual contribution: driving technical direction across teams, resolving technical disagreements, mentoring, handling ambiguous or conflicting priorities, influence without authority. Use a structured format (STAR: Situation, Task, Action, Result) and have 6-8 stories ready that map to common leadership themes (conflict, failure/mistake, ambiguity, technical trade-off under pressure, mentoring).
- **Research depth / "tell me about a paper" conversations** — be ready to discuss the architecture and trade-offs of whatever's current and relevant to the team (transformers, diffusion models, RLHF/DPO, retrieval-augmented generation) at a level deeper than a summary — know the actual mechanism, not just the name.
- **Code review / debugging rounds** — given a chunk of (sometimes deliberately buggy) ML code, find the bug. Common planted bugs: forgetting `model.eval()` / `torch.no_grad()`, data leakage (fitting a scaler on the full dataset before train/test split), off-by-one in indexing labels, wrong axis in a reduction, not detaching gradients, shape mismatches silently broadcasting into wrong results.
- **SQL** — still shows up for ML roles adjacent to product/data (window functions, joins, aggregations over event/feature tables) even at senior levels. Don't skip practicing it just because the role is "ML."

---

## 7. Common mistakes at this level (and how they read to the interviewer)

| Mistake | What it signals |
|---|---|
| Jumping straight to code without clarifying | Doesn't gather requirements — a leadership red flag, not just a coding one |
| Using `sklearn.LinearRegression()` when asked to implement it | Doesn't understand the underlying mechanism |
| Silent debugging (long pauses, no narration) | Can't communicate under pressure — a proxy for how you'd behave in an incident |
| Not stating complexity unprompted | Hasn't internalized complexity analysis as a habit, not just a fact to recite |
| Over-engineering a simple problem (premature abstraction, unnecessary design patterns) | Can't calibrate solution complexity to actual problem size — expensive in real engineering orgs |
| No edge-case testing without being asked | Wouldn't catch these in production either |
| Treating the ML coding round like a LeetCode round (ignoring numerical stability, vectorization) | Hasn't actually implemented ML systems, only used high-level libraries |

---

## 8. Practice strategy

1. **Time-box every practice problem** — 25-35 minutes, then force yourself to either finish or explain your incomplete approach out loud. Interviews don't wait for you to fully work it out silently.
2. **Practice out loud, even alone** — record yourself. The communication framework in section 2 needs to be reflexive, not something you remember to do mid-interview.
3. **Re-implement the section-3 list from memory, cold, weekly** — until you can write logistic regression or k-means without looking anything up, in under 10 minutes, with correct vectorization.
4. **Do at least a few mock interviews with another senior/staff engineer** — peer feedback on your *communication*, not just correctness, is the thing self-practice can't give you.
5. **For ML system design, build a personal template** (the pipeline stages in section 6) and practice slotting different problems into it, rather than improvising structure each time.

---

## Quick pre-interview checklist

- [ ] Can restate any problem back in your own words within 30 seconds
- [ ] Can state brute-force complexity before proposing an optimization
- [ ] Can implement linear regression, logistic regression, k-means, k-NN, and softmax+cross-entropy from memory, vectorized, in under 10 minutes each
- [ ] Can explain *why* softmax subtracts the max, *why* attention scales by `sqrt(d_k)`, *why* you clip before `log()`
- [ ] Has 6-8 STAR stories ready covering conflict, failure, ambiguity, mentoring, and technical trade-offs
- [ ] Has a repeatable ML system design template memorized
- [ ] Tests own code with at least one edge case, unprompted, every single time
