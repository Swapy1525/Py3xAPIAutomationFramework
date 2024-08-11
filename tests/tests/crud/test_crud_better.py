# Create token
# create booking id
# update booking
# delete booking
import allure

from src.Constants.api_constants import APIConstants


class TestCRUDBooking():
    @allure.title("Test CRUD Operations")
    @allure.description(
        "Verify that full update with booking id and Token is working."
    )

    def test_update_booking_id_token(self, create_token,get_booking_id):
        booking_id= get_booking_id
        token= create_token
        put_url= APIConstants.url_patch_put_delete(booking_id= booking_id)
        response = put_requests