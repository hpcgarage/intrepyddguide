# Performance Goal Metric

As mentioned [earlier](README.md), our current interest is in using
Energy-Delay-Squared (EDS) product, in units of Joules-seconds^2, as a
performance goal metric.  To that end, Intrepydd includes APIs to
compute estimates of this metric, so that testers can work on
improving the metric as they refine their implementations of Intrepydd
code.  These APIs access hardware performance monitors (HPMs), which
usually require running the docker container in privileged mode.
Intrepydd testers just call the high level APIs, and not need be aware
of the details of the HPM accesses performed by the APIs.  Further,
the docker container should be run in single-tenancy mode so as to
avoid the possibility of other jobs perturbing performance evaluations
of the Intrepydd code.

The API internally rely on PAPI (The Performance API) and Linux Perf. These
should already be bundles within the Docker container provided to you. Before
you can use the performance model, you must compile it. The following steps
must be performed:
1. cd /intrepydd/perf-model
2. Set the following enviornment variables:
 '$ export PAPI_INCLUDE=/usr/include/papi.h'
 '$ export PAPI_LIB=/usr/lib/x86_64-linux-gnu/libpapi.so'
 '$ export PFM_LIB=/usr/lib/x86_64-linux-gnu/libpfm.so'
 '$ export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:$PAPI_INCLUDE'
 '$ export LD_PRELOAD=$LD_PRELOAD:$PAPI_LIB:$PFM_LIB'
 '$ export PYTHONPATH=$PYTHONPATH:$PWD'
3. Build the performance model using pyddc:
 '/intrepydd/compiler/pyddc perf_api.cpp'

4. Now run the sample program:
 '$ cd sample'
 '$ ../../compiler/pyddc matopt_kernel.pydd'
 '$ python matopt_pydd_main.py'

You should see a output similar to the one below (Numbers may be different):

 ESTIMATED ENERGY = 0.396943
 ESTIMATED DELAY = 1.25747
 ENERGY-DELAY-SQUARED METRIC = 0.627656

Once the Performance Model has been built, it can be used any intrepydd program.
To import the perf model in your main files, you can add an 'import perf_api'
statement along with other imports. The API calls are described below:

There are four APIs that need to be used to obtain goal metrics:
1. perf_api.init_metric(), is used to initialize the performance
   metric subsystem, and should be called as close to start of program
   execution as possible.
2. perf_api.start_metric(), is used to mark the start of a
computationally relevant region of Python/Intrepydd code.
3. perf_api.stop_metric(), is used to mark the end of a
computationally relevant region of Python/Intrepydd code.
4. perf_api.init_metric(), is used to finalize the performance
   metric subsystem, and should be called after the last call to perf_api.stop_metric().

The below code snippet demonstrates the API usage in an Intrepydd program:

```
import matopt_kernel
import perf_api

perf_api.init_metric()  # Once at very beginning

perf_api.start_metric() # Every time at start of a kernel
r = matopt.inner_product(v1, v2)
perf_api.stop_metric()  # Every time at end of a kernel

perf_api.print_metric() # Once at very end
```
