The following sections show a set of program optimization techniques that
aim at the improvements of performance and energy while keeping
the underlying algorithms unchanged.
1. Loop invariant code motion
2. Dead code elimination (general case and sparse element-wise)
3. Loop fusion
4. Loop permutation
5. Parallelization

### 1. Loop invariant code motion

"Loop invariant code" is the code fragment that is enclosed one or
more loops and its computation results are invariant across loop
iterations.  For instance:

```python
    for val in set:
        x1 = x0.abs().sqrt()
        x2 = add(x1, val)
```

The first statement in the loop computes element-wise abs and sqrt of
array `x0` and stores the results in array `x1`.  Here the values of
`x0` are invariant across iterations, and hence the results stored in
`x1` are also invariant.  Such computations (i.e., loop invariant
code) can be moved from the loop body to reduce program execution time
and energy.

```python
    x1 = x0.abs().sqrt()
    for val in set:
        x2 = add(x1, val)
```

This situation often happens in Python, especially when a single line of
code contains many operations, e.g.,:

```python
    for val in set:
        x2 = add(x2, x1 @ x1.T)
```

Since the results of `x1 @ x1.T` (i.e., Symmetric Rank-k Update for
`x1`) are loop invariant, we can move this computation by storing its
result into a temporal variable, e.g.:

```python
    tmp = x1 @ x1.T
    for val in set:
        x2 = add(x2, tmp)
```

### 2. Dead code elimination (general case and sparse element-wise)

"Dead code" is the code fragment whose result is unused after its
definition.  For instance, the first statement in the following
function body is dead code, which we can simply eliminate to improve
performance and energy.

```python
def my_func(x1: Array(float64, 2)) -> float64:
    x2 = add(x1, 1.0)  # Dead code to be eliminated
    return sum(x1)
```

Although such dead code fragments may not be common in general, sparse
arrays can be a good source of this optimization opportunity.

```python
def my_func(vals: Array(float64, 1), cols: Array(int32, 1), idxs: Array(int32, 1), nrows: int32, ncols: int32,
            x2: Array(float64, 2), x3: Array(float64, 2)) -> Array(float64):
    spm1 = csr_to_spm(vals, cols, idxs, ncols)
    spm2 = spm_mul(spm1, x2 @ x3)
```

The second statement of function body first computes the matrix-matrix
multiply `x2 @ x3` and then applies element-wise multiplication with
sparse matrix `spm1`, which is constructed via `csr_to_spm` function
at the first line.

Here, we don't need to compute the whole matrix-matrix multiply `x2 @ x3`
because `spm2[r,c]` is always zero if `spm1[r,c]` is zero despite of
the element `[r,c]` of `x2 @ x3`.  This can be considered as
"element-wise" dead code to be eliminated as follow.

```python
def my_func(vals: Array(float64, 1), cols: Array(int32, 1), idxs: Array(int32, 1), nrows: int32, ncols: int32,
            x2: Array(float64, 2), x3: Array(float64, 2)) -> Array(float64):
    spm2 = empty_spm(nrows, ncols)
    for r in range(nrows):
        for i in range(idxs[r], idxs[r+1]):
            c = cols[i]
            v = vals[i]  # element [r,c] of spm1
            tmp = 0.0
            for k in range(shape(x2,1)):
                tmp += x2[r][k] * x3[k][c]  # compute element [r,c] of x2 @ x3
            spm2.set_item_unsafe(v * tmp, r, c)
```

If the sparsity of `spm2` is 1%, we can simply remove the 99% of
matrix-matrix multiply `x2 @ x3` as the manner of dead code
elimination in the above code.

### 3. Loop fusion

### 4. Loop permutation

### 5. Parallelization
