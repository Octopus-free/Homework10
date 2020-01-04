from CheckingCard import CheckingCard
from unittest import mock
from unittest.mock import patch
import io
import unittest
from re import findall

card = CheckingCard()

card_after_check = card.strike_numbers_answer_yes(1, 8, ' 5 11')
print(card_after_check.find('Игрок'))

if card_after_check.find('Игрок') == 0:
    print(card_after_check)
else:
    print(card.strike_numbers_answer_yes(1, 8, ' 8 11'))

