import json
import mtconnect
from mtconnect.rest import ApiException 
import logging

# create an instance of the API class
api_instance = mtconnect.DefaultApi()
api_instance.api_client.configuration.host = "http://192.168.0.224:5000"
api_instance.api_client.set_default_header('Accept', 'application/json')
device_type = 'Agent' # str | Values are 'Device' or 'Agent'. Selects only devices of that type. (optional)
pretty = False # bool | Instructs the result to be pretty printed (optional) (default to false)

# Get the MTConnect logger
logger = logging.getLogger('mtconnect')
logger.setLevel(logging.INFO)

def log_stuff(data):
	logger.info(f"Header: {data['MTConnectDevices']['Header']}")

try:
	# MTConnect probe request
	ret = api_instance.probe_get(device_type=device_type, pretty=pretty)
	stuff = api_instance.api_client.last_response
	assert stuff.status == 200
	probe_obj = json.loads(stuff.data)
	logger.info("Probe:")
	for key, value in probe_obj['MTConnectDevices']['Header'].items():
		logger.info(f"{key}: {value}")
	for device in probe_obj['MTConnectDevices']['Devices']:
		try:
			if device['Agent']:
				logger.info(f"Agent: {device['Agent']['uuid']}")
		except KeyError:
			logger.info(f"Device: {device['Device']['uuid']}")
except ApiException as e:
	print("Exception when calling DefaultApi->probe_get: %s\n" % e)

# try:
# 	ret = api_instance.device_probe_get(device="mxi_m001")
# 	# json_data = json.loads(ret)
# 	log_stuff(ret)
# except ApiException as e:
# 	print("Exception when calling DefaultApi->device_probe_get: %s\n" % e)