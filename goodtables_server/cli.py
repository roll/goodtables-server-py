# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import click
import logging
from aiohttp import web
from concurrent.futures import ProcessPoolExecutor
from .handler import Handler


# Module API

@click.command()
@click.option('--host', default='localhost')
@click.option('--port', default=5000)
@click.option('--path', default='/')
@click.option('--inspector', default=None)
def cli(host, port, path, inspector):
    logging.basicConfig(level=logging.DEBUG)
    handler = Handler(inspector)
    app = web.Application()
    app['executor'] = ProcessPoolExecutor()
    app.router.add_route('GET', path, handler.handle)
    web.run_app(app, host=host, port=port)


# Main program

if __name__ == '__main__':
    cli()
