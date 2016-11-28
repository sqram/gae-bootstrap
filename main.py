import sys
sys.path.append('./')
from os.path import dirname
from json import dumps as jsonify
#from json import loads as unjsonify
#from re import match


import webapp2
#from google.appengine.api import memcache, app_identity
from google.appengine.ext import ndb
from webapp2_extras import sessions, sessions_memcache, sessions_ndb

import jinja2


jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(dirname(__file__)+'/templates/'),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)


# Base handler for all our requests
class BaseHandler(webapp2.RequestHandler):
  def dispatch(self):
    self.session_store = sessions.get_store(request=self.request)
    try:
      webapp2.RequestHandler.dispatch(self)
    finally:
      self.session_store.save_sessions(self.response)

  @webapp2.cached_property
  def session(self):
    return self.session_store.get_session(name='fcheck', max_age=31104000, backend='datastore')


  def render(self, template, templatedata = {}, spfdata = {}, spf=''):
    template = jinja_env.get_template(template + '.html')
    
    if spf:
      templatedata['full'] = False
      spfdata['body'] = {'content': template.render(**templatedata) }
      return jsonify(spfdata)
    else:
      return template.render(**templatedata)



class Home(BaseHandler):

  def get(self):
    templatedata, spfdata  =  ({'full' : True}, {})
    spfdata['title'] = 'My Site'
    self.response.write(self.render('index', templatedata, spfdata, self.request.get('spf')))












routes = [
  ('/', Home),
]

conf = {
   'webapp2_extras.sessions': {
     'secret_key': 'super-secret-k3y',
     'cookie_args': {
     'max_age': 31104000
     }
   }
}


app = webapp2.WSGIApplication(routes=routes, config=conf, debug=True)