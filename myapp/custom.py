from django.contrib.admin import AdminSite
from django.conf import settings
from django.utils.decorators import  method_decorator
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.views.decorators.cache import never_cache
from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import login, authenticate
from django.utils.translation import gettext as _, gettext_lazy
from django.urls import NoReverseMatch, reverse
from django.http import Http404, HttpResponseRedirect

class CustomAdminSite(AdminSite):
    
    @never_cache
    def login(self, request, extra_context=None):
        """
        Displays the login form for the given HttpRequest.
        """
        if request.method == 'GET' and self.has_permission(request):
            # Already logged-in, redirect to admin index
            index_path = reverse('myapp:home', current_app=self.name)
            return HttpResponseRedirect(index_path)

        from django.contrib.auth.views import LoginView
        context = {
            'title': _('Log in'),
            'app_path': request.get_full_path(),
            REDIRECT_FIELD_NAME: reverse('myapp:home', current_app=self.name)

            # REDIRECT_FIELD_NAME: settings.ADMIN_LOGIN_REDIRECT_URL,
        }
        context.update(extra_context or {})

        defaults = {
            'extra_context': context,
            'authentication_form': self.login_form or AdminAuthenticationForm,
            'template_name': self.login_template or 'admin/login.html',
        }
        return LoginView.as_view(**defaults)(request)
        # return login(request, **defaults)
        

site = CustomAdminSite()