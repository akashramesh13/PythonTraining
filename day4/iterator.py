# simple iterator program to print odd numbers
class OddNumbers:
    def __iter__(self):
        self.a = -1
        return self

    def __next__(self):
        if self.a < 19:
            self.a += 2
            return self.a
        else:
            raise StopIteration


odd_numbers = OddNumbers()
itr = iter(odd_numbers)
for x in itr:
    print(x)