# Getting Started (for Python Programmers)#

We assume that you have access to an Intrepydd release with the pyddc
command, along with a standard Python environment.

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
