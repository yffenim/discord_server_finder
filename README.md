# Iteration I of Backend for Disboard Server Search 

## RoadMap

- [ ] webscraper lambda
- [ ] microservice lambda as search API 
- [ ] microservice lambda as API to handle DynamoDB interaction
- [ ] minimalist react front end to demo dynamic search function based on inclusion and exlusion tags

## Usage: scraper lamba

### Cloud: WIP

Using Postman, `curl`, or your own webserver, send a `POST` request with a `JSON` body object containing your search tag.

```
https://oxngnmwe2h.execute-api.us-east-1.amazonaws.com/scraper_lambda
```

Search Tag:

```
{ 
	"tag": "YOUR_TAG"
}
```

For example: 

```
curl --header "Content-Type: text/plain" -d "{\"a\":16,\"b\":12}" https://oxngnmwe2h.execute-api.us-east-1.amazonaws.com/scraper_lambda
```


### Locally:

Prerequisites: 
- Python3 (`brew install python` to install, `python3 --version` to verify)
- Pipenv (`pip install pipenv`)

Clone this repo: 
```
git clone git@github.com:yffenim/discord_server_finder.git
```

Install dependencies after entering `pipenv` environment in `/scraper_lambda/` directory:

```
pipenv shell
pipenv install
```

Run the app:
```
python /scraper_lambda/scrape_local.py
```
