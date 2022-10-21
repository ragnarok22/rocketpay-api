# CreateTransferDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tg_user_id** | **float** | Telegram user ID. If we dont have this user in DB, we will fail transaction with error: 400 - User not found | 
**currency** | **str** | Currency of transfer, info /currencies/available | [default to 'TONCOIN']
**amount** | **float** | Transfer amount. 9 decimal places, others cut off | 
**transfer_id** | **str** | Unique transfer ID in your system to prevent double spends | 
**description** | **str** | Transfer description | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

