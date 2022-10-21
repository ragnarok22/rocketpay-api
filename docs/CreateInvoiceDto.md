# CreateInvoiceDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Invoice amount. 9 decimal places, others cut off | 
**num_payments** | **float** | Num payments for invoice | [default to 1]
**currency** | **str** | Currency of transfer, info /currencies/available | [default to 'TONCOIN']
**description** | **str** | Description for invoice | [optional] 
**hidden_message** | **str** | Hidden message after invoice is paid | [optional] 
**callback_url** | **str** | Url for Return button after invoice is paid | [optional] 
**payload** | **str** | Any data. Invisible to user, will be returned in callback | [optional] 
**expired_in** | **float** | Invoice expire time in seconds, max 1 day, 0 - none expired | [optional] [default to 0]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

