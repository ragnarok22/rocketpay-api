# FullInvoiceDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Invoice ID | 
**amount** | **float** | Amount of invoice | 
**total_activations** | **float** | Total activations of invoice | 
**activations_left** | **float** | Activations left of invoice | 
**description** | **str** | Invoice description | [optional] 
**hidden_message** | **str** | Message that will be displayed after invoice payment | [optional] 
**payload** | **str** | Any data that is attached to invoice | [optional] 
**callback_url** | **str** | url that will be set for Return button after invoice is paid | [optional] 
**currency** | **str** |  | 
**created** | **datetime** | When invoice was created | 
**paid** | **datetime** | When invoice was paid | [optional] 
**status** | **str** |  | 
**expired_in** | **float** | Invoice expire time in seconds, max 1 day, 0 - none expired | [optional] [default to 0]
**link** | **str** |  | 
**payments** | [**list[PayInvoiceStatDto]**](PayInvoiceStatDto.md) | Payment stat of invoice | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

