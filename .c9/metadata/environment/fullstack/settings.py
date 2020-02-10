{"filter":false,"title":"settings.py","tooltip":"/fullstack/settings.py","undoManager":{"mark":71,"position":71,"stack":[[{"start":{"row":159,"column":23},"end":{"row":159,"column":63},"action":"remove","lines":["storages.backends.s3boto3.S3Boto3Storage"],"id":265},{"start":{"row":159,"column":23},"end":{"row":159,"column":24},"action":"insert","lines":["c"]},{"start":{"row":159,"column":24},"end":{"row":159,"column":25},"action":"insert","lines":["u"]},{"start":{"row":159,"column":25},"end":{"row":159,"column":26},"action":"insert","lines":["s"]},{"start":{"row":159,"column":26},"end":{"row":159,"column":27},"action":"insert","lines":["t"]},{"start":{"row":159,"column":27},"end":{"row":159,"column":28},"action":"insert","lines":["o"]},{"start":{"row":159,"column":28},"end":{"row":159,"column":29},"action":"insert","lines":["m"]},{"start":{"row":159,"column":29},"end":{"row":159,"column":30},"action":"insert","lines":["e"]},{"start":{"row":159,"column":30},"end":{"row":159,"column":31},"action":"insert","lines":["r"]}],[{"start":{"row":159,"column":30},"end":{"row":159,"column":31},"action":"remove","lines":["r"],"id":266},{"start":{"row":159,"column":29},"end":{"row":159,"column":30},"action":"remove","lines":["e"]}],[{"start":{"row":159,"column":29},"end":{"row":159,"column":30},"action":"insert","lines":["_"],"id":267},{"start":{"row":159,"column":30},"end":{"row":159,"column":31},"action":"insert","lines":["s"]},{"start":{"row":159,"column":31},"end":{"row":159,"column":32},"action":"insert","lines":["o"]}],[{"start":{"row":159,"column":31},"end":{"row":159,"column":32},"action":"remove","lines":["o"],"id":268}],[{"start":{"row":159,"column":31},"end":{"row":159,"column":32},"action":"insert","lines":["t"],"id":269}],[{"start":{"row":159,"column":23},"end":{"row":159,"column":32},"action":"remove","lines":["custom_st"],"id":270},{"start":{"row":159,"column":23},"end":{"row":159,"column":38},"action":"insert","lines":["custom_storages"]}],[{"start":{"row":159,"column":38},"end":{"row":159,"column":39},"action":"insert","lines":["."],"id":271},{"start":{"row":159,"column":39},"end":{"row":159,"column":40},"action":"insert","lines":["S"]},{"start":{"row":159,"column":40},"end":{"row":159,"column":41},"action":"insert","lines":["t"]},{"start":{"row":159,"column":41},"end":{"row":159,"column":42},"action":"insert","lines":["a"]},{"start":{"row":159,"column":42},"end":{"row":159,"column":43},"action":"insert","lines":["t"]},{"start":{"row":159,"column":43},"end":{"row":159,"column":44},"action":"insert","lines":["i"]},{"start":{"row":159,"column":44},"end":{"row":159,"column":45},"action":"insert","lines":["c"]},{"start":{"row":159,"column":45},"end":{"row":159,"column":46},"action":"insert","lines":["S"]}],[{"start":{"row":159,"column":39},"end":{"row":159,"column":46},"action":"remove","lines":["StaticS"],"id":272},{"start":{"row":159,"column":39},"end":{"row":159,"column":52},"action":"insert","lines":["StaticStorage"]}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"insert","lines":["#"],"id":273}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":1},"action":"remove","lines":["#"],"id":274}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"remove","lines":["#"],"id":275}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"remove","lines":["#"],"id":276}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"remove","lines":["#"],"id":277}],[{"start":{"row":97,"column":0},"end":{"row":97,"column":1},"action":"remove","lines":["#"],"id":278}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":1},"action":"remove","lines":["#"],"id":279}],[{"start":{"row":95,"column":0},"end":{"row":95,"column":1},"action":"remove","lines":["#"],"id":280}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"remove","lines":["#"],"id":281}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"remove","lines":["#"],"id":282}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["#"],"id":283}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"remove","lines":["#"],"id":284}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":1},"action":"insert","lines":["#"],"id":285}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"insert","lines":["#"],"id":286}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"insert","lines":["#"],"id":287}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"insert","lines":["#"],"id":288}],[{"start":{"row":97,"column":0},"end":{"row":97,"column":1},"action":"insert","lines":["#"],"id":289}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":1},"action":"insert","lines":["#"],"id":290}],[{"start":{"row":95,"column":0},"end":{"row":95,"column":1},"action":"insert","lines":["#"],"id":291}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"insert","lines":["#"],"id":292}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"insert","lines":["#"],"id":293}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"insert","lines":["#"],"id":294}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":23},"action":"remove","lines":["'/static/'"],"id":295},{"start":{"row":161,"column":13},"end":{"row":161,"column":75},"action":"insert","lines":["\"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)"]}],[{"start":{"row":161,"column":59},"end":{"row":161,"column":60},"action":"remove","lines":["A"],"id":296},{"start":{"row":161,"column":58},"end":{"row":161,"column":59},"action":"remove","lines":["I"]},{"start":{"row":161,"column":57},"end":{"row":161,"column":58},"action":"remove","lines":["D"]},{"start":{"row":161,"column":56},"end":{"row":161,"column":57},"action":"remove","lines":["E"]}],[{"start":{"row":161,"column":55},"end":{"row":161,"column":56},"action":"remove","lines":["M"],"id":297}],[{"start":{"row":161,"column":55},"end":{"row":161,"column":56},"action":"insert","lines":["S"],"id":298},{"start":{"row":161,"column":56},"end":{"row":161,"column":57},"action":"insert","lines":["T"]},{"start":{"row":161,"column":57},"end":{"row":161,"column":58},"action":"insert","lines":["A"]},{"start":{"row":161,"column":58},"end":{"row":161,"column":59},"action":"insert","lines":["T"]},{"start":{"row":161,"column":59},"end":{"row":161,"column":60},"action":"insert","lines":["I"]},{"start":{"row":161,"column":60},"end":{"row":161,"column":61},"action":"insert","lines":["C"]}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":76},"action":"remove","lines":["\"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)"],"id":299},{"start":{"row":161,"column":13},"end":{"row":161,"column":14},"action":"insert","lines":["?"]}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":14},"action":"remove","lines":["?"],"id":300}],[{"start":{"row":161,"column":13},"end":{"row":161,"column":15},"action":"insert","lines":["''"],"id":301}],[{"start":{"row":161,"column":14},"end":{"row":161,"column":15},"action":"insert","lines":["s"],"id":302},{"start":{"row":161,"column":15},"end":{"row":161,"column":16},"action":"insert","lines":["t"]},{"start":{"row":161,"column":16},"end":{"row":161,"column":17},"action":"insert","lines":["a"]},{"start":{"row":161,"column":17},"end":{"row":161,"column":18},"action":"insert","lines":["t"]},{"start":{"row":161,"column":18},"end":{"row":161,"column":19},"action":"insert","lines":["c"]}],[{"start":{"row":161,"column":18},"end":{"row":161,"column":19},"action":"remove","lines":["c"],"id":303}],[{"start":{"row":161,"column":18},"end":{"row":161,"column":19},"action":"insert","lines":["i"],"id":304},{"start":{"row":161,"column":19},"end":{"row":161,"column":20},"action":"insert","lines":["c"]}],[{"start":{"row":161,"column":14},"end":{"row":161,"column":15},"action":"insert","lines":["/"],"id":305}],[{"start":{"row":161,"column":21},"end":{"row":161,"column":22},"action":"insert","lines":["/"],"id":306}],[{"start":{"row":156,"column":29},"end":{"row":156,"column":30},"action":"insert","lines":["-"],"id":307},{"start":{"row":156,"column":30},"end":{"row":156,"column":31},"action":"insert","lines":["u"]},{"start":{"row":156,"column":31},"end":{"row":156,"column":32},"action":"insert","lines":["s"]}],[{"start":{"row":156,"column":32},"end":{"row":156,"column":33},"action":"insert","lines":["-"],"id":308},{"start":{"row":156,"column":33},"end":{"row":156,"column":34},"action":"insert","lines":["w"]},{"start":{"row":156,"column":34},"end":{"row":156,"column":35},"action":"insert","lines":["e"]},{"start":{"row":156,"column":35},"end":{"row":156,"column":36},"action":"insert","lines":["s"]},{"start":{"row":156,"column":36},"end":{"row":156,"column":37},"action":"insert","lines":["t"]}],[{"start":{"row":156,"column":37},"end":{"row":156,"column":38},"action":"insert","lines":["-"],"id":309},{"start":{"row":156,"column":38},"end":{"row":156,"column":39},"action":"insert","lines":["2"]}],[{"start":{"row":158,"column":24},"end":{"row":158,"column":25},"action":"insert","lines":["/"],"id":310}],[{"start":{"row":158,"column":31},"end":{"row":158,"column":32},"action":"insert","lines":["/"],"id":311}],[{"start":{"row":158,"column":24},"end":{"row":158,"column":25},"action":"remove","lines":["/"],"id":312}],[{"start":{"row":158,"column":30},"end":{"row":158,"column":31},"action":"remove","lines":["/"],"id":313}],[{"start":{"row":158,"column":30},"end":{"row":158,"column":31},"action":"insert","lines":["/"],"id":314}],[{"start":{"row":156,"column":53},"end":{"row":156,"column":54},"action":"remove","lines":[" "],"id":315}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["#"],"id":316}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"remove","lines":["#"],"id":317}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"remove","lines":["#"],"id":318}],[{"start":{"row":95,"column":0},"end":{"row":95,"column":1},"action":"remove","lines":["#"],"id":319}],[{"start":{"row":96,"column":0},"end":{"row":96,"column":1},"action":"remove","lines":["#"],"id":320}],[{"start":{"row":97,"column":0},"end":{"row":97,"column":1},"action":"remove","lines":["#"],"id":321}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"remove","lines":["#"],"id":322}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":1},"action":"remove","lines":["#"],"id":323}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"remove","lines":["#"],"id":324}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":1},"action":"remove","lines":["#"],"id":325}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"insert","lines":["#"],"id":326}],[{"start":{"row":46,"column":15},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":327},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":6},"action":"insert","lines":["''"],"id":328}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["p"],"id":329},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["o"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["s"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["t"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["a"]},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"remove","lines":["s"],"id":330},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"remove","lines":["a"]}],[{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["s"],"id":331}],[{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["<"],"id":332}],[{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"remove","lines":["<"],"id":333}],[{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":[","],"id":334}],[{"start":{"row":47,"column":5},"end":{"row":47,"column":10},"action":"remove","lines":["posts"],"id":335},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["s"]},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["u"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["b"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["s"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["c"]},{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["r"]},{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["i"]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["b"]},{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":86,"column":0},"end":{"row":91,"column":2},"action":"remove","lines":["#DATABASES = {","#    'default': {","#        'ENGINE': 'django.db.backends.sqlite3',","#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#    }","#}"],"id":336},{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"remove","lines":["",""]},{"start":{"row":84,"column":64},"end":{"row":85,"column":0},"action":"remove","lines":["",""]}]]},"ace":{"folds":[],"scrolltop":431.5,"scrollleft":0,"selection":{"start":{"row":96,"column":0},"end":{"row":96,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":25,"state":"start","mode":"ace/mode/python"}},"timestamp":1581312582927,"hash":"dbfa53feaba52c7c5a80e86462a27950f33c8217"}