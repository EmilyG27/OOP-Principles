class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self._category_name = category_name
        self.__allocated_budget = allocated_budget

    def get_category_name(self):
        return self._category_name
    
    def set_category_name(self, added_category):
        self.category_name = added_category

    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, amount):
        self.__allocated_budget = amount

    def add_expense(self, expense):
        if 0 < expense <= self.get_allocated_budget():
            self.set_allocated_budget(self.get_allocated_budget() - expense)
            print(expense)

budget = BudgetCategory("Food", 1000)
print(f"Category: {budget.get_category_name()}")
print(f"Budget: {budget.get_allocated_budget()}")

budget.add_expense(100)
print(f"Updated budget: {budget.get_allocated_budget()}")