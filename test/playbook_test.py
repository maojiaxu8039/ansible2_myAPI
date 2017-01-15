#!/usr/bin/env python
# coding:utf8


import sys
sys.path.append("../")
from playbook_runner import PlaybookRunner
from pprint import pprint

host_dict = {
    "group1": {
        'hosts': ["172.16.8.210"],
        'vars': {'host': 'var_value'}
    },
    "_meta":{
        "hostvars":{
            "172.16.8.210":{
                "zone_dirs": ["/home/gjobs3","/home/gjobs2"]
                }
            }
        }
}

host_list = ["172.16.8.210"]


runner = PlaybookRunner(
    playbook_path="debug.yml",
    hosts=host_dict,
    private_key_file="/home/joshua/.ssh/id_rsa_gjobs",
    connection_type="paramiko",
    passwords={"conn_pass": "8ql6,yhY"},
)


try:
    results = runner.run()
    pprint(results)
except Exception as e:
    print e