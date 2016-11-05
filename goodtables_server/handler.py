# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from aiohttp import web
from functools import partial
from goodtables import Inspector
from importlib import import_module


# Module API

class Handler(object):

    # Public

    def __init__(self, inspector=None):
        if inspector is not None:
            module, name = inspector.rsplit('.', 1)
            inspector = getattr(import_module(module), name)
        else:
            inspector = Inspector()
        self.__inspector = inspector

    async def handle(self, req):
        options = {key: value for key, value in req.GET.items() if value}
        options['preset'] = 'table'
        options['scheme'] = 'http'
        inspect = partial(self.__inspector.inspect, **options)
        report = await req.app.loop.run_in_executor(req.app['executor'], inspect)
        return web.json_response(report)
