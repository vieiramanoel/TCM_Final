class FEM():
    """docstring for FEM"""
    def __init__(self, l, m):
        self.m = m;
        self.dx = l/(m-1)
        self.dt = self.dx**2/2
        self.dt = int(100000000*self.dt)/100000000
        self.tal = self.dt/self.dx**2
        self.bound = [1, 0, 0]
        self.result = []

    def calculate(self):

        for i in range(0, 90):
            line = [self.bound[0]]            
            if not self.result:
                self.result.append([])
                self.result[0].append(self.bound[0])
                for i in range(1, self.m-1):
                    self.result[0].append(self.bound[2])
                self.result[0].append(self.bound[1])
            else:
                for x in range(1, self.m-1):
                    t = self.tal*self.bound[0] + (1-2*self.tal)*self.result[i-1][x] + self.tal*self.result[i-1][x+1]
                    line.append(t)
                line.append(self.bound[1])
                self.result.append(line)

        return self.result


if __name__ == '__main__':
    a = FEM(1, 20)
    b = a.calculate()
    print(b[-1])
    for i in b:
        pass
        