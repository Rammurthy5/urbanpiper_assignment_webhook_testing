Install RabbitMq
    brew install rabbitmq
    sudo scutil --set HostName myhost.local
    PATH=$PATH:/usr/local/sbin to .bash_profile file. 
    Source .bash_profile.
    sudo rabbitmqctl status
    To start: sudo rabbitmq-server
    To stop: sudo rabbitmqctl stop
    run it in the background:
    sudo rabbitmq-server -detached

    Setting up:
        sudo rabbitmqctl add_user myuser mypassword    <rabbituser/mypwd>
         

pip install
    celery
    django
    djangorestframework
