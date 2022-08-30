from math import log


class Functions:

    def display_as_percentage(self, value):   
        return '{:.1f}%'.format(value * 100)

    def simple_return(self, start_price, end_price, dividend=0):
        return ((end_price - start_price + dividend)/start_price)

    def log_return(self, start_price, end_price):
        return log(end_price) - log(start_price)

    def annualize_return(self, log_return, t):
        return log_return*t