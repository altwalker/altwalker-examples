# AltWalker Python E-commerce example

Demo tests repo to showcase how to design your tests as a graph and execute them using altwalker. Documentation of the demo is available [https://altom.gitlab.io/altwalker/altwalker/examples/python/e-commerce-demo.html](https://altom.gitlab.io/altwalker/altwalker/examples/python/e-commerce-demo.html). 

The site under test is available on gitlab pages [https://altom.gitlab.io/altwalker/snipcart-jekyll-ecommerce-demo/](https://altom.gitlab.io/altwalker/snipcart-jekyll-ecommerce-demo/)


## Setup your repo locally

```
cd ecommerce-snipcart-jekyll-example
python3 -m venv .virtualenv
source .virtualenv/bin/activate
pip install -r requirements.txt
```


## Install dependencies

Altwalker 

```bash
pip install altwalker
```

Geckodriver

```bash
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver* -C /
ln -s /geckodriver /usr/local/bin
```

See docs for [Altwalker installation](https://altom.gitlab.io/altwalker/altwalker/installation.html)

## Run the tests with altwalker

### online

`altwalker online -m models/default.json "random(edge_coverage(100))" tests`

### offline and walk

`altwalker offline -m models/default.json "random(edge_coverage(100) && vertex_coverage(100))" -f steps.json`

`altwalker walk tests ./steps.json`

### check

`altwalker check -m models/default.json "random(edge_coverage(100) && vertex_coverage(100))"`

### verify

`altwalker verify -m models/default.json tests`
