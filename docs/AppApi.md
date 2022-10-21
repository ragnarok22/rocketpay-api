# swagger_client.AppApi

All URIs are relative to *https://pay.ton-rocket.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apps_controller_get_app_info**](AppApi.md#apps_controller_get_app_info) | **GET** /app/info | Returns information about your application
[**apps_controller_transfer**](AppApi.md#apps_controller_transfer) | **POST** /app/transfer | Make transfer of funds to another user
[**apps_controller_withdrawal**](AppApi.md#apps_controller_withdrawal) | **POST** /app/withdrawal | Make withdrawal of funds to external wallet

# **apps_controller_get_app_info**
> AppDto apps_controller_get_app_info()

Returns information about your application

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = swagger_client.Configuration()
configuration.api_key['Rocket-Pay-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Rocket-Pay-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))

try:
    # Returns information about your application
    api_response = api_instance.apps_controller_get_app_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->apps_controller_get_app_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AppDto**](AppDto.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_controller_transfer**
> SimpleTransferDtoResponse apps_controller_transfer(body)

Make transfer of funds to another user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = swagger_client.Configuration()
configuration.api_key['Rocket-Pay-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Rocket-Pay-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateTransferDto() # CreateTransferDto | 

try:
    # Make transfer of funds to another user
    api_response = api_instance.apps_controller_transfer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->apps_controller_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateTransferDto**](CreateTransferDto.md)|  | 

### Return type

[**SimpleTransferDtoResponse**](SimpleTransferDtoResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apps_controller_withdrawal**
> SimpleWithdrawalDtoResponse apps_controller_withdrawal(body)

Make withdrawal of funds to external wallet

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = swagger_client.Configuration()
configuration.api_key['Rocket-Pay-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Rocket-Pay-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AppApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateWithdrawalDto() # CreateWithdrawalDto | 

try:
    # Make withdrawal of funds to external wallet
    api_response = api_instance.apps_controller_withdrawal(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppApi->apps_controller_withdrawal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateWithdrawalDto**](CreateWithdrawalDto.md)|  | 

### Return type

[**SimpleWithdrawalDtoResponse**](SimpleWithdrawalDtoResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

