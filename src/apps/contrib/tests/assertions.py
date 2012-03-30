from nose.tools import assert_equals as assert_equals_nose


def assert_equals(expected, actual):
    """
    Just a wrap around nose assert_equals for import convenience

    """
    assert_equals_nose(expected, actual)


def assert_post(response, final_url, status_code=302):
    """
    Usually we want to test a POST in a two steps way:
        * status_code should be 302 (sometimes 301, if permanent)
        * redirection url should be ``final_url``

    """
    assert_equals(response.status_code, status_code)
    assert response['Location'].endswith(final_url)


def assert_get(response, template_used):
    """
    Usually we want to test a GET in a two steps way:
        * status_code must be 200
        * some ``template_used`` is loaded into the response

    """
    assert_equals(response.status_code, 200)
    assert_equals(response.template_name, template_used)
