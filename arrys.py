import csv
from termcolor import colored
class PersistentResults():
    epsilon = [.001,.005, .01, .03, .05, .07, .1]
    # No Defense
    mnist_fgsm = []
    mnist_fgsm_box = []
    cifar_fgsm = []
    cifar_fgsm_box = []
    fashion_fgsm = []
    fashion_fgsm_box = []

    # Query Strength
    fashion_graph = []
    mnist_graph = []
    cifar_graph = []

    #### fasion ###
    # fgsm vs adv-training
    fgsm_acc = []
    fgsm_acc_box = []

    training_vs_fgsm = []
    training_vs_fgsm_box = []
    # fgsm vs adv-trainingR
    trainingR_vs_fgsm = []
    trainingR_vs_fgsm_box = []

    #fgsm2 vs adv-training
    training_vs_fgsm2 = []
    training_vs_fgsm2_box = []

    ### mnist ###
    mnist_fgsm_acc = []
    mnist_training_vs_fgsm = []
    mnist_fgsm_acc_box = []
    mnist_training_vs_fgsm_box = []

    ### cifar ###
    cifar_fgsm_acc = []
    cifar_training_vs_fgsm = []
    cifar_fgsm_acc_box = []
    cifar_training_vs_fgsm_box = []

    arrys = {'mnist_fgsm': mnist_fgsm,
        'mnist_fgsm_box': mnist_fgsm_box,
        'cifar_fgsm': cifar_fgsm,
        'cifar_fgsm_box':cifar_fgsm_box,
        'fashion_fgsm': fashion_fgsm,
        'fashion_fgsm_box': fashion_fgsm_box,
        'fgsm_acc': fgsm_acc,
        'fgsm_acc_box': fgsm_acc_box,
        'training_vs_fgsm': training_vs_fgsm,
        'training_vs_fgsm_box': training_vs_fgsm_box,
        'trainingR_vs_fgsm': trainingR_vs_fgsm,
        'trainingR_vs_fgsm_box': trainingR_vs_fgsm_box,
        'training_vs_fgsm2': training_vs_fgsm2,
        'training_vs_fgsm2_box': training_vs_fgsm2_box
    }

    arrys2d = {'fashion_graph': fashion_graph,
        'mnist_graph': mnist_graph,
        'cifar_graphs': cifar_graph
    }

    def __init(self):
        pass
        # # No Defense1
        # mnist_fgsm = []
        # mnist_fgsm_box = []
        # cifar_fgsm = []
        # cifar_fgsm_box = []
        # fashion_fgsm = []
        # fashion_fgsm_box = []
        #
        # # Query Strength
        # fashion_graph = []
        # mnist_graph = []
        # cifar_graph = []
        #
        # #### fasion ###
        # # fgsm vs adv-training
        # fgsm_acc = []
        # fgsm_acc_box = []
        #
        # training_vs_fgsm = []
        # training_vs_fgsm_box = []
        # # fgsm vs adv-trainingR
        # trainingR_vs_fgsm = []
        # trainingR_vs_fgsm_box = []
        #
        # #fgsm2 vs adv-training
        # training_vs_fgsm2 = []
        # training_vs_fgsm2_box = []
        #
        # ### mnist ###
        # mnist_fgsm_acc = []
        # mnist_training_vs_fgsm = []
        # mnist_fgsm_acc_box = []
        # mnist_training_vs_fgsm_box = []
        #
        # ### cifar ###
        # cifar_fgsm_acc = []
        # cifar_training_vs_fgsm = []
        # cifar_fgsm_acc_box = []
        # cifar_training_vs_fgsm_box = []
        #
        # self.arrys = {'mnist_fgsm': mnist_fgsm,
        #     'mnist_fgsm_box': mnist_fgsm_box,
        #     'cifar_fgsm': cifar_fgsm,
        #     'cifar_fgsm_box':cifar_fgsm,
        #     'fashion_fgsm': fashion_fgsm,
        #     'fashion_fgsm_box': fashion_fgsm_box,
        #     'fgsm_acc': fgsm_acc,
        #     'fgsm_acc_box': fgsm_acc_box,
        #     'training_vs_fgsm': training_vs_fgsm,
        #     'training_vs_fgsm_box': training_vs_fgsm_box,
        #     'trainingR_vs_fgsm': training_vs_fgsm_box,
        #     'training_vs_fgsm2': training_vs_fgsm2,
        #     'training_vs_fgsm2_box': training_vs_fgsm2_box
        # }
        #
        # self.arrys2d = {'fashion_graph': fashion_graph,
        #     'mnist_graph': mnist_graph,
        #     'cifar_graphs': cifar_graph
        # }


    def write_all(self, typein=True):
        with open('results', 'w+') as csvfile:
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
                    for j, eps in zip(self.arrys2d[key], self.epsilon):
                        row_name = key+"_"+str(eps)
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
            with open('results', 'r') as filein:
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
                                print(f'{key} populated')

        if typein == 2 or typein == True:
            with open('results', 'r') as filein:
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
                            loop_on = True
                            num = int(elems[0])
        self.update_arrs()

    def show_arrys(self, v=2):
        corr = 0
        empty = 0
        incorr = 0
        for key in self.arrys:
            print(f'{key}:', end=' ')
            if len(self.arrys[key]) == len(self.epsilon):
                corr +=1
                if v == 2:
                    print(colored('Correct', 'green'))
            elif len(self.arrys[key]) == 0:
                empty +=1
                if v == 2:
                    print(colored('Empty', 'blue'))
            else:
                incorr+=1
                if v == 2:
                    print(colored('Incorrect amount','red'))

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
            elif correct:
                corr+=1
                if v == 2:
                    print(colored('Correct', 'green'))
            elif not unempty:
                empty+=1
                if v == 2:
                    print(colored('Empty', 'blue'))
            else:
                incorr+=1
                if v == 2:
                    print(colored('Incorrect amount','red'))

        if v == 2:
            print()
        print(f'Correct: {corr}')
        print(f'Empty: {empty}')
        print(f'Incorrect amount: {incorr}')

    def replace(self,key):
        new_li = [key] + [str(i) for i in arry[key]]
        with open('results', 'r') as input_file, open('new_file', 'w') as output_file:
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

    def update_arrs(self):
        self.arrys = {'mnist_fgsm': self.mnist_fgsm,
        'mnist_fgsm_box': self.mnist_fgsm_box,
        'cifar_fgsm': self.cifar_fgsm,
        'cifar_fgsm_box': self.cifar_fgsm_box,
        'fashion_fgsm': self.fashion_fgsm,
        'fashion_fgsm_box': self.fashion_fgsm_box,
        'fgsm_acc': self.fgsm_acc,
        'fgsm_acc_box': self.fgsm_acc_box,
        'training_vs_fgsm': self.training_vs_fgsm,
        'training_vs_fgsm_box': self.training_vs_fgsm_box,
        'trainingR_vs_fgsm': self.trainingR_vs_fgsm,
        'trainingR_vs_fgsm_box': self.trainingR_vs_fgsm_box,
        'training_vs_fgsm2': self.training_vs_fgsm2,
        'training_vs_fgsm2_box': self.training_vs_fgsm2_box
        }
        self.arrys2d = {'fashion_graph': self.fashion_graph,
        'mnist_graph': self.mnist_graph,
        'cifar_graphs': self.cifar_graph
        }

    def diff(self, typein=True):
        # No Defense
        mnist_fgsm = []
        mnist_fgsm_box = []
        cifar_fgsm = []
        cifar_fgsm_box = []
        fashion_fgsm = []
        fashion_fgsm_box = []

        # Query Strength
        fashion_graph = []
        mnist_graph = []
        cifar_graph = []

        #### fasion ###
        # fgsm vs adv-training
        fgsm_acc = []
        fgsm_acc_box = []

        training_vs_fgsm = []
        training_vs_fgsm_box = []
        # fgsm vs adv-trainingR
        trainingR_vs_fgsm = []
        trainingR_vs_fgsm_box = []

        #fgsm2 vs adv-training
        training_vs_fgsm2 = []
        training_vs_fgsm2_box = []

        ### mnist ###
        mnist_fgsm_acc = []
        mnist_training_vs_fgsm = []
        mnist_fgsm_acc_box = []
        mnist_training_vs_fgsm_box = []

        ### cifar ###
        cifar_fgsm_acc = []
        cifar_training_vs_fgsm = []
        cifar_fgsm_acc_box = []
        cifar_training_vs_fgsm_box = []

        diff_arrys = {'mnist_fgsm': mnist_fgsm,
            'mnist_fgsm_box': mnist_fgsm_box,
            'cifar_fgsm': cifar_fgsm,
            'cifar_fgsm_box':cifar_fgsm_box,
            'fashion_fgsm': fashion_fgsm,
            'fashion_fgsm_box': fashion_fgsm_box,
            'fgsm_acc': fgsm_acc,
            'fgsm_acc_box': fgsm_acc_box,
            'training_vs_fgsm': training_vs_fgsm,
            'training_vs_fgsm_box': training_vs_fgsm_box,
            'trainingR_vs_fgsm': trainingR_vs_fgsm,
            'trainingR_vs_fgsm_box': trainingR_vs_fgsm_box,
            'training_vs_fgsm2': training_vs_fgsm2,
            'training_vs_fgsm2_box': training_vs_fgsm2_box
        }

        diff_arrys2d = {'fashion_graph': fashion_graph,
            'mnist_graph': mnist_graph,
            'cifar_graphs': cifar_graph
        }

        if typein == 1 or typein == True:
            with open('results', 'r') as filein:
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
            with open('results', 'r') as filein:
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
                            num = int(elems[0])
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
        with open('results', 'r') as filein:
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
                    print(f'{key} populated')
                    found = True
        if not found:
            print(colored('Err:', 'red'),end=' ')
            print(f'{key} not found)
