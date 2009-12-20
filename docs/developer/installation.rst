************
Installation
************

On a fresh ubuntu 9.10 box, install the following

.. code-block:: bash

    $ sudo apt-get install python-setuptools python-dev subversion git-core texlive texlive-latex-extra
    $ sudo easy_install virtualenv virtualenvwrapper

1. Checkout the source to ``/var/www/bap``

2. Setup the `Pinax <http://pinaxproject.com>`_ environment and active the `Virtual Environment <http://pypi.python.org/pypi/virtualenv>`_.

.. code-block:: bash

    $ python /var/www/bap/pinax-boot.py --development ~/.virtualenvs/bap
    $ source ~/.virtualenvs/bap/bin/activate

5. Get the external apps using `pip <http://pypi.python.org/pypi/pip>`_

.. code-block:: bash

    $ pip install -E ~/.virtualenvs/bap -r /var/www/bap/requirements.txt

6. Install PIL

.. code-block:: bash

    $ sudo apt-get install python-imaging

7. Setup apache

http://gist.github.com/106077

8. Install mysql

.. code-block:: bash

    $ apt-get install mysql-server python-mysqldb

9. Create the database using `Django <http://djangoproject.com>`_'s ``syncdb`` command.

.. code-block:: bash

    $ /var/www/bap/bap/manage.py syncdb

10. For locally building documentation and running deployment, install the development tools.

.. code-block:: bash
    $ pip install -E ~/.virtualenvs/bap -r /var/www/bap/dev_requirements.txt
