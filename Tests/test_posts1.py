import pytest
import requests

#
# def test_200(get_url_post):
#     "GET request to url returns a 200"
#     resp = get_url_post
#     assert resp.status_code == 200


@pytest.mark.skip(reason="dont't work")
def test_301(get_url_post):
    """HTTP requests should be redirected to HTTPS"""
    resp = get_url_post
    assert resp.url == 'https://jsonplaceholder.typicode.com/posts/1'
    assert resp.history[0].status_code == 301


# def test_http_to_https_redirect():
#     """HTTP requests should be redirected to HTTPS"""
#     url = 'http://monitorial.com/'
#     resp = requests.get(url)
#     assert resp.url == 'https://monitorial.com/'
#     assert resp.history[0].status_code == 301


def test_asdict(get_status_code, get_url_post):
    resp = get_url_post
    result = resp.json()
    expected = {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut"
                " quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    }
    assert result == expected
    assert get_status_code[1] == 200


def test_item_access(get_url_post):
    resp = get_url_post
    result = resp.json()
    assert result['id'] == 1
