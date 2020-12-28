"""
    Copyright (C) 2020  Basaac, piz2a

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""


import utils
import sys


class ZaQlus:

    variable_names = 'abcde'
    variables = dict()

    def __init__(self):
        for char in self.variable_names:
            self.variables[char] = None

    def main(self, code):  # Main function
        commands = utils.split_code(code)
        for command in commands:
            if command in [';', '']:
                continue
            if command[0] == '\n':
                command = command[1:]

            if utils.set_variables(self, command) == 1:
                utils.evaluate(command, self)

    @staticmethod
    def run(code):
        ZaQlus().main(code)


if __name__ == '__main__':
    ZaQlus.run(input())
