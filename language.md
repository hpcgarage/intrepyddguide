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
1. _Primitive types:_ int32, int64, float32, float64.  These are
   fixed-precision numeric types.  Intrepydd v0.2 does not support
   Python’s multi-precision integers.  Primitive types can be passed
   to an Intrepydd function from a Python program, and also returned
   to a Python program from an Intrepydd function.
2. _Dense arrays of primitive types_, which correspond to [NumPy arrays](https://www.numpy.org/devdocs/user/basics.creation.html).  A NumPy array can be allocated in
  the Python main program and passed to an Intrepydd function without
  copying array data.  It can also be allocated in Intrepydd code and
  returned to the Python main program without
  copying array data.
3. _Lists of primitive types:_  While lists in Intrepydd v0.2 bear
     some similarity to Python lists, there are many important
     differences.  Intrepydd v0.2 lists are homogeneous, i.e., all elements must
	 have same primitive data type.  Also, local Intrepydd lists which can only be allocated and used
in Intrepydd code, and cannot
interoperate (as paratmenters or return values) with Python lists


The three Intrepydd data types listed above are inferred automatically for
local variables and expressions, based on the type declarations
provided for parameters and
return values.   In some cases,
explicit type declarations may be needed for assignment statements by
using Python's PEP 484 type annotation with the “# type: …” syntax.
Support for other type annotations, e.g., PEP 526, is deferred to
future versions of Intrepydd
	 

There is a fourth case data type that can be  used in Intrepydd code to enable 
support for sparse matrix computations via wrappers for a subset of [scipy.sparse](https://docs.scipy.org/doc/scipy/reference/sparse.html)
library calls:
- Sparse arrays of primitive types, which correspond to 
  arrays.
Values of this type can only be used as parameters and
  return values in a subset of _scipy.sparse_ API calls in Intrepydd code.  Like Intrepydd lists, these sparse arrays cannot currently be passed to, or from, Intrepydd
  code or to Python code.  For convenience, we support a virtual
  method call syntax of the form a.foo() for calls to _scipy.sparse_ APIs, 
but general objects and method calls are not supported for other data
  types in Intrepydd v0.2.

### Statements

Intrepydd v0.2 supports the following standard statement types from Python:
- [Assignment statements](https://docs.python.org/2.0/ref/assignment.html).
- [Return statements](https://docs.python.org/2.0/ref/return.html).
- Sequential [for](https://docs.python.org/3/tutorial/controlflow.html#for-statements) and [while](https://docs.python.org/3/reference/compound_stmts.html#while) loops with [break](https://docs.python.org/3/reference/simple_stmts.html?highlight=break#grammar-token-break-stmt) / [continue](https://docs.python.org/3/reference/simple_stmts.html?highlight=break#the-continue-statement) statements.
- Conditional [if / elif / else](https://docs.python.org/3/reference/compound_stmts.html?highlight=elif#if) statements.
- Calls to user-defined and [built-in](library/functions.md) Intrepydd functions. 

In addition, Intrepydd v0.2 supports a _parallel for_ (_pfor_) loop
statement, which is not available in Python.  A simple example is as
follows:

```python
# Double each element of array A
pfor i in range(A.shape[0]):
  temp = 2*A[i]
  A[i] = temp
  ```

As can be seen from the simple example, sequential for loops that are
eligible for parallelization can be converted to parallel loops in
Intrepydd by replacing "for" by "pfor".  The main conditions for a
loop to be eligible for parallelization are:
1. The loop should have no cross-iteration dependences on array variables.  For example,
if "2*A[i]" in the above loop  is replaced by "2*A[i-1]", the loop
will no longer be eligible for parallelization since there can be a
race condition between (say) the write of A[0] in iteration i=0 and 
the read of A[0] in iteration i=1.  It is the user's responsibility to
check this condition.
2. The loop should have no read-after-write (flow) cross-iteration
dependences on scalar variables.  Note that that the above example has no cross-iteration
dependences on scalar variable, temp, since the value of temp is
written and read in the same iteration.  This condition will be checked by
the compiler.

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
