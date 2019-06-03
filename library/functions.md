# Intrepydd's built-in functions and libraries:

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
  - Note: only the first argument is supported and only printing primitive type is supported
- [range](https://docs.python.org/3/library/functions.html#func-range)
- [sum](https://docs.python.org/3/library/functions.html#sum)

### Subset of NumPy libraries

- [minus](https://docs.scipy.org/doc/numpy/reference/generated/numpy.negative.html)
- [mul](https://docs.scipy.org/doc/numpy/reference/generated/numpy.multiply.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [acos](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arccos.html)
  - Note: the first argument can be either an array or a scalar
- [add](https://docs.scipy.org/doc/numpy/reference/generated/numpy.add.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [allclose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html)
- [argmax](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html)
- [argmin](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmin.html)
- [asin](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arcsin.html)
  - Note: the first argument can be either an array or a scalar
- [atan](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan.html)
  - Note: the first argument can be either an array or a scalar
- [cos](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cos.html)
  - Note: the first argument can be either an array or a scalar
- [div](https://docs.scipy.org/doc/numpy/reference/generated/numpy.divide.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [elemwise_not](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logical_not.html)
- [empty](https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html)
  - Note: argument `order` is not supported. `dtype` is supported in another way.
  - Example: `empty([2,3], int32())`
- [eq](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_equal.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [exp](https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html)
  - Note: the first argument can be either an array or a scalar
- [float32](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - Convert a number to float32 type
- [float64](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - Convert a number to float64 type
- [ge](https://docs.scipy.org/doc/numpy/reference/generated/numpy.greater_equal.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [gt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.greater.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [innerprod](https://docs.s()https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.htmlcipy.org/doc/numpy/reference/generated/numpy.ma.innerproduct.html)
- [int32](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - Note: Convert a number to int32 type
- [int64](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)
  - Note: Convert a number to int64 type
- [isinf](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isinf.html)
  - Note: the first argument can be either an array or a scalar
- [isnan](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isnan.html)
  - Note: the first argument can be either an array or a scalar
- [lt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.less.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [le](https://docs.scipy.org/doc/numpy/reference/generated/numpy.less_equal.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [log](https://docs.scipy.org/doc/numpy/reference/generated/numpy.log.html)
  - Note: the first argument can be either an array or a scalar
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [tan](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tan.html)
  - Note: the first argument can be either an array or a scalar
- [transpose](https://docs.scipy.org/doc/numpy/reference/generated/numpy.transpose.html)
- [zeros](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html)
- [neq](https://docs.scipy.org/doc/numpy/reference/generated/numpy.not_equal.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [pow](https://docs.scipy.org/doc/numpy/reference/generated/numpy.pow.html)
  - The first argument can be either an array or a scalar
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar
- [prod](https://docs.scipy.org/doc/numpy/reference/generated/numpy.prod.html)
- [shape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html)
  - Note: is a function rather than an attribute. Example: `shape(arr, index)`
- [sin](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html)
  - Note: the first argument can be either an array or a scalar
- [sqrt](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sqrt.html)
  - Note: the first argument can be either an array or a scalar
- [sub](https://docs.scipy.org/doc/numpy/reference/generated/numpy.subtract.html)
  - Broadcasting is only supported if the first argument is an array and the scond argument is a scalar


### Subset of SciPy.sparse libraries

- empty_spm
- csr_to_spm
- spm_to_csr
- spm_set_item_unsafe
- spm_mul
- spmm
- spmv
- spmm_dense


TO BE COMPLETED

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
