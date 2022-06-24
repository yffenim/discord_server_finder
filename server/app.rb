class App
  def call(env)
    # [200, {"Content-Type" => "text/plain"}, "Hello from Rack"]
    
    result = `python ../scraper/scrape_all_servers.py`
    puts result

    test = { "server": "hello world" }
    [200, 
      {"Content-Type" => "application/json"}, test
    ]
  end
end
