from django.shortcuts import render

# Create your views here.

def api_1_homepage_view(request, *args, **kwargs):

	# a = args
	# kw = kwargs
	r = request
	u = r.user
	b = r.body
	context={'request':r,
			'user':u,
			'body':b,
			# 'args':a,
			# 'kw':kw
		}
	return render(r, 'api_1/index.html', context)

def homepage_view(request, *args, **kwargs):

	# a = args
	# kw = kwargs
	r = request
	u = r.user
	b = r.body
	context={'request':r,
			'user':u,
			'body':b,
			# 'args':a,
			# 'kw':kw
		}
	return render(r, 'api_1/home.html', context)