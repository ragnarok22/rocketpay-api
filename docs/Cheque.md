# Cheque

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | Cheque ID | 
**currency** | **str** |  | 
**total** | **float** | Total amount of cheque (this amount is charged from balance) | 
**per_user** | **float** | Amount of cheque per user | 
**users** | **float** | Number of users that can activate your cheque | 
**password** | **str** | Cheque password | 
**description** | **str** | Cheque description | 
**send_notifications** | **bool** | send notifications about cheque activation to application cheque webhook or not | 
**captcha_enabled** | **bool** | enable / disable cheque captcha | 
**ref_program_percents** | **float** | percentage of cheque that rewarded for referral program | 
**ref_reward_per_user** | **float** | amount of referral user reward | 
**state** | **str** | Active - cheque created and has unclaimed activations. Completed - cheque totally activated. | 
**link** | **str** |  | 
**tg_resources** | [**list[TgResource]**](TgResource.md) |  | 
**activations** | **float** | How many times cheque is activated | 
**ref_rewards** | **float** | How many times referral reward is payed | 
**disabled_languages** | **AllOfChequeDisabledLanguages** | Disable languages | 
**for_premium** | **bool** | Only users with Telegram Premium can activate this cheque | 
**linked_wallet** | **bool** | Only users with connected wallets can activate this cheque | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

