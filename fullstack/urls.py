from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from subscribe import urls as urls_create_subscribe
from patterns import urls as urls_patterns
from products.views import all_products
from django.views import static
from django.views.generic import RedirectView
from .settings import MEDIA_ROOT
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='products/')),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
    url(r'^create_subscribe/', include(urls_create_subscribe)),
    url(r'^patterns/', include(urls_patterns)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]
