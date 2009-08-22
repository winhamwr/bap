from fabric.contrib.project import rsync_project
from fabric.api import roles, env, sudo, run, cd

env.roledefs['webservers'] = ['weswinham.com']

@roles('webservers')
def deploy():
    # sudo('ln -s /home/wes/.virtualenvs/bap/lib/python2.6/site-packages/django/contrib/admin/media /var/www/bap/bap/media/admin')
    sudo('mkdir -p /var/www/bap')
    sudo('chown wes:bap -R /var/www/bap')
    rsync_project(remote_dir='/var/www', exclude=['*.pyc', '.git', 'dev.db'])
    run("cd /home/wes/.virtualenvs/bap/src/cas-consumer && git pull")
    run("touch /var/www/bap/bap/deploy/pinax.wsgi")

    sudo('chown www-data:bap -R /var/www/bap')
    sudo('chmod u+rw,g+rw -R /var/www/bap')

    build_docs()

@roles('webservers')
def build_docs():
    with cd('/var/www/bap/docs'):
        sudo('source /home/wes/.virtualenvs/bap/bin/activate && make html')
        sudo('chown www-data:bap -R _build')
        sudo('chmod u+rw,g+rw -R _build')


@roles('webservers')
def install_dev_reqs():
    with cd('/var/www/bap'):
        run('source /home/wes/.virtualenvs/bap/bin/activate && pip install -r dev_requirements.txt', pty=True)