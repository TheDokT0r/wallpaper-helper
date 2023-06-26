# wallpaper-helper
## The What
This is a small python program that converts webp files to jpeg so they can be displayed as a wallpaper

## The Why
I've recently reinstalled GNU/Linux, and I looked on the web for some cool wallpapers for my dekstop. To my horror, a big chunk of the images online were in the infamous webp format, that's not supported for wallpapers on KDE. I was way too lazy to use an online converter, so I've made my own... Enjoy!

## Build Binary
If you'd like to build this app into a binary, you can do so by following this insturctions:
paste into your shell the following commands:

`pip install -r requirements.txt` (requires python installed on your machine)

Next, you'd want to paste the following command:

`pyinstaller main.py`

You will then find the binary build of your app in the build directory. Don't forget to create a config.txt file in the same location as your binary! The config.txt file should look like that: 

`path=<your_path_here>`

## Final Notes
Hope you'll find my program useful!