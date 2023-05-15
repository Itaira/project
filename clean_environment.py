import requests

def clean():
    requests.get(f'http://127.0.0.1:5000/stop')
    requests.get(f'http://127.0.0.1:5001/stop')