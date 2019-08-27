import pytest
import pycm


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


def test_albums():
    test = pycm.artist.albums('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_cpp_data():
    test = pycm.artist.cpp_data('3380', 'rank')
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_charts():
    test = pycm.artist.charts('spotify_viral_daily', '1220', '2019-01-01')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    

def test_fanmetrics(dates):
    test = pycm.artist.fanmetrics('3380', dates['start'])
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0


def test_get_artist_ids():
    test = pycm.artist.get_artist_ids('chartmetric', 4031)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_get_artists():
    test = pycm.artist.get_artists('sp_monthly_listeners', 5000, 10000)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_metadata():
    test = pycm.artist.metadata('3380',) 
    assert isinstance(test, type(dict()))
    assert test is not None


def test_playlists(dates):
    test = pycm.artist.playlists('439', 'spotify', dates['start'], 'current') 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_related():
    test = pycm.artist.related('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_urls():
    test = pycm.artist.urls('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_tracks():
    test = pycm.artist.tracks('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_tunefind():
    test = pycm.artist.tunefind('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_listening(dates):
    test = pycm.artist.listening('3380', dates['start'])
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0
