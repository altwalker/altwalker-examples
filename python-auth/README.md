# AltWalker Example: Python Authentication Module

Demo tests to showcase how to write tests in python and execute them with AltWalker, using a State Transition Model for an authentication module. 

## Setup

Linux/MacOS:

```bash
$ cd python-auth
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Windows:

```bash
$ cd python-auth
$ python3 -m venv .venv
$ .venv/Scripts/activate.bat
$ pip install -r requirements.txt
```

Read more about venv [here](https://docs.python.org/3/library/venv.html).

### Install Dependencies

Read more on [AltWalker installation](https://altom.gitlab.io/altwalker/altwalker/installation.html).

#### Geckodriver

Download [geckodriver](https://github.com/mozilla/geckodriver/releases).

After you download and extract the executable, make sure you set the path to the geckodriver executable in the Path variable to make other programs aware of its location.

On Windows:

```
$ set PATH=%PATH%;C:\bin\geckodriver
```

On Linux/MacOS:

```
$ ln -s /path/to/geckodriver /urs/local/bin/geckodriver
```

#### Django Auth demo

You can start the demo application from the prebuilt docker image or from source: 

  * `docker run --rm -it -p 8000:8000 altwalker/demos:django-auth`

  or

  * Run from source. [https://gitlab.com/altom/altwalker/altwalker-demos/django-auth](https://gitlab.com/altom/altwalker/altwalker-demos/django-auth)

## Run the tests with AltWalker

### check

```
$ altwalker check -m models/models.json "random(edge_coverage(100)"
```

### verify

```
$ altwalker verify -m models/models.json tests
```

### online

```
$ altwalker online -m models/models.json "random(edge_coverage(100))" tests
```