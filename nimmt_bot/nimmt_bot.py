from distutils.command.install_egg_info import safe_name
from operator import truediv


class NimmtBot:
  MAX_CARDS_PER_LINE = 5

  def calculate_move(self, line_1, line_2, line_3, line_4, hand_cards):
    safe_lines = self.get_safe_lines(line_1, line_2, line_3, line_4)
    full_lines_last_cards = self.get_full_lines_last_cards(line_1, line_2, line_3, line_4)
    card_to_play = self.choose_card_from_hand(safe_lines, full_lines_last_cards, hand_cards)

    if card_to_play is None:
      return "RANDOM"      
    return "PLAY " + str(card_to_play)

  def get_safe_lines(self, line_1, line_2, line_3, line_4):
    safe_lines = []
    for line in line_1, line_2, line_3, line_4:
      if len(line) < self.MAX_CARDS_PER_LINE:
        safe_lines.append(line)

    return safe_lines

  def get_full_lines_last_cards(self, line_1, line_2, line_3, line_4):
    full_lines_last_cards = []
    for line in line_1, line_2, line_3, line_4:
      if len(line) >= self.MAX_CARDS_PER_LINE:
        full_lines_last_cards.append(line[len(line) - 1])

    return full_lines_last_cards

  def choose_card_from_hand(self, safe_lines, full_lines_last_cards, hand_cards):
    card_to_play = None
    min_card_value_diff = 200    

    for line in safe_lines:
      line_last_card = line[len(line) - 1]
      for card in hand_cards:
        diff = card - line_last_card
        if card > line_last_card and diff < min_card_value_diff and not self.is_card_going_to_full_line(card, line_last_card, full_lines_last_cards):
          min_card_value_diff = diff
          card_to_play = card

    return card_to_play

  def is_card_going_to_full_line(self, card, line_last_card, full_lines_last_cards):
    for full_line_last_card in full_lines_last_cards:
      if full_line_last_card > line_last_card and card > full_line_last_card:
        return True

    return False    