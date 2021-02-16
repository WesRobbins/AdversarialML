import csv
from termcolor import colored
class PersistentResults:
    epsilon = [.001,.005, .01, .03, .05, .07, .1]
    QS = [100, 500, 1000, 3000, 5000, 15000, 30000, None]
    adv_train_iterations = [1,2,3,5,7,10,13]


    arrys = {}

    arrys2d = {}

    def __init__(self, arrys_in, arrys2d_in):
        for key in arrys_in:
            self.arrys[key] = []
        for key in arrys2d_in:
            self.arrys2d[key] = []


    def write_all(self, typein=True):
        with open('results.csv', 'w+') as csvfile:
            if typein == 1 or typwin==True:
                writer = csv.writer(csvfile)
                for key in self.arrys:
                    line = self.arrys[key].copy()
                    try:
                        if len(line) == len(self.epsilon):
                            line.insert(0, key)
                            writer.writerow([str(r) for r in line])
                            print(colored(f'{key} was written', 'green'))
                        else:
                            print(colored('ERR:', 'red'),end=' ')
                            print(f'{key} is wrong size')
                    except:
                        print(f'ERR: no {key}')
            if typein == 2 or typein == True:
                for key in self.arrys2d:
                    len_dict = str(len(self.arrys2d[key]))
                    null_li = ['null']*(len(self.epsilon)-2)
                    if len(self.arrys2d[key]):
                        writer.writerow([key, len_dict]+null_li)
                    else:
                        print(colored('ERR:', 'red'),end=' ')
                        print(f'{key} is wrong size')
                    if key[-2:] == 'qs':
                        iter = self.QS
                        tag = 'QS'
                    elif key[-2:] == 'it':
                        iter = self.adv_train_iterations
                        tag = 'iter'
                    for j, stren in zip(self.arrys2d[key], iter):
                        row_name = key+"_"+tag+str(stren)
                        try:
                            if len(j) == len(self.epsilon):
                                writer.writerow([row_name] + [str(r) for r in j])
                                print(f'{row_name} was written')
                            else:
                                print(f'{row_name} is wrong size')
                        except:
                            print(f'no {row_name}')

    def read_results(self, typein=True):
        if typein == 1 or typein == True:
            with open('results.csv', 'r') as filein:
                csv_reader = csv.reader(filein, delimiter=',')
                for row in csv_reader:
                    name = row.pop(0)
                    try:
                        elems = [float(i) for i in row]
                    except:
                        pass
                    for key in self.arrys:
                        if key == name:
                            if len(self.arrys[key]) == 0:
                                self.arrys[key].extend(elems)
                                print(f'{key} loaded')

        if typein == 2 or typein == True:
            with open('results.csv', 'r') as filein:
                csv_reader = csv.reader(filein, delimiter=',')
                for key in self.arrys2d:
                    loop_on = False
                    count = 0
                    num = 0
                    full_list = []
                    for row in csv_reader:
                        name = row.pop(0)
                        try:
                            elems = [float(i) for i in row]
                        except:
                            pass
                        if loop_on:
                            count+=1
                            self.arrys2d[key].append(elems)
                            if count >= num:
                                loop_on = False
                                break
                        if name == key:
                            self.arrys2d[key].clear()
                            loop_on = True
                            num = int(row[0])

    def show_arrys(self, v=2):
        corr = 0
        empty = 0
        incorr = 0
        for key in self.arrys:
            if v >= 2:
                print(f'{key}:', end=' ')
            if len(self.arrys[key]) == len(self.epsilon):
                corr +=1
                if v == 2:
                    print(colored('Correct', 'green'))
                elif v >= 3:
                    print(colored('Correct', 'green'), end=' ')
            elif len(self.arrys[key]) == 0:
                empty +=1
                if v == 2:
                    print(colored('Empty', 'blue'))
                elif v >= 3:
                    print(colored('Empty', 'blue'), end=' ')
            else:
                incorr+=1
                if v == 2:
                    print(colored('Incorrect amount','red'))
                elif v >= 3:
                    print(colored('Incorrect amount', 'red'), end=' ')
            if v >= 3:
                print(f'- Len: {len(self.arrys[key])}')


        for key in self.arrys2d:
            print(f'{key}: ', end='')
            correct = True
            unempty = False
            for i in self.arrys2d[key]:
                if len(i) != 0:
                    unempty = True
                elif len(i) != len(self.epsilon):
                    correct = False

            if len(self.arrys2d[key]) == 0:
                empty+=1
                if v == 2:
                    print(colored('Empty', 'blue'))
                elif v >= 3:
                    print(colored('Empty', 'blue'), end=' ')
            elif correct:
                corr+=1
                if v == 2:
                    print(colored('Correct', 'green'))
                elif v >= 3:
                    print(colored('Correct', 'green'), end=' ')
            elif not unempty:
                empty+=1
                if v == 2:
                    print(colored('Empty', 'blue'))
                elif v >= 3:
                    print(colored('Empty', 'blue'), end=' ')
            else:
                incorr+=1
                if v == 2:
                    print(colored('Incorrect amount','red'))
                elif v >= 3:
                    print(colored('Incorrect amount', 'red'), end=' ')
            if v >= 3:
                print(f'- Len: {len(self.arrys[key])} x {len(self.arrys[key])[0]}')

        if v == 2:
            print()
        print(f'Correct: {corr}')
        print(f'Empty: {empty}')
        print(f'Incorrect amount: {incorr}')

    def replace(self,key):
        new_li = [key] + [str(i) for i in arry[key]]
        with open('results.csv', 'r') as input_file, open('new_file', 'w') as output_file:
            for line in input_file:
                if line[0] == key:
                    output_file.write(new_li)
                else:
                    output_file.write(line)

        os.rename('new_file.csv', 'results.csv')

    def add(self,key, typin):
        if typein == 1:
            new_li = [key] + [str(r) for r in self.arrys[key]]
            with open('new_file', 'a') as output_file:
                writer = csv.writer(csvfile)
                writer.writerow(new_li)


    def diff(self, typein=True):

        diff_arrys = {}
        diff_arrys2d = {}
        for key in self.arrys:
            diff_arrys[key] = []
        for key in self.arrys2d:
            diff_arrys2d[key] = []


        if typein == 1 or typein == True:
            with open('results.csv', 'r') as filein:
                csv_reader = csv.reader(filein, delimiter=',')
                for row in csv_reader:
                    name = row.pop(0)
                    try:
                        elems = [float(i) for i in row]
                    except:
                        pass
                    for key in diff_arrys:
                        if key == name:
                            if len(diff_arrys[key]) == 0:
                                diff_arrys[key].extend(elems)

        if typein == 2 or typein == True:
            with open('results.csv', 'r') as filein:
                csv_reader = csv.reader(filein, delimiter=',')
                for key in diff_arrys2d:
                    loop_on = False
                    count = 0
                    num = 0
                    for row in csv_reader:
                        name = row.pop(0)
                        try:
                            elems = [float(i) for i in row]
                        except:
                            pass
                        if loop_on:
                            count+=1
                            diff_arrys2d[key].append(elems)
                            if count >= num:
                                loop_on = False
                                break
                        if name == key:
                            loop_on = True
                            num = int(row[0])
        unequal = []
        for key in self.arrys:
            fil = 'Empty'
            mem = 'Empty'
            if self.arrys[key] != diff_arrys[key]:
                if len(diff_arrys[key]) != 0:
                    fil = 'Filled'
                if len(self.arrys[key]) != 0:
                    mem = 'Filled'
                unequal.append((key, fil, mem))
        for key in self.arrys2d:
            fil = 'Empty'
            mem = 'Empty'
            if self.arrys2d[key] != diff_arrys2d[key]:
                if len(diff_arrys2d[key]) != 0:
                    fil = 'Filled'
                if len(self.arrys2d[key]) != 0:
                    mem = 'Filled'
                unequal.append((key, fil, mem))


        print('The folling keys would be updated in case of a write:')
        print('------------------------------------------------------')
        for i in unequal:
            print(f'Key: {i[0]} - In memory: ', end="")
            if i[2] == 'Empty':
              col = 'blue'
            else:
              col = 'green'
            print(colored(i[2], col), end=' ')
            print('In File: ', end = '')
            if i[1] == 'Empty':
              col = 'blue'
            else:
              col = 'green'
            print(colored(i[1], col))

def show_keys(self):
    print('1d Keys')
    for key in self.arrys:
        print(key)
    for key in self.arrys2d:
        print(key)

def check_key(self, key_in):
    for key in self.arrys:
        if key_in == key:
            print(f'{key} exists in arrys')
            return
    for key in self.arrys2d:
        if key_in == key:
            print(f'{key} exists in arrys2d')
            return
    print('key not found')

def read_specific(self, li):
    for key in li:
        found = False
        with open('results.csv', 'r') as filein:
            csv_reader = csv.reader(filein, delimiter=',')
            for row in csv_reader:
                name = row.pop(0)
                try:
                    elems = [float(i) for i in row]
                except:
                    pass
                if key == name:
                    self.arrys[key].clear()
                    self.arrys[key].extend(elems)
                    print(f'{key} loaded')
                    found = True
        if not found:
            print(colored('Err:', 'red'),end=' ')
            print(f'{key} not found')

def clear_mem(self):
    for key in self.arrys:
        self.arrys[key].clear()
    for key in self.arrys2d:
        self.arrys2d[key].clear()
