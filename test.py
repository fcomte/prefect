from prefect import task, Flow, Parameter
from prefect.storage import GitHub

@task(log_stdout=True)
def say_hello(name):
    print("Hello, {}!".format(name))


with Flow("Mon flow github") as flow:
    name = Parameter('name')
    say_hello(name)

flow.storage = GitHub(repo="fcomte/prefect", path="test.py")
