class User:

    id = None
    name = None
    city = None
    food = None
    color = None
    score = 0

    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def set_city(self, city):
        self.city = city

    def set_food(self, food):
        self.food = food

    def set_color(self, color):
        self.color = color

    def add_score(self, new_score):
        self.score += new_score

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_food(self):
        return self.food

    def get_color(self):
        return self.color

    def get_score(self):
        return self.score


def add_score(val, choosed_value, user, users):
    if val in choosed_value:
        id = choosed_value[val]
        choosed_value[val] = -1
        user.add_score(5)
        for user2 in users:
            if user2.get_id() == id:
                user2.add_score(-5)
    else:
        user.add_score(10)
        choosed_value[val] = user.get_id()


def calculate_scores(letter, users):
    for func in [User.get_name, User.get_city, User.get_food, User.get_color]:
        choosed_value = {}
        for user in users:
            val = func(user)
            if val != "":
                if val[0] == letter:
                    add_score(val, choosed_value, user, users)


def print_scores(users):
    print("Scores:")
    for user in users:
        print("user: ", user.get_id(), " | ", "score: ", user.get_score())


def run(users, letter):
    for user in users:
        print("Turn: ", user.get_id())
        user.set_name(input("name: "))
        user.set_city(input("city: "))
        user.set_food(input("food: "))
        user.set_color(input("color: "))

    calculate_scores(letter, users)


if __name__ == "__main__":

    users = []
    number_of_player = input("Enter the number of players:")
    number_of_round = input("Enter the number of rounds:")

    for i in range(int(number_of_player)):
        users.append(User(i))

    for i in range(1, int(number_of_round) + 1):
        print("Round number: ", i)
        selected_letter = input("Enter a letter to start the game: ")
        run(users, selected_letter)

    print_scores(users)
