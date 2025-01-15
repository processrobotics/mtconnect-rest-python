# cppagent.DefaultApi

All URIs are relative to *http://172.18.0.4:5000/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_asset_id_delete**](DefaultApi.md#asset_asset_id_delete) | **DELETE** /asset/{assetId} | Delete asset identified by &#x60;assetId&#x60;
[**asset_asset_id_post**](DefaultApi.md#asset_asset_id_post) | **POST** /asset/{assetId} | Upload an asset by identified by &#x60;assetId&#x60;
[**asset_asset_id_put**](DefaultApi.md#asset_asset_id_put) | **PUT** /asset/{assetId} | Upload an asset by identified by &#x60;assetId&#x60;
[**asset_asset_ids_get**](DefaultApi.md#asset_asset_ids_get) | **GET** /asset/{assetIds} | MTConnect asset request
[**asset_delete**](DefaultApi.md#asset_delete) | **DELETE** /asset | Delete all assets for a device and type
[**asset_get**](DefaultApi.md#asset_get) | **GET** /asset | MTConnect asset request
[**asset_post**](DefaultApi.md#asset_post) | **POST** /asset | Upload an asset by identified by &#x60;assetId&#x60;
[**asset_put**](DefaultApi.md#asset_put) | **PUT** /asset | Upload an asset by identified by &#x60;assetId&#x60;
[**assets_asset_id_delete**](DefaultApi.md#assets_asset_id_delete) | **DELETE** /assets/{assetId} | Delete asset identified by &#x60;assetId&#x60;
[**assets_asset_id_post**](DefaultApi.md#assets_asset_id_post) | **POST** /assets/{assetId} | Upload an asset by identified by &#x60;assetId&#x60;
[**assets_asset_id_put**](DefaultApi.md#assets_asset_id_put) | **PUT** /assets/{assetId} | Upload an asset by identified by &#x60;assetId&#x60;
[**assets_asset_ids_get**](DefaultApi.md#assets_asset_ids_get) | **GET** /assets/{assetIds} | MTConnect assets request
[**assets_delete**](DefaultApi.md#assets_delete) | **DELETE** /assets | Delete all assets for a device and type
[**assets_get**](DefaultApi.md#assets_get) | **GET** /assets | MTConnect assets request
[**assets_post**](DefaultApi.md#assets_post) | **POST** /assets | Upload an asset by identified by &#x60;assetId&#x60;
[**assets_put**](DefaultApi.md#assets_put) | **PUT** /assets | Upload an asset by identified by &#x60;assetId&#x60;
[**current_get**](DefaultApi.md#current_get) | **GET** /current | MTConnect current request
[**device_asset_asset_id_post**](DefaultApi.md#device_asset_asset_id_post) | **POST** /{device}/asset/{assetId} | Upload an asset by identified by &#x60;assetId&#x60;
[**device_asset_asset_id_put**](DefaultApi.md#device_asset_asset_id_put) | **PUT** /{device}/asset/{assetId} | Upload an asset by identified by &#x60;assetId&#x60;
[**device_asset_delete**](DefaultApi.md#device_asset_delete) | **DELETE** /{device}/asset | Delete all assets for a device and type
[**device_asset_get**](DefaultApi.md#device_asset_get) | **GET** /{device}/asset | MTConnect asset request
[**device_asset_post**](DefaultApi.md#device_asset_post) | **POST** /{device}/asset | Upload an asset by identified by &#x60;assetId&#x60;
[**device_asset_put**](DefaultApi.md#device_asset_put) | **PUT** /{device}/asset | Upload an asset by identified by &#x60;assetId&#x60;
[**device_assets_asset_id_post**](DefaultApi.md#device_assets_asset_id_post) | **POST** /{device}/assets/{assetId} | Upload an asset by identified by &#x60;assetId&#x60;
[**device_assets_asset_id_put**](DefaultApi.md#device_assets_asset_id_put) | **PUT** /{device}/assets/{assetId} | Upload an asset by identified by &#x60;assetId&#x60;
[**device_assets_delete**](DefaultApi.md#device_assets_delete) | **DELETE** /{device}/assets | Delete all assets for a device and type
[**device_assets_get**](DefaultApi.md#device_assets_get) | **GET** /{device}/assets | MTConnect assets request
[**device_assets_post**](DefaultApi.md#device_assets_post) | **POST** /{device}/assets | Upload an asset by identified by &#x60;assetId&#x60;
[**device_assets_put**](DefaultApi.md#device_assets_put) | **PUT** /{device}/assets | Upload an asset by identified by &#x60;assetId&#x60;
[**device_current_get**](DefaultApi.md#device_current_get) | **GET** /{device}/current | MTConnect current request
[**device_get**](DefaultApi.md#device_get) | **GET** /{device} | MTConnect probe request
[**device_post**](DefaultApi.md#device_post) | **POST** /{device} | Non-normative POST to update a value in the agent
[**device_probe_get**](DefaultApi.md#device_probe_get) | **GET** /{device}/probe | MTConnect probe request
[**device_put**](DefaultApi.md#device_put) | **PUT** /{device} | Non-normative PUT to update a value in the agent
[**device_sample_get**](DefaultApi.md#device_sample_get) | **GET** /{device}/sample | MTConnect sample request
[**probe_get**](DefaultApi.md#probe_get) | **GET** /probe | MTConnect probe request
[**root_get**](DefaultApi.md#root_get) | **GET** / | MTConnect probe request
[**sample_get**](DefaultApi.md#sample_get) | **GET** /sample | MTConnect sample request

# **asset_asset_id_delete**
> asset_asset_id_delete(asset_id)

Delete asset identified by `assetId`

Marks the asset as removed and creates an AssetRemoved event

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
asset_id = 'asset_id_example' # str | An assetId to select

try:
    # Delete asset identified by `assetId`
    api_instance.asset_asset_id_delete(asset_id)
except ApiException as e:
    print("Exception when calling DefaultApi->asset_asset_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| An assetId to select | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_asset_id_post**
> asset_asset_id_post(asset_id, device=device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
asset_id = 'asset_id_example' # str | An assetId to select
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.asset_asset_id_post(asset_id, device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->asset_asset_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| An assetId to select | 
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_asset_id_put**
> asset_asset_id_put(asset_id, device=device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
asset_id = 'asset_id_example' # str | An assetId to select
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.asset_asset_id_put(asset_id, device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->asset_asset_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| An assetId to select | 
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_asset_ids_get**
> asset_asset_ids_get(asset_ids)

MTConnect asset request

Returns a set of assets identified by asset ids `asset` separated by semi-colon (;)

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
asset_ids = 'asset_ids_example' # str | Semi-colon (;) separated list of assetIds

try:
    # MTConnect asset request
    api_instance.asset_asset_ids_get(asset_ids)
except ApiException as e:
    print("Exception when calling DefaultApi->asset_asset_ids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | **str**| Semi-colon (;) separated list of assetIds | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_delete**
> asset_delete(device=device, type=type)

Delete all assets for a device and type

Device and type are optional. If they are not given, it assumes there is no constraint

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Delete all assets for a device and type
    api_instance.asset_delete(device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->asset_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_get**
> asset_get(count=count, device=device, pretty=pretty, removed=removed, type=type)

MTConnect asset request

Returns up to `count` assets

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
count = 100 # int | Maximum number of entities to include in results (optional) (default to 100)
device = 'device_example' # str | Device UUID or name (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)
removed = false # bool | Boolean indicating if removed assets are included in results (optional) (default to false)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # MTConnect asset request
    api_instance.asset_get(count=count, device=device, pretty=pretty, removed=removed, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Maximum number of entities to include in results | [optional] [default to 100]
 **device** | **str**| Device UUID or name | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]
 **removed** | **bool**| Boolean indicating if removed assets are included in results | [optional] [default to false]
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_post**
> asset_post(device=device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.asset_post(device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->asset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_put**
> asset_put(device=device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.asset_put(device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->asset_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_asset_id_delete**
> assets_asset_id_delete(asset_id)

Delete asset identified by `assetId`

Marks the asset as removed and creates an AssetRemoved event

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
asset_id = 'asset_id_example' # str | An assetId to select

try:
    # Delete asset identified by `assetId`
    api_instance.assets_asset_id_delete(asset_id)
except ApiException as e:
    print("Exception when calling DefaultApi->assets_asset_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| An assetId to select | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_asset_id_post**
> assets_asset_id_post(asset_id, device=device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
asset_id = 'asset_id_example' # str | An assetId to select
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.assets_asset_id_post(asset_id, device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->assets_asset_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| An assetId to select | 
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_asset_id_put**
> assets_asset_id_put(asset_id, device=device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
asset_id = 'asset_id_example' # str | An assetId to select
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.assets_asset_id_put(asset_id, device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->assets_asset_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**| An assetId to select | 
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_asset_ids_get**
> assets_asset_ids_get(asset_ids)

MTConnect assets request

Returns a set assets identified by asset ids `asset` separated by semi-colon (;)

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
asset_ids = 'asset_ids_example' # str | Semi-colon (;) separated list of assetIds

try:
    # MTConnect assets request
    api_instance.assets_asset_ids_get(asset_ids)
except ApiException as e:
    print("Exception when calling DefaultApi->assets_asset_ids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | **str**| Semi-colon (;) separated list of assetIds | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_delete**
> assets_delete(device=device, type=type)

Delete all assets for a device and type

Device and type are optional. If they are not given, it assumes there is no constraint

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Delete all assets for a device and type
    api_instance.assets_delete(device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->assets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_get**
> assets_get(count=count, device=device, pretty=pretty, removed=removed, type=type)

MTConnect assets request

Returns up to `count` assets

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
count = 100 # int | Maximum number of entities to include in results (optional) (default to 100)
device = 'device_example' # str | Device UUID or name (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)
removed = false # bool | Boolean indicating if removed assets are included in results (optional) (default to false)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # MTConnect assets request
    api_instance.assets_get(count=count, device=device, pretty=pretty, removed=removed, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->assets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Maximum number of entities to include in results | [optional] [default to 100]
 **device** | **str**| Device UUID or name | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]
 **removed** | **bool**| Boolean indicating if removed assets are included in results | [optional] [default to false]
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_post**
> assets_post(device=device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.assets_post(device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->assets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assets_put**
> assets_put(device=device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name (optional)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.assets_put(device=device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->assets_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | [optional] 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **current_get**
> current_get(at=at, device_type=device_type, interval=interval, path=path, pretty=pretty)

MTConnect current request

Gets a stapshot of the state of all the observations for all devices optionally filtered by the `path`

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
at = 56 # int | Sequence number at which the observation snapshot is taken (optional)
device_type = 'device_type_example' # str | Values are 'Device' or 'Agent'. Selects only devices of that type. (optional)
interval = 789 # int | Time in ms between publishing data–starts streaming (optional)
path = 'path_example' # str | XPath to filter DataItems matched against the probe document (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)

try:
    # MTConnect current request
    api_instance.current_get(at=at, device_type=device_type, interval=interval, path=path, pretty=pretty)
except ApiException as e:
    print("Exception when calling DefaultApi->current_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at** | **int**| Sequence number at which the observation snapshot is taken | [optional] 
 **device_type** | **str**| Values are &#x27;Device&#x27; or &#x27;Agent&#x27;. Selects only devices of that type. | [optional] 
 **interval** | **int**| Time in ms between publishing data–starts streaming | [optional] 
 **path** | **str**| XPath to filter DataItems matched against the probe document | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_asset_asset_id_post**
> device_asset_asset_id_post(device, asset_id, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
asset_id = 'asset_id_example' # str | An assetId to select
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.device_asset_asset_id_post(device, asset_id, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_asset_asset_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **asset_id** | **str**| An assetId to select | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_asset_asset_id_put**
> device_asset_asset_id_put(device, asset_id, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
asset_id = 'asset_id_example' # str | An assetId to select
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.device_asset_asset_id_put(device, asset_id, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_asset_asset_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **asset_id** | **str**| An assetId to select | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_asset_delete**
> device_asset_delete(device, type=type)

Delete all assets for a device and type

Device and type are optional. If they are not given, it assumes there is no constraint

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Delete all assets for a device and type
    api_instance.device_asset_delete(device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_asset_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_asset_get**
> device_asset_get(device, count=count, device=device, pretty=pretty, removed=removed, type=type)

MTConnect asset request

Returns up to `count` assets for deivce `device`

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
count = 100 # int | Maximum number of entities to include in results (optional) (default to 100)
device = 'device_example' # str | Device UUID or name (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)
removed = false # bool | Boolean indicating if removed assets are included in results (optional) (default to false)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # MTConnect asset request
    api_instance.device_asset_get(device, count=count, device=device, pretty=pretty, removed=removed, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **count** | **int**| Maximum number of entities to include in results | [optional] [default to 100]
 **device** | **str**| Device UUID or name | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]
 **removed** | **bool**| Boolean indicating if removed assets are included in results | [optional] [default to false]
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_asset_post**
> device_asset_post(device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.device_asset_post(device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_asset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_asset_put**
> device_asset_put(device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.device_asset_put(device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_asset_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_assets_asset_id_post**
> device_assets_asset_id_post(device, asset_id, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
asset_id = 'asset_id_example' # str | An assetId to select
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.device_assets_asset_id_post(device, asset_id, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_assets_asset_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **asset_id** | **str**| An assetId to select | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_assets_asset_id_put**
> device_assets_asset_id_put(device, asset_id, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
asset_id = 'asset_id_example' # str | An assetId to select
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.device_assets_asset_id_put(device, asset_id, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_assets_asset_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **asset_id** | **str**| An assetId to select | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_assets_delete**
> device_assets_delete(device, type=type)

Delete all assets for a device and type

Device and type are optional. If they are not given, it assumes there is no constraint

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Delete all assets for a device and type
    api_instance.device_assets_delete(device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_assets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_assets_get**
> device_assets_get(device, count=count, device=device, pretty=pretty, removed=removed, type=type)

MTConnect assets request

Returns up to `count` assets for deivce `device`

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
count = 100 # int | Maximum number of entities to include in results (optional) (default to 100)
device = 'device_example' # str | Device UUID or name (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)
removed = false # bool | Boolean indicating if removed assets are included in results (optional) (default to false)
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # MTConnect assets request
    api_instance.device_assets_get(device, count=count, device=device, pretty=pretty, removed=removed, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_assets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **count** | **int**| Maximum number of entities to include in results | [optional] [default to 100]
 **device** | **str**| Device UUID or name | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]
 **removed** | **bool**| Boolean indicating if removed assets are included in results | [optional] [default to false]
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_assets_post**
> device_assets_post(device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.device_assets_post(device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_assets_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_assets_put**
> device_assets_put(device, type=type)

Upload an asset by identified by `assetId`

Updates or adds an asset with the asset XML in the body

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
type = 'type_example' # str | Only include assets of type `type` in the results (optional)

try:
    # Upload an asset by identified by `assetId`
    api_instance.device_assets_put(device, type=type)
except ApiException as e:
    print("Exception when calling DefaultApi->device_assets_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **type** | **str**| Only include assets of type &#x60;type&#x60; in the results | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_current_get**
> device_current_get(device, at=at, device_type=device_type, interval=interval, path=path, pretty=pretty)

MTConnect current request

Gets a stapshot of the state of all the observations for device `device` optionally filtered by the `path`

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
at = 56 # int | Sequence number at which the observation snapshot is taken (optional)
device_type = 'device_type_example' # str | Values are 'Device' or 'Agent'. Selects only devices of that type. (optional)
interval = 789 # int | Time in ms between publishing data–starts streaming (optional)
path = 'path_example' # str | XPath to filter DataItems matched against the probe document (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)

try:
    # MTConnect current request
    api_instance.device_current_get(device, at=at, device_type=device_type, interval=interval, path=path, pretty=pretty)
except ApiException as e:
    print("Exception when calling DefaultApi->device_current_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **at** | **int**| Sequence number at which the observation snapshot is taken | [optional] 
 **device_type** | **str**| Values are &#x27;Device&#x27; or &#x27;Agent&#x27;. Selects only devices of that type. | [optional] 
 **interval** | **int**| Time in ms between publishing data–starts streaming | [optional] 
 **path** | **str**| XPath to filter DataItems matched against the probe document | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get**
> device_get(device, device_type=device_type, pretty=pretty)

MTConnect probe request

Provides metadata service for the MTConnect Devices information model for device identified by `device` matching `name` or `uuid`.

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
device_type = 'device_type_example' # str | Values are 'Device' or 'Agent'. Selects only devices of that type. (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)

try:
    # MTConnect probe request
    api_instance.device_get(device, device_type=device_type, pretty=pretty)
except ApiException as e:
    print("Exception when calling DefaultApi->device_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **device_type** | **str**| Values are &#x27;Device&#x27; or &#x27;Agent&#x27;. Selects only devices of that type. | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_post**
> device_post(device, time=time)

Non-normative POST to update a value in the agent

The data of the POST contains the dataItem=value observation data

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
time = 'time_example' # str |  (optional)

try:
    # Non-normative POST to update a value in the agent
    api_instance.device_post(device, time=time)
except ApiException as e:
    print("Exception when calling DefaultApi->device_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **time** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_probe_get**
> device_probe_get(device, device_type=device_type, pretty=pretty)

MTConnect probe request

Provides metadata service for the MTConnect Devices information model for device identified by `device` matching `name` or `uuid`.

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
device_type = 'device_type_example' # str | Values are 'Device' or 'Agent'. Selects only devices of that type. (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)

try:
    # MTConnect probe request
    api_instance.device_probe_get(device, device_type=device_type, pretty=pretty)
except ApiException as e:
    print("Exception when calling DefaultApi->device_probe_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **device_type** | **str**| Values are &#x27;Device&#x27; or &#x27;Agent&#x27;. Selects only devices of that type. | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_put**
> device_put(device, time=time)

Non-normative PUT to update a value in the agent

The data of the PUT contains the dataItem=value observation data

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
time = 'time_example' # str |  (optional)

try:
    # Non-normative PUT to update a value in the agent
    api_instance.device_put(device, time=time)
except ApiException as e:
    print("Exception when calling DefaultApi->device_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **time** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_sample_get**
> device_sample_get(device, count=count, device_type=device_type, _from=_from, heartbeat=heartbeat, interval=interval, path=path, pretty=pretty, to=to)

MTConnect sample request

Gets a time series of at maximum `count` observations for device `device` optionally filtered by the `path` and starting at `from`. By default, from is the first available observation known to the agent

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device = 'device_example' # str | Device UUID or name
count = 100 # int | Maximum number of entities to include in results (optional) (default to 100)
device_type = 'device_type_example' # str | Values are 'Device' or 'Agent'. Selects only devices of that type. (optional)
_from = 56 # int | Sequence number at to start reporting observations (optional)
heartbeat = 10000 # int | Time in ms between publishing a empty document when no data has changed (optional) (default to 10000)
interval = 789 # int | Time in ms between publishing data–starts streaming (optional)
path = 'path_example' # str | XPath to filter DataItems matched against the probe document (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)
to = 56 # int | Sequence number at to stop reporting observations (optional)

try:
    # MTConnect sample request
    api_instance.device_sample_get(device, count=count, device_type=device_type, _from=_from, heartbeat=heartbeat, interval=interval, path=path, pretty=pretty, to=to)
except ApiException as e:
    print("Exception when calling DefaultApi->device_sample_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | **str**| Device UUID or name | 
 **count** | **int**| Maximum number of entities to include in results | [optional] [default to 100]
 **device_type** | **str**| Values are &#x27;Device&#x27; or &#x27;Agent&#x27;. Selects only devices of that type. | [optional] 
 **_from** | **int**| Sequence number at to start reporting observations | [optional] 
 **heartbeat** | **int**| Time in ms between publishing a empty document when no data has changed | [optional] [default to 10000]
 **interval** | **int**| Time in ms between publishing data–starts streaming | [optional] 
 **path** | **str**| XPath to filter DataItems matched against the probe document | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]
 **to** | **int**| Sequence number at to stop reporting observations | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **probe_get**
> probe_get(device_type=device_type, pretty=pretty)

MTConnect probe request

Provides metadata service for the MTConnect Devices information model for all devices.

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device_type = 'device_type_example' # str | Values are 'Device' or 'Agent'. Selects only devices of that type. (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)

try:
    # MTConnect probe request
    api_instance.probe_get(device_type=device_type, pretty=pretty)
except ApiException as e:
    print("Exception when calling DefaultApi->probe_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type** | **str**| Values are &#x27;Device&#x27; or &#x27;Agent&#x27;. Selects only devices of that type. | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> root_get(device_type=device_type, pretty=pretty)

MTConnect probe request

Provides metadata service for the MTConnect Devices information model for all devices.

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
device_type = 'device_type_example' # str | Values are 'Device' or 'Agent'. Selects only devices of that type. (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)

try:
    # MTConnect probe request
    api_instance.root_get(device_type=device_type, pretty=pretty)
except ApiException as e:
    print("Exception when calling DefaultApi->root_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type** | **str**| Values are &#x27;Device&#x27; or &#x27;Agent&#x27;. Selects only devices of that type. | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_get**
> sample_get(count=count, device_type=device_type, _from=_from, heartbeat=heartbeat, interval=interval, path=path, pretty=pretty, to=to)

MTConnect sample request

Gets a time series of at maximum `count` observations for all devices optionally filtered by the `path` and starting at `from`. By default, from is the first available observation known to the agent

### Example
```python
from __future__ import print_function
import time
import cppagent
from cppagent.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cppagent.DefaultApi()
count = 100 # int | Maximum number of entities to include in results (optional) (default to 100)
device_type = 'device_type_example' # str | Values are 'Device' or 'Agent'. Selects only devices of that type. (optional)
_from = 56 # int | Sequence number at to start reporting observations (optional)
heartbeat = 10000 # int | Time in ms between publishing a empty document when no data has changed (optional) (default to 10000)
interval = 789 # int | Time in ms between publishing data–starts streaming (optional)
path = 'path_example' # str | XPath to filter DataItems matched against the probe document (optional)
pretty = false # bool | Instructs the result to be pretty printed (optional) (default to false)
to = 56 # int | Sequence number at to stop reporting observations (optional)

try:
    # MTConnect sample request
    api_instance.sample_get(count=count, device_type=device_type, _from=_from, heartbeat=heartbeat, interval=interval, path=path, pretty=pretty, to=to)
except ApiException as e:
    print("Exception when calling DefaultApi->sample_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Maximum number of entities to include in results | [optional] [default to 100]
 **device_type** | **str**| Values are &#x27;Device&#x27; or &#x27;Agent&#x27;. Selects only devices of that type. | [optional] 
 **_from** | **int**| Sequence number at to start reporting observations | [optional] 
 **heartbeat** | **int**| Time in ms between publishing a empty document when no data has changed | [optional] [default to 10000]
 **interval** | **int**| Time in ms between publishing data–starts streaming | [optional] 
 **path** | **str**| XPath to filter DataItems matched against the probe document | [optional] 
 **pretty** | **bool**| Instructs the result to be pretty printed | [optional] [default to false]
 **to** | **int**| Sequence number at to stop reporting observations | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

