import matplotlib.pyplot as plt

class FEM(): 
    """docstring for FEM""" 
    def __init__(self, l, m): 
        self.m = m; 
        self.dx = l/(m-1) 
        self.dt = self.dx**2/2 
        self.dt = int(100000000*self.dt)/100000000 
        self.tal = self.dt/self.dx**2 
        self.bound = [] 
        self.result = [] 
        self.it = 0
 
    def set_boundary(self):
        try:
            self.bound.append(int(input('Digite a condição T(0,t): ')))
            self.bound.append(int(input('Digite a condição T(1,t): ')))
            self.bound.append(int(input('Digite a condição T(x,0): ')))
        except (KeyboardInterrupt, SystemExit, ValueError) as e:
            if type(e) == ValueError:
                print('Erro: Digite um número')
                get_info()            
            elif type(e) == KeyboardInterrupt or type(e) == SystemExit:
                print('')
                exit(1)
        print('bound ' +     str(self.bound))

    def set_it(self):
        try:
            self.it = int(input('Digite o numero de iterações: '))
        except (KeyboardInterrupt, SystemExit, ValueError) as e:
            if type(e) == ValueError:
                print('Erro: Digite um número')
                self.set_it()
            elif type(e) == KeyboardInterrupt or type(e) == SystemExit:
                print('')
                exit(1)

    def calculate(self): 
        for i in range(0, self.it): 
            line = [self.bound[0]]             
            if not self.result: 
                self.result.append([]) 
                self.result[0].append(self.bound[0]) 
                for i in range(1, self.m-1): 
                    self.result[0].append(self.bound[2]) 
                self.result[0].append(self.bound[1]) 
            else: 
                for x in range(1, self.m-1): 
                    t = self.tal*self.result[i-1][x-1] + (1-2*self.tal)*self.result[i-1][x] + self.tal*self.result[i-1][x+1] 
                    line.append(t) 
                line.append(self.bound[1]) 
                self.result.append(line) 
 
        return self.result 
    
    def get_times(self):
        dt = self.dx**2/2
        times = []
        for i in range(self.it):
            times.append(i*dt)
        return self.it

    def get_xs(self):
        x = []
        for i in range(self.m):
            x.append(i*self.dx)
        return x

def get_info():
    try:
        l = int(input('Digite o comprimento da placa: '))
        m = int(input('Digite o numero de pontos desejados: '))
    except (KeyboardInterrupt, SystemExit, ValueError) as e:
        if type(e) == ValueError:
            print('Erro: Digite um número')
            get_info()            
        elif type(e) == KeyboardInterrupt or type(e) == SystemExit:
            print('')
            exit(1)
    return (l, m)

if __name__ == '__main__': 
    info = get_info()
    a = FEM(info[0], info[1]) 
    a.set_boundary()
    a.set_it()
    it = a.get_times()
    images = a.calculate()
    domain = a.get_xs()
    print(images[0])
    for i in range(it-1):
        plt.plot(domain, images[i])
        plt.ylim(0,1.5)
        plt.xlabel('Comprimento')
        plt.ylabel('Temperatura')
        name = 'lala' + str(i) + '.jpg'
        plt.savefig(name)
        plt.clf()
        plt.cla()
        plt.close()


