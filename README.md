# goodtables-server

[![Travis](https://img.shields.io/travis/frictionlessdata/goodtables-server/master.svg)](https://travis-ci.org/frictionlessdata/goodtables-server)
[![Coveralls](http://img.shields.io/coveralls/frictionlessdata/goodtables-server.svg?branch=master)](https://coveralls.io/r/frictionlessdata/goodtables-server?branch=master)
[![PyPi](https://img.shields.io/pypi/v/goodtables-server.svg)](https://pypi.python.org/pypi/goodtables-server)
[![SemVer](https://img.shields.io/badge/versions-SemVer-brightgreen.svg)](http://semver.org/)
[![Gitter](https://img.shields.io/gitter/room/frictionlessdata/chat.svg)](https://gitter.im/frictionlessdata/chat)

[under development]

### CLI

A server could be started via CLI:

```
$ python -m goodtables_server.cli --port 5000 --path /api
======== Running on http://localhost:5000/ ========
(Press CTRL+C to quit)
```

Type in the browser (non secure for now):

```
http://localhost:5000/api?source=data/invalid.csv
```

And a report (the same as in the initial example) will be returned as JSON response to the browser.
