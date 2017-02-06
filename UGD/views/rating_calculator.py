from django.views.generic.base import TemplateView
from functions import rate_calc_func
# todo Незакончено


class RatingCalculatorView(TemplateView):
    template_name = 'UGD/rating_calculator.html'
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super(RatingCalculatorView, self).get_context_data(**kwargs)
        try:
            context['new_rating'] = int(self.request.GET['first_rating']) + rate_calc_func.growth(self.request.GET['first_rating'], self.request.GET['second_rating'], self.request.GET['result'])
            print(context['new_rating'])
        except KeyError:
            print(2)
        return context
