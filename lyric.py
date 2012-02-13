from constants import Constants
from json import loads
import httplib2
from urllib import urlencode
import copy

class LyricApi(object):
  def __init__(self):
    return

  def song_look_up_by_lyric(self, lyric):
    args = {
      'reqtype': 'default',
      'searchtype': 'track',
      'lyrics': lyric,
      'displaykey': Constants.LYRICFIND_DISPLAY,
    }
    lyric_response = self._look_up('search', **args)

    return lyric_response.get('tracks', [])[0]

  def get_lyric_for_song(self, id):
    args = {
          'reqtype': 'default',
          'searchtype': 'track',
          'trackid': 'amg:' + str(id),
          'lrckey': Constants.LYRICFIND_DISPLAY,
          'format': 'lrc',
          'alltracks': 'no',
        }
    lyric_response = self._look_up('lyric', **args)
    lyric_track = lyric_response.get('track')
    if lyric_track:
      valid_lyric = lyric_track.get('flattened')
      return valid_lyric
    return None
  def _look_up(self, api , **kwargs):
    args = copy.copy(kwargs)
    args.update({
      'apikey': Constants.LYRICFIND_API[api],
      'output': 'json',
    })
    look_up_url = "http://test.lyricfind.com/api_service/"
    look_up_url += api +'.do?'
    encoded_args = urlencode(args)
    look_up_url += encoded_args
    http = httplib2.Http()
    print look_up_url
    response, content = http.request(look_up_url)
    json_content = loads(content)
    return json_content