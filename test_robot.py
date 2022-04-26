import unittest
from robot import Robot

class TestRobot(unittest.TestCase):

    def test_rotate_left(self):
        robot = Robot(3, 3, 'N')
        robot.move('L')
        self.assertEqual(robot.facing, 'W')
        robot.move('L')
        self.assertEqual(robot.facing, 'S')
        robot.move('L')
        self.assertEqual(robot.facing, 'E')
        robot.move('L')
        self.assertEqual(robot.facing, 'N')

    def test_rotate_right(self):
        robot = Robot(3, 3, 'N')
        robot.move('R')
        self.assertEqual(robot.facing, 'E')
        robot.move('R')
        self.assertEqual(robot.facing, 'S')
        robot.move('R')
        self.assertEqual(robot.facing, 'W')
        robot.move('R')
        self.assertEqual(robot.facing, 'N')

    def test_rotate_negative_initial_position(self):
        robot = Robot(-3, -3, 'N')
        robot.move('L')
        self.assertEqual(robot.facing, 'W')
        robot.move('L')
        self.assertEqual(robot.facing, 'S')
        robot.move('L')
        self.assertEqual(robot.facing, 'E')
        robot.move('L')
        self.assertEqual(robot.facing, 'N')

    def test_move_forward(self):
        robot = Robot(3, 3, 'N')
        robot.move('M')
        self.assertEqual(robot.y, 4)
        robot.move('M')
        self.assertEqual(robot.y, 5)
        robot.move('M')
        self.assertEqual(robot.y, 6)

    def test_move_negative_position(self):
        robot = Robot(-3, -3, 'N')
        robot.move('M')
        self.assertEqual(robot.y, -2)
        robot.move('M')
        self.assertEqual(robot.y, -1)
        robot.move('M')
        self.assertEqual(robot.y, 0)

    def test_move_with_wrong_direction(self):
        robot = Robot(3, 3, 'N')
        self.assertEqual(robot.move('X'), 'Invalid command')
        self.assertEqual(robot.y, 3)
        self.assertEqual(robot.x, 3)
        self.assertEqual(robot.facing, 'N')

if __name__ == '__main__':
    unittest.main()