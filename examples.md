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
def sum(x2: Array(float32,2)) -> float64:
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
    Can also use zeros([m], int32())
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
    Allocate a copy of array x2 in array y.  Intrepydd v0.2 does not support x2.copy(), so this is an alternate way of creating a copy.
    '''
```

### For loops
```python
    for elem in x2:
        . . .
    '''
    Iterate through all elements of 2-D array x2
    '''
```python
    for i in range(shape(x2,0)):
        for j in range(shape(x2,1)):
            elem = x2[i,j]
            . . .
    '''
    Iterate through all elements of 2-D array x2 using explicit subscripts
    '''
```
```python
    for i in range(index[src], index[src+1]):
             . . .
    '''
    Iterate through all values of i such that index[src] <= i < index[src+1]
    '''
```

### Sparse matrix operations
```python
    s1 = empty_spm(n, n, float64())
    s1.spm_set_item_unsafe(1.0, i, j)
    '''
    Create an empty sparse matrix with n*n elements of type float64, and set element i,j to 1.0
    '''
```
```python
    s2 = csr_to_spm(vals, cols, idxs, ncols)
    '''
    Create a sparse matrix (spm) from the three components of a CSR representation
    '''
```
