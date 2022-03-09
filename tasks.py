from celery import Celery

celery_app = Celery(__name__, backend='redis://localhost', broker='redis://localhost')

@celery_app.task
def factorial(n):
    
    def f(i):
        return 1 if i < 2 else i * f(i - 1)

    return f(n)
