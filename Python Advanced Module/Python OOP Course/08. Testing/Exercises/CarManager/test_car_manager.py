from car_manager import Car
import unittest


class TestsCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "RAV4", 8, 60)

    def test_init_method_with_arg_should_set_proper_make_name(self):
        self.assertEqual(self.car.make, "Toyota")
        self.assertEqual(self.car.model, "RAV4")
        self.assertEqual(self.car.fuel_consumption, 8)
        self.assertEqual(self.car.fuel_capacity, 60)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_property_should_set_make(self):
        actual = self.car.make
        self.assertEqual(actual, "Toyota")

    def test_make_property_setter_with_invalid_input(self):
        with self.assertRaises(Exception):
            self.car.make = ""
        with self.assertRaises(Exception):
            self.car.make = None

    def test_make_property_setter_with_valid_input(self):
        self.car.make = "Honda"
        expected = "Honda"
        actual = self.car.make
        self.assertEqual(actual, expected)

    def test_model_property_setter_with_invalid_input_should_throw_Expection(self):
        with self.assertRaises(Exception):
            self.car.model = ""
        with self.assertRaises(Exception):
            self.car.model = None

    def test_model_property_with_valid_input_should_change_make(self):
        self.car.model = "Corolla"
        expected = "Corolla"
        actual = self.car.model
        self.assertEqual(actual, expected)

    def test_fuel_consumption_setter_with_valid_input_should_change_fuel_consumption(self):
        self.car.fuel_consumption = 10
        expected = 10
        actual = self.car.fuel_consumption
        self.assertEqual(actual, expected)

    def test_fuel_consumption_setter_with_invalid_input_should_throw_Exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = 0
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -1

    def test_fuel_capacity_setter_with_valid_input_should_change_fuel_capacity(self):
        self.car.fuel_capacity = 100
        expected = 100
        actual = self.car.fuel_capacity
        self.assertEqual(actual, expected)

    def test_fuel_capacity_setter_with_invalid_input_should_throw_Exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = -1
        with self.assertRaises(Exception):
            self.car.fuel_capacity = 0

    def test_fuel_amount_setter_should_set_fuel_amount(self):
        self.car.fuel_amount = 60
        expected = 60
        actual = self.car.fuel_amount
        self.assertEqual(actual, expected)

    def test_refuel_method_with_negative_value_should_throw_Exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(-1)
        with self.assertRaises(Exception):
            self.car.refuel(0)

    def test_refuel_method_with_positive_value_should_change_fuel_amount(self):
        self.car.refuel(10)
        expected = 10
        actual = self.car.fuel_amount
        self.assertEqual(actual, expected)

    def test_refuel_method_with_positive_value_greater_than_fuel_capacity(self):
        self.car.refuel(10000)
        expected = 60
        actual = self.car.fuel_amount
        self.assertEqual(actual, expected)

    # def test_drive_method_with_invalid_distance_should_throw_Exception(self):
    #     with self.assertRaises(Exception):
    #         self.car.drive(-1)

    def test_drive_method_with_valid_input_should_change_fuel_amount(self):
        with self.assertRaises(Exception):
            self.car.drive(1000000)


if __name__ == "__main__":
    unittest.main()
