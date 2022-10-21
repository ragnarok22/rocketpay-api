# swagger_client.MultiChequesApi

All URIs are relative to *https://pay.ton-rocket.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cheques_controller_create_cheque**](MultiChequesApi.md#cheques_controller_create_cheque) | **POST** /multi-cheques | Create multi-cheque
[**cheques_controller_delete_cheque**](MultiChequesApi.md#cheques_controller_delete_cheque) | **DELETE** /multi-cheques/{id} | Delete multi-cheque
[**cheques_controller_edit_cheque**](MultiChequesApi.md#cheques_controller_edit_cheque) | **PUT** /multi-cheques/{id} | Edit multi-cheque
[**cheques_controller_get_cheque**](MultiChequesApi.md#cheques_controller_get_cheque) | **GET** /multi-cheques/{id} | Get multi-cheque info
[**cheques_controller_get_cheques**](MultiChequesApi.md#cheques_controller_get_cheques) | **GET** /multi-cheques | Get list of multi-cheques

# **cheques_controller_create_cheque**
> SimpleChequeResponse cheques_controller_create_cheque(body)

Create multi-cheque

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
api_instance = swagger_client.MultiChequesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateChequeDto() # CreateChequeDto | 

try:
    # Create multi-cheque
    api_response = api_instance.cheques_controller_create_cheque(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultiChequesApi->cheques_controller_create_cheque: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateChequeDto**](CreateChequeDto.md)|  | 

### Return type

[**SimpleChequeResponse**](SimpleChequeResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cheques_controller_delete_cheque**
> DeleteResponseDto cheques_controller_delete_cheque(id)

Delete multi-cheque

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
api_instance = swagger_client.MultiChequesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete multi-cheque
    api_response = api_instance.cheques_controller_delete_cheque(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultiChequesApi->cheques_controller_delete_cheque: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DeleteResponseDto**](DeleteResponseDto.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cheques_controller_edit_cheque**
> SimpleChequeResponse cheques_controller_edit_cheque(body, id)

Edit multi-cheque

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
api_instance = swagger_client.MultiChequesApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateChequeDto() # UpdateChequeDto | 
id = 'id_example' # str | 

try:
    # Edit multi-cheque
    api_response = api_instance.cheques_controller_edit_cheque(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultiChequesApi->cheques_controller_edit_cheque: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateChequeDto**](UpdateChequeDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**SimpleChequeResponse**](SimpleChequeResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cheques_controller_get_cheque**
> SimpleShortChequeDtoResponse cheques_controller_get_cheque(id)

Get multi-cheque info

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
api_instance = swagger_client.MultiChequesApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get multi-cheque info
    api_response = api_instance.cheques_controller_get_cheque(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultiChequesApi->cheques_controller_get_cheque: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SimpleShortChequeDtoResponse**](SimpleShortChequeDtoResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cheques_controller_get_cheques**
> PaginatedShortChequeDtoResponse cheques_controller_get_cheques(limit=limit, offset=offset)

Get list of multi-cheques

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
api_instance = swagger_client.MultiChequesApi(swagger_client.ApiClient(configuration))
limit = 100 # float |  (optional) (default to 100)
offset = 0 # float |  (optional) (default to 0)

try:
    # Get list of multi-cheques
    api_response = api_instance.cheques_controller_get_cheques(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MultiChequesApi->cheques_controller_get_cheques: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**|  | [optional] [default to 100]
 **offset** | **float**|  | [optional] [default to 0]

### Return type

[**PaginatedShortChequeDtoResponse**](PaginatedShortChequeDtoResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

