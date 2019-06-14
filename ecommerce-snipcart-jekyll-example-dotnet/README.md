# AltWalker C# E-commerce example

Demo tests repo to showcase how to design your tests as a graph and execute them using altwalker. Documentation of the demo is available [https://altom.gitlab.io/altwalker/altwalker/examples/dotnet/e-commerce-demo.html](https://altom.gitlab.io/altwalker/altwalker/examples/dotnet/e-commerce-demo.html). 

The site under test is available on gitlab pages [https://altom.gitlab.io/altwalker/snipcart-jekyll-ecommerce-demo/](https://altom.gitlab.io/altwalker/snipcart-jekyll-ecommerce-demo/)


## Setup your repo locally

```
cd ecommerce-snipcart-jekyll-example-dotnet
dotnet build tests
```
    

## Install dependencies

Altwalker 

```bash
pip install altwalker
```

See docs for [Altwalker installation](https://altom.gitlab.io/altwalker/altwalker/installation.html)

## Run the tests with altwalker

### online

`altwalker online -l c# -m models/default.json "random(edge_coverage(100))" tests`

### offline and walk

`altwalker offline -m models/default.json "random(edge_coverage(100) && vertex_coverage(100))" -f steps.json`

`altwalker walk -l c# tests ./steps.json`

### check

`altwalker check -m models/default.json "random(edge_coverage(100) && vertex_coverage(100))"`

### verify

`altwalker verify -l c# -m models/default.json tests`
