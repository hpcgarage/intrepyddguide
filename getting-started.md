# Getting Started (for Python Programmers)

We assume that you have access to an Intrepydd release with the pyddc
command, along with a standard Python environment.

The recommended use of the Intrepydd v0.2 release in implementing a
data analytics workflow is as follows:
1. Create a pure Python implementation of the workflow, using
standard libraries as you see fit.
2. Insert calls to evaluate the energy-delay^2 goal metric (in
   Joules-seconds^2)  for the core computation in the pure Python
   implementation (ignoring initialization, data input, and data output).
3. Use a standard Python profiler to identify the performance-critical code regions of the Python implementation.
4. Select a  performance-critical code region in the Python code that is a promising
   candidate to convert to Intrepydd code.  (The region should 
uses Python features and libraries that are supported by Intrepydd.)
5. Move the performance-critical function to a new function in a single
Intrepydd file for the workflow (.pydd
extension).
6. Add type declarations for function parameters and return values to
   the new Intrepydd  function;
   in some cases, additional type declarations may be needed for some
   of the internal assignment statements in the function.
7. Compile the .pydd file with the "pyddc -O2" option (default
   optimization level) to automatically 
   generate optimized C/C++ code from the .pydd file.
8. Execute the new Python main program with calls to the optimized
   Intrepydd code, and record its new energy-delay^2 goal metric (in
   Joules-seconds^2).
9. For completeness, measure and record the goal metric for
   optimization levels -O0 and -O1.  Optimization level -O0 can also be
  used for debugging in a standard Python environment.  
10. Repeat steps 3-9 for additional performance-critical code regions.
