team1_num = 7
team2_num = 8
score_1 = 45
score_2 = 43
team1_time = 1552.512
team2_time = 2153.31451

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else: challenge_result = 'Ничья!'

team1_participants = "В команде Мастера кода участников: %s!" % team1_num
print(team1_participants)

total_participants = "Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num)
print(total_participants)

team2_score = "Команда Волшебники данных решила задач: {}!".format(score_2)
print(team2_score)

team2_time_string = "Волшебники данных решили задачи за {} с!".format(team2_time)
print(team2_time_string)

teams_scores = f"Команды решили {score_1} и {score_2} задач."
print(teams_scores)

battle_result = f"Результат битвы: {challenge_result}"
print(battle_result)

tasks_info = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(tasks_info)