# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import six
import json
import click
import asyncio
import logging
from aiohttp import web
from functools import partial
from importlib import import_module
from concurrent.futures import ProcessPoolExecutor
from goodtables import Inspector, exceptions


# Module API

@click.command()
@click.option('--host', default='localhost')
@click.option('--port', default=5000)
@click.option('--path', default='/')
@click.option('--inspector', default=None)
def cli(host, port, path, inspector):
    logging.basicConfig(level=logging.DEBUG)
    handler = _Handler(inspector)
    app = web.Application()
    app['executor'] = ProcessPoolExecutor()
    app.router.add_route('GET', path, handler.handle)
    web.run_app(app, host=host, port=port)


# Internal

class _Handler(object):

    # Public

    def __init__(self, inspector=None):
        if inspector is None:
            inspector = Inspector()
        elif isinstance(inspector, six.string_types):
            module, name = inspector.rsplit(':', 1)
            inspector = getattr(import_module(module), name)
        self.__inspector = inspector

    async def handle(self, req):
        options = req.GET.copy()
        source = options.pop('source')
        profile = options.pop('profile', 'table')
        inspect = partial(self.__inspector.inspect, source, profile=profile, **options)
        report = await req.app.loop.run_in_executor(req.app['executor'], inspect)
        return web.json_response(report)


# Main program

if __name__ == '__main__':
    cli()
