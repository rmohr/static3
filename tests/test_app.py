#
# Copyright 2013 Roman Mohr <roman@fenkhuber.at>
#
# This file is part of static3.
#
# static3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

import pytest
import webtest

import sys


@pytest.fixture
def _cling():
    from static import Cling
    return Cling(root="testdata/pub")


@pytest.fixture
def _shock():
    from static import Shock, StringMagic, KidMagic, GenshiMagic
    magics = (StringMagic(title="String Test"),
              KidMagic(title="Kid Test"), GenshiMagic(title="Genshi Test"))
    return Shock(root="testdata/pub", magics=magics)

@pytest.fixture
def ascii_shock(_shock):
    _shock.encoding='ascii'
    return webtest.TestApp(_shock)

@pytest.fixture
def cling(_cling):
    return webtest.TestApp(_cling)


@pytest.fixture
def shock(_shock):
    return webtest.TestApp(_shock)


@pytest.mark.skipif("sys.version_info >= (3,0)")
def test_kid(shock):
    response = shock.get("/kid.html.kid")
    assert "Title: Kid Test" in response
    assert "REQUEST_METHOD" in response


def test_genshi(shock):
    response = shock.get("/test.html")
    assert "Title: Genshi Test" in response
    assert "REQUEST_METHOD" in response


def test_string(shock):
    response = shock.get("/sub.html.stp")
    assert "<h1>String Test</h1>" in response
    assert "Path info: /sub.html." in response


def test_static_cling(cling):
    response = cling.get("/index.html")
    assert "Mixed Content" in response
    assert response.content_type == "text/html"
    response = cling.get("/test.xml")
    assert "green" in response
    #dependes on the mimetypes version, both is fine
    assert (response.content_type == "text/xml" 
            or response.content_type == "application/xml")

def test_static_shock(shock):
    response = shock.get("/index.html")
    assert "Mixed Content" in response

@pytest.mark.skipif("sys.version_info >= (3,0)")
def test_encoding(ascii_shock):
    with pytest.raises(UnicodeEncodeError):
        response = ascii_shock.get("/encoding.html")

@pytest.mark.skipif("sys.version_info < (3,0)")
def test_decoding(ascii_shock):
    with pytest.raises(UnicodeDecodeError):
        response = ascii_shock.get("/encoding.html")
