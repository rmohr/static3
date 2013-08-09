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
def _cling(tmpdir):
    from static import Cling
    return Cling(root="testdata/pub")

@pytest.fixture
def _shock(tmpdir):
    from static import Shock, StringMagic, KidMagic, GenshiMagic
    magics = (StringMagic(title="String Test"),
              KidMagic(title="Kid Test"), GenshiMagic(title="Genshi Test"))
    return Shock(root="testdata/pub", magics=magics)

@pytest.fixture
def cling(_cling):
    return webtest.TestApp(_cling)

@pytest.fixture
def shock(_shock):
    return webtest.TestApp(_shock)

@pytest.mark.skipif("sys.version_info >= (3,0)")
def test_kid(shock):
    pass

def test_genshi(shock):
    pass

def test_string(shock):
    pass

def test_static(shock):
    pass
