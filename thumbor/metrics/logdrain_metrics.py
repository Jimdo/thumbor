#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.utils import logger
from thumbor.metrics import BaseMetrics


class Metrics(BaseMetrics):

    def incr(self, metricname, value=1):
        pass


    def timing(self, metricname, value):
        mappings = self.config.CUSTOM_TIMINGS_MAPPING
        if mappings.has_key(metricname):
            print "logdrain-metrics source=logdrain-metrics sample#%s=%sms" % (mappings.get(metricname), value)
