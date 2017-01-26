from UGD.models.ranks import Rank


def current_rank(rating):
    if 100 <= rating <= 2700:
        return Rank.objects.get(pk=(rating//100))
    else:
        return 0

print(current_rank(2700))