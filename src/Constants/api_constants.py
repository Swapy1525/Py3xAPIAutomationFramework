#API Constants - class which contains all the endpoints
# keep the URL's

class APIConstants():
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def url_createToken(self):
        return "https://restful-booker.herokuapp.com/auth"

    # PUT PATCH DELETE - Booking id

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(booking_id)



