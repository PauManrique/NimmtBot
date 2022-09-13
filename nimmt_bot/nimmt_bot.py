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

  def calculate_line(self, line_1, line_2, line_3, line_4):
    line_to_play = None
    min_line_points = 100
    for idx, line in enumerate([line_1, line_2, line_3, line_4]):
      line_points = self.calculate_line_points(line)
      if line_points < min_line_points:
        line_to_play = idx
        min_line_points = line_points
    
    return "PICK " + str(line_to_play)  

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
    min_risk = 1000    

    for line in safe_lines:
      line_last_card = line[len(line) - 1]
      for card in hand_cards:
        risk = self.calculate_risk(card, line)
        if card > line_last_card and risk < min_risk and not self.is_card_going_to_full_line(card, line_last_card, full_lines_last_cards):
          min_risk = risk
          card_to_play = card

    return card_to_play

  def is_card_going_to_full_line(self, card, line_last_card, full_lines_last_cards):
    for full_line_last_card in full_lines_last_cards:
      if full_line_last_card > line_last_card and card > full_line_last_card:
        return True

    return False

  def calculate_risk(self, card, line):
    card_space_risk = (card - line[len(line) - 1]) ** 1.2
    line_length_risk = len(line) ** 2
    line_points_risk = (self.calculate_line_points(line) + self.calculate_card_points(card)) ** 1.3
    print("card = " + str(card) + " last in line = " + str(line[len(line) - 1]) + " line length = " + str(len(line)) + " risk = " + str(card_space_risk + line_length_risk + line_points_risk))
    print("line points risk = " + str(line_points_risk) + " card_space_risk = " + str(card_space_risk) + " line_length_risk = " + str(line_length_risk))
    return card_space_risk + line_length_risk + line_points_risk

  def calculate_line_points(self, line):
    points = 0
    for card in line:
      points += self.calculate_card_points(card)
    return points

  def calculate_card_points(self, card):
    if card == 55:
      return 7
    elif card % 11 == 0:
      return 5
    elif card % 10 == 0:
      return 3      
    elif card % 5 == 0:
      return 2
    else:
      return 1        