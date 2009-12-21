import os

from fabric.contrib.project import rsync_project
from fabric.api import roles, env, sudo, run, cd, put

env.roledefs['webservers'] = ['weswinham.com']
env.roledefs['dbserver'] = ['weswinham.com']

env.warn_only = True

@roles('webservers')
def deploy():
    env.project_root = '/var/www/bap'
    env.pinax_root = os.path.join(env.project_root, 'bap')
    env.virtualenv = '/home/wes/.virtualenvs/bap'

    # sudo('ln -s /home/wes/.virtualenvs/bap/lib/python2.6/site-packages/django/contrib/admin/media /var/www/bap/bap/media/admin')
    sudo('mkdir -p %(project_root)s' % env)
    sudo('chown wes:bap -R %(project_root)s' % env)
    rsync_project(remote_dir='/var/www', exclude=['*.pyc', '.git', 'dev.db', '/bap/site_media/media'])
    run("cd %(virtualenv)s/src/cas-consumer && git pull" % env)
    run("touch %(pinax_root)s/deploy/pinax.wsgi" % env)

    sudo('chown www-data:bap -R %(project_root)s' % env)
    sudo('chmod u+rw,g+rw -R %(project_root)s' % env)

    build_docs()
    install_reqs()

@roles('webservers')
def install_reqs():
    with cd('/var/www/bap'):
        run('source /home/wes/.virtualenvs/bap/bin/activate && pip install -r requirements.txt')


@roles('webservers')
def build_docs():
    with cd('/var/www/bap/docs'):
        sudo('source /home/wes/.virtualenvs/bap/bin/activate && make html --silent')
        sudo('source /home/wes/.virtualenvs/bap/bin/activate && make latex --silent')
        with cd('_build/latex'):
            sudo('source /home/wes/.virtualenvs/bap/bin/activate && make --silent')
            sudo('mv IUBAPWebsite.pdf ../html/')
        sudo('chown www-data:bap -R _build')
        sudo('chmod u+rw,g+rw -R _build')

@roles('webservers')
def reset_db():
    with cd('/var/www/bap/bap'):
        sudo('source /home/wes/.virtualenvs/bap/bin/activate && ./manage.py reset_db --noinput')
        sudo('source /home/wes/.virtualenvs/bap/bin/activate && ./manage.py syncdb --noinput')
        sudo('source /home/wes/.virtualenvs/bap/bin/activate && ./manage.py loaddata fixtures/default_users.json fixtures/required_pages.json fixtures/advertisement.json fixtures/calendars.json')
        sudo('chown www-data:bap dev.db')
        sudo('chmod u+rw,g+rw dev.db')

@roles('webservers')
def install_dev_reqs():
    with cd('/var/www/bap'):
        run('source /home/wes/.virtualenvs/bap/bin/activate && pip install -r dev_requirements.txt')

@roles('dbserver')
def create_db():
    mysql_cmds = [
        "CREATE USER 'bap'@'localhost' IDENTIFIED BY 'Pass The CPA exam';",
        "CREATE DATABASE bap;",
        "GRANT ALL on bap.* TO 'bap'@'localhost';"
    ]
    run_mysql = 'mysql -u root -e "%s"'

    for cmd in mysql_cmds:
        result = sudo(run_mysql % cmd)