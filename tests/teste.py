import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
  "question": "How can I contact Lamna Healthcare?",
  "chat_history": []
}

body = str.encode(json.dumps(data))

url = 'https://rag-1976-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCIsImtpZCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzMwZjcwZDdkLThkMzgtNDU5Yi1hM2Y5LTAyMjMzNmYwYTI3MS8iLCJpYXQiOjE3MjkwNTE0MzgsIm5iZiI6MTcyOTA1MTQzOCwiZXhwIjoxNzI5MDU2MjUzLCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFlBQUFBOXNUMUFpVjBSaVRlSXJlZmFSUW83cHd1OFZ2bm9xWElQUFNPMnhOVzBseG1FNVdWRHM3MGRYT1Z4MENsSWhxV3p6MHY5bHRVblBkRVlHTkM1dWFFNjlBaHF3ejdST3Jnek8wS3VCVzNScG89IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiQWRtaW5pc3RyYXRvciIsImdpdmVuX25hbWUiOiJTeXN0ZW0iLCJncm91cHMiOlsiOWVmNjAxNDEtZTQ2ZC00NDBmLTk3ZjktMTYwYTI5MjdmMThjIl0sImlkdHlwIjoidXNlciIsImlwYWRkciI6IjE1OS4xOTYuMTAuMTIiLCJuYW1lIjoiU3lzdGVtIEFkbWluaXN0cmF0b3IiLCJvaWQiOiI2MzM2NDY4NS1iZGQ3LTQ4ODYtODMyOC01ZDI3OTgxNjZhYzEiLCJwdWlkIjoiMTAwMzIwMDNBQzJDNDg1NSIsInJoIjoiMC5BYmNBZlEzM01EaU5tMFdqLVFJak52Q2ljVjl2cGhqZjJ4ZE1uZGNXTkhFcW5MNzhBR2cuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiNTdzcFFQUnF5ekk1SzZyWDI3WDNpMkN2NzBxb3FzMlZpYzB0TU5GRFp3cyIsInRpZCI6IjMwZjcwZDdkLThkMzgtNDU5Yi1hM2Y5LTAyMjMzNmYwYTI3MSIsInVuaXF1ZV9uYW1lIjoiYWRtaW5ATW5nRW52TUNBUDkzODA4Mi5vbm1pY3Jvc29mdC5jb20iLCJ1cG4iOiJhZG1pbkBNbmdFbnZNQ0FQOTM4MDgyLm9ubWljcm9zb2Z0LmNvbSIsInV0aSI6IjZwR0xSNTJlaEV1bmZMRkFHMzgtQUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfaWRyZWwiOiIxIDIifQ.f8-KOlBVMMA_-RhBLORsbGExbJVLY5sKVeezRoJx-6JOYCynlt9_B2cW6nctR2iHREj4fZepnGldy8ItPFZ_7cClVGgGi56VDDo_g6gPCrm97ogavp84502falDnkHM92XrmDeP8XjBnJtoaGeMgafIp44YY7zuqPapxzwKCYTvMahD5I6erRhcA3TrXQnBjXrlJYFTyToe2kWV98NdqwisaPIfqg04PmM3L5ph76SmuMxhhOKqVB0OWavHLE2-SHaKcB1n39Gk0lkD8AYRBqUV_eeov_DR5fdad5J0h2cKvyJrWvL5Bs1iVnrj1P2N72P8r9E-snnXC1LL25-Ti6Q'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))