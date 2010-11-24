from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.task import Task
from celery.registry import tasks

@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"))
def test():
	print "running sample celery test"

class MyTask(Task):
	def run(self, some_arg, **kwargs):
		logger = self.get_logger(**kwargs)
		sample_file = open("/sample.txt", 'w')
		sample_file.write(some_arg)
		logger.info("Did something: %s" % some_arg)

tasks.register(MyTask)