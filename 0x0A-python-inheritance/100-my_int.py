#!/usr/bin/python3
"""
module My int rebel class.
"""


class MyInt(int):
    """MyInt class"""
    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
