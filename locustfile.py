from locust import HttpUser, task, between
from random import randint

class LoadTestUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_square(self):
        self.client.get("/square-numbers")

    @task
    def load_test_endpoint(self):
        a = randint(0, 10)
        b = randint(0, 10)
        self.client.get(f'/add-two-numbers/?a={a}&b={b}')