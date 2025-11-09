import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_korkeimmat_pisteet(self):
        self.assertEqual(len(self.stats.top(1)), 2)

    def test_nimi_haku_ei_loydy(self):
        self.assertEqual(self.stats.search("Jorma"), None)

    def test_haku_joukkueella(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)

    def test_nimi_haku_loytyy(self):
        self.assertNotEqual(self.stats.search("Kurri"), None)
