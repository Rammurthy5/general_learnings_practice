"""
Sort by counting number occurrences of each element, and then print them.
"""


class Sorter:
    def __init__(self, array):
        self.array = array
        self.sort_(self.split_())

    def split_(self):
        try:

            _temp = list()
            for i in self.array:
                L = len(_temp)
                if L<i+1:
                    _temp+=[0]*(i-L+1)

                _temp[i]+=1

            return _temp
        except Exception as e:
            import pdb; pdb.set_trace()

    def sort_(self, counterDict):
        final=list()

        for i,j in enumerate(counterDict):
            if j>0:
                final+=[i]*j
        self.array=final


s = Sorter([3,4,1,1,1,5,7])
print(s.array)
