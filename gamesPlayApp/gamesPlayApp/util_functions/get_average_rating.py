def get_average_rating(games_count, rating_sum):
    average_rating = 0.0

    if games_count > 0:
        average_rating = rating_sum / games_count

    return average_rating
