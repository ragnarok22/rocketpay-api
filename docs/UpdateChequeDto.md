# UpdateChequeDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password for cheque | [optional] 
**description** | **str** | Description for cheque | [optional] 
**send_notifications** | **bool** | Send notifications about activations | [optional] [default to True]
**enable_captcha** | **bool** | Enable captcha | [optional] [default to True]
**telegram_resources_ids** | **list[str]** | IDs of telegram resources (groups, channels, private groups) | [optional] 
**for_premium** | **bool** | Only users with Telegram Premium can activate this cheque | [optional] [default to False]
**linked_wallet** | **bool** | Only users with linked wallet can activate this cheque | [optional] [default to False]
**disabled_languages** | **list[str]** | Disable languages | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

