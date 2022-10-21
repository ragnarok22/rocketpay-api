# swagger_client.CurrenciesApi

All URIs are relative to *https://pay.ton-rocket.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currencies_controller_get_coins**](CurrenciesApi.md#currencies_controller_get_coins) | **GET** /currencies/available | Returns available currencies
[**currencies_controller_get_rates**](CurrenciesApi.md#currencies_controller_get_rates) | **GET** /currencies/rate | Returns rates from simple simple-order

# **currencies_controller_get_coins**
> AvailableCoins currencies_controller_get_coins()

Returns available currencies

### Example

```python
from __future__ import print_function
import time
import rocketpay
from rocketpay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rocketpay.CurrenciesApi()

try:
    # Returns available currencies
    api_response = api_instance.currencies_controller_get_coins()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_controller_get_coins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AvailableCoins**](AvailableCoins.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currencies_controller_get_rates**
> Rates currencies_controller_get_rates(coin_from, coin_to)

Returns rates from simple simple-order

### Example

```python
from __future__ import print_function
import time
import rocketpay
from rocketpay.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = rocketpay.CurrenciesApi()
coin_from = 1.2 # float | ID of coin from
coin_to = 1.2 # float | ID of coin to

try:
    # Returns rates from simple simple-order
    api_response = api_instance.currencies_controller_get_rates(coin_from, coin_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_controller_get_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coin_from** | **float**| ID of coin from | 
 **coin_to** | **float**| ID of coin to | 

### Return type

[**Rates**](Rates.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

