import zipfile
import random
import time

"""
If he had anything confidential to say, 
he wrote it in cipher, that is, by so changing 
the order of the letters of the alphabet, that 
not a word could be made out. mipt_ctf_zipper_just_zip
"""

data = """
49 66 20 68 65 20 68 61 64 20 61 6e 
79 74 68 69 6e 67 20 63 6f 6e 66 69 
64 65 6e 74 69 61 6c 20 74 6f 20 73 
61 79 2c 20 0a 68 65 20 77 72 6f 74 
65 20 69 74 20 69 6e 20 63 69 70 68 
65 72 2c 20 74 68 61 74 20 69 73 2c 
20 62 79 20 73 6f 20 63 68 61 6e 67 
69 6e 67 20 0a 74 68 65 20 6f 72 64 
65 72 20 6f 66 20 74 68 65 20 6c 65 
74 74 65 72 73 20 6f 66 20 74 68 65 
20 61 6c 70 68 61 62 65 74 2c 20 74 
68 61 74 20 0a 6e 6f 74 20 61 20 77 
6f 72 64 20 63 6f 75 6c 64 20 62 65 
20 6d 61 64 65 20 6f 75 74 2e 20 6d 
69 70 74 5f 63 74 66 5f 7a 69 70 70 
65 72 5f 6a 75 73 74 5f 7a 69 70
"""


def process():
    dt = data.replace(' ', '')
    dt = dt.split('\n')
    dt.remove('')
    dt.remove('')
    ultra = 'mipt_ctf_'
    names = list('combineitallpls')[::-1] + ['ultra_zipper_text.txt', ]
    prev_i = 'tests.py'
    alph = 'abcdefghijklmnopqrstuvwxyz'
    numb = '0123456789_'
    inf = alph + numb
    rnd_names = []
    for i in range(1000):
        rnd = [random.choice(inf) for _ in range(33)]
        rnd = ''.join(rnd)
        rnd_names.append(rnd)
        file = open(rnd, 'w')
        file.write('nononono not this')
        file.close()

    for j, i in enumerate(names):
        n = f"{j}{i}.zip"
        z = zipfile.ZipFile(n, 'w')
        z.write(prev_i)

        name = ultra + dt[j]
        print(len(name))
        file = open(name, 'w+')
        file.write('combineitallpls')
        file.close()
        z.write(name)
        for k in rnd_names:
            z.write(k)
        prev_i = n
        z.close()


if __name__ == '__main__':
    process()
