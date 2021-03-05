"""
    pip install eventlet
    pip install gevent

    celery -A <app> worker --loglevel=info -P eventlet

    celery -A <app> worker --loglevel=info -P gevent 

    celery -A <app> worker --loglevel=info -P solo

    celery -A core worker -E -Q messaging --loglevel=INFO --autoscale=10,4 --without-heartbeat --without-gossip --without-mingle
    celery -A core worker -n worker1  -l info -P gevent

"""