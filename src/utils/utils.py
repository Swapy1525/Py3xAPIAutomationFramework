# contains common utilities
# read dara from excel file
# read data from csv file
# set the headers- application/json, application/xml

class Utils(object):

    def commom_headers_json(self):
        headers = {
            "Content-type": "application/json",
        }
        return headers

    def commom_headers_xml(self):
        headers = {
            "Content-type": "application/xml",
        }
        return headers

    def commom_header_put_patch_delete_basic_auth(self, basic_auth_value):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic" + str(basic_auth_value),
        }
        return headers

    def read_csv_file(self):
        pass

    def read_env_files(self):
        pass

    def read_database(self):
        pass


