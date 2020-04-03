# AltWalker Example: Python Config

Demo tests to showcase how to use config files with altwalker.

## Setup

Linux/MacOS:

```bash
$ cd python-config
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Windows:

```bash
$ cd python-config
$ python3 -m venv .venv
$ .venv/Scripts/activate.bat
$ pip install -r requirements.txt
```

Read more about venv [here](https://docs.python.org/3/library/venv.html).

## Run the debugger with AltWalker

Inside `config/config.ini` and `config/config.json` we have two configurations one for a development enviroment and for a production enviroment. The tests use the `TEST_ENV` env variabile to switch between the development enviroment and the production enviroment (by default the tests will use the developent enviroment if `TEST_ENV` is not set).

```bash
$ altwalker online tests -m models/model.json "random(vertex_coverage(100))"
```

You will see somethig like this:

```
Running:
[2020-04-01 18:15:29.957335] setUpRun Running
[2020-04-01 18:15:29.960251] setUpRun Status: PASSED
Output:
INI CONFIG:

Section: default
  port = 8888

Section: dev
  url = "dev.env"

Section: prod
  url = "prod.env"

JSON CONFIG:

{
    "default": {
        "port": 8888
    },
    "dev": {
        "url": "dev.env"
    },
    "prod": {
        "url": "prod.env"
    }
}

INI URL:  dev.env
JSON URL:  "dev.env"

[2020-04-01 18:15:29.985578] ConfigModel.v_state_a Running
[2020-04-01 18:15:29.985860] ConfigModel.v_state_a Status: PASSED

[2020-04-01 18:15:30.010624] ConfigModel.e_action_a Running
[2020-04-01 18:15:30.011356] ConfigModel.e_action_a Status: PASSED

[2020-04-01 18:15:30.030350] ConfigModel.v_state_b Running
[2020-04-01 18:15:30.030617] ConfigModel.v_state_b Status: PASSED

[2020-04-01 18:15:30.051084] ConfigModel.e_action_b Running
[2020-04-01 18:15:30.051406] ConfigModel.e_action_b Status: PASSED

[2020-04-01 18:15:30.078480] ConfigModel.v_state_c Running
[2020-04-01 18:15:30.079005] ConfigModel.v_state_c Status: PASSED

Statistics:

  Model Coverage..................100%
  Number of Models...................1
  Completed Models...................1
  Failed Models......................0
  Incomplete Models..................0
  Not Executed Models................0

  Edge Coverage....................66%
  Number of Edges....................3
  Visited Edges......................2
  Unvisited Edges....................1

  Vertex Coverage.................100%
  Number of Vertices.................3
  Visited Vertices...................3
  Unvisited Vertices.................0

Status:  PASS

```

If you want to use the url for `prod` you will need the set `TEST_ENV`.

* MacOS/Linx:

   ```bash
   $ export TEST_ENV=prod
   ```

* Windows:

  ```bash
  C:\path\to\tests> set TEST_ENV=prod
  ```

* PowerShell:

  ```
  PS C:\path\to\tests> $env:TEST_ENV= "prod"
  ```

And if you ran the tests after setting the `TEST_ENV` you will see somethig like this:

```bash
$ altwalker online tests -m models/model.json "random(vertex_coverage(100))"
Running:
[2020-04-01 18:15:29.957335] setUpRun Running
[2020-04-01 18:15:29.960251] setUpRun Status: PASSED
Output:
INI CONFIG:

Section: default
  port = 8888

Section: dev
  url = "dev.env"

Section: prod
  url = "prod.env"

JSON CONFIG:

{
    "default": {
        "port": 8888
    },
    "dev": {
        "url": "dev.env"
    },
    "prod": {
        "url": "prod.env"
    }
}

INI URL:  prod.env
JSON URL:  "prod.env"

[2020-04-01 18:15:29.985578] ConfigModel.v_state_a Running
[2020-04-01 18:15:29.985860] ConfigModel.v_state_a Status: PASSED

[2020-04-01 18:15:30.010624] ConfigModel.e_action_a Running
[2020-04-01 18:15:30.011356] ConfigModel.e_action_a Status: PASSED

[2020-04-01 18:15:30.030350] ConfigModel.v_state_b Running
[2020-04-01 18:15:30.030617] ConfigModel.v_state_b Status: PASSED

[2020-04-01 18:15:30.051084] ConfigModel.e_action_b Running
[2020-04-01 18:15:30.051406] ConfigModel.e_action_b Status: PASSED

[2020-04-01 18:15:30.078480] ConfigModel.v_state_c Running
[2020-04-01 18:15:30.079005] ConfigModel.v_state_c Status: PASSED

Statistics:

  Model Coverage..................100%
  Number of Models...................1
  Completed Models...................1
  Failed Models......................0
  Incomplete Models..................0
  Not Executed Models................0

  Edge Coverage....................66%
  Number of Edges....................3
  Visited Edges......................2
  Unvisited Edges....................1

  Vertex Coverage.................100%
  Number of Vertices.................3
  Visited Vertices...................3
  Unvisited Vertices.................0

Status:  PASS

```

## Models

> **Note**: For this example the model is irelevant.

* Example Model from `models/debug.json`

![Config Model](img/model.png)
