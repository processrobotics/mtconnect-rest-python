# MTConnect Streaming Test Documentation

## Overview

The test stubs in `test/test_default_api.py` have been configured to test persistent streaming from **demo.mtconnect.org**.

## Test Methods

All four streaming test methods are configured to connect to `https://demo.mtconnect.org`:

### 1. test_current_get
Tests the `/current` endpoint with streaming enabled.
- **Endpoint**: `/current`
- **Interval**: 1000ms (streams data every second)
- **Purpose**: Gets snapshots of current observations with streaming

### 2. test_device_current_get
Tests device-specific `/device/{device}/current` endpoint with streaming.
- **Endpoint**: `/device/{device}/current`
- **Interval**: 1000ms
- **Purpose**: Gets current observations for a specific device with streaming

### 3. test_sample_get
Tests the `/sample` endpoint with streaming enabled.
- **Endpoint**: `/sample`
- **Interval**: 1000ms
- **Heartbeat**: 10000ms
- **Purpose**: Gets time-series sample data with streaming

### 4. test_device_sample_get
Tests device-specific `/device/{device}/sample` endpoint with streaming.
- **Endpoint**: `/device/{device}/sample`
- **Interval**: 1000ms
- **Heartbeat**: 10000ms
- **Purpose**: Gets sample data for a specific device with streaming

## How Streaming Works

When the `interval` parameter is provided:
1. The MTConnect agent starts streaming mode
2. Data is published at the specified interval (in milliseconds)
3. The `_preload_content=False` parameter prevents buffering the entire response
4. The response object can be read incrementally to process stream chunks

## Running the Tests

### Using unittest

```bash
# Run all streaming tests
python -m unittest test.test_default_api.TestDefaultApi.test_sample_get
python -m unittest test.test_default_api.TestDefaultApi.test_current_get
python -m unittest test.test_default_api.TestDefaultApi.test_device_sample_get
python -m unittest test.test_default_api.TestDefaultApi.test_device_current_get
```

### Using the test script directly

```python
import sys
sys.path.insert(0, 'test')
from test_default_api import TestDefaultApi

# Create test instance
test = TestDefaultApi()
test.setUp()

# Run a specific streaming test
test.test_sample_get()
```

## Example: Reading Stream Data

Here's how to actually consume the stream data:

```python
import mtconnect
from mtconnect.rest import ApiException
import time

# Configure API instance
api_instance = mtconnect.DefaultApi()
api_instance.api_client.configuration.host = "https://demo.mtconnect.org"

try:
    # Start streaming
    response = api_instance.sample_get(
        interval=1000,           # Stream every 1 second
        heartbeat=10000,         # Heartbeat every 10 seconds
        _preload_content=False   # Don't buffer entire response
    )
    
    print(f"Stream status: {response.status}")
    
    # Read stream for 60 seconds
    end_time = time.time() + 60
    while time.time() < end_time:
        chunk = response.read(8192)  # Read 8KB chunks
        if chunk:
            # Process chunk (XML/JSON data)
            print(f"Received {len(chunk)} bytes")
        else:
            break
            
except ApiException as e:
    print(f"Error: {e}")
```

## Configuration Details

All tests are configured with:
- **Host**: `https://demo.mtconnect.org`
- **Interval**: `1000` (1 second between updates)
- **Heartbeat**: `10000` (10 seconds, for sample endpoints)
- **Path filter**: `//DataItem[@type="POSITION"]` (XPath filter)
- **Device type**: `'Device'`
- **Preload content**: `False` (enables streaming mode)

## Notes

- The tests will attempt to connect to demo.mtconnect.org when executed
- If the server is not accessible, an `ApiException` will be caught and printed
- The tests are designed to demonstrate the streaming API usage pattern
- For production use, replace with your actual MTConnect agent URL
