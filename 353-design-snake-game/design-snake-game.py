# -*- coding:utf-8 -*-


# Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.
#
# The snake is initially positioned at the top left corner (0,0) with length = 1 unit.
#
# You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.
#
# Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.
#
# When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.
#
#
# Example:
#
# Given width = 3, height = 2, and food = [[1,2],[0,1]].
#
# Snake snake = new Snake(width, height, food);
#
# Initially the snake appears at position (0,0) and the food at (1,2).
#
# |S| | |
# | | |F|
#
# snake.move("R"); -> Returns 0
#
# | |S| |
# | | |F|
#
# snake.move("D"); -> Returns 0
#
# | | | |
# | |S|F|
#
# snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )
#
# | |F| |
# | |S|S|
#
# snake.move("U"); -> Returns 1
#
# | |F|S|
# | | |S|
#
# snake.move("L"); -> Returns 2 (Snake eats the second food)
#
# | |S|S|
# | | |S|
#
# snake.move("U"); -> Returns -1 (Game over because snake collides with border)
#
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all test cases.


class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self._map = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        self.set = set([0])
        self.queue = [0]

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """

        old_head = self.queue[0]
        self.set.remove(self.queue[-1])  #new head is legal to be in old tail's position, remove from set temporarily
        old_height, old_width = old_head / self.width, old_head % self.width
        new_height, new_width = old_height + self._map[direction][0], old_width + self._map[direction][1]
        new_head = new_height*self.width + new_width
        
        if not (0<=new_height<self.height and 0<=new_width<self.width): 
            # crosses the screen boundary
            return -1
        elif new_head in self.set:
            # bites tail
            return -1
        
        self.queue.insert(0, new_head)
        self.set.add(new_head)
        if self.food_index < len(self.food) and [new_height, new_width] == self.food[self.food_index]:
            # reaches food
            self.food_index += 1
            self.set.add(self.queue[-1])
            return self.food_index
        else:
            self.queue.pop() 
            return self.food_index


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
