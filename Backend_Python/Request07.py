import requests
import json

base_url = "https://br.leanix.net"
endpointADRs = "/services/documents/v1/documents"
token_acess = ""
url = f"{base_url}{endpointADRs}"

print(f"\nURL base e endpoint das ADRs: {url}\n")

headers = {
    "Content-Type": ""
}