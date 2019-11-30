'''"This endpoint can be used to get the most recent data collected from resources with sensor capabilities. As a consequence, a response will contain at most one value for each of the included capabilities for a given resource. One may use the following parameters to filter the result of the data.\n\n* **uuids** - a list of
    resource identifiers that must be considered to obtain the data.
    You may use *curl* to test it:
    '''



\n```\n$ curl -H \"Content-Type: application/json\" -X POST -d '{\"uuids\":[\"5ad20589-a3db-4521-b1bc-a21dde00a25c\",\"b5d170b5-aaf3-42bc-9e47-58e3fe2a4846\"]}' http://localhost:8000/collector/resources/data/last\n```\n\n\n* **capabilities**
