import urllib.request,json



random_url='http://quotes.stormconsultancy.co.uk/random.json?callback=random_quotes'

def configure_request(app):
    global api_key
    global random_url
    # api_key = app.config['API_KEY']



