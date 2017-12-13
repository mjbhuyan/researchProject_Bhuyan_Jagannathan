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

import os
import shutil
import tempfile
import subprocess

from dice_plugin import utils
from cloudify.decorators import operation
from cloudify.exceptions import NonRecoverableError


@operation
def run_script(ctx, script, arguments, resources, language):
    supported_langs = {"bash", "python"}

    if language not in supported_langs:
        msg = "Unknown language: {}. Available languages: {}."
        raise NonRecoverableError(
            msg.format(language, ", ".join(supported_langs))
        )

    workdir = tempfile.mkdtemp()
    ctx.logger.info("Created working directory {}".format(workdir))

    ctx.logger.info("Getting '{}' script".format(script))
    local_script = utils.obtain_resource(ctx, script, dir=workdir,
                                         keep_name=True)
    cmd = map(str, [language, local_script] + arguments)

    ctx.logger.info("Getting resources".format(script))
    for res in resources:
        utils.obtain_resource(ctx, res, dir=workdir, keep_name=True)

    ctx.logger.info("Running command: {}".format(" ".join(cmd)))
    proc = subprocess.Popen(cmd, stdin=open(os.devnull, "r"), cwd=workdir,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in iter(proc.stdout.readline, ""):
        ctx.logger.info(line.strip())
    proc.wait()

    shutil.rmtree(workdir)

    if proc.returncode != 0:
        msg = "Script terminated with non-zero ({}) status."
        raise NonRecoverableError(msg.format(proc.returncode))

    ctx.instance.runtime_properties["ip"] = ctx.instance.host_ip
    ctx.instance.runtime_properties["fqdn"] = utils.get_fqdn()
