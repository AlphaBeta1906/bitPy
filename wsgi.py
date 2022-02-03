from web import run

app = run()

if __name__ == "__main__":
    """
    # uncomment this code below to activate live reload
    from livereload import Server
    server = Server(app.wsgi_app)
    server.serve(port=8000)
    """
    app.run(port=8000)
