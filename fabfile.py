from fabric.api import local, lcd

def prepare_deployment():
    local('python manage.py test django_project')
    local('git add -p && git commit') # or local('hg add && hg commit')

def deploy():
    with lcd('/home/sean/python/django_project/'):

        # With git...
        local('git pull /home/sean/python/dev/django_project/')


        # With both
        local('python manage.py migrate myapp')
        local('python manage.py test myapp')
        local('python manage.py runserver')
