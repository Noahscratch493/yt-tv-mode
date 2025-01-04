import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":

    app = QApplication(sys.argv)
    web = QWebEngineView()

    print(web.page().profile().httpUserAgent())

    # Set the user agent to the Wii U one to display YouTube's TV Mode
    web.page().profile().setHttpUserAgent(
        "Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.28 (KHTML, like Gecko) NX/3.0.3.12.15 NintendoBrowser/4.1.1.9601.EU"
    )
    
    # Load YouTube TV
    web.load(QUrl("https://youtube.com/tv"))
    
    # Set the window title
    web.setWindowTitle("YouTube - TV Mode")
    
    # Set the window icon
    web.setWindowIcon(QIcon("youtube.ico"))  # Make sure the 'youtube.ico' file is in the same directory or provide the full path.
    
    # Show and resize the window to 1280x720 (HD resolution)
    web.show()
    web.resize(1280, 720)

    sys.exit(app.exec_())
