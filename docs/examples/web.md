# Web Interface Example

Use Python web framework Flask to create a simple web interface to switch socket(s) on and off

![](images/web.png)

## Requirements

Install the Python flask module with:

```bash
sudo pip install flask
```

## Files

- [app.py](https://github.com/bennuttall/energenie/blob/master/examples/advanced/web/app.py)

    The web application routes for `/`, `/on/` and `/off/`.

- [templates/index.html](https://github.com/bennuttall/energenie/blob/master/examples/advanced/web/templates/index.html)

    The HTML template containing "ON" and "OFF" buttons

- [static/style.css](https://github.com/bennuttall/energenie/blob/master/examples/advanced/web/static/style.css)

    The CSS file to style the page

## Usage

Download and extract these files:

```bash
wget http://goo.gl/ULIk1x -O web.tar.gz
tar xzf web.tar.gz
```

Find your Pi's IP address, enter the `web` folder and run the Python script to start the web server:

```bash
hostname -I
cd web
sudo python app.py
```

Then open a web browser on the Pi or any device on the same network and enter the IP address of the Pi. You'll see the `ON` and `OFF` buttons. Press these to control the Energenie.
