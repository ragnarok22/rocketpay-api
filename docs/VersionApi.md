# swagger_client.VersionApi

All URIs are relative to *https://pay.ton-rocket.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_controller_get_version**](VersionApi.md#version_controller_get_version) | **GET** /version | Returns current version of API. You may use it as healthcheck

# **version_controller_get_version**
> Version version_controller_get_version()

Returns current version of API. You may use it as healthcheck

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionApi()

try:
    # Returns current version of API. You may use it as healthcheck
    api_response = api_instance.version_controller_get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->version_controller_get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

