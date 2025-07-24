class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses


class Football(Results):
    def number_of_wins(self):
        return f"Футбольных побед: {self.victories}"

    def number_of_draws(self):
        return f"Футбольных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Футбольных поражений: {self.losses}"

    def total_points(self):
        points = 3 * self.victories + self.draws
        return f"Общее количество очков: {points}"


class Hockey(Results):
    def number_of_wins(self):
        return f"Хоккейных побед: {self.victories}"

    def number_of_draws(self):
        return f"Хоккейных ничьих: {self.draws}"

    def number_of_losses(self):
        return f"Хоккейных поражений: {self.losses}"

    def total_points(self):
        points = 2 * self.victories + self.draws
        return f"Общее количество очков: {points}"


football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

teams = [football_team, hockey_team]

methods = ["number_of_wins", "number_of_draws", "number_of_losses", "total_points"]

for team in teams:
    for method_name in methods:
        method = getattr(team, method_name)
        print(method())