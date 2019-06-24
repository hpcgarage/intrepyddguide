# Intrepydd's built-in functions and libraries

Intrepydd v0.2 supports the following classes of multiple built-in functions  and library
wrappers for
the convenience of the programmer. Recall that all standard Python
functions and libraries can be used in the Python main program that
invokes Intrepydd functions.

### Subset of Python built-in functions

Intrepydd supports the following subset of [Python built-in functions](https://docs.python.org/3/library/functions.html#built-in-functions):
- [abs](https://docs.python.org/3/library/functions.html#abs)
- [all](https://docs.python.org/3/library/functions.html#all)
- [any](https://docs.python.org/3/library/functions.html#any)  
- [len](https://docs.python.org/3/library/functions.html#len)
- [max](https://docs.python.org/3/library/functions.html#max)
- [min](https://docs.python.org/3/library/functions.html#min)
- [pow](https://docs.python.org/3/library/functions.html#pow)
  - Note: the last argument `z` is not supported
- [print](https://docs.python.org/3/library/functions.html#print)
  - Note: only the first argument is supported, and only printing
    primitive type is supported.  General calls to print can be
    performed in the Python main program that invokes the Intrepydd code.
- [range](https://docs.python.org/3/library/functions.html#func-range)
- [sum](https://docs.python.org/3/library/functions.html#sum)

### Subset of NumPy libraries

Intrepydd supports the following subset of NumPy libraries. Each function name points to the Numpy reference page for the function, and can have some bullets to note its prototype in Intrepydd and other differences from the Numpy version. `T`, `T1` etc stand for either `int32`, `int64`, `float32`, `float64` in function prototype.
- [acos](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arccos.html)
  - Note: the first argument can be either an array or a scalar
- [add](https://docs.scipy.org/doc/numpy/reference/generated/numpy.add.html)
  - `(Array<T1> x1, T2 x2) -> Array<double>`
  - `(T1 x1, Array<T2> x2) -> Array<double>`
  - `(Array<T1> x1, Array<T2> x2) -> Array<double>`
  - `(Array<T> x1, Array<T> x2) -> Array<T>`
  
- [allclose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)
  - `(Array<T>, T atol) -> bool`
- [argmin](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmin.html)
  - `(Array<T> a) -> List<int>`
- [argmax](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html)
  - `(Array<T> a) -> List<int>`

- [asin](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arcsin.html)
  - Note: the first argument can be either an array or a scalar
- [atan](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan.html)
  - Note: the first argument can be either an array or a scalar
- [cos](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cos.html)
  - Note: the first argument can be either an array or a scalar
- [div](https://docs.scipy.org/doc/numpy/reference/generated/numpy.divide.html)
- [elemwise_not](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logical_not.html)
- [empty](https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html)
  - Note: argument `order` is not supported. `dtype` is supported in another way.
  - Example: `empty([2,3], int32())`
- [eq](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_equal.html)
- [exp](https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html)
  - Note: the first argument can be either an array or a scalar
- [float32](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - Convert a number to float32 type
- [float64](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - Convert a number to float64 type
- [ge](https://docs.scipy.org/doc/numpy/reference/generated/numpy.greater_equal.html)
- [gt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.greater.html)
- [innerprod](https://docs.s()https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.htmlcipy.org/doc/numpy/reference/generated/numpy.ma.innerproduct.html)
- [int32](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - Note: Convert a number to int32 type
- [int64](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - Note: Convert a number to int64 type
- [isinf](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isinf.html)
  - Note: the first argument can be either an array or a scalar
- [isnan](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isnan.html)
  - Note: the first argument can be either an array or a scalar
- [le](https://docs.scipy.org/doc/numpy/reference/generated/numpy.less_equal.html)
- [log](https://docs.scipy.org/doc/numpy/reference/generated/numpy.log.html)
  - Note: the first argument can be either an array or a scalar
- [lt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.less.html)
- [minus](https://docs.scipy.org/doc/numpy/reference/generated/numpy.negative.html)
- [mul](https://docs.scipy.org/doc/numpy/reference/generated/numpy.multiply.html)
  - `(Array<T1> x1, T2 x2) -> Array<double>`
  - `(T1 x1, Array<T2> x2) -> Array<double>`
  - `(Array<T1> x1, Array<T2> x2) -> Array<double>`
  - `(Array<T> x1, Array<T> x2) -> Array<T>`
- [neq](https://docs.scipy.org/doc/numpy/reference/generated/numpy.not_equal.html)
- [pow](https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html)
  - The first argument can be either an array or a scalar
- [prod](https://docs.scipy.org/doc/numpy/reference/generated/numpy.prod.html)
- [shape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html)
  - Note: is a function rather than an attribute. Example: `shape(arr, index)`
- [sin](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html)
  - Note: the first argument can be either an array or a scalar
- [sqrt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sqrt.html)
  - Note: the first argument can be either an array or a scalar
- [sub](https://docs.scipy.org/doc/numpy/reference/generated/numpy.subtract.html)
  - `(Array<T1> x1, T2 x2) -> Array<double>`
  - `(T1 x1, Array<T2> x2) -> Array<double>`
  - `(Array<T1> x1, Array<T2> x2) -> Array<double>`
  - `(Array<T> x1, Array<T> x2) -> Array<T>`

- [tan](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tan.html)
  - Note: the first argument can be either an array or a scalar
- [transpose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.transpose.html)
- [zeros](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html)
- [@](https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html)
  - Syntax sugar for matrix matrix multiplication
  - Equivalent function is `matmult`

### Subset of CombBLAS libraries

Intrepydd supports the following subset of CombBLAS libraries.
Currently only float64 type is supported for the data type of sparse array.
- [csr_to_spm(arr_values: Array(float64), arr_columns: Array(int32), arr_indexes: Array(int32), nc: int32)](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/classcombblas_1_1_sp_mat.html#a3fe039448e6e15c8949f066eea204efa)
  - Construct and return a sparse matrix from three 1-D arrays and a scalar --- arr_values,
    arr_columns, arr_indexes, and nc (number of columns) --- with the values corresponding
    to a CSR representation of spm.
- [empty_spm(nr: int32, nc: int32)](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/classcombblas_1_1_sp_mat.html#aec83f0568245560ac797cbf181c47051)
  - Construct and return an empty sparse matrix with nr rows and nc columns.
- [spmm(spm1, spm2)](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/classcombblas_1_1_sp_mat.html#a981ab02ac32e92fcf6bbc193bfdf3bd5)
  - Return the matrix product of sparse matrices spm1 and spm2 as a sparse matrix.
- [spmm_dense(spm1 [/ arr1], spm2 [/ arr2])](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/classcombblas_1_1_sp_mat.html#a981ab02ac32e92fcf6bbc193bfdf3bd5)
  - Return the matrix product of sparse matrices spm1 and spm2 a dense matrix.
  - Note: either of frst or second argument can be dense 2-D matrix (Array(float64)).
- [spm_add(spm1, spm2 [/ arr2])](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/namespacecombblas.html#a17148c59f16d4908b17b807a959abcc5)
  - Return the element-wise sum of sparse matrices spm1 and spm2 as a sparse matrix.
  - Note: the second argument can be dense 2-D matrix (Array(float64)).
- [spm_mul(spm1, spm2 [/ arr2])](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/namespacecombblas.html#a1fca28136b736b66fea4f09e01b199c5)
  - Return the element-wise product of sparse matrices spm1 and spm2 as a sparse matrix.
  - Note: the second argument can be dense 2-D matrix (Array(float64)).
- spm_set_item(spm, v: float64, r: int32, c: int32) 
  - Set item [r,c] of sparse matrix spm to v.
    If item [r,c] already had a nonzero entry in spm, its value is overwritten with v.
- spm_set_item_unsafe(spm, v: float64, r: int32, c: int32)
  - Set item [r,c] of sparse matrix spm to v, and assumes without checking that item [r,c]
    does not have a nonzero entry in spm.
- spm_to_csr(spm, arr_values: Array(float64), arr_columns: Array(int32), arr_indexes: Array(int32))
  - Takes sparse matrix spm as input, and fills in three 1-D arrays --- arr_values,
    arr_columns, arr_indexes --- with the values corresponding to a CSR representation of spm.
- [spmv(spm, arr: Array(float64))](https://people.eecs.berkeley.edu/~aydin/CombBLAS/html/namespacecombblas.html#af6d7c2a1ec21df8ebdd4cff3eb728fc7)
  - Returns the product of sparse matrix spm and dense vector arr as a new dense vector.

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
