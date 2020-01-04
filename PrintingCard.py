# создаем класс для отрисовки в терминале карточек игроков
class PrintingCard:

    # функция для отрисовки карточек игроков людей
    def print_human_cards(self, human_number, human_card):
        name_message = f'Карточка игрока {human_number} '
        underline_message = f'--'*13
        func_message = f'{name_message}\n{underline_message}\n{human_card}\n{underline_message}'
        return func_message

    # функция для отрисовки карточек игроков компьютеров
    def print_computers_cards(self, computers_players_cards):

        func_message = ''
        for computer_card in computers_players_cards:
            computer_number = computers_players_cards.index(computer_card) + 1
            name_message = f'Карточка компьютерного игрока {computer_number} '
            underline_message = f'--' * 13
            func_message += f'{name_message}\n{underline_message}\n{computer_card}\n{underline_message}\n'
        return func_message
