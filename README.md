# 4d_pro
Python script to analyse slow queries in MongoDB 4.4+ json kind log file

How to use

- Download the 4d_pro.py script to local
- Call the script by passing the MongoDB log file
- Enter the sort key hit enter twice

You should get output like below:


```
MacBook-Pro-52:OMs darshanj$ /Users/darshanj/anaconda3/bin/python /Users/darshanj/Downloads/4D_PlusAnalyser/4d_pro.py /Users/darshanj/Downloads/4D_PlusAnalyser/sample.log 
Please enter sort key: 
1. minTime
2. maxTime
3. count
4. Namespace
5. Operation
5
Namespace                                                                        Operation       Pattern                                                                                              Count  totalTime(ms) minTime(ms) maxTime(ms)
636e6c******7937fba6.Sta******                                    update          {'q': {'TypeNames': '*', '_id': {'$in': '*'}}}                                                         3108    1048214      200     2988
636e6******0-457c-a5b9-d1547937fba6.Sta******                                     update          {'q': {'TypeNames': '*', 'SystemUpdateTime': {'$lt': {'$date': '*'}}}, 'u': {'$set': {'AutomaticCustomEntityAttributeDefinitionIds': '*', 'SystemUpdateTime': {'$date': '*'}}}, 'multi': '*', 'upsert': '*'}    543    1625404      203   133118
f56*****b-b9b8-d321ba050131.Ent*****                                    update          {'q': {'TypeNames': '*', 'TenantId': '*', 'SystemUpdateTime': {'$lt': {'$date': '*'}}, 'SystemD*****onTime': '*'}, 'u': {'$set': {'SystemDeletionTime': {'$date': '*'}, 'SystemUpdateTime': {'$date': '*'}}}, 'multi': '*', 'upsert': '*'}    371     313583      200    13513
2c4fc******7e-be70-279af937903b.Ev******rs                            update          {'q': {'_id': '*'}, 'u': {'TypeNames': '*', '_id': '*', 'SystemCreationTime': {'$date': '*'}, 'System*****nTime': '*', 'SystemUpdateTime': {'$date': '*'}, 'TypeName': '*', 'TenantId': '*', 'EventT*****atorMap': '*'}, 'multi': '*', 'upsert': '*'}    190      49622      200      618
178234a3-81*****4-ac45-a58fe7c7a820.Ca*****                                      update          {'q': {'TypeNames': '*', '_id': '*'}, 'u': {'TypeNames': '*', '_id': '*', 'SystemCreationTime': {'$date': '*'}, 'SystemDeletionTime': '*', 'SystemUpdateTime': {'$date': '*'}, 'TypeName': '*', 'TenantId': '*', 'Attributes': '*', 'DisplayNameValue': '*', 'Entity': {'TypeNames': '*', '_id': '*', 'SystemCreationTime': {'$date': '*'}, 'Syste*****onTime': '*', 'SystemUpdateTime': {'$date': '*'}, 'TypeName': '*', 'TenantId': '*', 'Displ*****': '*', 'Name': '*', 'RawId': '*', 'Applicati*****nments': '*', 'CreationTime': {'$date': '*'}, 'JobInfo': {'CompanyName': '*', 'Department': '*', 'EmployeeRawId': '*', 'ManagerUserId': '*', 'Title': '*'}, 'Mail': '*', 'Type': '*', 'UserPrincipalName': '*'}, 'EntityConfiguration': '*', 'EntityIds': '*', 'EntityNetwork': '*', 'EntityProfile': {'TypeNames': '*', '_id': '*', 'SystemCreationTime': {'$date': '*'}, 'SystemDeletionTime': '*', 'SystemUpdateTime': {'$date': '*'}, 'TypeName': '*', 'Azure': {'ActivityTime': '*', 'TenantIdToActivityTimeMap': '*'}, 'SignInTime': {'$date': '*'}, 'ActivityTime': '*', 'Aws': {'ActivityTime': '*', 'RoleIdToActivityTimeMap': '*'}}, 'Exa*****alues': '*', 'OpenRelatedEntityRiskCount': '*', 'OpenRe*****HighestSeverity': '*', 'OpenRelatedEntityRiskHighestSeverityValue': '*', 'OpenR*****skIds': '*', 'OpenRiskedEntityRiskIdsValue': '*', 'PartialSearchTermsValue': '*', 'UiEntity': '*', 'Access': {'TypeNames': '*', 'ActivityTime': '*', 'ActivityTimeType': '*', 'ExcessivePermissionActionStats': {'Count': '*', 'SecuredCount': '*', 'UnsecuredSeverityToCountMap': '*'}, 'ExcessivePermissions': '*', 'Permissions': {'ActionResourceIds': '*', 'ActionResourceIdsValue': '*', 'ActionRiskCategories': '*', 'ActionRiskCategoryToSeverityMap': '*', 'ActionRiskCategoryToSeverityMapValue': '*', 'ActionServiceIds': '*', 'ActionServiceIdsValue': '*', 'Attributes': '*', 'AttributesValue': '*', 'BuiltInAttributeTypeNames': '*', 'CustomAttributeDefinitionIds': '*', 'RiskSeverity': '*', 'RiskSeverityValue': '*'}, 'Risk': {'Category': '*', 'JiraIssueUrl': '*', 'OpenAccessPrincipalRiskId': '*', 'ServiceNowIncidentUrl': '*'}, 'Types': '*'}, 'AzureRoleAssignmentIds': '*', 'AzureRoleDefinitionIds': '*', 'AzureRoleDefinitionIdsValue': '*', 'GroupIds': '*', 'GroupIdsValue': '*', 'AwsRoleIds': '*', 'AwsRoleIdsValue': '*', 'JobTitleValue': '*', 'MailValue': '*'}, 'multi': '*', 'upsert': '*'}      1        250      250      250
```
