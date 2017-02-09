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
 
    def setboundary(self):
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

    def setit(self):
        try:
            self.it = int(input('Digite o numero de iterações: '))
        except (KeyboardInterrupt, SystemExit, ValueError) as e:
            if type(e) == ValueError:
                print('Erro: Digite um número')
                get_info()            
            elif type(e) == KeyboardInterrupt or type(e) == SystemExit:
                print('')
                exit(1)
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
    return get_info()

if __name__ == '__main__': 
    info = get_info()
    a = FEM(info[0], info[1]) 
    a.setboundary()
    a.setit()

    b = a.calculate() 
    print(b[-1]) 
    for i in b: 
        pass 