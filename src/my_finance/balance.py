

class ShowBalance:
    def __init__(self, data=None):
        self.data = data
        
    @property
    def show_amount(self):
        amount_income = 0
        amount_consumption = 0
        for key, value in self.data.items:
            if key['category'] == "Доход":
                amount_income += value
            else:
                amount_consumption += value

        return f'Доход - {amount_income}\nРасход - {amount_consumption}\nБаланс - {amount_income - amount_consumption}'
