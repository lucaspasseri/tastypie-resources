from django.shortcuts import render

# Create your views here.

def api_2_homepage_view(request, *args, **kwargs):

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
	return render(r, 'api_2/index.html', context)