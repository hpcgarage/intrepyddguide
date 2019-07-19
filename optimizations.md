The following sections summarize a set of  optimization techniques that
aim to improve the performance and energy of an Intrepydd kernel:
1. Algorithmic improvement -- Loop Invariant Code Motion (LICM)
2. Algorithmic improvement -- Dead Code Elimination (DCE), including element-based DCE for sparse matrices
3. Parallelization
4. Locality optimizations

The
algorithmic improvement examples in sections 1 and 2 represent two simple approaches.
Many other related improvements are possible, depending on the algorithms
that you are working on. 

### 1. Algorithmic improvement -- Loop Invariant Code Motion (LICM)

"Loop invariant code" refers to subcomputations that redundantly compute the same
value in different iterations of a loop.  Consider the following
Intrepydd code example:
```python
    # Example 1-1 (before loop invariant code motion)
    for val in set:
        x1 = x0.abs().sqrt()
        x2 = add(x1, val)
        ...  # more code to use x2
```
The first statement in the loop computes the element-wise abs and sqrt of
array `x0` and stores the result in array `x1`.  In this example.  the value of
`x0` is invariant across iterations of the for loop, and hence the result computed in
`x1` is also invariant.  Such loop-invariant computations can be moved outside the loop body as follows, to reduce program execution time
and energy:
```python
    # Example 1-1 (after loop invariant code motion)
    x1 = x0.abs().sqrt()
    for val in set:
        x2 = add(x1, val)
        ...  # more code to use x2
```
After the LICM, there are fewer operations performed by the algorithm because
the operations to evaluate `x0.abs().sqrt()` are only performed once,
instead of `|set|` times.

There can be many opportunities for LICM in Python and Intrepydd
code, some of which may require the introduction of a new "temporary"
variable.  An example of LICM with a temporary variable is as follows:
```python
    # Example 1-2 (before loop invariant code motion)
    for val in set:
        x2 = add(x2, x1 @ x1.T)
```
Since the result of `x1 @ x1.T` (i.e., Symmetric Rank-k Update for
`x1`) is loop-invariant, we can move this computation outside the loop
by storing its
result into a temporary variable as follows:
```python
    # Example 1-2 (after loop invariant code motion)
    tmp = x1 @ x1.T
    for val in set:
        x2 = add(x2, tmp)
```

### 2. Algorithmic improvement -- Dead Code Elimination (DCE), including element-based DCE for sparse matrices

"Dead code" is a term used for code fragments whose results are unused after their
definition.  For instance, the first statement (computation of `x2`) in the following
function body, `x2 = add(x1, 1.0) `, is dead code, which  can  be eliminated to improve
performance and energy.
```python
# Example 2-1 (before dead code elimination)
def my_func(x1: Array(float64, 2)) -> float64:
    x2 = add(x1, 1.0)  # Dead code to be eliminated
    return sum(x1)
```

Although such obvious dead code fragments may not be common in practice, sparse
arrays can also be a good source of this optimization opportunity as illustrated in the following example:
```python
# Example 2-2 (before element-wise dead code elimination)
def my_func(vals: Array(float64, 1), cols: Array(int32, 1), idxs: Array(int32, 1), nrows: int32, ncols: int32,
            x2: Array(float64, 2), x3: Array(float64, 2)) -> Array(float64):
    spm1 = csr_to_spm(vals, cols, idxs, ncols)
    spm2 = spm_mul(spm1, x2 @ x3)
```

The second statement of function body first computes the matrix-matrix
multiply `x2 @ x3` and then applies element-wise multiplication with
sparse matrix `spm1`, which is constructed by the `csr_to_spm` function
in the first line.

In this example, we don't need to compute the entire matrix product, `x2 @ x3`,
because `spm2[r,c]` is always zero if `spm1[r,c]` is zero, regardless of
the value of  element `[r,c]` of `x2 @ x3`.  This can be considered as
an opportunity for
partial dead code elimination as shown below:
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
                tmp += x2[r,k] * x3[k,c]  # compute element [r,c] of x2 @ x3
            spm2.spm_set_item_unsafe(v * tmp, r, c)
```
For example, if the sparsity of `spm2` is 1%, we can  remove 99% of
the computation needed for the matrix-matrix product `x2 @ x3` by
using the partial dead code elimination illustrated above.

### 3. Parallelization 

As indicated in the [Intrepydd v0.2 Language Summary ](language.md),
eligible sequential loops can be converted to parallel loops by simply
replacing `for` by `pfor`.  As an example, consider the following loop
nest which performs a stencil computation:
```python
# Example 3-1 (before loop parallelization)
    for i in range(1, n-1):
        for j in range(1, m-1):
            B[i,j] = (A[i,j] + A[i,j-1] + A[i,j+1] + A[i-1,j] + A[i+1,j]) / 5.0
```

This code satisfies all the necessary conditions for parallelizing the outer
i-loop, which results in the following code, which should be efficient
for sufficiently large values of `n` and `m`:
```python
# Example 3-2 (efficient coarse-grained loop parallelization)
    pfor i in range(1, n-1):      # Parallel
        for j in range(1, m-1):   # Sequential
            B[i,j] = (A[i,j] + A[i,j-1] + A[i,j+1] + A[i-1,j] + A[i+1,j]) / 5.0
```

While parallelizing the inner j-loop is also legal, it is not efficient
because there is some intrinsic overhead in creating a `pfor` loop,
which gets amplified when the `pfor` loop is in the innermost location
as shown below:
```python
# Example 3-3 (inefficient fine-grained loop parallelization)
    for i in range(1, n-1):       # Sequential
        pfor j in range(1, m-1):  # Parallel
            B[i,j] = (A[i,j] + A[i,j-1] + A[i,j+1] + A[i-1,j] + A[i+1,j]) / 5.0
```

### 4. Locality optimizations

Finally, an important way to further reduce energy and delay is to
improve the locality in an Intrepydd kernel by 1) ensuring that
array elements are traversed in a row-major order as much as possible, and 2) replacing multiple passes over an array
by a single pass.

For 1), a common code transformation that is used is loop permutation,
as illustrated in the following examples:
```python
# Example 4-1 (before loop permutation)
    for i in range(n):
        for j in range(m):  # Column-major accesses on: A[j,i], B[j,i], C[j,i]
            D[i,j] = A[j,i] + B[j,i] + C[j,i]
```

Since the above loop nest has efficient row-major accesses on `D[i,j]`
but inefficient column-major accesses on `A[j,i], B[j,i], C[j,i]`, it
will be a net win to permute (interchange) the two loops to obtain
the following loop nest consisting of row-major accesses on  `A[j,i],
B[j,i], C[j,i]` and column-major accesses on `D[i,j]`:
```python
# Example 4-1 (after loop permutation)
    for j in range(m):
        for i in range(n):  # Column-major access on: D[i,j]
            D[i,j] = A[j,i] + B[j,i] + C[j,i]
```

Another example can be found in the following code fragment
```python
# Example 4-2 (before loop permutation)
    for i in range(ni):
        for j in range(nj):
           for k in range(nk):  # Stride access on: B[k,j]
            C[i,j] += alpha * A[i,k] * B[k,j]
```
This example can  be fixed by interchanging the `k` and `j` loops,
as shown below:
```python
# Example 4-2 (after loop permutation)
    for i in range(ni):
        for k in range(nk):
            for j in range(nj):  # No stride access on all arrays
                C[i,j] += alpha * A[i,k] * B[k,j]
```

Another way to improve locality is to fuse adjacent loops so as to replace
multiple traversals over an array by a smaller number of traversals,
ideally one, as illustrated in the following code example:
```python
# Example 4-3 (before loop fusion)
    for i in range(n):
        B[i] += A[i] * alpha
    for i in range(n):
        C[i] += B[i] * beta
```

After fusing the two loops, we will only performs one pass over array
`B`, instead of two passes in the original version:
```python
# Example 4-3 (after loop fusion)
    for i in range(n):
        B[i] += A[i] * alpha
        C[i] += B[i] * beta
```

Loop fusion can also be performed on nested loops as illustrated in
the following example:
```python
# Example 4-2 (before loop fusion)
    for i in range(n):
        for j in range(m):
            D[i,j] = A[i,j] + B[i,j] + C[i,j]
    for i in range(n):
        for j in range(m):
            E[i,j] = D[i,j] / 3.0
    for i in range(1, n-1):
        for j in range(1, m-1):
            F[i,j] = D[i,j] + D[i,j-1] + D[i,j+1] + D[i-1,j] + D[i+1,j]
    for i in range(1, n-1):
        for j in range(1, m-1):
            G[i,j] = F[i,j] / 5.0
```
After fusion, we obtain two loop nests instead of four loop nests, as
shown below.  The main reason why  loop fusion cannot be
performed on all loops is that the first and second fused loop nests
have different loop bounds:
```python
# Example 4-2 (after loop fusion)
    for i in range(n):
        for j in range(m):
            D[i,j] = A[i,j] + B[i,j] + C[i,j]
            E[i,j] = D[i,j] / 3.0
    for i in range(1, n-1):
        for j in range(1, m-1):
            F[i,j] = D[i,j] + D[i,j-1] + D[i,j+1] + D[i-1,j] + D[i+1,j]
            G[i,j] = F[i,j] / 5.0
```
