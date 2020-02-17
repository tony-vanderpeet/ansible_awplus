#
# -*- coding: utf-8 -*-
# Copyright 2020 Allied Telesis
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
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
"""
The arg spec for the awplus_lacp module
"""


class LacpArgs(object):  # pylint: disable=R0903
    """The arg spec for the awplus_lacp module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'options': {'system': {'options': {'priority': {'required': True,
                                                                                'type': 'int'}},
                                                       'type': 'dict'}},
                                'type': 'dict'},
                     'state': {'choices': ['merged', 'replaced', 'deleted'],
                               'default': 'merged',
                               'type': 'str'}}  # pylint: disable=C0301