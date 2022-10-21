# swagger_client.TgInvoicesApi

All URIs are relative to *https://pay.ton-rocket.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_controller_create_invoice**](TgInvoicesApi.md#invoices_controller_create_invoice) | **POST** /tg-invoices | Create invoice
[**invoices_controller_delete_invoice**](TgInvoicesApi.md#invoices_controller_delete_invoice) | **DELETE** /tg-invoices/{id} | Delete invoice
[**invoices_controller_get_invoice**](TgInvoicesApi.md#invoices_controller_get_invoice) | **GET** /tg-invoices/{id} | Get invoice info
[**invoices_controller_get_invoices**](TgInvoicesApi.md#invoices_controller_get_invoices) | **GET** /tg-invoices | Get list of invoices

# **invoices_controller_create_invoice**
> SimpleInvoiceResponse invoices_controller_create_invoice(body)

Create invoice

### Example

```python
from __future__ import print_function
import time
import rocketpay
from rocketpay.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = rocketpay.Configuration()
configuration.api_key['Rocket-Pay-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Rocket-Pay-Key'] = 'Bearer'

# create an instance of the API class
api_instance = rocketpay.TgInvoicesApi(rocketpay.ApiClient(configuration))
body = rocketpay.CreateInvoiceDto() # CreateInvoiceDto | 

try:
    # Create invoice
    api_response = api_instance.invoices_controller_create_invoice(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TgInvoicesApi->invoices_controller_create_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInvoiceDto**](CreateInvoiceDto.md)|  | 

### Return type

[**SimpleInvoiceResponse**](SimpleInvoiceResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_controller_delete_invoice**
> DeleteResponseDto invoices_controller_delete_invoice(id)

Delete invoice

### Example

```python
from __future__ import print_function
import time
import rocketpay
from rocketpay.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = rocketpay.Configuration()
configuration.api_key['Rocket-Pay-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Rocket-Pay-Key'] = 'Bearer'

# create an instance of the API class
api_instance = rocketpay.TgInvoicesApi(rocketpay.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Delete invoice
    api_response = api_instance.invoices_controller_delete_invoice(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TgInvoicesApi->invoices_controller_delete_invoice: %s\n" % e)
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

# **invoices_controller_get_invoice**
> SimpleFullInvoiceDtoResponse invoices_controller_get_invoice(id)

Get invoice info

### Example

```python
from __future__ import print_function
import time
import rocketpay
from rocketpay.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = rocketpay.Configuration()
configuration.api_key['Rocket-Pay-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Rocket-Pay-Key'] = 'Bearer'

# create an instance of the API class
api_instance = rocketpay.TgInvoicesApi(rocketpay.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Get invoice info
    api_response = api_instance.invoices_controller_get_invoice(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TgInvoicesApi->invoices_controller_get_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SimpleFullInvoiceDtoResponse**](SimpleFullInvoiceDtoResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_controller_get_invoices**
> PaginatedInvoiceResponse invoices_controller_get_invoices(limit=limit, offset=offset)

Get list of invoices

### Example

```python
from __future__ import print_function
import time
import rocketpay
from rocketpay.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = rocketpay.Configuration()
configuration.api_key['Rocket-Pay-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Rocket-Pay-Key'] = 'Bearer'

# create an instance of the API class
api_instance = rocketpay.TgInvoicesApi(rocketpay.ApiClient(configuration))
limit = 100 # float |  (optional) (default to 100)
offset = 0 # float |  (optional) (default to 0)

try:
    # Get list of invoices
    api_response = api_instance.invoices_controller_get_invoices(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TgInvoicesApi->invoices_controller_get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**|  | [optional] [default to 100]
 **offset** | **float**|  | [optional] [default to 0]

### Return type

[**PaginatedInvoiceResponse**](PaginatedInvoiceResponse.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

