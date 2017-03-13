from UGD.models.basic import Rank


def get_current_rank(rating):
    """
    Считает приблизительный ранг игрока на основании его рейтинга
    """
    if 100 <= rating <= 2700:
        return Rank.objects.get(pk=(rating//100))
    else:
        return Rank.objects.get(pk=1)
