from fabric.contrib.project import rsync_project
from fabric.api import roles, env, sudo, run

env.roledefs['webservers'] = ['weswinham.com']

@roles('webservers')
def deploy():
    rsync_project(remote_dir='/var/www', exclude=['*.pyc', '.git', 'dev.db'])
    run("cd /home/wes/.virtualenvs/bap/src/cas-consumer && git pull")
    run("touch /var/www/bap/bap/deploy/pinax.wsgi")

    sudo('chown www-data:bap -R /var/www/bap')
    sudo('chmod u+rw,g+rw -R /var/www/bap')