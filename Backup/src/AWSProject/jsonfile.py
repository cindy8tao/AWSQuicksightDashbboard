from csv import excel
import datetime
from importlib.resources import Resource
from urllib.request import Request
import boto3
import json
import pprint


class JsonFile:

    def create_json_manifest_file(self, uri, uri_prefixes):
        json_file = {
            "fileLocations": [
                {
                    "URIs": [
                        uri
                    ]
                },
                {
                    "URIPrefixes": [
                        uri_prefixes
                    ]
                }
            ],
            "globalUploadSettings": {
                "format": "JSON",
                "delimiter": ",",
                "textqualifier": "'",
                "containsHeader": "true"
            }
        }

        manifest = json.dumps(json_file)
        with open('manifest.json', 'a') as outfile:
            outfile.write(json.dumps(manifest))
            outfile.close()

        # return manifest