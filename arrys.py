class PersistentResults():
	def __init(self):
		# No Defense
		self.mnist_fgsm = []
		self.mnist_fgsm_box = []
		self.cifar_fgsm = []
		self.cifar_fgsm_box = []
		self.fashion_fgsm = []
		self.fashion_fgsm_box = []

		# Query Strength
		self.fashion_graph = []
		self.mnist_graph = []
		self.cifar_graph = []

		#### fasion ###
		# fgsm vs adv-training
		self.fgsm_acc = []
		self.fgsm_acc_box = []

		self.training_vs_fgsm = []
		self.training_vs_fgsm_box = []
		# fgsm vs adv-trainingR
		self.trainingR_vs_fgsm = []
		self.trainingR_vs_fgsm_box = []

		#fgsm2 vs adv-training
		self.training_vs_fgsm2 = []
		self.training_vs_fgsm2_box = []

		### mnist ###
		self.mnist_fgsm_acc = []
		self.mnist_training_vs_fgsm = []
		self.mnist_fgsm_acc_box = []
		self.mnist_training_vs_fgsm_box = []

		### cifar ###
		self.cifar_fgsm_acc = []
		self.cifar_training_vs_fgsm = []
		self.cifar_fgsm_acc_box = []
		self.cifar_training_vs_fgsm_box = []

		self.arrys = {'mnist_fgsm': mnist_fgsm,
    		'mnist_fgsm_box': mnist_fgsm_box,
    		'cifar_fgsm': cifar_fgsm,
    		'cifar_fgsm_box': cifar_fgsm,
    		'fashion_fgsm': fashion_fgsm,
    		'fashion_fgsm_box': fashion_fgsm_box,
    		'fgsm_acc': fgsm_acc,
    		'fgsm_acc_box': fgsm_acc_box,
    		'training_vs_fgsm': training_vs_fgsm,
    		'training_vs_fgsm_box': training_vs_fgsm_box,
    		'trainingR_vs_fgsm': training_vs_fgsm_box,
    		'training_vs_fgsm2': training_vs_fgsm2,
    		'training_vs_fgsm2_box': training_vs_fgsm2_box
		}

		self.arrys2d = {'fashion_graph': fashion_graph,
    		'mnist_graph': mnist_graph,
    		'cifar_graphs': cifar_graph
		}

    def write_all(self, typein=True):
        with open('results', 'w+') as csvfile:
            if typein == 1 or typwin==True:
                writer = csv.writer(csvfile)
                for key in self.arrys:
                    line = self.arrys[key].copy()
                    try:
                        if len(line) == len(epsilon):
                            line.insert(0, key)
                            writer.writerow([str(r) for r in line])
                            print(f'{key} was written')
                        else:
                            print(f'ERR: {key} is wrong size')
                    except:
                        print(f'ERR: no {key}')
            if typein == 2 or typein == True:
                for key in self.arrys:
                    len_dict = str(len(self.arrys[key]))
                    writer.writerow([key, len_dict])
                    for j, eps in zip(self.arrys[key], epsilon):
                        row_name = key+"_"+str(eps)
                        try:
                            if len(j) == len(epsilon):
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
                    elems = [float(i) for i in row]
                    for key in arrys:
                        if key == name:
                            if len(arrys[key]) == 0:
                                arrys[key].extend(elems)
                                print(f'{key} populated')

        if typein == 2 or typein == True:
            with open('results', 'r') as filein:
                csv_reader = csv.reader(filein, delimiter=',')
                for key in arrys2d:
                    loop_on = False
                    count = 0
                    num = 0
                    full_list = []
                    for row in csv_reader:
                        name = row.pop(0)
                        elems = [float(i) for i in row]
                        if loop_on:
                            count+=1
                            arrys2d[key].append(elems)
                            if count >= num:
                                loop_on = False
                                break
                            if name == key:
                                loop_on = True
                                num = int(elems[0])

    def show_arrys(self, v=2):
        int corr = 0
        int empty = 0
        int incorr = 0
        for key in arrys:
            print(f'{key}:', end=' ')
            if len(arrys[key]) == len(epsilon):
                corr +=1
                if v == 2:
                    print('Correct')
            elif len(arrys[key]) == 0:
                empty +=1
                if v == 2:
                    print('Empty')
            else:
                incorr+=1
                if v == 2:
                    print('Incorrect amount')

        for key in arrys2d:
            print(f'{key}: ', end='')
            correct = True
            unempty = False
            for i in arrys2d[key]:
                if len(i) != 0:
                    unempty = True
                elif len(i) != len(epsilon):
                    correct = False
            if correct:
                corr+=1
                if v == 2:
                    print('Correct')
            elif not unempty:
                empty+=1
                if v == 2:
                    print('Empty')
            else:
                incorr+=1
                if v == 2:
                    print('Incorrect Count')
        print(f'Correct: {incorr}')
        print(f'Empty: {empty}')
        print(f'Incorrect amount: {incorr}')

    def replace(key):
        new_li = [key] + [str(i) for i in arry[key]]
        with open('results', 'r') as input_file, open('new_file', 'w') as output_file:
            for line in input_file:
                if line[0] == key:
                    output_file.write(new_li)
                else:
                    output_file.write(line)

        os.rename('new_file.csv', 'results.csv')

    def add(key, typin):
        if typein == 1:
            new_li = [key] + [str(r) for r in arrys[key]]
            with open('new_file', 'a') as output_file:
                writer = csv.writer(csvfile)
                writer.writerow(new_li)