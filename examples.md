The following sections show example code fragments for common
Intrepydd programming idioms.

### Type declarations in function headers
```python
def inc(x1: Array(int32,1), val: int32):
    '''
    Increment every element in 1-D array `x1` by `val`.
    '''
```
```python	
def sum_up(x2: Array(float32,2)) -> float64:
    '''
    Add up all elements in 2-D array `x2` and return their sum.
    The array bounds can also be accessed as x2.shape(0) and x2.shape(1).
    Individual array elements can be accessed as xs[i,j].
    '''	
```

### Array allocation 
```python
    x1 = empty(m, int32())
    '''
    Allocate a 1-D array of int32 with m elements that are uninitialized.
    Can also use zeros([m], int32()).
    '''
```
```python
    x2 = zeros([m,n], float64())
    '''
    Allocate a 2-D array of float64 with m*n elements initialized to zero.
    '''
```
```python
    y = add(x2, 0.0)
    '''
    Allocate a copy of array x2 in array y.
    Intrepydd v0.2 does not support x2.copy(), so this is an alternate way of creating a copy.
    '''
```

### For loops
```python
    for elem in x2:
        . . .
    '''
    Iterate through all elements of 2-D array x2.
    '''
```
```python
    for i in range(shape(x2,0)):
        for j in range(shape(x2,1)):
            elem = x2[i,j]
            . . .
    '''
    Iterate through all elements of 2-D array x2 using explicit subscripts.
    '''
```
```python
    for i in range(index[src], index[src+1]):
             . . .
    '''
    Iterate through all values of i such that index[src] <= i < index[src+1].
    '''
```

### Dense array operations and reduction
```python
    y2a = sqrt(abs(x2))

    y2b = x2.abs().sqrt()
    '''
    Element-wise abs is first applied to multi-dimensional array x2, and then
    element-wise sqrt is applied to the abs result (both computations are equivalent).
    '''
```
```python
    deltaa = sum(sub(y2a, y2b))

    deltab = sub(y2a, y2b).sum()
    '''
    Element-wise sub is first applied to multi-dimensional arrays y2a and y2b, and then
    the total sum of the sub result is computed (both computations are equivalent).
    '''
```

### Sparse matrix operations
```python
    s1 = csr_to_spm(vals, cols, idxs, ncols)
    '''
    Create a sparse matrix (spm) from the three components of a CSR representation.
    '''
```
```python
    s2 = empty_spm(nrows, ncols)
    for i in range(nrows):
        for j in range(ncols):
            if (x[i,j] != 0.0):
                s2.spm_set_item_unsafe(x[i,j], i, j)
    '''
    Create an empty sparse matrix with nrows*ncols elements, and set element i,j to x[i,j],
    i.e., convert dense array x into sparse format.
    '''
```
```python
    s3a = spm_mul(s1, s2)
    '''
    Element-wise sparse product with two sparse matrices s1 and s2.
    '''
```
```python
    s3b = spm_mul(s1, x)
    '''
    Element-wise sparse product with one sparse matrix s1 and dense array x.
    '''
```
```python
    s4a = spmm(s1, s2)
    '''
    Sparse matrix matrix multiplication with two sparse matrices s1 and s2,
    and return the result as a sparse matrix s4a (assume s1's # columns == s2's # rows).
    '''
```
```python
    x2 = spmm_dense(s1, x)
    '''
    Sparse matrix matrix multiplication with one sparse matrix s1 and dense array s2,
    and return the result as a dense array x2 (assume s1's # columns == s2's # rows).
    '''
```
