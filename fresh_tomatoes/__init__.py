import os
import re
import SocketServer
import webbrowser
from SimpleHTTPServer import SimpleHTTPRequestHandler

import entertainment_center
import fresh_tomatoes
import media


def get_html_template(path):
    '''
    Open the html file at the specified path. Read, close and return contents

    @param [String] path: relative filepath to html file
    @return [String] contents of html file
    '''

    file = open(os.path.dirname(__file__) + '/' + path + '.html', 'r')
    template = file.read()
    file.close()

    return template


def create_movie_tiles(movies):
    '''
    Load movie tile template, iterate over movies list and generate movie tiles

    @param [List] movies
    @return [String] movie_tiles
    '''

    movie_tile_template = get_html_template('../templates/movie-tile')
    movie_tiles = ''

    for movie in movies:
        movie_tiles += movie_tile_template.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=movie.youtube_trailer_id
        )

    return movie_tiles


def generate_index_page(movies):
    '''
    Create or overwrite the index.html file.
    Load page layout template and replace movie tiles placeholder with
    dynamically generated movie tiles content

    @param [List] movies
    '''

    index_page = open('public/index.html', 'w')
    movie_tiles = create_movie_tiles(movies)

    page_layout_template = get_html_template('../templates/layout')
    rendered_content = page_layout_template.format(movie_tiles=movie_tiles)
    index_page.write(rendered_content)
    index_page.close()


def start_server(port):
    '''
    Set up a simple http server to allow serving static assests
    i.e. css stylesheets and javascript files

    @param [Int] port: port number for server to listen to on localhost
    '''

    class TCPServer (SocketServer.TCPServer):
        allow_reuse_address = True

    os.chdir('public')
    print('serving at port ' + str(port))
    server = TCPServer(('0.0.0.0', int(port)), SimpleHTTPRequestHandler)
    server.serve_forever()


def open_movies_page(port):
    '''
    Open web browser to movie app on localhost
    Open in a new tab, if possible

    @param [Int] port: port number that the server is listening to on localhost
    '''

    webbrowser.open('http://localhost:' + str(port), new=2)


def start(port=8000):
    generate_index_page(entertainment_center.movies)
    open_movies_page(port)
    start_server(port)
