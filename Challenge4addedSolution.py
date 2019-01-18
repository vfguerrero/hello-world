import requests
import json

def login():
    url = "http://192.168.10.1/api/aaaLogin.json"
    payload = "{\r\n\t\"aaaUser\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"name\" : \"admin\",\r\n\t\t\t\"pwd\" : \"ciscoapic\"\r\n\t\t}\r\n\t}\r\n}"
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    json_response = json.loads(response.text)
    tokenfromLogin = (json_response['imdata'][0]['aaaLogin']['attributes']['token'])
    return tokenfromLogin

def createtenant(token,tenant):
    url = "http://192.168.10.1/api/node/mo/uni/tn-"+tenant+".json"
    payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-%s\",\r\n\t\t\t\"name\": \"%s\",\r\n\t\t\t\"rn\": \"tn-%s\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}" % (tenant,tenant,tenant)
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json"
    }
    cookie = {"APIC-Cookie" : token}
    response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)
    print(response.text)

def createapppro(token,tenant,apppro):
    url = "http://192.168.10.1/api/node/mo/uni/tn-"+tenant+"/ap-"+apppro+".json"
    payload = "{\r\n\t\"fvAp\": {\r\n\t\"attributes\": {\r\n\t\t\t\"descr\": \"\",\r\n\t\t\t\"dn\": \"uni/tn-%s/ap-%s\",\r\n\t\t\t\"name\": \"%s\",\r\n\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\"ownerTag\": \"\",\r\n\t\t\t\"prio\": \"unspecified\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}" % (tenant,apppro,apppro)
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json"
    }
    cookie = {"APIC-Cookie" : token}
    response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)
    print(response.text)

def createepg(token,tenant,apppro,epg):
    url = "http://192.168.10.1/api/node/mo/uni/tn-"+tenant+"/ap-"+apppro+"/epg-"+epg+".json"
    payload = "{\r\n\t\"fvAEPg\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"descr\": \"\",\r\n\t\t\t\"dn\": \"uni/tn-%s/ap-%s/epg-%s\",\r\n\t\t\t\"matchT\": \"AtleastOne\",\r\n\t\t\t\"name\": \"%s\",\r\n\t\t\t\"prio\": \"unspecified\"\r\n\t\t},\r\n\t\t\"children\": [{\r\n\t\t\t\"fvRsCustQosPol\": {\r\n\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\"tnQosCustomPolName\": \"\"\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t}, {\r\n\t\t\t\"fvRsBd\": {\r\n\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\"tnFvBDName\": \"\"\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t}, {\r\n\t\t\t\"fvCrtrn\": {\r\n\t\t\t\t\"attributes\": {\r\n\t\t\t\t\t\"descr\": \"\",\r\n\t\t\t\t\t\"name\": \"default\",\r\n\t\t\t\t\t\"ownerKey\": \"\",\r\n\t\t\t\t\t\"ownerTag\": \"\"\r\n\t\t\t\t}\r\n\t\t\t}\r\n\t\t}]\r\n\t}\r\n}" % (tenant,apppro,epg,epg)
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json"
    }
    cookie = {"APIC-Cookie" : token}
    response = requests.request("POST", url, data=payload, headers=headers, cookies=cookie)
    print(response.text)

if __name__ == "__main__":
    token = login()
    tenants = ["acme"]
    apppros = ["Accounting"]
    epgs = ["Payroll","Bills"]
    for tenant in tenants:
        createtenant(token,tenant)
        for apppro in apppros:
            createapppro(token,tenant,apppro)
            for epg in epgs:
                createepg(token,tenant,apppro,epg)
