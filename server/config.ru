require 'rack'
require_relative 'app.rb'

handler = Rack::Handler::Thin
handler.run App.new
