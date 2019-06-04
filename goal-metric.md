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

There are four APIs that need to be used to obtain goal metrics:
1. perf_api.init_metric(), is used to initialize the performance
   metric subsystem, and should be called as close to start of program
   execution as possible.
2. perf_api.start_metric(), is used to mark the start of a
computationally relevant region of Python/Intrepydd code.
3. perf_api.stop_metric(), is used to mark the end of a
computationally relevant region of Python/Intrepydd code.
4. perf_api.init_metric(), is used to finalize the performance
   metric subsystem, and should be called after teh last call to perf_api.stop_metric().
