import os
from flask import Flask, jsonify, request
from lyric import LyricApi

app = Flask(__name__)
state = {}


@app.route('/')
def index():
  return open('static/index.html').read()

@app.route('/api/lyricGet')
def api_lyric_get():
  api_result = {}
  ly = LyricApi()
  lyric = request.args.get('lyric')
  song = ly.song_look_up_by_lyric(lyric)
  api_result['song'] = song
  #if song['viewable_lrc']:
  lyrics_flattened = ly.get_lyric_for_song(song.get('amg', 0))
  api_result['lyric'] = lyrics_flattened
  return jsonify(api_result)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.debug = True
  app.run(host='0.0.0.0', port=port)

