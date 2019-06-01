# Intrepydd's built-in functions and libraries:#


### Built-in functions

Intrepydd v0.2 supports multiple built-in functions  and library
wrappers for
the convenience of the programmer

<---
:  abs, acos, add, all, allclose, any, argmax, argmin, arraysub, asin, atan, cos, div, elemwise_not, empty, eq, exp, float32, float64, ge, gt, innerprod, int32, int64, isinf, isnan, le, len, log, lt, max, min, minus, mul, multiply, neq, pow, print, prod, range, shape, sin, sqrt, sub, sum, tan, transpose, zeros.

Some of these built-in functions serve as wrappers for
standard native libraries.  All functions are supported at the -O2
optimization level, but not all
built-in functions are supported at the -O0 and -O1 levels.
-->

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


