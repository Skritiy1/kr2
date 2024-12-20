'''Обработать результаты первенства по футболу. Результаты каж- дой игры заданы в виде названий команд и счета (количество забитых
и пропущенных мячей). Сформировать таблицу очков (выигрыш - 3,ничья - 1, проигрыш - 0) и упорядочить результаты в соответствии с занятым местом. Если сумма очков у двух команд одинакова, то срав- ниваются разности забитых и пропущенных мячей. Вывести резуль- тирующую таблицу, содержащую место, название команды, количе-
ство очков.'''

class FootballTeam:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.goal_difference = 0

    def update_stats(self, goals_scored, goals_conceded):
        self.goals_scored += goals_scored
        self.goals_conceded += goals_conceded
        self.goal_difference = self.goals_scored - self.goals_conceded

        if goals_scored > goals_conceded:
            self.points += 3  
        elif goals_scored == goals_conceded:
            self.points += 1 

class ChampionshipTable:
    def __init__(self):
        self.teams = {}

    def add_match_result(self, team1_name, team1_goals, team2_name, team2_goals):
        if team1_name not in self.teams:
            self.teams[team1_name] = FootballTeam(team1_name)
        if team2_name not in self.teams:
            self.teams[team2_name] = FootballTeam(team2_name)

        self.teams[team1_name].update_stats(team1_goals, team2_goals)
        self.teams[team2_name].update_stats(team2_goals, team1_goals)

    def get_sorted_table(self):
        sorted_teams = sorted(
            self.teams.values(), 
            key=lambda x: (x.points, x.goal_difference), 
            reverse=True
        )
        return sorted_teams

    def print_table(self):
        sorted_teams = self.get_sorted_table()
        print("Место | Команда | Очки")
        print("-" * 30)
        for place, team in enumerate(sorted_teams, 1):
            print(f"{place:4d} | {team.name:6s} | {team.points:4d}")

def main():
    championship = ChampionshipTable()

    championship.add_match_result("Спартак", 3, "Зенит", 1)
    championship.add_match_result("ЦСКА", 2, "Локомотив", 2)
    championship.add_match_result("Спартак", 1, "ЦСКА", 1)
    championship.add_match_result("Зенит", 4, "Локомотив", 0)

    championship.print_table()

if __name__ == "__main__":
    main()