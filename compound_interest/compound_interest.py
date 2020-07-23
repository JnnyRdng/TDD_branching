class CompoundInterest:
    def __init__(self, principal, percent, years):
        self.principal = principal
        self.percent = percent/100
        self.years = years
        self.frequency = 12

    def get_interest(self):
        power = self.years * self.frequency
        result = self.principal * (1 + (self.percent / self.frequency)) ** power
        return round(result, 2)






# A = P(1 + r/n)**nt

# Where:

# P is the principal amount
# r is the annual rate of interest
# t is the number of years the amount is invested
# n is the number of times the interest is compounded per year
# A is the amount at the end of the investment
