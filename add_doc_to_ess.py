#!/bin/env python
#Example code, adding a document to an index inside an AWS ElasticSearch

from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3
import json
import sys

#Example:
#python add_doc_to_ess.py 'https://vpc-ess-dovi-es-43wyabmkqtssyezmtpavqnivny.us-east-2.es.amazonaws.com'

host = sys.argv[1].replace('http://','').replace('https://','')
region = sys.argv[2] # e.g. us-east-2

service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

document = {
    "title": "Moneyball",
    "director": "Bennett Miller",
    "year": "2011"
}

es.index(index="movies", doc_type="_doc", id="5", body=document)
data = es.get(index="movies", doc_type="_doc", id="5")

#print(type(data)) #dict
print(json.dumps(data)) #printing as json
