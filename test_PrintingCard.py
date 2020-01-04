from PrintingCard import PrintingCard
import unittest


class TestPrintingCard(unittest.TestCase):

    # создаем функцию для избежания дублирования кода в каждой тестовой функции
    def setUp(self):
        self.print_card = PrintingCard()
        self.test_human_card = '10'
        self.test_computer_card = '11'
        self.list_computers_cards = ['10', '11']

    # функция для тестирования отрисовки карточек игроков людей
    def test_print_human_cards(self):
        self.assertIn(self.test_human_card, self.print_card.print_human_cards(1, self.test_human_card))

    # функция для тестирования отрисовки карточек игроков компьютеров
    def test_print_computers_cards(self):
        self.assertIn(self.test_computer_card, self.print_card.print_computers_cards(self.list_computers_cards))
