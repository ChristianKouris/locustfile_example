from locust import HttpUser, TaskSet, task

class MyTaskSet(TaskSet):
	@task
	def index(self):
		self.client.get("/")

class MyLocust(HttpUser):
	tasks = [MyTaskSet]
	min_wait = 5000
	max_wait = 15000
