# Web Interface Example

Use Python web framework Flask to create a simple web interface to switch socket(s) on and off

![](../images/web.png)

## Requirements

Install the Python flask module with:

```bash
sudo pip install flask
```

## Files

- [app.py](web/app.py)

   The web application routes for `/`, `/on/` and `/off/`.

- [templates/index.html](templates/index.html)

    The HTML template containing "ON" and "OFF" buttons

- [static/style.css](static/style.css)

    The CSS file to style the page

## Usage

Download these files and run the web app with the following commands:

```bash
wget http://goo.gl/ULIk1x -O web.tar.gz
tar xzf web.tar.gz
cd web
sudo python app.py
```

Find your Pi's IP address with the following command:

```bash
hostname -I
```

Then open a web browser on the Pi or any device on the same network and enter the IP address of the Pi. You'll see the `ON` and `OFF` buttons. Press these to control the Energenie.
