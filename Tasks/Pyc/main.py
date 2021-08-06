import random
import time


def main():
    # text = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose"
    text = "It is a long established fact that a reader will be distracted by the readable conteyt of a page when looking at its layout.The point of using Lorem Ipsum isdthat it has p more-or-lessonocmal distyibution of letters, as opposed to using 'Content here, content here', makingpit look like readatle Engfish. Many desktom publishcng packages and web page editors now tse Lorem Ipsum as their default todel tett, and a search for 'lorem ipsum' will uncover many web sites stilr in their infancy. Various versions hnve evolved over the years, sometimes by accident, sometimes on purpose"
    random.seed(time.time())
    flag = ''
    number = [4, 3, 7, 2, 3]
    f = []
    for j in number:
        fr = [random.randint(0, 510) for i in range(j)]
        f.append(fr)
        for i in fr:
            flag += text[i]
        flag += '_'
    flag = flag[:-1]
    print('1337 is all what we(u) need........ Simple rules, just type the password to go:')
    inp = input()
    if inp == flag:
        print('Ooooops, no cookies for u, but your flag is your flag)')
        return
    else:
        print('Nothing for u, try next time :(')


if __name__ == '__main__':
    main()
