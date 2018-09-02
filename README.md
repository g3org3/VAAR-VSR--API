# EPAV-API

Is developed in python to expose the `epav` a.k.a. "The Validator" features through a RESTful API.

- python
- flask
- epav-core

## Index - Overview

`GET /api/config`

`GET /api/tosca-conf`

`GET /api/rules`

`GET /api/output.smt`

`GET /api/output.json`

`GET /api/maindata.json`

`POST /api/config`

`POST /api/tosca-conf`

`POST /api/rules`

`GET /api/run`



### CURL Example

```sh
CONFIG=`cat path/to/config/file`
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"data":"$CONFIG"}' \
  http://localhost:5000/api/config
```

### Python Example

```python
import requests
import json

# set correct headers
headers = { "Content-Type": "application/json" }

# read file or grab content of the config
configFileContent = file('path/to/config/file').read()

# python:Dictionary -> json:objects
payload = json.dumps({ "data": configFileContent })

# make the request
requests.post('http://localhost:5000/api/config', data=payload, headers=headers)
```



## Endpoints



### CONFIG

#### - read

HTTP Request

`GET /api/config`

Response:

```
timeout=60
suggestions=0
maxChanges=10
apiOutput=
experimental=1
optimize=1
```

#### - write

HTTP Request

`POST /api/config`

Headers:

```
Content-Type: 'application/json'
```

Body/Payload:

```
{
    "data": "timeout=60\nsuggestions=0\n"
}
```





### TOSCA-CONF

#### - read

HTTP Request

`GET /api/tosca-conf`

Response:

```
tosca_definitions_version: tosca_simple_profile_for_nfv_1_0_0
description: example of a SFC VSR

topology_template:
  node_templates:
  . . .
```

#### - write

HTTP Request

`POST /api/tosca-conf`

Headers:

```
Content-Type: 'application/json'
```

Body/Payload:

```
{
    "data": "tosca_definitions_version: tosca_simple_profile_for_nfv_1_0_0\ndescription: example of a SFC VSR\n\ntopology_template:"
}
```



### RULES

#### - read

HTTP Request

`GET /api/rules`

Response:

```
;;for vdu in vdus
(and
  (< vdu.mem_size 600 MB )
  (> vdu.num_cpus 0 )
  (< vdu.num_cpus 6 )
)
```

#### - write

HTTP Request

`POST /api/rules`

Headers:

```
Content-Type: 'application/json'
```

Body/Payload:

```
{
    "data": ";;for vdu in vdus\n(and\n  (< vdu.mem_size 600 MB )\n  (> vdu.num_cpus 0 )\n  (< vdu.num_cpus 6 )\n)"
}
```



### OUTPUT.smt

#### - read

HTTP Request

`GET /api/output.smt`

Response:

```

;;-----------------------------
;;  VDUS Setup
;;  tosca.nodes.nfv.VDU
;;-----------------------------
(declare-const vdus (Array Int (Array String Int)))
(declare-const props_vdu_0 (Array String Int))
(declare-const props_vdu_1 (Array String Int))
(declare-const props_vdu_2 (Array String Int))
(declare-const vdus_size Int)
```





### OUTPUT.json

HTTP Request

`GET /api/output.json`

Response:

```json
{
  "quitReason": {
    "output": "Max suggestions found (0)",
    "reason": "MaxSolutions",
    "data": 0
  },
  "suggestions": [],
  "totalVariables": 9,
  "FPIssues": {},
  "time": 0.02187204360961914,
  "sat": "unsat"
}
```



### MAINDATA.json

The state of the validator, great for debuging

HTTP Request

`GET /api/maindata.json`

Response:

```json
{
  "blob": null,
  "customTypes": [],
  "custom_rules": "files/rules.smt",
  "nested": {},
  "nodes": {
    "tosca.nodes.nfv.CP": ["..."],
    "tosca.nodes.nfv.VDU": [
      {
        "name": "VDU1",
        "props": {
          "architecture": "x86_64",
          "disk_size": "100 GB",
          "distribution": "Debian",
          "max_instances": 1,
          "mem_size": "2GB",
          "min_instances": 1,
          "num_cpus": 2,
          "secure": true,
          "type": "linux",
          "version": 9.5
        },
        "type": "tosca.nodes.nfv.VDU"
      }
	],
    "tosca.nodes.nfv.VL": ["..."],
    "tosca.nodes.nfv.VNF": ["..."]
  },
  "optimized": true,
  "rules": {
    "attributes": [
      "mem_size",
      "num_cpus",
      "address",
      "nsh_aware"
    ]
  },
  "sizes": {
    "cps": 4,
    "fps": 2,
    "networks": 0,
    "vdus": 4,
    "vls": 2,
    "vms": 0,
    "vnfs": 4
  },
  "skipIDs": [],
  "stringsHashMap": {},
  "types": {
    "cps": "tosca.nodes.nfv.CP",
    "fps": "tosca.nodes.nfv.FP",
    "networks": "tosca.nodes.network.Network",
    "vdus": "tosca.nodes.nfv.VDU",
    "vls": "tosca.nodes.nfv.VL",
    "vms": "tosca.nodes.Compute",
    "vnfs": "tosca.nodes.nfv.VNF"
  },
  "valueTypes": {
    "mem_size": "size",
    "nsh_aware": "bool",
    "num_cpus": "int"
  },
  "variables": {
    "names": [
      "VDU2.props_vdu_2.num_cpus",
      "LB.props_vnf_0.nsh_aware",
      "FW.props_vnf_1.nsh_aware",
      "NAT.props_vnf_2.nsh_aware"
    ],
    "total": 9
  }
}
```



### RUN

HTTP Request

`GET /api/run`

Response:

```
NFS
⚠️  ForwardingPath2
  |> Found loop!
    • Length: 3
    •    CPs: CP11, CP21, CP31

User Rules
  ⚠️ unsat
Max suggestions found (0)
time (seconds)  : 0.0218720436096
```

