import signal
from os import kill, getpid
from django.shortcuts import redirect
# todo ЗАКОНЧИТЬ ГЛАВНУЮ СТРАНИЦУ


# Create your views here.
def mod_wsgi_reload(request):
    if request.user.is_authenticated():
        try:
            if request.META['mod_wsgi.process_group'] != '':
                kill(getpid(), signal.SIGINT)
            return redirect('admin:index')
        except KeyError:
            return redirect('admin:index')
    else:
        return redirect('UGD:index')