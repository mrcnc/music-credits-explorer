from flask import Flask, request, render_template
import json
from amg import AllMusicGuide
from pyechonest import config, artist

app = Flask(__name__)
amg = AllMusicGuide()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/album")
def get_album():
    """
    Makes a request to the album endpoint. Requires a 'title' request parameter.
    http://prod-doc.rovicorp.com/mashery/index.php/Data/music-api/v1.1/album/info
    """
    album_title = request.args.get('title')

    album = {}
    info = json.loads(amg.get('album/info', {'album': album_title}))
    album['title'] = info.get('album').get('title')
    album['originalReleaseDate'] = info.get('album').get('originalReleaseDate')
    album['albumId'] = info.get('album').get('ids').get('albumId')
    credits = json.loads(amg.get('album/credits', {'albumId': album['albumId']}))
    album['credits'] = credits.get('credits')
    #images = json.loads(amg.get('album/images', {'albumId': album['albumId']}))
    #album['img'] = credits.get('')
    return render_template('index.html', album=album)

@app.route("/song")
def get_song():
    """
    Makes a request to the song endpoint. Requires a 'title' request parameter.
    http://prod-doc.rovicorp.com/mashery/index.php/Data/music-api/v1.1/song/info
    """
    song_title = request.args.get('title')

    song = {}
    info = json.loads(amg.get('song/info', {'track': song_title}))
    song['title'] = info.get('song').get('title')
    song['primaryArtists'] = info.get('song').get('primaryArtists')

    return render_template('index.html', song=song)

@app.route("/artist")
def get_artist():
    """
    Makes a request to the EchoNest api for artist info
    """
    artist_name = request.args.get('name')
    print 'artist name %s' % artist_name
    a = artist.Artist(artist_name)
    return render_template('artist.html', artist=a)

if __name__ == "__main__":
    app.debug = True
    app.run()
