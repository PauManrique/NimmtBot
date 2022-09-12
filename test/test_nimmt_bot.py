from nimmt_bot.nimmt_bot import NimmtBot


def test_random():
    bot = NimmtBot()
    assert "RANDOM" == bot.calculate_move()
