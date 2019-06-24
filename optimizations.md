The following sections summarize a set of  optimization techniques that
aim to improve the performance and energy of an Intrepydd kernel.  The
algorithm improvement examples represent two simple possibilities.
Many other such improvements are possible, depending on the algorithms
that you are working on.
1. Algorithmic improvement -- Loop Invariant Code Motion (LICM)
2. Algorithmic improvement -- Dead Code Elimination (DCE), including element-based DCE for sparse matrices
3. Parallelization
4. Locality optimizations

 using pfor loops to reduce the delay term in the goal metric via parallelism,
   and also fusing/merging loops to reduce the energy term with
   improved locality, e.g., by replacing multiple passes over an array
   by a single pass.

### 1. Loop invariant code motion

"Loop invariant code" refers to subcomputations that redundantly compute the same
value in different iterations of a loop.  Consider the following
Intrepydd code example:
```python
    # Example 1-1 (before loop invariant code motion)
    for val in set:
        x1 = x0.abs().sqrt()
        x2 = add(x1, val)
```
The first statement in the loop computes the element-wise abs and sqrt of
array `x0` and stores the result in array `x1`.  In this example.  the value of
`x0` is invariant across iteration of the for loop, and hence the result computed in
`x1` is also invariant.  Such computations (i.e., loop invariant
code) can be moved outside the loop body as follows, to reduce program execution time
and energy:
```python
    # Example 1-1 (after loop invariant code motion)
    x1 = x0.abs().sqrt()
    for val in set:
        x2 = add(x1, val)
```
After the LICM, there are fewer operations performed by the algorithm because
the operations to evaluate `x0.abs().sqrt()` are only performed once,
instead of `|set|` times.

There can be many opportunities for LICM in Python and Intrepydd
code, some of which may require the introduction of a new "temporary" variable.  Another example is as follows:
```python
    # Example 1-2 (before loop invariant code motion)
    for val in set:
        x2 = add(x2, x1 @ x1.T)
```
Since the result of `x1 @ x1.T` (i.e., Symmetric Rank-k Update for
`x1`) is loop invariant, we can move this computation outside the loop
by storing its
result into a temporary variable as follows:
```python
    # Example 1-2 (after loop invariant code motion)
    tmp = x1 @ x1.T
    for val in set:
        x2 = add(x2, tmp)
```

### 2. Algorithmic improvement -- Dead Code Elimination (DCE), including element-based DCE for sparse matrices

"Dead code" is the code fragment whose result is unused after its
definition.  For instance, the first statement in the following
function body is dead code, which we can simply eliminate to improve
performance and energy.

```python
# Example 2-1 (before dead code elimination)
def my_func(x1: Array(float64, 2)) -> float64:
    x2 = add(x1, 1.0)  # Dead code to be eliminated
    return sum(x1)
```

Although such dead code fragments may not be common in general, sparse
arrays can be a good source of this optimization opportunity.

```python
# Example 2-2 (before element-wise dead code elimination)
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
# Example 2-2 (after element-wise dead code elimination)
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

### 3. Parallelization 

### 4. Locality optimizations
