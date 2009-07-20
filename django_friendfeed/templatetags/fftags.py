import datetime
from django import template
from django.template.loader import render_to_string

from django_friendfeed.friendfeed import FriendFeed

class FFNode(template.Node):
    def __init__(self, action, template_name, **kwargs):
        self.template_name = template_name
        self.options = kwargs
        self.ff = FriendFeed()
        
        self.render = getattr(self,action)

    def user_feed(self, context):
        username_var = template.Variable(self.options['username'])
        username = username_var.resolve(context)

        items = self.ff.fetch_user_feed(username)['entries']
        items_requested = int(self.options.get('num_items', len(items)))
        num_items = min(items_requested, len(items))

        context['items'] = items[:num_items]
        context['username'] = username

        return render_to_string(self.template_name, context)

def do_ff_user_feed(parser, token):
    """
    Arguments should be:
    
    1. The username of the feed to parse.
    
    2. The number of items to render (if not supplied, renders all
       items in the feed).
       
    3. The name of a template to use for rendering the results into HTML.
    
    The template used to render the results will receive two variables:
    
    ``items``
        A list of dictionaries representing feed items.
    
    ``username``
        The username.
    
    Syntax::
    
        {% ff_user_feed [username] [num_items] [template_name] %}
    
    Example::
    
        {% ff_user_feed "ctrochalakis" 10 partial/ff_feeds.html %}
    
    """
    bits = token.contents.split()
    if len(bits) == 3:
        return FFNode(action='user_feed', username=bits[1], template_name=bits[2])
    elif len(bits) == 4:
        return FFNode(action='user_feed', username=bits[1], num_items=bits[2], template_name=bits[3])
    else:
        raise template.TemplateSyntaxError("'%s' tag takes either two or three arguments" % bits[0])

register = template.Library()
register.tag('ff_user_feed', do_ff_user_feed)

