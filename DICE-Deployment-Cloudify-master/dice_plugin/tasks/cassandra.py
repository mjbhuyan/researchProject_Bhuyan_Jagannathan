# -*- coding: utf-8 -*-

# Copyright (C) 2016 XLAB d.o.o.
#
# This file is part of dice-plugin.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, * WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. * See the
# License for the specific language governing permissions and * limitations
# under the License.
#
# Author:
#     Tadej Borovšak <tadej.borovsak@xlab.si>

from __future__ import absolute_import

from cloudify.decorators import operation


@operation
def gather_seeds(ctx):
    msg = "Copying seed ip address of '{}' into seeds runtime poperty"
    ctx.logger.info(msg.format(ctx.target.instance.id, property))
    address = ctx.target.instance.host_ip
    ctx.source.instance.runtime_properties["seeds"] = [address]
