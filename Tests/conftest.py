import pytest
import requests


@pytest.fixture(scope='session')
def get_url_post():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    resp = requests.get(url)
    yield resp
    print(' OK!')


@pytest.fixture(scope='session')
def get_url_comments():
    url = 'https://jsonplaceholder.typicode.com/posts/1/comments'
    resp = requests.get(url)
    yield resp


@pytest.fixture(scope='module')
def get_status_code(get_url_comments, get_url_post):
    resp_comments = get_url_comments.status_code
    resp_posts = get_url_post.status_code
    yield resp_comments, resp_posts
