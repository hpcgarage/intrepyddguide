# Intrepydd's built-in functions and libraries

Intrepydd v0.2 supports the following classes of  built-in functions  and library
wrappers for
the convenience of the programmer.  When an entry below corresponds to
a 
standard Python function or library, we include a link to the Python
documentation and also summarize limitations in the Intrepydd version
relative to the Python version.  We also use Intrepydd-style type
declarations for function prototypes to summarize the acceptable
parameters and types.  For convenience, we use `T`, `T1`, `T2`, etc. as
type parameters below to represent any Intrepydd numeric type: `int32`, `int64`, `float32`, or `float64`, and use `BT`, `BT1`, `BT2` etc. as
type parameters to represent any numeric type or `bool`.

Finally, note that all standard Python
functions and libraries can be used without limitations in the Python main program that
invokes Intrepydd functions.

### Subset of Python built-in functions

Intrepydd supports the following subset of [Python built-in functions](https://docs.python.org/3/library/functions.html#built-in-functions):
- [abs](https://docs.python.org/3/library/functions.html#abs)
  - `(x: T1) -> T1`
- [all](https://docs.python.org/3/library/functions.html#all)
  - `(iterable: Array(BT)) -> bool`
  - `(iterable: List(BT)) -> bool`
- [any](https://docs.python.org/3/library/functions.html#any)
  - `(iterable: Array(BT)) -> bool`
  - `(iterable: List(BT)) -> bool`
- [len](https://docs.python.org/3/library/functions.html#len)
  - `(s: Array(BT)) -> int64`
  - `(s: List(BT)) -> int64`
- [max](https://docs.python.org/3/library/functions.html#max)
  - `(arr: Array(T)) -> T`
- [min](https://docs.python.org/3/library/functions.html#min)
  - `(arr: Array(T)) -> T`
- [pow](https://docs.python.org/3/library/functions.html#pow)
  - `(base: float64, exp: float64) -> float64`
  - Note: the last argument `z` is not supported
- [print](https://docs.python.org/3/library/functions.html#print)
  - `(v: BT)`
  - `(ls: List(BT))`
  - Note: only the first argument is supported, and only printing
    primitive type is supported.  General calls to print can be
    performed in the Python main program that invokes the Intrepydd code.
- [range](https://docs.python.org/3/library/functions.html#func-range)
  - `(len: int64) -> List(int)`
  - Note: When used together with `for ... in`, the prototype is `(start: int64, stop: int64, step: int64) -> List(int)`
- [sum](https://docs.python.org/3/library/functions.html#sum)
  - `(arr: Array(T)) -> T`

### Subset of NumPy libraries

Intrepydd supports the following subset of NumPy libraries. Each function name points to the Numpy reference page for the function, and can have some bullets to note its prototype in Intrepydd (often only supports a subset of parameters) and other differences from the Numpy version. 
- [acos](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arccos.html)
  - `(arr: Array(T)) -> Array(double)`
  - `(val: T) -> double`
- [add](https://docs.scipy.org/doc/numpy/reference/generated/numpy.add.html)
  - `(x1: Array(T1), x2: T2) -> Array(double)`
  - `(x1: T1, x2: Array(T2)) -> Array(double)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(double)`
  - `(x1: Array(T), x2: Array(T)) -> Array(T)`
- [allclose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)
  - `(arr: Array(T), eps: T) -> bool`
- [asin](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arcsin.html)
  - `(arr: Array(T)) -> Array(double)`
  - `(val: T) -> double`
- [atan](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan.html)
  - `(arr: Array(T)) -> Array(double)`
  - `(val: T) -> double`
- [cos](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cos.html)
  - `(arr: Array(T)) -> Array(double)`
  - `(val: T) -> double`
- [div](https://docs.scipy.org/doc/numpy/reference/generated/numpy.divide.html)
  - `(x1: Array(T1), x2: T2) -> Array(double)`
  - `(x1: T1, x2: Array(T2)) -> Array(double)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(double)`
- [elemwise_not](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logical_not.html)
  - `(arr: Array(T)) -> Array(bool)`
- [empty](https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html)
  - `(shape: List(int32), dtype: T) -> Array()`
  - `(shape: List(int64), dtype: T) -> Array()`
  - `(shape: int64, dtype: T) -> Array()`
  - Note: argument `order` is not supported. `dtype` is supported by specifying a number of desired type.
  - Example: `empty([2,3], int32())`
- [eq](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_equal.html)
  - `(x1: Array(BT1), x2: BT2) -> Array(bool)`
  - `(x1: BT1, x2: Array(BT2)) -> Array(bool)`
  - `(x1: Array(BT1), x2: Array(BT2)) -> Array(bool)`
- [exp](https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html)
  - `(arr: Array(T)) -> Array(double)`
  - `(val: T) -> double`
  - Note: the first argument can be either an array or a scalar
- [float32](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - `() -> float32`
  - `(x: T) -> float32`
  - Convert a number to float32 type 
- [float64](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - `() -> float64`
  - `(x: T) -> float64`  
  - Convert a number to float64 type 
- [ge](https://docs.scipy.org/doc/numpy/reference/generated/numpy.greater_equal.html)
  - `(x1: Array(T1), x2: T2) -> Array(bool)`
  - `(x1: T1, x2: Array(T2)) -> Array(bool)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(bool)`
- [gt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.greater.html)
  - `(x1: Array(T1), x2: T2) -> Array(bool)`
  - `(x1: T1, x2: Array(T2)) -> Array(bool)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(bool)`
- [innerprod](https://docs.s()https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.htmlcipy.org/doc/numpy/reference/generated/numpy.ma.innerproduct.html)
  - `(arr1: Array(T1), arr2: Array(T2)) -> double`
- [int32](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - `() -> int32`
  - `(x: T) -> int32`  
  - Convert a number to int32 type 
- [int64](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - `() -> int64`
  - `(x: T) -> int64`  
  - Convert a number to int64 type 
- [isinf](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isinf.html)
  - `(arr: Array(T)) -> Array(bool)`
  - `(val: T) -> bool`
- [isnan](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isnan.html)
  - `(arr: Array(T)) -> Array(bool)`
  - `(val: T) -> bool`
- [le](https://docs.scipy.org/doc/numpy/reference/generated/numpy.less_equal.html)
  - `(x1: Array(T1), x2: T2) -> Array(bool)`
  - `(x1: T1, x2: Array(T2)) -> Array(bool)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(bool)`
- [log](https://docs.scipy.org/doc/numpy/reference/generated/numpy.log.html)
  - `(x1: Array(T1), x2: T2) -> Array(double)`
  - `(x1: T1, x2: Array(T2)) -> Array(double)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(double)`
  - `(x1: T1, x2: T2) -> double`
- [lt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.less.html)
  - `(x1: Array(T1), x2: T2) -> Array(bool)`
  - `(x1: T1, x2: Array(T2)) -> Array(bool)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(bool)`
- [minus](https://docs.scipy.org/doc/numpy/reference/generated/numpy.negative.html)
  - `(arr: Array(T)) -> Array(T)`
- [mul](https://docs.scipy.org/doc/numpy/reference/generated/numpy.multiply.html)
  - `(x1: Array(T1), x2: T2) -> Array(double)`
  - `(x1: T1, x2: Array(T2)) -> Array(double)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(double)`
  - `(x1: Array(T), x2: Array(T)) -> Array(T)`
- [neq](https://docs.scipy.org/doc/numpy/reference/generated/numpy.not_equal.html)
  - `(x1: Array(BT1), x2: BT2) -> Array(bool)`
  - `(x1: BT1, x2: Array(BT2)) -> Array(bool)`
  - `(x1: Array(BT1), x2: Array(BT2)) -> Array(bool)`
- [pow](https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html)
  - `(x1: Array(T1), x2: T2) -> Array(double)`
  - `(x1: T1, x2: Array(T2)) -> Array(double)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(double)`
  - `(x1: T1, x2: T2) -> double`
  - The first argument can be either an array or a scalar
- [prod](https://docs.scipy.org/doc/numpy/reference/generated/numpy.prod.html)
  - `(arr: Array(T)) -> T`
- [shape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html)
  - `(arr: Array(BT), i: int) -> int`
  - Note: is a function rather than an attribute. Example: `shape(arr, index)`
- [sin](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html)
  - `(arr: Array(T)) -> Array(double)`
  - `(val: T) -> double`
- [sqrt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sqrt.html)
  - `(arr: Array(T)) -> Array(double)`
  - `(var: T) -> double`
- [sub](https://docs.scipy.org/doc/numpy/reference/generated/numpy.subtract.html)
  - `(x1: Array(T1), x2: T2) -> Array(double)`
  - `(x1: T1, x2: Array(T2)) -> Array(double)`
  - `(x1: Array(T1), x2: Array(T2)) -> Array(double)`
  - `(x1: Array(T), x2: Array(T)) -> Array(T)`
- [tan](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tan.html)
  - `(arr: Array(T)) -> Array(double)`
  - `(val: T) -> double`
- [transpose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.transpose.html)
  - `(arr: Array(T)) -> Array(T)`
- [zeros](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html)
  - `(shape: List(int32), dtype: BT) -> Array()`
  - `(shape: List(int64), dtype: BT) -> Array()`
  - `(shape: int64, dtype: BT) -> Array()`
  - Note: argument `order` is not supported. `dtype` is supported by specifying a number of desired type.
  - Example: `zeros([2,3], int32())`
- [@](https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html)
  - Convenient syntax for matrix-matrix multiplication (equivalent to `matmult`)

### Subset of CombBLAS libraries

Intrepydd supports the following subset of CombBLAS libraries for
sparse matrices.
Currently, only  `float64` is supported as an element type for sparse
matrices in Intrepydd.

- [csr_to_spm](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/classcombblas_1_1_sp_mat.html#a3fe039448e6e15c8949f066eea204efa)
  - `(values: Array(float64), columns: Array(int32), indexes: Array(int32), nc: int32) -> SparseMat(float64)`
  - Construct and return a sparse matrix from three 1-D arrays and a scalar --- `values`,
    `columns`, `indexes`, and `nc` (number of columns) --- with the values corresponding
    to a CSR representation of spm.
- [empty_spm](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/classcombblas_1_1_sp_mat.html#aec83f0568245560ac797cbf181c47051)
  - `(nr: int32, nc: int32) -> SparseMat(float64)`
  - Construct and return an empty sparse matrix with `nr` rows and `nc` columns.
- [spmm](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/classcombblas_1_1_sp_mat.html#a981ab02ac32e92fcf6bbc193bfdf3bd5)
  - `(spm1, spm2) -> SparseMat(float64)`
  - Return the matrix product of sparse matrices `spm1` and `spm2` as a sparse matrix.
- [spmm_dense](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/classcombblas_1_1_sp_mat.html#a981ab02ac32e92fcf6bbc193bfdf3bd5)
  - `(spm1, spm2) -> Array(float64)`
  - `(spm, arr) -> Array(float64)`
  - `(arr, spm) -> Array(float64)`
  - Return the matrix product of sparse matrices `spm1` and `spm2` as a dense matrix.
    - Also accepts a dense matrix as the first or second argument
- [spm_add](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/namespacecombblas.html#a17148c59f16d4908b17b807a959abcc5)
  - `(spm1, spm2) -> SparseMat(float64)`
  - `(spm, arr) -> SparseMat(float64)`
  - Return the element-wise sum of sparse matrices `spm1` and `spm2` as a sparse matrix.
    - The second argument can be a dense matrix.
- [spm_mul](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/namespacecombblas.html#a1fca28136b736b66fea4f09e01b199c5)
  - `(spm1, spm2) -> SparseMat(float64)`
  - `(spm, arr) -> SparseMat(float64)`
  - Return the element-wise product of sparse matrices `spm1` and `spm2` as a sparse matrix.
    - The second argument can be a dense matrix.
- spm_set_item
  - `(spm, v: float64, r: int32, c: int32)`
  - Set item `[r,c]` of sparse matrix `spm` to `v`.
    If item `[r,c]` already had a nonzero entry in `spm`, its value is overwritten with `v`.
- spm_set_item_unsafe
  - `(spm, v: float64, r: int32, c: int32)`
  - Set item `[r,c]` of sparse matrix `spm` to `v`; assume without checking that item `[r,c]`
    does not already have a nonzero entry in `spm`.
- spm_to_csr
  - `(spm, values: Array(float64), columns: Array(int32), indexes: Array(int32))`
  - Takes sparse matrix spm as input, and fills in three 1-D arrays --- values,
    columns, indexes --- with the values corresponding to a CSR representation of spm.
- [spmv](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/namespacecombblas.html#af6d7c2a1ec21df8ebdd4cff3eb728fc7)
  - `(spm, arr) -> Array(float64)`
  - Returns the product of sparse matrix `spm` and dense vector `arr` as a new dense vector.

Note that the data types of arguments `spm`, `spm1`, and `spm2` are
`SparseMat(float64)` while the data type of `arr` is `Array(float64)`.

<!---
### API Wrappers 
The built-in functions are listed here in alphabetical order.

**abs**(x)
- Return the absolute value of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.

**all**(iterable)
- Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:

  ```python
  def all(iterable):
      for element in iterable:
          if not element:
              return False
      return True
  ```
  
**any**(iterable)
- Return True if any element of the iterable is true. If the iterable is empty, return False. Equivalent to:

  ```python
  def any(iterable):
      for element in iterable:
          if element:
              return True
      return False
  ```
**len**(s)
- Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).

**pow**(x, y) 
- Return x to the power y; Equivalent to using the power operator: x**y.

- The arguments must have numeric types. With mixed operand types, the coercion rules for binary arithmetic operators apply. For int operands, the result has the same type as the operands (after coercion) unless the second argument is negative; in that case, all arguments are converted to float and a float result is delivered. For example, `10**2` returns 100, but `10**-2` returns 0.01. 

--->

<!---
   - Broadcasting is only supported if the first argument is an array and the second argument is a scalar
--->
