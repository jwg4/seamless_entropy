# Seamless entropy

The purpose of this package is to test and demonstrate how to create Python modules which can correctly fallback to supported functionality if dependencies such as C compilation, scipy, numba, etc., are not available.

This packages exports a single function, `binary_entropy`, which returns the entropy of a probability, expressed in bits (rather than using the natural logarithm, as is customary in most mathematical applications).

```
>>> from seamless_entropy import binary_entropy
>>> binary_entropy(0.25)
0.5

```

## Choosing an implementation
The package will choose from one of several implementations of this function, depending on the environment 

 a. at build time, and 
 b. at run time.

For example, if C compilation is supported and enabled, either when building a wheel, or when installing from source, an implementation in a C extension module will be built and used in preference.

If numba is present, either because the package was installed as `seamless_entropy[numba]`, or because it happened to be installed anyway, the Python function will be jitted before use.

If scipy is present, again either by installing `seamless_entropy[scipy]` or incidentally, an implementation which calls a scipy function will be preferred.

## Controlling the build
When building (this can mean either building a redistributable wheel, or installing from source), you can set environment variables to control how the package is built.

- DISABLE_SPEEDUPS: setting this to '1' means that C code will not be built even if that is supported.
- REQUIRE_SPEEDUPS: setting this to '1' means that if C code cannot be built, the 

## TODO
It would be nice to have a Cython implementation. Note that Cython support depends on C support; if Cython is available than native C should work, but not the converse. Thus the Cython implementation should take priority over the C one.

How about configurable order of preference for different platforms?

## Installation errors
The aim with this package is to solve in one place all the packaging issues which arise from a package which optionally includes faster and more efficient versions. This technology is intended to be re-used in other packages. It would be nice to make this package as robust as possible on various Python platforms. If you encounter any problems installing or running this package, on any Python setup no matter how weird, please let me know! I would love to know about your environment so that I can make this package work on it.