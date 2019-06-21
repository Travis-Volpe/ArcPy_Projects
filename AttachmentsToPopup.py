import requests, json, arcpy, sys, linecache, ssl

#Parameters
hostedFeatureService = arcpy.GetParameterAsText(0)
agsService = arcpy.GetParameterAsText(1)
federatedServer = arcpy.GetParameterAsText(2)
portalURL = arcpy.GetParameterAsText(3)
username = arcpy.GetParameterAsText(4)
password = arcpy.GetParameterAsText(5)
baseURL = arcpy.GetParameterAsText(6)
fieldName = arcpy.GetParameterAsText(7)

# Disable warnings
requests.packages.urllib3.disable_warnings()

#Report error function
def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    arcpy.AddError('Error:  Line {} -- "{}": {}'.format(lineno, line.strip(), exc_obj))
    sys.exit()

#generate token for AGOL Hosted Feature Service
if hostedFeatureService == 'true':
    if username and password:
        try:
            tokenURL = 'https://www.arcgis.com/sharing/rest/generateToken'
            params = {'f': 'pjson', 'username': username, 'password': password, 'referer': 'https://www.arcgis.com', 'expiration': str(21600)}
            response = requests.post(tokenURL, data = params, verify = False)
            token = response.json()['token']
        except:
            PrintException()
    else:
        token = ''

#generate token for AGS service
if agsService == 'true':
    # If Portal for ArcGIS has a federated server
    if federatedServer == 'true':
        if username and password:
            try:
                # Generate token for Portal
                tokenURL = 'https://' + portalURL + ':7443/arcgis/sharing/rest/generateToken/'
                params = {'f': 'json', 'username': username, 'password': password, 'referer': 'https://' + portalURL, 'expiration': str(1440)}
                response = requests.post(tokenURL, data = params, verify = False)
                token = response.json()['token']
            except:
                PrintException()
        else:
            token = ''

    # If not federated
    if federatedServer == 'false':
        if username and password:
            try:
                server = baseURL.split("//")[1].split("/")[0]
                tokenURL = 'http://' + server + '/arcgis/admin/generateToken'
                params = {'username': username, 'password': password, 'client': 'requestip', 'f': 'pjson', 'expiration': str(1440)}
                response = requests.post(tokenURL, data = params, verify = False)
                token = response.json()['token']
            except:
                PrintException()
        else:
            token = ''

#create OID list
OIDs = []

url = baseURL
params = {'f': 'pjson', 'token': token}
response = requests.post(url, data = params, verify = False)
data = response.json()
if 'error' in data:
    PrintException()
    sys.exit()
else:
    pass

#check if service has attachments
try:
    if data["hasAttachments"] == 1:
        params = {'where': '1=1', 'returnIdsOnly': 'true', 'token': token, 'f': 'json'}
        response = requests.post(url + "/query", data = params, verify = False)
        data = response.json()
        #obtain OBJECTID field
        objectidField = data['objectIdFieldName']
        data['objectIds'].sort()
        for OID in data['objectIds']:
            OIDs.append(OID)
except:
    arcpy.AddError("Feature service does not contain attachments")
    sys.exit()

#iterate through OIDs to see which contain attachments
for OID in OIDs:
    url = baseURL + "/" + str(OID) + "/attachments"
    params = {'f': 'pjson', 'token': token}
    try:
        response = requests.post(url, data = params, verify = False)
    except:
        PrintException()
    data = response.json()
    if len(data['attachmentInfos']) > 0:
        #obtain attachment ID
        id = data['attachmentInfos'][0]['id']

        #update Picture field with URL to attachment
        updateURL = baseURL + '/updateFeatures'
        pictureURL = url + "/" + str(id) + "?token=" + token
        updates = json.dumps([{"attributes" : {str(objectidField): OID, str(fieldName): str(pictureURL)}}])
        params = {'features': updates, 'token': token, 'f': 'json'}
        response = requests.post(updateURL, data = params, verify = False)
        data = response.json()
        if str(data['updateResults'][0]['success']) == 'True':
            arcpy.AddMessage("ObjectID: " + str(data['updateResults'][0]['objectId']) + " successfully updated.")
        elif str(data['updateResults'][0]['success']) == 'False':
            arcpy.AddError("ObjectID: " + str(data['updateResults'][0]['objectId']) + " -- error: " + str(data['updateResults'][0]['error']['description']))

