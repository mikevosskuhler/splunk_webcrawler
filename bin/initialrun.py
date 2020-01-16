#!/usr/bin/env python3
# coding=utf-8
#
# Copyright © 2011-2015 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import absolute_import, division, print_function, unicode_literals
import app
import os,sys
import time
from fetch_product_list import get_urls
import csv
import lxml

splunkhome = os.environ['SPLUNK_HOME']
sys.path.append(os.path.join(splunkhome, 'etc', 'apps', 'searchcommands_app', 'lib'))
from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators
from splunklib.six.moves import range


@Configuration()
class generate_product_list(GeneratingCommand):

    url = Option(require=True)
    vendor = Option(require=True)
    print(type(url))

    def generate(self):
        self.logger.debug("Generating %s events" % self.url)
        urls = get_urls(self.url, self.vendor)
        n = 0
        for i in urls:
            product_name = i[0]
            product_url = i[1]
            text = f'product_name={product_name}, product_url={product_url}'
            yield {'_time': time.time(), 'event_no': n, '_raw': text}
            n += 1 

dispatch(generate_product_list, sys.argv, sys.stdin, sys.stdout, __name__)