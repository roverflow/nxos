#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Cisco and/or its affiliates.
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
The module file for nxos_bfd_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: nxos_bfd_interfaces
short_description: BFD interfaces resource module
description: Manages attributes of Bidirectional Forwarding Detection (BFD) on the
  interface.
version_added: 1.0.0
author: Chris Van Heuveln (@chrisvanheuveln)
notes:
- Tested against NX-OS 7.0(3)I5(1).
- Feature bfd should be enabled for this module.
options:
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the NX-OS device
      by executing the command B(show running-config | section '^interface|^feature
      bfd').
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  config:
    description: The provided configuration
    type: list
    elements: dict
    suboptions:
      name:
        type: str
        description: The name of the interface.
      bfd:
        type: str
        description:
        - Enable/Disable Bidirectional Forwarding Detection (BFD) on the interface.
        choices:
        - enable
        - disable
      echo:
        type: str
        description:
        - Enable/Disable BFD Echo functionality on the interface.
        choices:
        - enable
        - disable
  state:
    description:
    - The state of the configuration after module completion
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged

"""
EXAMPLES = """
# Using deleted

- name: Configure interfaces
  cisco.nxos.nxos_bfd_interfaces:
    state: deleted


# Using merged

- name: Configure interfaces
  cisco.nxos.nxos_bfd_interfaces:
    config:
    - name: Ethernet1/1
      bfd: enable
      echo: enable
    - name: Ethernet1/2
      bfd: disable
      echo: disable
    state: merged


# Using overridden

- name: Configure interfaces
  cisco.nxos.nxos_bfd_interfaces:
    config:
    - name: Ethernet1/1
      bfd: enable
      echo: enable
    - name: Ethernet1/2
      bfd: disable
      echo: disable
    state: overridden


# Using replaced

- name: Configure interfaces
  cisco.nxos.nxos_bfd_interfaces:
    config:
    - name: Ethernet1/1
      bfd: enable
      echo: enable
    - name: Ethernet1/2
      bfd: disable
      echo: disable
    state: replaced

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_bfd_interfaces:
    config:
    - name: Ethernet1/800
      bfd: enable
      echo: enable
    - name: Ethernet1/801
      bfd: disable
      echo: disable
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#   - "interface Ethernet1/800"
#   - "bfd"
#   - "bfd echo"
#   - "interface Ethernet1/801"
#   - "no bfd"
#   - "no bfd echo"

# Using parsed

# parsed.cfg
# ------------

# feature bfd
# interface Ethernet1/800
#   no switchport
#   no bfd
#   no bfd echo
# interface Ethernet1/801
#   no switchport
#   no bfd
# interface Ethernet1/802
#   no switchport
#   no bfd echo
# interface mgmt0
#   ip address dhcp
#   vrf member management

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_bfd_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------

# parsed:
#   - bfd: disable
#     echo: disable
#     name: Ethernet1/800
#   - bfd: disable
#     echo: enable
#     name: Ethernet1/801
#   - bfd: enable
#     echo: disable
#     name: Ethernet1/802
#   - bfd: enable
#     echo: enable
#     name: mgmt0

# Using gathered

# Existing device config state
# -------------------------------

# feature bfd
# interface Ethernet1/1
#   no switchport
#   no bfd
# interface Ethernet1/2
#   no switchport
#   no bfd echo
# interface mgmt0
#   ip address dhcp
#   vrf member management

- name: Gather bfd_interfaces facts from the device using nxos_bfd_interfaces
  cisco.nxos.nxos_bfd_interfaces:
    state: gathered

# Task output (redacted)
# -----------------------
# gathered:
# - name: Ethernet1/1
#   bfd: disable
#   echo: enable
# - name: Ethernet1/3
#   echo: disable
#   bfd: enable
# - name: mgmt0
#   bfd: enable
#   echo: enable
"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['interface Ethernet1/1', 'no bfd', 'no bfd echo']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.argspec.bfd_interfaces.bfd_interfaces import (
    Bfd_interfacesArgs,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.config.bfd_interfaces.bfd_interfaces import (
    Bfd_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=Bfd_interfacesArgs.argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    result = Bfd_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
