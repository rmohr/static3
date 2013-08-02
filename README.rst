.. -*- mode: rst; coding: utf-8 -*-

static3 - A really simple WSGI way to serve static (or mixed) content.
====================================================================================

:Authors: Roman Mohr <roman@fenkhuber.at>
:Version: 0.5
:Date: 2013-08-06
:Code: https://github.com/rmohr/static3

.. contents:: Table of Contents
  :backlinks: top

This software is a Python3 compatible fork of Luke Arnos library static_.

The library is now Python3 compatible and Genshi_ support (the sucessor of
kid_) is added. On Python2 Genshi and/or kid can be used as template engine. On
Python3 only Genshi is available.

This library provides an easy way to include static content
in your WSGI applications. There is a convenience method for serving
files located via pkg_resources. There are also facilities for serving
mixed (static and dynamic) content using "magic" file handlers.
Python builtin string substitution and Genshi template support are provided
and it is easy to roll your own handlers. Note that this distribution
does not require Genshi unless you want to use that type of template. Also
provides a command of the same name as a convenience when you just want
to share a little content over HTTP, ad hoc.

Installation and Usage
----------------------

TODO

.. _static: https://pypi.python.org/pypi/static
.. _kid: https://pypi.python.org/pypi/kid
.. _Genshi: https://pypi.python.org/pypi/Genshi
