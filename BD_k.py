import pickle
import os

data = [[12.00, 13.15, 14.10, 16.20], [14.40, 16.10, 18.10, 18.40], [18.00, 18.10, 19.00, 20.20]]

temp_data = []
n = 0

if os.stat("file.txt").st_size == 0:
    with open('file.txt', 'wb') as f:
        pickle.dump(data, f)

temp = raw_input('Enter command\n')

while temp != 'quit':
    with open('file.txt', 'rb') as f:
        if temp == 'view':
            while 1:
                try:
                    out = pickle.load(f)
                    print(out)
                except (EOFError):
                    break

        if temp == 'sort':
            with open('file.txt', 'rb') as f:
                while 1:
                    try:
                        out = pickle.load(f)
                    except (EOFError):
                        break
                for i in range(len(out)):
                    for j in range(len(out[i])):
                        if out[i][j] == 'videoadapter':
                            print(out[i])
                            break

        if temp == 'add':
            with open('file.txt', 'rb') as f:
                a = []

                while 1:
                    try:
                        out = pickle.load(f)
                    except (EOFError):
                        break
                
                n = int(input('Number of elements\n'))
                for i in range(n):
                    a.append(input('New element\n'))
                out.append(a)
                with open('file.txt', 'w') as f:
                    pickle.dump(out, f)

        if temp == 'mod':
            with open('file.txt', 'a+') as f:
                n = input('Computer number\n')
                while 1:
                    try:
                        out = pickle.load(f)
                    except (EOFError):
                        break
                temp_data = (out[n])
                c = raw_input('Modification command\n')
                if c == 'add':
                    temp = input('New element\n')
                    temp_data.append(temp)
                    temp_data.sort()
                    out.append(temp_data)

                if c == 'del_element':
                    temp = input('Specify elemnt position\n')
                    temp_data.pop(temp)
                    out.pop(n)
                    out.append(temp_data)

                if c == 'del':
                    out.pop(n)

            with open('file.txt', 'w') as f:
                pickle.dump(out, f)

    temp = raw_input('Enter command\n')
