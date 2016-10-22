from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, FormView, RedirectView, View
from .forms import LoginForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.
class Index(View):
	def get(self, request, *args, **kwargs):

		if not request.user.is_authenticated():
			return HttpResponseRedirect(reverse_lazy('login'))
		else:
			return HttpResponseRedirect(reverse_lazy('inicio'))


class Inicio(TemplateView):
	template_name = 'inicio/index.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Inicio, self).dispatch(*args, **kwargs)


class Main(TemplateView):
	template_name = 'inicio/main.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Main, self).dispatch(*args, **kwargs)


class Reportes(TemplateView):
	template_name = 'inicio/reportes.html'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(Reportes, self).dispatch(*args, **kwargs)


class LoginView(FormView):
	form_class = LoginForm
	template_name = "inicio/login.html"
	success_url = reverse_lazy("inicio")
	print 'dasdfasdf'
	
	def form_valid(self, form):
		print 'cvcvcvc'
		login(self.request, form.get_user())
		return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
	pattern_name = 'index'
	success_url = reverse_lazy("index")

	def get(self, request, *args, **kwargs):
		logout(request)
		request.session.flush()
		return super(LogoutView, self).get(request, *args, **kwargs)