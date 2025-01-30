import unittest
from Module_12_1 import RunnerTest
from Module_12_2 import TournamentTest

suite = unittest.TestSuite()

suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
