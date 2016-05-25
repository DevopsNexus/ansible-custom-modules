#!/usr/bin/python

import urllib2
from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(argument_spec={"url": {"required": True, "type": "str" }})
    response = urllib2.urlopen(module.params["url"])
    module.exit_json(changed=True, meta={"return_code":response.code})

if __name__ == '__main__':  
    main()
