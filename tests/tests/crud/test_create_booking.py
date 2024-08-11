import allure
import pytest


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("verify that create booking id and Booking Status should not be null")
    @allure.description(
        "Creating a booking from a paylaod and verify that the booking id should not null")
    def test_create_booking_positive(self):
        # 5 parts that we need to add

        pass
