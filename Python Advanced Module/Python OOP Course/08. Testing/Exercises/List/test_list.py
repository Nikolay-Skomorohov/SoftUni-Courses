from list import IntegerList
import unittest


class TestIntegerList(unittest.TestCase):
    def test_init_with_no_args_should_create_empty_data(self):
        data = []
        integer_list = IntegerList(*data)
        expected = []
        actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected)

    def test_init_with_int_for_args_should_add_elements_to_data(self):
        data = [1, 2, 5]
        integer_list = IntegerList(*data)
        expected = [1, 2, 5]
        actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected)

    def test_init_with_invalid_input_data_should_not_add_element_to_data(self):
        data = ["Coronavirus", "SARS", "MERS"]
        integer_list = IntegerList(*data)
        expected = []
        actual = integer_list._IntegerList__data
        self.assertEqual(actual, expected)

    def test_get_data_returns_proper_data(self):
        data = [10, 900]
        integer_list = IntegerList(*data)
        expected = integer_list._IntegerList__data
        actual = integer_list.get_data()
        self.assertEqual(actual, expected)

    def test_add_method_with_invalid_data_should_not_add_element(self):
        data = []
        integer_list = IntegerList(*data)
        with self.assertRaises(ValueError):
            integer_list.add("Social Distancing")

    def test_add_method_with_valid_data_should_add_element(self):
        data = [1, 5]
        integer_list = IntegerList(*data)
        expected = [1, 5, 10]
        actual = integer_list.add(10)
        self.assertEqual(actual, expected)

    def test_remove_index_method_with_index_out_range_should_raise_indexError(self):
        data = [1, 2]
        integer_list = IntegerList(*data)
        with self.assertRaises(IndexError):
            integer_list.remove_index(10)

    def test_remove_index_method_with_valid_data_for_proper_func_return(self):
        data = [1, 5, 10]
        integer_list = IntegerList(*data)
        expected = 5
        actual = integer_list.remove_index(1)
        self.assertEqual(actual, expected)

    def test_get_method_with_invalid_index_should_throw_IndexError(self):
        data = [10, 1000, 10000]
        integer_list = IntegerList(*data)
        with self.assertRaises(IndexError):
            integer_list.get(10)

    def test_get_method_with_valid_index_should_return_item_at_index(self):
        data = [1, 5, 10]
        integer_list = IntegerList(*data)
        expected = 5
        actual = integer_list.get(1)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
