class Food:
    name = 'Burger'
    def make(self):
        return self.name + ' Buns and meat'

food = Food()
my_name = 'jamal'
lucky_number = 5
my_name = my_name.capitalize()
print('My name is', my_name)
print('I got ' + lucky_number.__str__() +' on it')


print(food.make())