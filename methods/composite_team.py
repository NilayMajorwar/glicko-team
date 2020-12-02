from .classes import Match


# Composite team rating update
# TODO: Complete this after implementing Glicko2
def update_ratings_from_match(match: Match):
    for i, team in enumerate(match.teams):
        team_result = match.get_team_result(i)
        other_team = match.teams[2 - i]
        for player_a in team.players:
            for player_b in other_team.players:
                player_a.update(player_b, team_result)
