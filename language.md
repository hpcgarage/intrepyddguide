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
program written in Python; as such, Intrepydd v0.2 is not intended for
writing complete/main programs.  Intrepydd v0.2 only runs on
multicore CPU processors, though future versions of Intrepydd under
development also support GPUs and other accelerators.

The recommended use of the Intrepydd v0.2 release in implementing a
data analytics workflow is as follows:
1. Create a pure Python implementation of the workflow
2. Use profiling to identify the performance-critical code regions of the Python implementation
3. Restructure the code so as to create a Python function for each
performance-critical region
4. Move the performance-critical functions to an Intrepydd file (.pydd
extension)
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



```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/hpcgarage/intrepydddocs/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
