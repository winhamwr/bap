************
Installation
************

On a fresh ubuntu 9.04 box, install the following

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

7. Create the database using `Django <http://djangoproject.com>`_'s ``syncdb`` command.

.. code-block:: bash

    $ /var/www/bap/bap/manage.py syncdb

8. Setup apache
