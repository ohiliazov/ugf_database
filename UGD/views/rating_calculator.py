from django.views.generic.base import TemplateView
from functions import rate_calc_func
# todo Незакончено


class RatingCalculatorView(TemplateView):
    template_name = 'UGD/rating_calculator.html'
    http_method_names = ['get', 'post']

    def get_context_data(self, **kwargs):
        context = super(RatingCalculatorView, self).get_context_data(**kwargs)
        try:
            first_rating = int(self.request.GET['first_rating'])
            second_rating = int(self.request.GET['second_rating'])
            result = int(self.request.GET['result'])
            context['new_rating_1'] = rate_calc_func.new_rating(
                first_rating, second_rating, result)
            context['new_rating_1a'] = rate_calc_func.new_rating(
                first_rating, second_rating, (1-result))
            context['new_rating_2'] = rate_calc_func.new_rating(
                second_rating, first_rating, (1-result))
            context['new_rating_2a'] = rate_calc_func.new_rating(
                second_rating, first_rating, result)
            context['con_param_1'] = rate_calc_func.con(first_rating)
            context['con_param_2'] = rate_calc_func.con(second_rating)
            context['a_param_1'] = rate_calc_func.a_param(first_rating)
            context['a_param_2'] = rate_calc_func.a_param(second_rating)
            context['win_exp_1'] = round(rate_calc_func.winning_expectancy(first_rating, second_rating), 2)
            context['win_exp_2'] = round(rate_calc_func.winning_expectancy(second_rating, first_rating), 2)
        except KeyError:
            print(2)
        return context
