# Getting Started

We assume that you have access to an Intrepydd release with the pyddc
command, along with a standard Python environment.

The recommended use of the Intrepydd v0.2 release in implementing a
data analytics workflow is as follows:
1. Create a pure Python implementation of the workflow, using
standard libraries such as NumPy, SciPy.sparse, and PyTorch.
2. Use a standard Python profiler to identify the performance-critical code regions of the Python implementation.
3. Select a  performance-critical code region in the Python code that is a promising
   candidate to convert to Intrepydd code.  (The region should 
   uses Python libraries that are supported by
   Intrepydd.)
4. Insert calls to evaluate the Energy-Delay-Squared goal metric (in
   Joules-Seconds^2)  for the core computation in the pure Python
   implementation (ignoring initialization, data input, and data output).
5. Move the performance-critical function to a new function in a single
Intrepydd file for the workflow (.pydd
extension).
6. Add type declarations for function parameters and return values to
   the new Intrepydd  function;
   sometimes, additional type declarations may be needed for some
   of the internal assignment statements in the function.
7. Compile the .pydd file with the pyddc command to automatically 
   generate C/C++ code from the .pydd file.
8. Execute the new Python main program with calls to the optimized
   Intrepydd code, and record its new Energy-Delay-Squared goal metric (in
   Joules-Seconds^2).
9. Repeat steps 3-8 for additional performance-critical code regions.
