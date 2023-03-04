from app.container import Container

if __name__ == '__main__':
    container = Container()
    application = container.application()
    application.start()