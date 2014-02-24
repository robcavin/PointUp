from points import celery


@celery.task()
def test_task():
    print "success"