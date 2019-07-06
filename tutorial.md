# Using Intrepydd from Jupyter (includes demo video, code examples, setup info)

### Overview
You can use Intrepydd from within Jupyter. The following collection of notebooks shows you how.

**Video Preview.** For a quick video overview, which goes through the k-means case study below, [click here (YouTube)](https://www.youtube.com/watch?v=00CkXStroOk).

> Below, the title links directly to a Jupyter notebook. If, instead, you just want to preview the notebook, click the _"Preview"_ links, which redirect you to the GitHub versions.

1. ["Hello, world!"](./notebooks/001-hello-world.ipynb) -- [Preview](https://github.com/hpcgarage/intrepyddguide/blob/master/notebooks/001-hello-world.ipynb)
2. [Type specialization basics](./notebooks/002-typing-basics.ipynb) -- [Preview](https://github.com/hpcgarage/intrepyddguide/blob/master/notebooks/002-typing-basics.ipynb)
3. [Profiling basics](./notebooks/003-profiling.ipynb) -- [Preview](https://github.com/hpcgarage/intrepyddguide/blob/master/notebooks/003-profiling.ipynb)
4. [Case study: profiling and optimizing k-means](./notebooks/004-kmeans.ipynb) -- [Preview](https://github.com/hpcgarage/intrepyddguide/blob/master/notebooks/004-kmeans.ipynb)

### Setup info for connecting Jupyter to Docker instance running Intrepydd

Since Jupyter is usually run on a web browser on your local machine, the following three steps need to be performed to enable Jupyter to connect with a Docker instance running Intrepydd.  In the following, we will assume that the Docker instance is running on a server named ubuntu@54.198.41.116, that is representative of a typical EC2 instance.  The actual path names may vary depending on the server instance that you use.

Step 1: ssh to the server and run Jupyter via Docker
```
$ ssh -i key_CqPMRtDoyTYq.pem ubuntu@54.198.41.116
$ sudo docker run -p 8888:8888 --privileged -it --rm --net=host -v /data:/data sdhph1-eval1 /bin/bash -c "/opt/conda/bin/jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"
```
Copy the URL returned by the "docker run" command, e.g., http://127.0.0.1:8888/?token=0628d41265d1fa85e7d6c489ad3834317e9a2e6234bd9e29

Step 2: forward port 8888 from the  server to your local machine
```
$ ssh -i key_CqPMRtDoyTYq.pem -L 8888:localhost:8888 ubuntu@54.198.41.116
```
Step 3: Open the URL copied at the end of step 1 in a web browser, e.g., http://127.0.0.1:8888/?token=0628d41265d1fa85e7d6c489ad3834317e9a2e6234bd9e29




