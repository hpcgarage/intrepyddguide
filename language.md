# Intrepydd v0.2 Language Summary 


### Overview

Intrepydd is a Python-based programming language developed in the
DARPA Software Defined Hardware (SDH) program to support writing
_data analytics kernels_ with the productivity of high-level Python
code and the
performance of low-level C/C++ code on current and future hardware
platforms.  This programming guide is focused on v0.2 of Intrepydd.

The primary goal of the Intrepydd v0.2
release is the development of kernels that  are amenable to
ahead-of-time compilation and can be called from a main
program written in Python.  As a result, Intrepydd v0.2 is not intended for
writing complete/main programs, and has a number
of limitations relative to standard Python as outlined below.  Some of
these limitations will be removed in future releases of Intrepydd.
However, all standard Python features can be used in the main program
that invokes Intrepydd kernels.

Intrepydd v0.2 only runs on
multicore CPU processors, though future versions of Intrepydd under
development also support execution on GPUs and simulators for future
hardware.  See the Getting Started page for details on how to get
started with system setup for programming in Intrepydd.


### Data Types

Intrepydd v0.2 supports three kinds of data types for
function parameters, function return values, and variables:
1. Primitive types: int32, int64, float32, float64.  These are fixed-precision numeric types.  Intrepydd v0.2 does not support Python’s multi-precision integers.
2. NumPy arrays of primitive types.  A NumPy array can be allocated in
  the Python main program and passed to an Intrepydd function without
  copying array data; it can also be allocated in Intrepydd code and
  returned to the Python main program without
  copying array data.
3. Lists of primitive types.  While lists in Intrepydd v0.2 bear
     some similarity to Python lists, there are many important
     differences.  Intrepydd v0.2 lists are homogeneous, i.e., all elements must
	 have same primitive data type.
	 
Cases 1. and 2. above represent Intrepydd data types that can be used in function
parameters and return values invoked from the Python main programs.
Case 3 represents local Intrepydd lists which can only be allocated and used
in Intrepydd code, and cannot
interoperate with Python lists.  Note that Intrepydd v0.2 does not
support dictionaries or user-defined objects.

Variable data types are inferred automatically, but in some cases an
explicit type declaration may be needed on assignment statements by
using Python's PEP 484 type annotation with the “# type: …” syntax.
Support for other type annotations, e.g., PEP 526, is deferred to
future versions of Intrepydd.

### Statements

Intrepydd v0.2 supports the following standard statement types from Python:
- Assignment statements.
- Return statements.
- Sequential for and while loops with break / continue statements.
- Conditional if / elif / else statements.
- Calls to user-defined and built-in
Intrepydd functions.  Note that objects and method calls are not supported in Intrepydd v0.2.

In addition, Intrepydd v0.2 supports a _parallel for_ (_pfor_) loop
statement, which is not available in Python.

### Expressions

Intrepydd v0.2 supports the following operators, which can be used to
write expressions:
- Unary operators.
- Binary operators.
- Array element operator, _A[i0, i1, ...]_, can be used to access an
   element of a NumPy array, _A_, both as an lval and as an rval.
- List constructors, e.g., [1, 2, 3].

### Optimization levels

To enable experimentation with different optimization levels, Intrepydd
v0.2 supports three optimization levels:
- Level 0 (pyddc -O0): At this level, the Intrepydd compiler generates pure
  Python code to facilitate debugging, since the combination of
  the Python main program code and Intrepydd-generated Python kernel
  code can be executed in a standard Python environment.
- Level 1 (pyddc -O1): At this level, the Intrepydd compiler generates
  Python code with annotations to make the code amenable to Numba JIT
  compilation. built-in functions
- Level 2 (pyddc -O2): At this level, the Intrepydd compiler generates
  C++ code which can be compiled to a static module that can be
  loaded by the Python main program.

Since Intrepydd is focused on high-performance code, the default
optimization level used by the pyddc compiler is -O2.

### Built-in functions

Intrepydd v0.2 supports multiple built-in functions  for
the convenience of the programmer:  abs, acos, add, all, allclose, any, argmax, argmin, arraysub, asin, atan, cos, div, elemwise_not, empty, eq, exp, float32, float64, ge, gt, innerprod, int32, int64, isinf, isnan, le, len, log, lt, max, min, minus, mul, multiply, neq, pow, print, prod, pydd_dsyrk, range, shape, sin, sqrt, sub, sum, tan, transpose, zeros.

Some of these built-in functions serve as wrappers for
standard native libraries.  All functions are supported at the -O2
optimization level, but not all
built-in functions are supported at the -O0 and -O1 levels.
