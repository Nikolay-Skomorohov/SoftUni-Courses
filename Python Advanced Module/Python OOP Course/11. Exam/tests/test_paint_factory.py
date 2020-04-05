from project.factory.paint_factory import PaintFactory
import unittest


class TestsPaintFactory(unittest.TestCase):

    def test_init_method_with_proper_values_should(self):
        inputs = ["Test Factory", 1000]
        test_object = PaintFactory(*inputs)
        self.assertEqual(test_object.name, "Test Factory")
        self.assertEqual(test_object.capacity, "Test Factory")
        self.assertEqual(test_object.ingredients, {})

    def test_add_ingredient_with_invalid_type_input_should_raise_error(self):
        inputs = ["Test Factory", 1000]
        test_object = PaintFactory(*inputs)
        with self.assertRaises(TypeError):
            test_object.add_ingredient("Wrong Input", 1000)

    def test_add_ingredient_with_invalid_quantity_input_should_raise_error(self):
        inputs = ["Test Factory", 1000]
        test_object = PaintFactory(*inputs)
        with self.assertRaises(ValueError):
            test_object.add_ingredient("white", "Error")

    def test_add_ingredient_with_quantity_larger_than_capacity_should_raise_error(self):
        inputs = ["Test Factory", 1000]
        test_object = PaintFactory(*inputs)
        with self.assertRaises(ValueError):
            test_object.add_ingredient("white", 100000)

    def test_add_ingredient_with_valid_inputs_should_add_ingredient(self):
        inputs = ["Test Factory", 1000]
        test_object = PaintFactory(*inputs)
        test_object.add_ingredient("white", 10)
        expected = {"white": 10}
        actual = test_object.ingredients
        self.assertEqual(actual, expected)

    def test_remove_ingredient_with_invalid_ingredient_type_should_raise_error(self):
        inputs = ["Test Factory", 1000]
        test_object = PaintFactory(*inputs)
        test_object.ingredients = {"white": 10}
        with self.assertRaises(KeyError):
            test_object.remove_ingredient("Wrong Ingredient", 5)

    def test_remove_ingredient_with_invalid_quantity_should_raise_error(self):
        inputs = ["Test Factory", 1000]
        test_object = PaintFactory(*inputs)
        test_object.ingredients = {"white": 10}
        with self.assertRaises(ValueError):
            test_object.remove_ingredient("white", 1000)

    def test_remove_ingredient_with_valid_inputs_should_remove_ingredient(self):
        inputs = ["Test Factory", 1000]
        test_object = PaintFactory(*inputs)
        test_object.ingredients = {"white": 10}
        test_object.remove_ingredient("white", 5)
        expected = {"white": 5}
        actual = test_object.ingredients
        self.assertEqual(actual, expected)

    def test_products_method_should_return_ingredients(self):
        inputs = ["Test Factory", 1000]
        test_object = PaintFactory(*inputs)
        test_object.ingredients = {"white": 10, "red": 5}
        expected = {"white": 10, "red": 5}
        actual = test_object.products
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
