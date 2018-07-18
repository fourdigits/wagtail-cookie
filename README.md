Cookie
======

Reusable Wagtail app to setup a cookie wall.


Install
-------

    pip install -e git+git ...#egg=cookie


Add 'cookie' AFTER your app. Also make sure 'django.contrib.sessions' is in installed apps:

    INSTALLED_APPS = [
        'your_app',
        'cookie',
        ...
        'django.contrib.sessions'
    ]


Make sure the session backend is enabled.

    MIDDLEWARE = [
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        ...
    ]


Include cookie urls in your urls.py BEFORE wagtail urls:

    from cookie import urls as cookie_urls

    url_patterns = [
        ...
        url(r'', include(cookie_urls, namespace='cookie')),
        url(r'', include(wagtail_urls)),
    ]


Register the cookie settings in your wagtail_hooks.py:

    from cookie.wagtail_hooks import AbstractCookie

    @register_setting
    class Cookie(AbstractCookie):
        pass


Add the cookie template tag to your base template head section:

    {% load cookie_tags %}

    <body>
        ...
        {% cookie_modal %}
    </body>


Wrap all template code that set third_party cookies in a `{% if request|third_party_cookies %}`:


      {% if request|third_party_cookies %}
        {% include_block self %}
      {% else %}
        <p><a href="{{ self.url }}">{{ self.url }}</a></p>
        <p><a href="{% url 'cookie:cookie' %}">Schakel third cookies in om embeds te zien.</a></p>
      {% endif %}


Wrap all template code that set analytical cookies in a `{% if request|analytical_cookies %}`:

    {% if request|analytical_cookies %}
      <script async src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXXXX-XX"></script>
      <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'UA-XXXXXXX-XX');
      </script>
    {% endif %}


Override templates
------------------

If you want to customise the templates. Copy them to your own project:

    $ cp cookie/templates/modal.html yourapp/templates/cookie/



Production
----------

As users create new sessions on your website, session data can accumulate in your session store. The django_session
database table will grow and needs to be cleaned up from time to time.

Setup a cronjob (Every day at 3AM) to run the clear sessions management command. Eg:

    $ crontab -e

    * 3 * * * cd /path/to/project && /path/to/python manage.py clearsessions --setttings=settings.production  >/dev/null 2>&1
