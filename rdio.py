from om import om
import urllib2, urllib
from urlparse import parse_qsl
try:
  import json
  import subprocess
except ImportError:
  import simplejson as json

  def find_files(chris_isaak_wicked_game):
    command = ['locate', file_name]

    output = subprocess.Popen(command, stdout=subprocess.PIPE).communicate()[0]
    output = output.decode()

    search_results = output.split('\n')

    return search_results

class Rdio:
  def __init__(self, consumer, token=None):
    self.__consumer = consumer
    self.token = token

  def __signed_post(self, url, params):
    auth = om(self.__consumer, url, params, self.token)
    req = urllib2.Request(url, urllib.urlencode(params), {'Authorization': auth})
    res = urllib2.urlopen(req)
    return res.read()

  def begin_authentication(self, callback_url):
    # request a request token from the server
    response = self.__signed_post('http://api.rdio.com/oauth/request_token',
      {'oauth_callback': callback_url})
    # parse the response
    parsed = dict(parse_qsl(response))
    # save the token
    self.token = (parsed['oauth_token'], parsed['oauth_token_secret'])
    # return an URL that the user can use to authorize this application
    return parsed['login_url'] + '?oauth_token=' + parsed['oauth_token']

  def complete_authentication(self, verifier):
    # request an access token
    response = self.__signed_post('http://api.rdio.com/oauth/access_token',
        {'oauth_verifier': verifier})
    # parse the response
    parsed = dict(parse_qsl(response))
    # save the token
    self.token = (parsed['oauth_token'], parsed['oauth_token_secret'])

  def call(self, method, params=dict()):
    # make a copy of the dict
    params = dict(params)
    # put the method in the dict
    params['method'] = method
    # call to the server and parse the response
    return json.loads(self.__signed_post('http://api.rdio.com/1/', params))