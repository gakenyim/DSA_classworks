class DateCalculator:
    def __init__(self, Y, m, q):
        self.original_year = Y
        self.original_month = m
        self.day = q
        self.adjust_date()

    def adjust_date(self):
        # Adjust month and year if month is Jan or Feb
        if self.original_month < 3:
            self.month = self.original_month + 12
            self.year = self.original_year - 1
        else:
            self.month = self.original_month
            self.year = self.original_year

        self.K = self.year % 100##year of the century
        self.J = self.year // 100##zero-based century

    def calculate_weekday(self):
        q = self.day
        m = self.month
        K = self.K
        J = self.J

        h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) + 5 * J) % 7

        # Mapping Zeller's output to days of the week
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday"]
        return days[h-1]

date = DateCalculator(2025, 5, 1)
weekday = date.calculate_weekday()
print(f"it is a {weekday}.")
