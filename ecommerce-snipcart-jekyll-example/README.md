# Altwalker ecommerce example

Demo tests repo to showcase how to design your tests as a graph and execute them using altwalker. Documentation of the demo is available [https://gitlab.com/altom/altwalker/altwalker/tree/master/docs/demo.md](https://gitlab.com/altom/altwalker/altwalker/tree/master/docs/demo.md)


## Setup your repo locally

```
cd ecommerce-snipcart-jekyll-example
python3 -m venv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt
```

## Run the tests with altwalker

See docs for [Altwalker](https://gitlab.com/altom/altwalker/altwalker/tree/master/docs/installation.md)

### online

`altwalker online -m models/default.json "random(edge_coverage(100))" tests`

### offline and walk

`altwalker offline -m models/default.json "random(edge_coverage(100) && vertex_coverage(100))" -f steps.json`

`altwalker walk tests ./steps.json`

### check

`altwalker check -m models/default.json "random(edge_coverage(100) && vertex_coverage(100))"`

### verify

`altwalker verify -m models/default.json tests`
