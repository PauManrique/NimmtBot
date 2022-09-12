from nimmt_bot.nimmt_bot import NimmtBot


def test_should_play_the_next_consecutive_card():
    line_1 = [1, 2, 3, 4, 5]
    line_2 = [6, 7, 8, 9, 10]
    line_3 = [11, 12, 13, 14]
    line_4 = [16, 17, 18, 19, 20]
    hand_card = [15, 24, 36, 47, 50]
    bot = NimmtBot()
    assert "PLAY 15" == bot.calculate_move(line_1, line_2, line_3, line_4, hand_card)

def test_should_fallback_to_random():
    line_1 = [1, 2, 3, 4, 5]
    line_2 = [6, 7, 8, 9, 10]
    line_3 = [11, 12, 13, 14, 15]
    line_4 = [16, 17, 18, 19, 20]
    hand_card = [30, 24, 36, 47, 50]
    bot = NimmtBot()
    assert "RANDOM" == bot.calculate_move(line_1, line_2, line_3, line_4, hand_card)    
