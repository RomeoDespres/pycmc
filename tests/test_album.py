import pytest
import pycm
import pandas as pd
import requests.exceptions as exceptions

#.HTTPError as HTTPError

@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()

@pytest.fixture
def dates():
    return {'start': '2018-03-01', 'end': '2018-03-03'}

@pytest.fixture
def srkeys():
    return [
        'id', 
        'name',
        'release_date', 
    ]


def test_metadata(srkeys):
    test = pycm.album.metadata('1119543')
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0
   
    # standard use
    for srelem in srkeys:
        assert srelem in test.keys()
    # standard
    assert isinstance(test['id'], type(1))
    # standard
    assert isinstance(test['name'], type("mystring"))

    # standard
    assert isinstance(test['release_date'], type("str"))
    assert isinstance(
        pd.to_datetime(test['release_date']), 
        type(pd.datetime(2017,1,1))
    )
    # alt test examples, alt tests ~ weird stuff
    try:
        # alt test
        #assert [1, 2, ] == [3, 4]

        test = pycm.album.metadata('Michael Jackson')

    except exceptions.HTTPError as err:
        print(
        f"pycm.album.metadata -> {err}")
    try:
        test = pycm.album.metadata(
            '12394871234598762345'
        )
        assert isinstance(test['id'], type(3))

    except exceptions.HTTPError as err:
        print(f"pycm.album.metadata -> {err}")

def test_tunefind():
    test = pycm.album.tunefind('1119543')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_playlists(dates):
    # playlist placement
    test = pycm.album.playlists('1119543', dates['start'], )
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_charts():
    # 403 Client Error: Forbidden for url
    test = pycm.album.charts('itunes', 1119543, '2018-01-01')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_get_album_ids():
    test = pycm.album.get_album_ids('chartmetric', 1119543)
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_stats():
    test = pycm.album.stats(1119543, 'spotify')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_tracks():
    test = pycm.album.tracks(1119543)
    assert isinstance(test, type(list()))
    assert len(test) > 0
