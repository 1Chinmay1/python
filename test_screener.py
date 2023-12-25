import unittest

from screener import (calculate_volume_change, filter_stocks,
                      get_all_nse_stocks, get_volume_data)


class TestScreener(unittest.TestCase):

    def test_get_all_nse_stocks(self):
        result = get_all_nse_stocks()
        self.assertIsInstance(result, pd.DataFrame)

    def test_get_volume_data(self):
        result = get_volume_data('AAPL')
        self.assertIsInstance(result, pd.Series)

    def test_calculate_volume_change(self):
        result = calculate_volume_change('AAPL')
        self.assertIsInstance(result, float)

    def test_filter_stocks(self):
        stocks = {'AAPL': {'Volume': 100}, 'GOOG': {'Volume': 200}, 'TSLA': {'Volume': 300}}
        result = filter_stocks(stocks)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
