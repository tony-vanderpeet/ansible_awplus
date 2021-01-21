#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The facts class for awplus
this file validates each subset of facts and selectively
calls the appropriate facts gathering function
"""

from ansible_collections.alliedtelesis.awplus.plugins.module_utils.network.awplus.argspec.facts.facts import FactsArgs
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts import (
    FactsBase,
)
from ansible_collections.alliedtelesis.awplus.plugins.module_utils.network.awplus.facts.l3_interfaces.l3_interfaces import L3_interfacesFacts
from ansible_collections.alliedtelesis.awplus.plugins.module_utils.network.awplus.facts.lacp.lacp import LacpFacts
from ansible_collections.alliedtelesis.awplus.plugins.module_utils.network.awplus.facts.lag_interfaces.lag_interfaces import Lag_interfacesFacts
from ansible_collections.alliedtelesis.awplus.plugins.module_utils.network.awplus.facts.lldp_global.lldp_global import Lldp_globalFacts
from ansible_collections.alliedtelesis.awplus.plugins.module_utils.network.awplus.facts.static_lag_interfaces.static_lag_interfaces import (
    Static_lag_interfacesFacts,
)


FACT_LEGACY_SUBSETS = {}
FACT_RESOURCE_SUBSETS = dict(
    l3_interfaces=L3_interfacesFacts,
    lacp=LacpFacts,
    lag_interfaces=Lag_interfacesFacts,
    lldp_global=Lldp_globalFacts,
    static_lag_interfaces=Static_lag_interfacesFacts,
)


class Facts(FactsBase):
    """ The fact class for awplus
    """

    VALID_LEGACY_GATHER_SUBSETS = frozenset(FACT_LEGACY_SUBSETS.keys())
    VALID_RESOURCE_SUBSETS = frozenset(FACT_RESOURCE_SUBSETS.keys())

    def __init__(self, module):
        super(Facts, self).__init__(module)

    def get_facts(self, legacy_facts_type=None, resource_facts_type=None, data=None):
        """ Collect the facts for awplus

        :param legacy_facts_type: List of legacy facts types
        :param resource_facts_type: List of resource fact types
        :param data: previously collected conf
        :rtype: dict
        :return: the facts gathered
        """
        if self.VALID_RESOURCE_SUBSETS:
            self.get_network_resources_facts(FACT_RESOURCE_SUBSETS, resource_facts_type, data)

        if self.VALID_LEGACY_GATHER_SUBSETS:
            self.get_network_legacy_facts(FACT_LEGACY_SUBSETS, legacy_facts_type)

        return self.ansible_facts, self._warnings
