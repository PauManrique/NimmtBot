class NimmtBot:
  MAX_CARDS_PER_LINE = 5

  def calculate_move(self, line_1, line_2, line_3, line_4, hand_cards):
    safe_lines = []
    for line in line_1, line_2, line_3, line_4:
      if len(line) < self.MAX_CARDS_PER_LINE:
        safe_lines.append(line)
    card_to_play = None
    min_card_value_diff = 200    
    for line in safe_lines:
      line_last_card = line[len(line) - 1]
      for card in hand_cards:
        diff = card - line_last_card
        if card > line_last_card and diff < min_card_value_diff:
          min_card_value_diff = diff
          card_to_play = card
    if card_to_play is None:
      return "RANDOM"      
    return "PLAY " + str(card_to_play)