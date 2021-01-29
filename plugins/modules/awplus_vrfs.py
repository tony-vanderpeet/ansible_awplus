#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2021 Allied Telesis
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for awplus_vrfs
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'network'
}

DOCUMENTATION = """
---
module: awplus_vrfs
version_added: 2.9
short_description: Manage VRF definition on Allied Telesis devices.
description: This module manages properties of VRFs on Allied Telesis AlliedWare Plus devices, allowing the
             creation, deletion and modification of VRFs. These are referenced by the VRF name by other
             modules.
author: Tony van der Peet
notes:
- Tested against AlliedWare Plus on SBx908NG.
options:
  config:
    description: A list of VRF configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - name of the VRF (the main reference)
        type: str
        required: True
      id:
        description:
        - numerical ID of the VRF used for internal operation.
        - the range is from 1 to 600
        - note that this is not a required parameter in Alliedware Plus devices, but is for Ansible operations.
        type: str
        required: True
      description:
        description:
        - general format text describing this VRF in user terms.
        type: str
      route_target:
        description:
        - list of route target descriptors associated with this VRF.
        type: list
        element: dict
        suboptions:
          target:
            description:
            - the route target descriptor
            - can be <asn#>:<n> or <ip address>:<n>
            type: str
          direction:
            description:
            - which direction to apply this route target
            type: str
            choices:
              - import
              - export
              - both
      export_map:
        description:
        - reference to a route map used to control export of routes from the VRF.
        type: str
      import_map:
        description:
        - reference to a route map used to control import of routes into the VRF.
        type:: str
      max_fib_routes:
        description:
        - the maximum number of routes allowed for this VRF.
        type: str
      max_fib_routes_warning:
        description:
        - control warnings when number of routes gets too high.
        - this can be a number from 1-100 to set a percentage level when warnings start.
        - or the string "warning-only" to allow the limit to be exceeded with only warnings.
        type: str
      max_static_routes:
        description:
        - maximum number of static routes allowed in this VRF.
        - the range is 1 to 65535, with an initial value of 1000.
        type: str
      rd:
        description:
        - route distinguisher for this VRF for use in BGP.
        - must be formatted as <ANS#>:<n> or <IP address>:<n>
        type: str
      router_id:
        description:
        - router ID to use when routing protocols use this VRF.
        - should take the form of an IPv4 address (a.b.c.d)
        type: str
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
# Using merged

# Before:
# -------
#
# ip vrf bob 1
#  description VRF for Bob
#  max-fib-routes 234 warning-only
# ip vrf bill 2
#  description VRF for Bill
#  max-static-routes 200

- name: Change VRF description
  alliedtelesis.awplus.awplus_vrfs:
    config:
      name: bob
      id: 1
      description: VRF for Bob and family

# After:
# ------
#
# ip vrf bob 1
#  description VRF for Bob and family
#  max-fib-routes 234 warning-only
# ip vrf bill 2
#  description VRF for Bill
#  max-static-routes 200


# Using replaced

# Before:
# -------
#
# ip vrf bob 1
#  description VRF for Bob
#  max-fib-routes 234 warning-only
# ip vrf bill 2
#  description VRF for Bill
#  max-static-routes 200

- name: Change VRF description
  alliedtelesis.awplus.awplus_vrfs:
    config:
      name: bob
      id: 1
      description: VRF for Bob and family
    state: replaced

# After:
# ------
#
# ip vrf bob 1
#  description VRF for Bob and family
# ip vrf bill 2
#  description VRF for Bill
#  max-static-routes 200


# Using overridden

# Before:
# -------
#
# ip vrf bob 1
#  description VRF for Bob
#  max-fib-routes 234 warning-only
# ip vrf bill 2
#  description VRF for Bill
#  max-static-routes 200

- name: Change VRF description
  alliedtelesis.awplus.awplus_vrfs:
    config:
      name: bob
      id: 1
      description: VRF for Bob and family
      max-fib-routes: 234
      max_fib_routes_warning: warning_only
      max-static-routes: 200
    state: overridden

# After:
# ------
#
# ip vrf bob 1
#  description VRF for Bob and family
#  max-fib-routes 234 warning-only
#  max-static-routes 200


# Using deleted

# Before:
# -------
#
# ip vrf bob 1
#  description VRF for Bob
#  max-fib-routes 234 warning-only
# ip vrf bill 2
#  description VRF for Bill
#  max-static-routes 200

- name: Change VRF description
  alliedtelesis.awplus.awplus_vrfs:
    config:
      name: bob
      id: 1
    state: deleted

# After:
# ------
#
# ip vrf bill 2
#  description VRF for Bill
#  max-static-routes 200


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.alliedtelesis.awplus.plugins.module_utils.network.awplus.argspec.vrfs.vrfs import VrfsArgs
from ansible_collections.alliedtelesis.awplus.plugins.module_utils.network.awplus.config.vrfs.vrfs import Vrfs


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=VrfsArgs.argument_spec,
                           supports_check_mode=True)

    result = Vrfs(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()