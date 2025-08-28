# Flask Basics

Flask is a lightweight Web Server Gateway Interface (WSGI) web application framework. The idea behind flask is that it is a microframework, giving you a core of the important basic features for creating a web application/service while allowing it's feature set to be expanded as needed. For example, Flask on it's own, does not support login authentication, but the are other packages like flask-login that can provide those features.

A minimal flask application can be as small as one single Python file. For this example, `demo.py` is that single file. The `requirements.txt` file is only to provide the necessary dependencies for setting up a virtual environment for Flask development and not strictly a requirement of a flask application.

Comments in `demo.py` explain the application.

To run this program, make sure you first have your virtual environment activated and have installed the dependencies in `requirements.txt`. Requirements can be installed with the command:

```bash
pip install -r requirements.txt
```

Dependencies will only need to be installed once, and as long as your virtual environment is active, you can run the application using:

```bash
flask --app demo run
```

For this command, `flask` is the command line program which will execute our code, the `--app` option is where you tell flask which Python source file is the entry point where your `Flask` object is created, and `run` is the command to start the development server.
