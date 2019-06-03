# Intrepydd's built-in functions and libraries:



Intrepydd v0.2 supports the following classes of multiple built-in functions  and library
wrappers for
the convenience of the programmer.  Recall that all standard Python
functions and libraries can be used in the Python main program that
invokes Intrepydd functions.

### Subset of Python built-in functions

Intrepydd supports the following subset of [Python built-in functions](https://docs.python.org/3/library/functions.html#built-in-functions):
abs, all, any, len, max, min, minus, mul, multiply, pow, print, range, sum.

### Subset of NumPy libraries

acos, add, allclose, argmax, argmin, arraysub, asin, atan, cos, div,
elemwise_not, empty, eq, exp, float32, float64, ge, gt, innerprod,
int32, int64, isinf, isnan, le, log, lt, isinf, isnan, le, len, , tan, transpose, zeros.
log, lt, neq, prod, shape, sin, sqrt, sub, 

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
