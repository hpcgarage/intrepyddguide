The following sections show a set of program optimization techniques that
aim at the improvements of performance and energy while keeping
the underlying algorithms unchanged.
1. Loop invariant code motion
2. Dead code elimination (general case and sparse element-wise)
3. Loop fusion
4. Loop permutation
5. Parallelization

### 1. Loop invariant code motion

"Loop invariant code" is the code fragment that are enclosed one or
more loops and its computation results are the same across loop
iterations.  For instance:

```python
    for val in set:
        x1 = x0.abs().sqrt()
        x2 = add(x1, val)
```

The first statement in the loop computes element-wise abs and sqrt of
array `x0` and stores the results in array `x1`.  Here the values of
`x0` are unchanged across iterations, and hence the results stored in
`x1` are also same.  Such computations (i.e., loop invariant code) can
be moved out of the loop to reduce program execution time and energy.

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

Since the results of `x1 @ x1.T` (i.e., Symmetric Rank-k Update for `x1`)
are loop invariant, we can move out by using a temporal variable, e.g.:

```python
    tmp = x1 @ x1.T
    for val in set:
        x2 = add(x2, tmp)
```

### 2. Dead code elimination (general case and sparse element-wise)

### 3. Loop fusion

### 4. Loop permutation

### 5. Parallelization
