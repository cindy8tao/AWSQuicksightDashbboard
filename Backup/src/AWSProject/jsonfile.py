from csv import excel
import datetime
from importlib.resources import Resource
from urllib.request import Request
import boto3
import json
import pprint


class JsonFile:

    def create_json_manifest_file(self, uri, uri_prefixes, format):
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
                "format": format,
                "delimiter": ",",
                "textqualifier": "'",
                "containsHeader": "true"
            }
        }

        manifest = json.dumps(json_file, indent=4)
        # manifest = json.dumps(json_file)
        with open('manifest.json', 'a') as outfile:
            outfile.write(manifest)
            outfile.close()

        return json_file
