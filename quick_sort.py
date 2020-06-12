"""
Take a pivot element, and move lesser to left, and higher to the right. Repeat the same for sub-array until it reach
single element.
"""

# [5,4,1,7,2,9,6,8]
#
# [4,1,2][5][7,9,6,8]
# [4,1,2]                 [5]             [7,9,6,8]
# [1,2][4][]
# [1,2]                   [4]
# [][1][2]                [1]              [2]
#
# Take right loop through _right   [1,2,4,5]
# [7,9,6,8]
# [6][7][9,8]
# [9,8]
# [8][9][]


class Sorter:
    def __init__(self, array: list):
        self.array = array
        self._right = list()
        self._intermittent = list()
        self.final = list()
        self.decider(self.array)

    def partition(self, array):

        pivot = array[0]
        right = []
        left = []

        for j in array[1:]:
            if j > pivot:
                right.append(j)
            elif j == pivot or j < pivot:
                left.append(j)

        return pivot, left, right

    def sort_(self, pivot, left, right):

        if not left and len(right)==1:
            self.final.append(pivot)
            self.final+=right
            self.final+=self._intermittent
            self._intermittent.clear()

            if self._right:
                right = self._right.pop()
                self.decider(right)

        elif len(left)==1:
            self.final+=left
            self.final.append(pivot)

            if right:
                self.decider(right)
            elif self._right:
                right = self._right.pop()
                self.decider(right)

        else:
            self._intermittent.insert(0, pivot)
            if right:
                self._right.append(right)
            self.decider(left)


    def decider(self, array):
        if array:
            pivot, left, right = self.partition(array)
            self.sort_(pivot, left, right)

    def __repr__(self):
        return str(self.final)



s = Sorter([5,4,1,7,2,9,6,8])
print(s)