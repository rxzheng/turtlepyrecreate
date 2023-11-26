This is a script that allows you to recreate an image with Python turtle. It uses a pixel-scanning technique and iterates through a list to print an image with Python turtle.


In order to run this code, please do this:
```bash
git clone https://github.com/rxzheng/turtlepyrecreate
```

```bash
nano recreate.py
```
Change the path that the script searches for to the image that you would like to use.

Change the text inside Image.open() to point towards your path.
```python
# REPLACE IMGPATH WITH THE IMAGE'S PATH
img = Image.open('/Users/richardzheng/Documents/GitHub/turtlepyrecreate/hangingRockImage.jpg')
```

How to find this on Linux:
https://linuxhandbook.com/get-file-path/

How to find this on Windows:
https://www.wikihow.com/Find-a-File%27s-Path-on-Windows

How to find this on Mac:
https://www.tomsguide.com/how-to/how-to-show-a-file-path-on-mac

To execute the code, either:
1. Open it in your code editor and execute it

2. Navigate to the place that you cloned the git repository.
```bash
cd turtlepyrecreate
python3 recreate.py
```