class Calcurator:
    numlist = 0
    def __init__(self, numlist):
        self.numlist = numlist
    def sum(self):
        sum = 0
        for i in self.numlist:
            sum += i
        return sum
    def avg(self):
        avg = 0
        for i in self.numlist:
            avg += i
        return avg/len(self.numlist)
if __name__ == '__main__':
    cal1 = Calcurator([1,2,3,4,5])
    print(cal1.sum())
    print(cal1.avg())
    cal2 = Calcurator([6,7,8,9,10])
    print(cal2.sum())
    print(cal2.avg())