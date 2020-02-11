{"filter":false,"title":"urls.py","tooltip":"/fullstack/urls.py","undoManager":{"mark":43,"position":43,"stack":[[{"start":{"row":15,"column":0},"end":{"row":19,"column":37},"action":"remove","lines":["from django.conf.urls import url","from django.contrib import admin","","urlpatterns = [","    url(r'^admin/', admin.site.urls),"],"id":2},{"start":{"row":15,"column":0},"end":{"row":34,"column":77},"action":"insert","lines":["from django.conf.urls import url, include","from django.contrib import admin","from accounts import urls as urls_accounts","from products import urls as urls_products","from cart import urls as urls_cart","from search import urls as urls_search","from checkout import urls as urls_checkout","from products.views import all_products","from django.views import static","from .settings import MEDIA_ROOT"," ","urlpatterns = [","    url(r'^admin/', admin.site.urls),","    url(r'^$', all_products, name='index'),","    url(r'^accounts/', include(urls_accounts)),","    url(r'^products/', include(urls_products)),","    url(r'^cart/', include(urls_cart)),","    url(r'^checkout/', include(urls_checkout)),","    url(r'^search/', include(urls_search)),","    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),"]}],[{"start":{"row":33,"column":43},"end":{"row":34,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":34,"column":4},"end":{"row":34,"column":57},"action":"insert","lines":["url(r'^$', create_subscribe, name='create_subscribe')"],"id":4}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"remove","lines":["$"],"id":5}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["s"],"id":6},{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":["u"]},{"start":{"row":34,"column":13},"end":{"row":34,"column":14},"action":"insert","lines":["b"]}],[{"start":{"row":34,"column":11},"end":{"row":34,"column":14},"action":"remove","lines":["sub"],"id":7},{"start":{"row":34,"column":11},"end":{"row":34,"column":20},"action":"insert","lines":["subscribe"]}],[{"start":{"row":34,"column":20},"end":{"row":34,"column":21},"action":"insert","lines":["/"],"id":8}],[{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["c"],"id":9},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["r"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["e"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["a"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["t"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["e"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["_"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["s"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["u"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["b"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["s"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["c"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["r"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["i"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["b"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["e"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":[","]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":[" "]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["n"]}],[{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["a"],"id":10},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["m"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["e"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["="]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["'"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["c"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["r"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["e"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["a"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["t"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["e"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["_"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["s"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["u"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["b"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["s"]}],[{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["c"],"id":11},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["r"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["i"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["b"]},{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"remove","lines":["e"]}],[{"start":{"row":34,"column":24},"end":{"row":34,"column":25},"action":"insert","lines":["i"],"id":12},{"start":{"row":34,"column":25},"end":{"row":34,"column":26},"action":"insert","lines":["n"]},{"start":{"row":34,"column":26},"end":{"row":34,"column":27},"action":"insert","lines":["c"]},{"start":{"row":34,"column":27},"end":{"row":34,"column":28},"action":"insert","lines":["l"]},{"start":{"row":34,"column":28},"end":{"row":34,"column":29},"action":"insert","lines":["u"]},{"start":{"row":34,"column":29},"end":{"row":34,"column":30},"action":"insert","lines":["d"]},{"start":{"row":34,"column":30},"end":{"row":34,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":31},"end":{"row":34,"column":32},"action":"insert","lines":["("],"id":13},{"start":{"row":34,"column":32},"end":{"row":34,"column":33},"action":"insert","lines":["u"]},{"start":{"row":34,"column":33},"end":{"row":34,"column":34},"action":"insert","lines":["r"]},{"start":{"row":34,"column":34},"end":{"row":34,"column":35},"action":"insert","lines":["l"]}],[{"start":{"row":34,"column":35},"end":{"row":34,"column":36},"action":"insert","lines":["s"],"id":14},{"start":{"row":34,"column":36},"end":{"row":34,"column":37},"action":"insert","lines":["_"]}],[{"start":{"row":34,"column":37},"end":{"row":34,"column":38},"action":"insert","lines":["s"],"id":15},{"start":{"row":34,"column":38},"end":{"row":34,"column":39},"action":"insert","lines":["u"]},{"start":{"row":34,"column":39},"end":{"row":34,"column":40},"action":"insert","lines":["b"]}],[{"start":{"row":34,"column":40},"end":{"row":34,"column":41},"action":"insert","lines":["s"],"id":16},{"start":{"row":34,"column":41},"end":{"row":34,"column":42},"action":"insert","lines":["r"]},{"start":{"row":34,"column":42},"end":{"row":34,"column":43},"action":"insert","lines":["c"]},{"start":{"row":34,"column":43},"end":{"row":34,"column":44},"action":"insert","lines":["i"]}],[{"start":{"row":34,"column":44},"end":{"row":34,"column":45},"action":"insert","lines":["b"],"id":17}],[{"start":{"row":34,"column":44},"end":{"row":34,"column":45},"action":"remove","lines":["b"],"id":18},{"start":{"row":34,"column":43},"end":{"row":34,"column":44},"action":"remove","lines":["i"]}],[{"start":{"row":34,"column":43},"end":{"row":34,"column":44},"action":"insert","lines":["i"],"id":19},{"start":{"row":34,"column":44},"end":{"row":34,"column":45},"action":"insert","lines":["v"]}],[{"start":{"row":34,"column":44},"end":{"row":34,"column":45},"action":"remove","lines":["v"],"id":20}],[{"start":{"row":34,"column":44},"end":{"row":34,"column":45},"action":"insert","lines":["b"],"id":21},{"start":{"row":34,"column":45},"end":{"row":34,"column":46},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":46},"end":{"row":34,"column":47},"action":"insert","lines":[")"],"id":22}],[{"start":{"row":34,"column":47},"end":{"row":34,"column":48},"action":"remove","lines":["'"],"id":23}],[{"start":{"row":34,"column":48},"end":{"row":34,"column":49},"action":"insert","lines":[","],"id":24}],[{"start":{"row":21,"column":42},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":25},{"start":{"row":22,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["f"]},{"start":{"row":22,"column":1},"end":{"row":22,"column":2},"action":"insert","lines":["r"]},{"start":{"row":22,"column":2},"end":{"row":22,"column":3},"action":"insert","lines":["o"]},{"start":{"row":22,"column":3},"end":{"row":22,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":[" "],"id":26}],[{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["s"],"id":27},{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["u"]},{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["b"]},{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":5},"end":{"row":22,"column":9},"action":"remove","lines":["subs"],"id":28},{"start":{"row":22,"column":5},"end":{"row":22,"column":14},"action":"insert","lines":["subscribe"]}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":[" "],"id":29},{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["i"]},{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["m"]},{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":["p"]},{"start":{"row":22,"column":18},"end":{"row":22,"column":19},"action":"insert","lines":["o"]},{"start":{"row":22,"column":19},"end":{"row":22,"column":20},"action":"insert","lines":["r"]},{"start":{"row":22,"column":20},"end":{"row":22,"column":21},"action":"insert","lines":["t"]}],[{"start":{"row":22,"column":21},"end":{"row":22,"column":22},"action":"insert","lines":[" "],"id":30},{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":["u"]},{"start":{"row":22,"column":23},"end":{"row":22,"column":24},"action":"insert","lines":["r"]},{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"remove","lines":["s"],"id":31}],[{"start":{"row":22,"column":24},"end":{"row":22,"column":25},"action":"insert","lines":["l"],"id":32},{"start":{"row":22,"column":25},"end":{"row":22,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":26},"end":{"row":22,"column":27},"action":"insert","lines":[" "],"id":33},{"start":{"row":22,"column":27},"end":{"row":22,"column":28},"action":"insert","lines":["a"]},{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":["s"]}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":[" "],"id":34},{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lines":["u"]},{"start":{"row":22,"column":31},"end":{"row":22,"column":32},"action":"insert","lines":["r"]},{"start":{"row":22,"column":32},"end":{"row":22,"column":33},"action":"insert","lines":["l"]},{"start":{"row":22,"column":33},"end":{"row":22,"column":34},"action":"insert","lines":["s"]},{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"insert","lines":["-"]}],[{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"remove","lines":["-"],"id":35}],[{"start":{"row":22,"column":34},"end":{"row":22,"column":35},"action":"insert","lines":["_"],"id":36}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":35},"action":"remove","lines":["urls_"],"id":37},{"start":{"row":22,"column":30},"end":{"row":22,"column":44},"action":"insert","lines":["urls_subsrcibe"]}],[{"start":{"row":22,"column":40},"end":{"row":22,"column":41},"action":"remove","lines":["c"],"id":38},{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"remove","lines":["r"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"remove","lines":["s"]}],[{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["s"],"id":39},{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"insert","lines":["c"]},{"start":{"row":22,"column":40},"end":{"row":22,"column":41},"action":"insert","lines":["r"]}],[{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"remove","lines":["b"],"id":40},{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"remove","lines":["i"]},{"start":{"row":35,"column":42},"end":{"row":35,"column":43},"action":"remove","lines":["c"]},{"start":{"row":35,"column":41},"end":{"row":35,"column":42},"action":"remove","lines":["r"]}],[{"start":{"row":35,"column":41},"end":{"row":35,"column":42},"action":"remove","lines":["e"],"id":41},{"start":{"row":35,"column":40},"end":{"row":35,"column":41},"action":"remove","lines":["s"]}],[{"start":{"row":35,"column":40},"end":{"row":35,"column":41},"action":"insert","lines":["s"],"id":42},{"start":{"row":35,"column":41},"end":{"row":35,"column":42},"action":"insert","lines":["c"]},{"start":{"row":35,"column":42},"end":{"row":35,"column":43},"action":"insert","lines":["r"]},{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"insert","lines":["i"]},{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"insert","lines":["b"]},{"start":{"row":35,"column":45},"end":{"row":35,"column":46},"action":"insert","lines":["e"]}],[{"start":{"row":35,"column":11},"end":{"row":35,"column":12},"action":"insert","lines":["c"],"id":43},{"start":{"row":35,"column":12},"end":{"row":35,"column":13},"action":"insert","lines":["r"]},{"start":{"row":35,"column":13},"end":{"row":35,"column":14},"action":"insert","lines":["e"]},{"start":{"row":35,"column":14},"end":{"row":35,"column":15},"action":"insert","lines":["a"]},{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"insert","lines":["t"]},{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["e"]},{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["_"]}],[{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"insert","lines":["c"],"id":44},{"start":{"row":35,"column":45},"end":{"row":35,"column":46},"action":"insert","lines":["r"]},{"start":{"row":35,"column":46},"end":{"row":35,"column":47},"action":"insert","lines":["e"]},{"start":{"row":35,"column":47},"end":{"row":35,"column":48},"action":"insert","lines":["a"]},{"start":{"row":35,"column":48},"end":{"row":35,"column":49},"action":"insert","lines":["t"]},{"start":{"row":35,"column":49},"end":{"row":35,"column":50},"action":"insert","lines":["e"]},{"start":{"row":35,"column":50},"end":{"row":35,"column":51},"action":"insert","lines":["_"]}],[{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":["c"],"id":45},{"start":{"row":22,"column":36},"end":{"row":22,"column":37},"action":"insert","lines":["r"]},{"start":{"row":22,"column":37},"end":{"row":22,"column":38},"action":"insert","lines":["e"]},{"start":{"row":22,"column":38},"end":{"row":22,"column":39},"action":"insert","lines":["a"]},{"start":{"row":22,"column":39},"end":{"row":22,"column":40},"action":"insert","lines":["t"]},{"start":{"row":22,"column":40},"end":{"row":22,"column":41},"action":"insert","lines":["e"]},{"start":{"row":22,"column":41},"end":{"row":22,"column":42},"action":"insert","lines":["_"]}]]},"ace":{"folds":[],"scrolltop":394.5,"scrollleft":0,"selection":{"start":{"row":22,"column":51},"end":{"row":22,"column":51},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":23,"state":"start","mode":"ace/mode/python"}},"timestamp":1581403638872,"hash":"1af4d348798a2032528f3235e62cfdd09c5a8edd"}