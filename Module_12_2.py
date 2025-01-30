import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in sorted(self.participants, key = lambda x: -x.speed):
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Усэйн", speed = 10)
        self.runner_andrey = Runner("Андрей", speed = 9)
        self.runner_nick = Runner("Ник", speed = 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            formatted_results = {place: str(runner) for place, runner in value.items()}
            print(f"{key}: {formatted_results}")

    @unittest.skip('Тесты в этом кейсе заморожены')
    def test_race_usain_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results["Усэйн vs Ник"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @unittest.skip('Тесты в этом кейсе заморожены')
    def test_race_andrey_nick(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results["Андрей vs Ник"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

    @unittest.skip('Тесты в этом кейсе заморожены')
    def test_race_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        self.__class__.all_results["Усэйн vs Андрей vs Ник"] = results
        self.assertTrue(results[max(results.keys())].name == "Ник")

if __name__ == '__main__':
    unittest.main()