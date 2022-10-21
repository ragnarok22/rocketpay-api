import swagger_client
from swagger_client.rest import ApiException

# Configure API key authorization: api-key
configuration = swagger_client.Configuration()
configuration.is_testnet = True
configuration.api_key['Rocket-Pay-Key'] = '78ed1f31392b1e270a7b8d672'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Rocket-Pay-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))

try:
    # Returns information about your application
    api_response = api_instance.apps_controller_get_app_info()
    print(api_response)
except ApiException as e:
    print("Exception when calling AppApi->apps_controller_get_app_info: %s\n" % e)
