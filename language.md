# Intrepydd v0.2 Language Summary 


### Overview

The primary goal of the Intrepydd v0.2
release is the development of kernels that  are amenable to
ahead-of-time compilation and can be called from a main
program written in Python.  As a result, Intrepydd v0.2 is not intended for
writing complete/main programs, and has a number
of limitations relative to standard Python as summarized below.  Many of
these limitations will be removed in future releases of Intrepydd.
However, all standard Python features can be used in the main program
that invokes Intrepydd kernels.

This page summarizes the language features  available in
Intrepydd v0.2, which only runs on
multicore CPU processors; later versions of Intrepydd under
development support execution on GPUs and simulators for future
hardware.

See the links at the bottom of the [Intrepydd README page](README.md) for
additional information, including built-in functions and libraries,
Jupyter-based tutorials and the Getting Started page with details on system setup for programming in Intrepydd.


### Data Types

Intrepydd v0.2 requires that _each Intrepydd function parameter and
return value be declared with one of the following data types:_
1. _Primitive types:_ int32, int64, float32, float64.  These are fixed-precision numeric types.  Intrepydd v0.2 does not support Python’s multi-precision integers.
2. _Dense arrays of primitive types_, which correspond to NumPy
  arrays:  A NumPy array can be allocated in
  the Python main program and passed to an Intrepydd function without
  copying array data; it can also be allocated in Intrepydd code and
  returned to the Python main program without
  copying array data.
3. _Lists of primitive types:_  While lists in Intrepydd v0.2 bear
     some similarity to Python lists, there are many important
     differences.  Intrepydd v0.2 lists are homogeneous, i.e., all elements must
	 have same primitive data type.


Cases 1. and 2. above NumPy represent Intrepydd data types that can be used in function
parameters and return values within an Intrepydd file and also across
the Python main program.
Case 3 represents local Intrepydd lists which can only be allocated and used
in Intrepydd code, and cannot
interoperate with Python lists.  (Note that Intrepydd v0.2 does not
support dictionaries.)

Variable data types are inferred automatically from parameters and
return values, but in some cases
explicit type declarations may be needed on assignment statements by
using Python's PEP 484 type annotation with the “# type: …” syntax.
Support for other type annotations, e.g., PEP 526, is deferred to
future versions of Intrepydd
	 

There is a fourth case of data types used in Intrepydd to enable 
support for sparse matrix computations via wrappers for _scipy.sparse_
library calls:
4. Sparse arrays of primitive types, which correspond to 
  arrays.
However, these sparse arrays cannot currently be passed to, or from, Intrepydd
  code or to Python code



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
create expressions:
- Unary operators.
- Binary operators.
- Array element operator, _A[i0, i1, ...]_, can be used to access an
   element of a NumPy array, _A_, both as an lval and as an rval.
- List constructors, e.g., [1, 2, 3].

<!---
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
-->
