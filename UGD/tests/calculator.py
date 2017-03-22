from django.test import TestCase

from functions.rate_calc_func import new_rating, calculate_tournament


class FullTournamentTests(TestCase):
    def test_001(self):
        START_RATINGS = {
            1: 2704,
            2: 2680,
            3: 2368,
            4: 2561,
            5: 2414,
            6: 2548,
            7: 2500,
            8: 2459
        }
        TOURNAMENT_DATA = {
            1: [(8, 1), (6, 1), (7, 1), (4, 1), (2, 1), (5, 1), (3, 1)],
            2: [(7, 1), (3, None), (4, 0), (8, 1), (1, 0), (6, 1), (5, 1)],
            3: [(5, 1), (2, None), (8, 1), (6, 1), (7, 1), (4, 1), (1, 0)],
            4: [(6, 1), (7, 1), (2, 1), (1, 0), (5, 0), (3, 0), (8, 1)],
            5: [(3, 0), (8, 1), (6, 1), (7, 0), (4, 1), (1, 0), (2, 0)],
            6: [(4, 0), (1, 0), (5, 0), (3, 0), (8, 1), (2, 0), (7, 1)],
            7: [(2, 0), (4, 0), (1, 0), (5, 1), (3, 0), (8, 0), (6, 0)],
            8: [(1, 0), (5, 0), (3, 0), (2, 0), (6, 0), (7, 1), (4, 0)]
        }

        FINISH_RATINGS = {1: 2713, 2: 2672, 3: 2507, 4: 2563, 5: 2438, 6: 2531, 7: 2479, 8: 2447}
        RESULTS = calculate_tournament(START_RATINGS, TOURNAMENT_DATA)
        NEXT_RATINGS = {}
        for place in RESULTS:
            NEXT_RATINGS[place] = round(RESULTS[place])

        self.assertEqual(NEXT_RATINGS, FINISH_RATINGS)

    def test_002(self):
        TOTAL_ROUNDS = 6

        START_RATINGS = {1: 1330.0, 2: 1286.0, 3: 866.0, 4: 843.0, 5: 695.0, 6: 799.0, 7: 482.0, 8: 512.0, 9: 717.0,
                         10: 370.0, 11: 467.0, 12: 324.0, 13: 386.0, 14: 100.0, 15: 103.0, 16: 187.0, 17: 101.0,
                         18: 232.0, 19: 142.0, 20: 100.0, 21: 100.0, 22: 100.0, 23: 100.0, 24: 100.0}

        TOURNAMENT_DATA = {
            1: [(6, 1), (3, 1), (2, 1), (4, 1), (5, 1), (7, 1)],
            2: [(9, 1), (4, 1), (1, 0), (3, 1), (7, 1), (8, 1)],
            3: [(5, 1), (1, 0), (6, 1), (2, 0), (8, 0), (9, 1)],
            4: [(8, 1), (2, 0), (7, 1), (1, 0), (9, 1), (5, 0)],
            5: [(3, 0), (10, 0), (11, 1), (8, 1), (1, 0), (4, 1)],
            6: [(1, 0), (8, 1), (3, 0), (7, 0), (10, 1), (12, 1)],
            7: [(11, 1), (9, 1), (4, 0), (6, 1), (2, 0), (1, 0)],
            8: [(4, 0), (6, 0), (12, 1), (5, 0), (3, 1), (2, 0)],
            9: [(2, 0), (7, 0), (10, 1), (13, 1), (4, 0), (3, 0)],
            10: [(12, 1), (5, 1), (9, 0), (11, 1), (6, 0), (14, 1)],
            11: [(7, 0), (13, 1), (5, 0), (10, 0), (12, 0), (15, 1)],
            12: [(10, 0), (21, 1), (8, 0), (14, 1), (11, 1), (6, 0)],
            13: [(18, 1), (11, 0), (19, 1), (9, 0), (15, 0), (16, 1)],
            14: [(15, 1), (18, 1), (16, 1), (12, 0), (19, 1), (10, 0)],
            15: [(14, 0), (22, 1), (20, 1), (18, 1), (13, 1), (11, 0)],
            16: [(23, 1), (20, 1), (14, 0), (17, 1), (21, 1), (13, 0)],
            17: [(20, 0), (24, 1), (22, 1), (16, 0), (18, 1), (19, 1)],
            18: [(13, 0), (14, 0), (21, 1), (15, 0), (17, 0), (24, 1)],
            19: [(22, 1), (23, 1), (13, 0), (20, 1), (14, 0), (17, 0)],
            20: [(17, 1), (16, 0), (15, 0), (19, 0), (24, 1), (23, 1)],
            21: [(24, 1), (12, 0), (18, 0), (23, 1), (16, 0), (22, 0)],
            22: [(19, 0), (15, 0), (17, 0), (24, 0), (23, 1), (21, 1)],
            23: [(16, 0), (19, 0), (24, 1), (21, 0), (22, 0), (20, 0)],
            24: [(21, 0), (17, 0), (23, 0), (22, 1), (20, 0), (18, 0)]
        }

        FINISH_RATINGS = {
            1: 1373, 2: 1288, 3: 878, 4: 843, 5: 753, 6: 772, 7: 671, 8: 594, 9: 671,
            10: 542, 11: 418, 12: 416, 13: 401, 14: 294, 15: 312, 16: 290, 17: 291,
            18: 179, 19: 169, 20: 226, 21: 100, 22: 225, 23: 100, 24: 100
        }

        RESULTS = calculate_tournament(START_RATINGS, TOURNAMENT_DATA)

        NEXT_RATINGS = {}

        for place in RESULTS:
            NEXT_RATINGS[place] = round(RESULTS[place])
        self.maxDiff = None
        self.assertEqual(NEXT_RATINGS, FINISH_RATINGS)


class SingleTournamentCalculator(TestCase):
    def test_001(self):
        self.assertAlmostEqual(new_rating(1286, 717, 1), 1289.88, places=2)
        self.assertAlmostEqual(new_rating(717, 1286, 0), 718.2, places=2)

    def test_002(self):
        self.assertAlmostEqual(new_rating(1289.88, 857.14, 1), 1295.49, places=2)
        self.assertAlmostEqual(new_rating(857.14, 1289.88, 0), 855.60, places=2)

    def test_003(self):
        self.assertAlmostEqual(new_rating(1295.49, 1339.05, 0), 1274.13, places=2)
        self.assertAlmostEqual(new_rating(1339.05, 1295.49, 1), 1363.53, places=2)

    def test_004(self):
        self.assertAlmostEqual(new_rating(1274.13, 921.76, 1), 1281.71, places=2)
        self.assertAlmostEqual(new_rating(921.76, 1274.13, 0), 917.72, places=2)

    def test_005(self):
        self.assertAlmostEqual(new_rating(1281.71, 666.31, 1), 1285.25, places=2)
        self.assertAlmostEqual(new_rating(666.31, 1281.71, 0), 668.19, places=2)

    def test_006(self):
        self.assertAlmostEqual(new_rating(1285.25, 590.94, 1), 1288.32, places=2)
        self.assertAlmostEqual(new_rating(590.94, 1285.25, 0), 593.79, places=1)


class SingleGameHighDanCalculator(TestCase):
    def test_001(self):
        self.assertEqual(round(new_rating(2704, 2459, 1)), 2705)
        self.assertEqual(round(new_rating(2459, 2704, 0)), 2459)

    def test_002(self):
        self.assertEqual(round(new_rating(2680, 2500, 1)), 2681)
        self.assertEqual(round(new_rating(2500, 2680, 0)), 2499)

    def test_003(self):
        self.assertEqual(round(new_rating(2472, 2414, 1)), 2477)
        self.assertEqual(round(new_rating(2414, 2472, 0)), 2409)

    def test_004(self):
        self.assertEqual(round(new_rating(2561, 2548, 1)), 2567)
        self.assertEqual(round(new_rating(2548, 2561, 0)), 2543)

    def test_005(self):
        self.assertEqual(round(new_rating(2705, 2543, 1)), 2706)


class SingleGameTournamentCalculatorTests(TestCase):
    def test_001(self):
        self.assertEqual(round(new_rating(2348, 1373, 1), 2), 2348.26)
        self.assertEqual(round(new_rating(1373, 2348, 0), 2), 1374.76)

    def test_002(self):
        self.assertEqual(round(new_rating(2323, 1372, 1), 2), 2323.29)
        self.assertEqual(round(new_rating(1372, 2323, 0), 2), 1373.75)

    def test_003(self):
        self.assertEqual(round(new_rating(1730, 1317, 1), 2), 1732.88)
        self.assertEqual(round(new_rating(1317, 1730, 0), 2), 1316.28)

    def test_004(self):
        self.assertEqual(round(new_rating(1730, 1317, 1), 2), 1732.88)
        self.assertEqual(round(new_rating(1317, 1730, 0), 2), 1316.28)

    def test_005(self):
        self.assertEqual(round(new_rating(1113, 1134, 1), 2), 1149.99)
        self.assertEqual(round(new_rating(1134, 1113, 0), 2), 1102.62)

    def test_006(self):
        self.assertEqual(round(new_rating(1058, 843, 1), 2), 1074.88)
        self.assertEqual(round(new_rating(843, 1058, 0), 2), 830.1)

    def test_007(self):
        self.assertEqual(round(new_rating(753, 636, 1), 2), 784.64)
        self.assertEqual(round(new_rating(636, 753, 0), 2), 610.6)

    def test_008(self):
        self.assertEqual(round(new_rating(827, 878, 1), 2), 875.98)
        self.assertEqual(round(new_rating(878, 827, 0), 2), 837.45)

    def test_009(self):
        self.assertEqual(round(new_rating(772, 705, 1), 2), 808.56)
        self.assertEqual(round(new_rating(705, 772, 0), 2), 674.94)

    def test_010(self):
        self.assertEqual(round(new_rating(671, 542, 1), 2), 703.41)
        self.assertEqual(round(new_rating(542, 671, 0), 2), 516.44)

    def test_011(self):
        self.assertEqual(round(new_rating(671, 542, 1), 2), 703.41)
        self.assertEqual(round(new_rating(542, 671, 0), 2), 516.44)

    def test_012(self):
        self.assertEqual(round(new_rating(594, 416, 1), 2), 623.41)
        self.assertEqual(round(new_rating(416, 594, 0), 2), 393.98)

    def test_013(self):
        self.assertEqual(round(new_rating(312, 243, 1), 2), 360.78)
        self.assertEqual(round(new_rating(243, 312, 0), 2), 204.78)

    def test_014(self):
        self.assertEqual(round(new_rating(291, 225, 1), 2), 340.75)
        self.assertEqual(round(new_rating(225, 291, 0), 2), 186.05)

    def test_015(self):
        self.assertEqual(round(new_rating(294, 226, 1), 2), 343.41)
        self.assertEqual(round(new_rating(226, 294, 0), 2), 187.34)

    def test_016(self):
        self.assertEqual(round(new_rating(294, 226, 1), 2), 343.41)
        self.assertEqual(round(new_rating(226, 294, 0), 2), 187.34)

    def test_017(self):
        self.assertEqual(round(new_rating(294, 226, 1), 2), 343.41)
        self.assertEqual(round(new_rating(226, 294, 0), 2), 187.34)

    def test_018(self):
        self.assertEqual(round(new_rating(100, 100, 1), 2), 164.96)
        self.assertEqual(round(new_rating(100, 100, 0), 2), 100)

    def test_019(self):
        self.assertEqual(round(new_rating(169, 100, 1), 2), 221.93)
        self.assertEqual(round(new_rating(100, 169, 0), 2), 100)

    def test_020(self):
        self.assertEqual(round(new_rating(103, 100, 1), 2), 167.42)
        self.assertEqual(round(new_rating(100, 103, 0), 2), 100)

    def test_021(self):
        self.assertAlmostEqual(new_rating(2348.26, 1732.88, 1), 2348.60, places=1)
        self.assertAlmostEqual(new_rating(1732.88, 2348.26, 0), 1733.71, places=1)

    def test_022(self):
        self.assertAlmostEqual(new_rating(2323.29, 1588.72, 1), 2323.60, places=1)
        self.assertAlmostEqual(new_rating(1588.72, 2323.29, 0), 1589.91, places=1)
