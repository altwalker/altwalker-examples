We are using python for writing tests inside `tests/test.py`

Our graph is defined in `models/default.json`

The tests can be executed using altwalker. 

The path through the graph is generated using graphwalker.

## Setup

`python3 -m venv .virtualenv`

`source .virtualenv/bin/activate`

`pip install -r requirements.txt`

`altwalker online -m models/default.json "random(edge_coverage(100) && vertex_coverage(100))" tests/`