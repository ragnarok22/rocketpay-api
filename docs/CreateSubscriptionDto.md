# CreateSubscriptionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Subscription name, view in bot | [optional] 
**description** | **str** | Subscription description, view in bot | [optional] 
**currency** | **str** | Subscription currency | 
**interval** | [**list[SubscriptionIntervalDto]**](SubscriptionIntervalDto.md) | Subscription interval | 
**tg_resource** | **str** | Subscription TG resource | [optional] 
**referral_percent** | **float** | Subscription referral percent | [default to 0]
**return_url** | **str** | Return link after payment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

