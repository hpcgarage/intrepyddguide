# Intrepydd v0.2 Language Summary #


### Overview

Intrepydd is a Python-based programming language developed in the
DARPA Software Defined Hardware (SDH) program to support writing
_data analytics kernels_ with the productivity of high-level Python
code and the
performance of low-level C/C++ code on current and future hardware platforms.

The primary focus of the Intrepydd v0.2
release is the development of kernels that  are amenable to
ahead-of-time compilation and can be called from a main
program written in Python.  As a result, Intrepydd v0.2 is not intended for
writing complete/main programs, and has a number
of limitations relative to standard Python as outlined below.
However, all standard Python features can be used in the main program
that invokes Intrepydd kernels.

Intrepydd v0.2 only runs on
multicore CPU processors, though future versions of Intrepydd under
development also support GPUs and other accelerators.

The recommended use of the Intrepydd v0.2 release in implementing a
data analytics workflow is as follows:
1. Create a pure Python implementation of the workflow.
2. Use profiling to identify the performance-critical code regions of the Python implementation.
3. Restructure the code so as to create a Python function for each
performance-critical region, while ensuring that each such function
only uses Python features supported by Intrepydd.
4. Move the performance-critical functions to an Intrepydd file (.pydd
extension).
5. Add type declarations for function parameters and return values;
   in some cases, additional type declarations may be needed for some
   of the internal statements in the functions.
6. Compile the .pydd file with the "pyddc -O0" option to automatically
   generate unoptimized
   (Python) code for debugging purposes (since it can be debugged
   using standard Python debugging tools), and record its performance
   using our _goal metric_ in abstract units for the energy-delay^2
   product.
7. Once you confirm that the -O0 version runs correctly, use the
   "pyddc -O1" option to automatically generate a more optimized version of the code
   (using Python's Numba JIT compiler), and record its performance.
8.  Next, use the
   "pyddc -O2" option to automatically generate a more optimized version of the code
   (through generation of C/C++ code), and record its performance.
9.  Finally, search for opportunities to replace some of the Intrepydd
    code in the .pydd file with calls to stand ard libraries supported
    in the Intrepydd v0.2 release.  Some of these libraries arfe
    supported across -O0, -O1, and -O2 options, and some are only
    supported with the -O2 option.  Direct debugging of code containing calls
    to libraries that are only supported with the -O2 option is
    currently not supported, though use of such libraries cna provide
    significant performance boosts.
10. Repeat steps 3-10 for additional performance-critical code regions.

### Data Types

Intrepydd v0.2 supports three kinds of data types for
function parameters, function return values, and variables:
1. Primitive types (int32, int64, float32, float64)
2. NumPy arrays of primitive types (homogeneous -- all elements must
   have same data type)
3. Lists of primitive types (homogeneous -- all elements must
have same data type).
Cases 1. and 2. represent Intrepydd data types that can be used in function
parameters and return values invoked from the Python main programs.
Case 3 represents local Intrepydd lists that cannot
interoperate with Python lists.

The following code snippets show example uses of  data types in
function headers:
```
def inc(xs: Array(int32), val: int32):
    '''
    Increment every element in array `xs` by `val`
    '''
	. . .
def sum(xs: Array(float32)) -> float64:
    '''
    Add up all elements in array `xs` and return their sum
    '''	
```
Variable data types are inferred automatically, but in some cases an
explicit type declaration may be needed on assignment statements by
using a  “# type: …” pseudocomment

### Statements

Intrepydd v0.2 supports the following standard statements from Python:
- Assignment statements.
- Sequential for and while loops with optional break / continue statements.
- Conditional if / elif / else statements.
- Function calls (user-defined Intrepydd functions and built-in
library calls).  Note that objects and method calls are not supported in Intrepydd v0.2.

In addition, Intrepydd v0.2 supports a _parallel for_ loop (_pfor_)
with the following syntax:
