import os
import json

with open('report.json') as f:
    json_data = json.load(f)

if json_data[0]['score'] >= 0:
    exit(0)
else:
    exit(1)
