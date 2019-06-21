The following sections show example code fragments for the common
Intrepydd programming idioms listed below.  Suggestions are most
welcome for additional examples to add to this list:

[1. Type declarations in function headers](1.-type-declarations-in-function-headers)

2. Array allocation
3. For loops
4. Dense array operations and reduction (can also be used for deep learning applications)
5. Sparse matrix operations (can also be used for graph processing applications)
6. Performance goal APIs

### 1. Type declarations in function headers
```python
def inc(x1: Array(int32,1), val: int32):
    '''
    Increment every element in 1-D array `x1` by `val`.
    '''
```
```python	
def sum_up(x2: Array(float64,2)) -> float64:
    '''
    Add up all elements in 2-D array `x2` and return their sum.
    The array bounds can also be accessed as x2.shape(0) and x2.shape(1).
    Individual array elements can be accessed as xs[i,j].
    '''	
```

### 2. Array allocation 
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

### 3. For loops
```python
    for elem in x1:
        . . .
    '''
    Iterate through all elements of 1-D array x1.
    Currently, element iteration is not supported for multidimensional arrays.
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

### 4. Dense array operations and reduction (can also be used for deep learning applications)
```python
    y = sqrt(abs(x))

    z = x.abs().sqrt()
    '''
    Element-wise abs is first applied to multi-dimensional array x, and then
    element-wise sqrt is applied to the abs result (both lines are equivalent).
    '''
```
```python
    delta1 = sum(sub(y, z))

    delta2 = sub(y, z).sum()
    '''
    Element-wise sub is first applied to multi-dimensional arrays y and z, and then
    the total sum of the sub result is computed (both lines are equivalent).
    '''
```
```python
def my_func(x1: Array(float64,1), x2: Array(float64,2)):

    y1 = x1 @ x2    # Equivalent to 'y1 = matmult(x1, x2)'

    y1 = x2 @ y1    # Equivalent to 'y1 = matmult(x2, y1)'

    y2 = x2 @ x2.T  # Equivalent to 'y2 = matmult(x2, transpose(x2))'
    '''
    1st line: vector-matrix multiplication to result in vector (1-D array).
    2nd line: matrix-vector multiplication to result in vector (1-D array).
    3rd line: matrix-matrix multiplication to result in matrix (2-D array), where 2nd argument is transpose of x2 (i.e., Symmetric Rank-k Update).
    '''
```

### 5. Sparse matrix operations (can also be used for graph processing applications)
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
    s4 = spmm(s1, s2)
    '''
    Sparse matrix matrix multiplication with two sparse matrices s1 and s2,
    and return the result as a sparse matrix s4 (error if s1's # columns != s2's # rows).
    '''
```
```python
    x2 = spmm_dense(s1, x)
    '''
    Sparse matrix matrix multiplication with one sparse matrix s1 and dense array s2,
    and return the result as a dense array x2 (error if s1's # columns != s2's # rows).
    '''
```

### 6. Performance Goal APIs
```python
import perf_api

perf_api.init_metric()  # Once at very beginning

perf_api.start_metric() # Every time at start of a kernel
r = matopt.inner_product(v1, v2)
perf_api.stop_metric()  # Every time at end of a kernel

perf_api.print_metric() # Once at very end
```
