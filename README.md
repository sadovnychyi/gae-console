# GAE Console
Powerful Interactive Console for App Engine applications. Powered by Ace editor with multi select support.


I've created this package because sometimes it's really useful to be able to run code without doing new deployment, but keep in mind that you're able to run anything from here and you can easily corrupt your data.

* Press **⌘ + B** to run current code.
* Press **⌘ + S** to save current state into local storage, so it will be loaded on next visit.

# Screenshots

![image](https://cloud.githubusercontent.com/assets/193864/6576869/f5aef548-c774-11e4-8ca1-34a10a7eb41f.png)

![image](https://cloud.githubusercontent.com/assets/193864/6576832/d1297fcc-c774-11e4-8f4b-7178e9d275f8.png)

# Installation

From GAE project directory run:

    $ pip install gae-console --target .

This will install the library in the root of your project.
Then you can simply import it from your module configuration file (usually its `app.yaml`):

```yaml
includes:
- gae_console/include.yaml
```

This will make console available on `/_ah/console` path in your application.

Or, if you want to use custom path, create a handler for it manually:

```yaml
handlers:
- url: /admin/console(/.*)?
  script: gae_console.application
  login: admin
```

# Configuration

You can configure a list of libraries which will be imported by default using apengine_config.py:

```
gae_console_IMPORTS = {
  'memcache': 'google.appengine.api.memcache',
  'modules': 'google.appengine.api.modules',
  'taskqueue': 'google.appengine.api.taskqueue',
  'urlfetch': 'google.appengine.api.urlfetch',
  'ndb': 'google.appengine.ext.ndb',
  'deferred': 'google.appengine.ext.deferred',
  'model': 'model',
}
```


`memcache`, `modules`, `taskqueue`, `urlfetch`, `ndb`, and `deferred` are imported by default.
