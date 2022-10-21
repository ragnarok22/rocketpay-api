# swagger_client.SubscriptionsApi

All URIs are relative to *https://pay.ton-rocket.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_controller_check_subscription**](SubscriptionsApi.md#subscriptions_controller_check_subscription) | **POST** /subscriptions/check/{subscriptionId} | 
[**subscriptions_controller_create_subscription**](SubscriptionsApi.md#subscriptions_controller_create_subscription) | **POST** /subscriptions | Create subscription
[**subscriptions_controller_crete_subscription_interval**](SubscriptionsApi.md#subscriptions_controller_crete_subscription_interval) | **POST** /subscriptions/{subscriptionId}/interval | Create subscription interval
[**subscriptions_controller_delete_subscription**](SubscriptionsApi.md#subscriptions_controller_delete_subscription) | **DELETE** /subscriptions/{subscriptionId} | Delete subscription
[**subscriptions_controller_delete_subscription_interval**](SubscriptionsApi.md#subscriptions_controller_delete_subscription_interval) | **DELETE** /subscriptions/{subscriptionId}/interval/{intervalCode} | Delete subscription interval
[**subscriptions_controller_edit_subscription_interval**](SubscriptionsApi.md#subscriptions_controller_edit_subscription_interval) | **PUT** /subscriptions/{subscriptionId}/interval/{intervalCode} | Edit subscription interval
[**subscriptions_controller_get_subscription**](SubscriptionsApi.md#subscriptions_controller_get_subscription) | **GET** /subscriptions/{subscriptionId} | Get subscription info
[**subscriptions_controller_get_subscription_interval**](SubscriptionsApi.md#subscriptions_controller_get_subscription_interval) | **GET** /subscriptions/{subscriptionId}/interval/{intervalCode} | Get subscription interval info
[**subscriptions_controller_get_subscriptions**](SubscriptionsApi.md#subscriptions_controller_get_subscriptions) | **GET** /subscriptions | Get list of subscription

# **subscriptions_controller_check_subscription**
> SimpleUserSubscriptionResponse subscriptions_controller_check_subscription(body, subscription_id)



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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CheckSubscriptionDto() # CheckSubscriptionDto | 
subscription_id = 'subscription_id_example' # str | 

try:
    api_response = api_instance.subscriptions_controller_check_subscription(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_controller_check_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckSubscriptionDto**](CheckSubscriptionDto.md)|  | 
 **subscription_id** | **str**|  | 

### Return type

[**SimpleUserSubscriptionResponse**](SimpleUserSubscriptionResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_create_subscription**
> SimpleSubscriptionResponse subscriptions_controller_create_subscription(body)

Create subscription

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateSubscriptionDto() # CreateSubscriptionDto | 

try:
    # Create subscription
    api_response = api_instance.subscriptions_controller_create_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_controller_create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSubscriptionDto**](CreateSubscriptionDto.md)|  | 

### Return type

[**SimpleSubscriptionResponse**](SimpleSubscriptionResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_crete_subscription_interval**
> SimpleSubscriptionIntervalResponse subscriptions_controller_crete_subscription_interval(body, subscription_id)

Create subscription interval

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SubscriptionIntervalDto() # SubscriptionIntervalDto | 
subscription_id = 'subscription_id_example' # str | 

try:
    # Create subscription interval
    api_response = api_instance.subscriptions_controller_crete_subscription_interval(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_controller_crete_subscription_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionIntervalDto**](SubscriptionIntervalDto.md)|  | 
 **subscription_id** | **str**|  | 

### Return type

[**SimpleSubscriptionIntervalResponse**](SimpleSubscriptionIntervalResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_delete_subscription**
> DeleteResponseDto subscriptions_controller_delete_subscription(subscription_id)

Delete subscription

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 

try:
    # Delete subscription
    api_response = api_instance.subscriptions_controller_delete_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_controller_delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**DeleteResponseDto**](DeleteResponseDto.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_delete_subscription_interval**
> SimpleSubscriptionIntervalResponse subscriptions_controller_delete_subscription_interval(subscription_id, interval_code)

Delete subscription interval

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
interval_code = 'interval_code_example' # str | 

try:
    # Delete subscription interval
    api_response = api_instance.subscriptions_controller_delete_subscription_interval(subscription_id, interval_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_controller_delete_subscription_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **interval_code** | **str**|  | 

### Return type

[**SimpleSubscriptionIntervalResponse**](SimpleSubscriptionIntervalResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_edit_subscription_interval**
> SimpleSubscriptionIntervalResponse subscriptions_controller_edit_subscription_interval(body, subscription_id, interval_code)

Edit subscription interval

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.EditSubscriptionIntervalDto() # EditSubscriptionIntervalDto | 
subscription_id = 'subscription_id_example' # str | 
interval_code = 'interval_code_example' # str | 

try:
    # Edit subscription interval
    api_response = api_instance.subscriptions_controller_edit_subscription_interval(body, subscription_id, interval_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_controller_edit_subscription_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditSubscriptionIntervalDto**](EditSubscriptionIntervalDto.md)|  | 
 **subscription_id** | **str**|  | 
 **interval_code** | **str**|  | 

### Return type

[**SimpleSubscriptionIntervalResponse**](SimpleSubscriptionIntervalResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_get_subscription**
> SimpleSubscriptionResponse subscriptions_controller_get_subscription(subscription_id)

Get subscription info

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 

try:
    # Get subscription info
    api_response = api_instance.subscriptions_controller_get_subscription(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_controller_get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 

### Return type

[**SimpleSubscriptionResponse**](SimpleSubscriptionResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_get_subscription_interval**
> SimpleSubscriptionIntervalResponse subscriptions_controller_get_subscription_interval(subscription_id, interval_code)

Get subscription interval info

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | 
interval_code = 'interval_code_example' # str | 

try:
    # Get subscription interval info
    api_response = api_instance.subscriptions_controller_get_subscription_interval(subscription_id, interval_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_controller_get_subscription_interval: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**|  | 
 **interval_code** | **str**|  | 

### Return type

[**SimpleSubscriptionIntervalResponse**](SimpleSubscriptionIntervalResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_controller_get_subscriptions**
> PaginatedSubscriptionResponse subscriptions_controller_get_subscriptions(limit=limit, offset=offset)

Get list of subscription

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
limit = 100 # float |  (optional) (default to 100)
offset = 0 # float |  (optional) (default to 0)

try:
    # Get list of subscription
    api_response = api_instance.subscriptions_controller_get_subscriptions(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->subscriptions_controller_get_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**|  | [optional] [default to 100]
 **offset** | **float**|  | [optional] [default to 0]

### Return type

[**PaginatedSubscriptionResponse**](PaginatedSubscriptionResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

