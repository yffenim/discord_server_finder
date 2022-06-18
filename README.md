# Iteration I of Backend for Disboard Server Search 

## RoadMap

- [ ] serverless scraper via AWS lambda
- [ ] node.js API with fastify.io for search filtering 
- [ ] minimalist front-end with React.js to demo

## Usage: scraper lamba

### Cloud 

### Locally:

Prerequisites: 
- Python3 (`brew install python` to install, `python3 --version` to verify)
- Pipenv (`pip install pipenv`)

Clone this repo: 
```
git clone git@github.com:yffenim/discord_server_finder.git
```

Install dependencies after entering `pipenv` environment:
```
pipenv shell
pipenv install
```

Run the app:
```
python scrape.py
```
