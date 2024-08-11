import allure
import pytest
import logging

from src.helpers.api_request_wrapper import post_request
from src.Constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("verify that create booking id and Booking Status should not be null")
    @allure.description(
        "Creating a booking from a payload and verify that the booking id should not null")
    def test_create_booking_positive(self):
        Logger = logging.getLogger(__name__)
        # 5 parts that we need to add
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().commom_headers_json(),
            paylaod= payload_create_booking(),
            in_json= False,
        )
        booking_id= response.json()["bookingid"]
        verify_http_status_code(response_data=response,expect_data= 200),
        verify_json_key_for_not_null_token(booking_id)

        Logger.info(response.json()["bookingid"])


