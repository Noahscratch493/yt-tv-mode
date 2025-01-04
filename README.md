# YouTube TV Mode on Desktop 

This project allows you to use **YouTube TV Mode** on your **desktop or laptop computer** by simulating the **Wii U browser's user-agent**. It brings the TV-optimized YouTube interface to your computer, providing a familiar experience for anyone who enjoys watching YouTube on a TV or gaming console.

## Features:
- **YouTube TV Interface**: Get the full TV mode experience with a simplified, large interface optimized for large screens.
- **Google Account Login**: Sign in with your Google account to access personalized features such as subscriptions, recommendations, and playlists.
- **Keyboard & Mouse Support**: Navigate and control YouTube TV mode with your keyboard and mouse.


## Requirements:
- **Python 3.x**
- **PyQt5** for GUI and web engine support

## Installation:

1. Clone this repository or download the project files.
2. Install the necessary Python dependencies:

    ```bash
    pip install PyQt5
    ```

3. Download the YouTube favicon from [YouTube favicon](https://www.youtube.com/favicon.ico) and save it as `youtube.ico` in the project folder.

4. Run the Python script:

    ```bash
    python yt-tv.py
    ```

## How It Works:
The application opens a PyQt5-based window, which emulates the **Wii U's browser** user-agent, prompting YouTube to display the **TV mode interface** (youtube.com/tv). This gives users a simplified YouTube layout suitable for TV screens. 

When you visit YouTube TV mode, a code is shown on the screen. You can go to a URL on your browser to enter the code and log in with your Google account, which allows you to access your personalized YouTube experience (subscriptions, recommendations, playlists).

## Important Note:
**Google Account Security Disclaimer**: 
This project does not hack or steal your Google account information. The login process is handled through YouTube's standard code-based authentication. Your Google credentials are not stored by this project. Authentication is performed directly through YouTube, and the project only provides the interface to enter the required code.

**If you are concerned about security**, feel free to check the code yourself. It does **not** store or process your Google credentials in any way. The login process is fully handled by YouTube itself.

## How to Set the Icon:
- The application window icon is set to the YouTube favicon. Download the [favicon](https://www.youtube.com/favicon.ico) and save it as `youtube.ico` in the project directory.
- The icon can be customized by replacing the `youtube.ico` file with any other valid `.ico` file.

## Contributions:
Feel free to fork this project, submit issues, and propose improvements. All contributions are welcome!

## License:
This project is open source and available under the MIT License.
