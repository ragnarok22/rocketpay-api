# UserSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **float** | Subscription id for this payment | 
**subscription_code** | **str** | Subscription code for this payment | 
**user_id** | **float** | TG user ID who pay subscription | 
**amount** | **float** | Sum all payments which added to app balance | 
**currency** | **str** | Subscription currency | 
**interval** | **str** | Payed interval | 
**ref_fee** | **float** | Sum all referral rewards | 
**is_ref_pay** | **bool** | This payment by ref link | 
**total_amount** | **float** | Sum all payments which user pay | 
**payment_start** | **datetime** | When subscribe start | 
**payment_end** | **datetime** | When subscribe ends | 
**auto_renewal** | **bool** | Is auto renewal | 
**transactions** | [**list[UserSubscriptionTransaction]**](UserSubscriptionTransaction.md) | Payments for this user | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

