import os
import re
import SimpleHTTPServer
import SocketServer
import webbrowser
import entertainment_center



def get_html_template (path) :
    '''
    Open the html file at the specified path. Read, close and return contents

    @param [String] path: relative filepath to html file
    @return [String] contents of html file
    '''

    file = open(os.path.dirname(__file__) + '/' + path + '.html', 'r')
    template = file.read()
    file.close()

    return template



def get_youtube_id (youtube_url) :
    '''
    Extract the youtube ID from a youtube url

    @param [String] youtube_url
    @return [String] youtube id
    '''

    youtube_id_match = re.search(r'(?<=v=)[^&#]+', youtube_url)
    youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', youtube_url)
    youtube_id = youtube_id_match.group(0) if youtube_id_match else None

    return youtube_id



def create_movie_tiles (movies) :
    '''
    Load movie tile template, iterate over movies list and generate movie tiles

    @param [List] movies
    @return [String] movie_tiles
    '''

    movie_tile_template = get_html_template('../templates/movie-tile')
    movie_tiles = ''

    for movie in movies:
        movie_tiles += movie_tile_template.format(
            movie_title = movie.title,
            poster_image_url = movie.poster_image_url,
            trailer_youtube_id = get_youtube_id(movie.trailer_youtube_url)
        )

    return movie_tiles



def generate_index_page (movies) :
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



def start_server (port) :
    '''
    Set up a simple http server to allow serving static assests
    i.e. css stylesheets and javascript files

    @param [Int] port: port number for server to listen to on localhost
    '''

    os.chdir('public')
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", int(port)), Handler)
    print("serving at port " + str(port))
    httpd.serve_forever()



def open_movies_page (port) :
    '''
    Open web browser to movie app on localhost
    Open in a new tab, if possible

    @param [Int] port: port number that the server is listening to on localhost
    '''

    webbrowser.open("http://localhost:" + str(port), new = 2)



def start (port = 8080) :
    generate_index_page(entertainment_center.movies)
    open_movies_page(port)
    start_server(port)
