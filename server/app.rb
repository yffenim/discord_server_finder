require 'csv'
require 'json'

# Routing
class App
  def call(env)
    # routing based on env
    case env['REQUEST_PATH']
    when '/'
      # req = Rack::Request.new(env).params
      # p req.inspect
    # simple search by 1 tag 
    # run script to get servers w/  args of tag and total pages to search
    # servers_json = `python ../scraper/scrape_local.py buffy 5`
      servers_json = { "dev": "temporary json return" }
      [200, 
        {"Content-Type" => "application/json"}, servers_json
      ]
    when '/advanced'
    # advanced search 
    # get all the tags to include and exclude
    # run the script 
    # return the array 
      puts "env: #{env}"

    else
      [
        '404',
        {"Content-Type" => 'text/plain', "Content-Length" => '13'},
        ["404 Not Found"]
      ]
    end
  end
end
