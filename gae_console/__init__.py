import os
import sys
import importlib
import traceback
import cStringIO
from google.appengine.ext.webapp import _template
from google.appengine.ext import webapp
from google.appengine.api import lib_config

_config = lib_config.register(
  'gae_console', {'IMPORTS': {
    'memcache': 'google.appengine.api.memcache',
    'modules': 'google.appengine.api.modules',
    'taskqueue': 'google.appengine.api.taskqueue',
    'urlfetch': 'google.appengine.api.urlfetch',
    'ndb': 'google.appengine.ext.ndb',
    'deferred': 'google.appengine.ext.deferred',
  }})

for name, module in _config.IMPORTS.items():
  try:
    globals().update({name: importlib.import_module(module)})
  except ImportError:
    continue


def _render(self, template_name, **values):
  directory = os.path.dirname(__file__)
  path = os.path.join(directory, template_name)
  self.response.out.write(_template.render(path, values))


class ConsoleHandler(webapp.RequestHandler):
  """Shows our interactive console HTML."""

  def get(self):
    return _render(self, 'console.html')


class ExecuteHandler(webapp.RequestHandler):
  """Executes the Python code submitted in a POST within this context.

  For obvious reasons, this should only be available to administrators
  of the applications.
  """

  def post(self):
    save_stdout = sys.stdout
    results_io = cStringIO.StringIO()
    try:
      sys.stdout = results_io

      code = self.request.get('code')
      code = code.replace('\r\n', '\n')

      try:
        compiled_code = compile(code, '<string>', 'exec')
        exec(compiled_code, globals())
      except Exception:
        traceback.print_exc(file=results_io)
    finally:
      sys.stdout = save_stdout

    results = results_io.getvalue()
    return self.response.write(results)


class RedirectHandler(webapp.RequestHandler):
  def get(self):
    return self.redirect(self.request.path + '/')

application = webapp.WSGIApplication([
  ('.*/execute', ExecuteHandler),
  ('.*/', ConsoleHandler),
  ('.*', RedirectHandler),
], debug=True)
