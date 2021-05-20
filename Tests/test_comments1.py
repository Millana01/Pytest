import pytest
import requests
import json

class Test_comments():

    def test_headers(self, get_status_code, get_url_comments):
        resp = get_url_comments
        assert get_status_code[0] == 200
        assert resp.headers["Content-Type"] == "application/json; charset=utf-8"
        assert resp.headers["Connection"] == "keep-alive"
        assert resp.headers["cache-control"] == "max-age=43200"

    expected = [(["postId", "id", "name", "email", "body"]),
               (["last name", "id", "name", "gmail", "body"]),
               (["address", "id", "", "email", "body"])]

    expected_ids = ["Task: " for i in expected]


    @pytest.mark.xfail()
    @pytest.mark.parametrize("expected", expected, ids=expected_ids)
    def test_body(self, get_url_comments, expected):
        resp = get_url_comments
        response_body = resp.json()
        for i in range(len(response_body)):
            list_keys = list(response_body[i].keys())
            assert expected == list_keys


