# Remote administration with Fabric

## A Brief Introduction to Fabric

[Fabric](http://docs.fabfile.org) is a deployment management framework written in Python which makes remotely managing multiple servers incredibly easy. If you've ever had to issue a change to a group servers, this should look pretty familiar:

```bash
for s in $(cat servers.txt); do ssh $s service httpd graceful; done
```

Fabric improves on this process by providing a suite of functions to run commands on the servers, as well as a number of other features which just aren't possible in a simple for loop. While a working knowledge of Python is helpful when using Fabric, it certainly isn't necessary. This tutorial will show how Fabric can be installed and used on our StoRM Distributed Testbed to update and/or reconfigure all the involved nodes.

## Installing Fabric

One of the best things about Fabric is that the systems which you are remotely administering require nothing beyond the standard OpenSSH server. The master server which you are running Fabric from will, however, need a few things installed before you can get started. Let's get started.

#### Requirements

* Python 2.5+ with the development headers
* python-setuptools and pip (optional, but preferred)
* gcc

If you already have all of these dependencies, you can just run `pip install fabric` and move on to the next section. 
Otherwise, here are some instructions for getting them installed:

#### RHEL 6.x

```bash
# yum install python-pip
# yum install gcc python-devel python-setuptools
# pip install fabric
```

In some cases you need to install latest gmp libraries before installing fabric:

```bash
# wget https://gmplib.org/download/gmp/gmp-6.0.0a.tar.bz2
# tar -xvjpf gmp-6.0.0a.tar.bz2
# cd gmp-6.0.0
# ./configure
# make
# make check
# make install
```

## Using Fabric

Now for the fun part. The installation process added a Python script called `fab` to a directory in your path (hopefully). This is the script which will be used to make magic happen with Fabric. However, just running `fab` from the command-line won't do much at all. In order to do anything interesting, we'll need to create our first fabfile. 

#### Creating a fabfile

The fabfile is where all of your functions, roles, configurations, etc. will be defined. It's just a little bit of Python which tells Fabric exactly what it needs to do. By convention, this file should be named `fabfile.py`, but you can name it anything you'd like. Just keep in mind that if it's something other than fabfile.py, you'll need to specify the path with `fab -f /path/to/notfabfile.py`. Here's a simple example which runs `uptime` locally:

**fabfile.py**

``` python
#!/usr/bin/env python
from fabric.api import local

def uptime():
  local('uptime')
```

Now, let's run the script by calling the uptime function with `fab uptime`:

```
# fab uptime
[localhost] local: uptime
 17:19:31 up 29 min,  1 user,  load average: 0.03, 0.04, 0.06

Done.
```

Sweet! Well, not really. There's nothing too special about just running commands locally. Let's learn some more about what Fabric can do so that we can get this show on the road.

#### Remote Administration

The aimed target is managing our StoRM distributed testbed hosts updates from remote.

![StoRM Distributed Testbed](https://camo.githubusercontent.com/225c82a516da54818909f58f23a2e2e85b12bb85/68747470733a2f2f646c2e64726f70626f7875736572636f6e74656e742e636f6d2f752f32373330363930372f494e464e2f73746f726d2d746573746265642d6c6573732e706e67)

<center>Fig.1 - StoRM Distributed Testbed schema</center>

We were looking for a simple solution to easily keep different type of node updated and/or reconfigured via YAIM.

As you can see from Fig.1 we can identify the following kinds of node:

- BE node (**storm-backend**)
- FE node (**storm-frontend**)
- TR node (**storm-webdav**, **storm-gridhttps-server** and **storm-globus-gridftp**)

On *storm-ui* node Fabric has been installed.
To update all the StoRM distributed testbed nodes, logged with our personal user, we can run the following commands:

```bash
git clone git@github.com:enricovianello/fabric-storm.git
cd fabric-storm
sh update-and-configure-storm-distributed-testbed.sh
```
The script output log can be seen [here](https://gist.github.com/enricovianello/f17c8090f46324627da1)

To update an all in one StoRM node (e.g. omii006-vm03.cnaf.infn.it) you can run another script instead:

```bash
sh update-and-configure-storm-node.sh omii006-vm03.cnaf.infn.it
```

The script output log can be seen [here](https://gist.github.com/enricovianello/5a3a306fe99c23e23823)


