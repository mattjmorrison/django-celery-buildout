from celery.task.schedules import crontab
from celery.decorators import periodic_task

@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def test():
	print "running sample celery test"