.. _deployment:

***************************************
Deploying Code Changes to the Live Site
***************************************

We use `fabric`_ as a deployment tool to update the live site with our local
modifications.

.. _`fabric`: http://fabfile.org

Workflow
========

* Make a modification
* Test it locally
* Deploy it to the live site

Deploying
=========

Deploying is done with a few simple shell commands. For details on what each
command means, see ``fabfile.py`` in the project root and read the `fabric`_
documentation. An example deployment would be::

    $ cd /path/to/project/root
    $ workon bap
    $ fab deploy

