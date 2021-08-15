from pprint import pprint

import pytest
import requests

@pytest.mark.usefixtures("setup", "broker_test_data")
class TestPriceChangesBrokerService:

    def test_custom_defined(self, order_id):
        url = f'https://api-dev.cloudmore.com/api/resellers/01d3a8ac-3fa2-7144-8149-14c83a35b4ed/settings/CustomProperties'
        headers = {'accept': 'application/json',
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IkMzRERCQTEzNkU4MzFDNEFDMzM4OUY0OTM0NTJERjc1MDk3N0FFNjAiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJ3OTI2RTI2REhFckRPSjlKTkZMZmRRbDNybUEifQ.eyJuYmYiOjE2Mjg2ODE5OTMsImV4cCI6MTYyODc2ODM5MywiaXNzIjoiaHR0cHM6Ly9hcGktZGV2LmNsb3VkbW9yZS5jb20iLCJhdWQiOlsiaHR0cHM6Ly9hcGktZGV2LmNsb3VkbW9yZS5jb20vcmVzb3VyY2VzIiwiYXBpIl0sImNsaWVudF9pZCI6InJvLmN1c3RvbWVyLmNsaWVudCIsInN1YiI6ImF1dG90ZXN0QGNsb3VkbW9yZS5jb20iLCJhdXRoX3RpbWUiOjE2Mjg2ODE5OTMsImlkcCI6ImxvY2FsIiwicm9sZSI6IjEiLCJuYW1lIjoiYXV0b3Rlc3RAY2xvdWRtb3JlLmNvbSIsIlBhcmVudElkIjoiMDFkM2E4YWMtM2ZhMi03MTQ0LTgxNDktMTRjODNhMzViNGVkIiwic2NvcGUiOlsiYXBpIl0sImFtciI6WyJwYXNzd29yZCJdfQ.boacTbp7NlULhPXhT3Xpx8o_2Y7Fcje5cETUzgDGpbx0lE7qMEGYKbTaRjn4yy12TFVerjEa7CxsnFpwuNKPxvN5MZOveTGk0AC20M7nkkY0Qq-V_riVwI19BfvM6iUb8Ahbnidx6ffcELBGCZmD3O7SQhsHAuiMWrbLXigepl6L4QcIZa031CRbLnSihQhAZvIkr5G5_aJjqy8MzU3cokv3jIWy-Rl8Cj0hpHgywsPCfNry5QqCii7RN3m04Yc3KeSXIorX24_lCAuLosBG4h7iHD5eH7TqOfOV3-y_rfF6eYRzML4by6Y-wA7Uss07jae8VXNh-LATJPjyW9CISA'}

        response = requests.get(url, headers=headers)
        pprint()
 
