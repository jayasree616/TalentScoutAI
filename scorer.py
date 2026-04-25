def final_score(match_score, interest_score):
    # match_score already includes:
    # skill + experience + communication + location

    # Interest Score scaled to 20%
    interest_weighted = (interest_score / 100) * 20

    final = round(
        match_score + interest_weighted,
        2
    )

    return final