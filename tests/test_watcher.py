import unittest
import os


class GeobricksTest(unittest.TestCase):

    # Raster
    def test_placeholder(self):
        self.assertEqual(True, True)



def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(GeobricksTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    run_test()


