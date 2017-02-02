from UGD.models.ranks import Rank


def current_rank(rating: int):
    """
    Считает приблизительный ранг игрока на основании его рейтинга
    """
    if 100 <= rating <= 2700:
        return Rank.objects.get(pk=(rating//100))
