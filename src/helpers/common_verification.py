def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, "Failed ER != AR"


def verify_response_key(key, expected_data):
    assert key == expected_data

def verify_json_key_for_not_null_token(key):
    assert key != 0, "Failed - Key is non Empty" + key

