************
Installation
************

On a fresh ubuntu 9.10 box, install the following

.. code-block:: bash

    $ sudo apt-get install python-setuptools python-dev subversion git-core texlive texlive-latex-extra
    $ sudo easy_install virtualenv virtualenvwrapper pip

1. Checkout the source to ``/var/www/bap``

2. Setup the `Pinax <http://pinaxproject.com>`_ version ``0.7.1`` environment and active the `Virtual Environment <http://pypi.python.org/pypi/virtualenv>`_.

.. code-block:: bash

    $ wget http://github.com/pinax/pinax/blob/0.7.1/scripts/pinax-boot.py
    $ python pinax-boot.py --development ~/.virtualenvs/bap
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

    $ mysql -u root -p
    mysql> CREATE DATABASE bap;
    mysql> CREATE USER 'bap'@'localhost' IDENTIFIED BY 'Pass The CPA exam';
    mysql> GRANT ALL on bap.* TO 'bap'@'localhost';
    mysql> exit
    $ /var/www/bap/bap/manage.py syncdb

10. For locally building documentation and running deployment, install the development tools.

.. code-block:: bash
    $ pip install -E ~/.virtualenvs/bap -r /var/www/bap/dev_requirements.txt
