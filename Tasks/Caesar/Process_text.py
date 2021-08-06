def process():
    # https://cryptii.com/pipes/caesar-cipher

    # https://www.ushistory.org/civ/6b.asp
    # http://www.perseus.tufts.edu/hopper/text;jsessionid=205D83A2883AC263B608CF457C5DEDAB?doc=Perseus%3Atext%3A1999.03.0078%3Atext%3DCaes.
    flag = 'mipt_ctf_caesar_one_love'
    flag_caesar = 'tpwa_jam_jhlzhy_vul_svcl'
    flag_reverse = 'lcvs_luv_yhzlhj_maj_awpt'
    flag_spelling = 'Lima Charlie Victor Sierra _ Lima Uniform Victor _ Yankee Hotel Zulu Lima Hotel Juliett _ Mike Alfa Juliett _ Alfa Whiskey Papa Tango'
    flag_base32 = 'JRUW2YJAINUGC4TMNFSSAVTJMN2G64RAKNUWK4TSMEQF6ICMNFWWCICVNZUWM33SNUQFM2LDORXXEIC7EBMWC3TLMVSSASDPORSWYIC2OVWHKICMNFWWCICIN52GK3BAJJ2WY2LFOR2CAXZAJVUWWZJAIFWGMYJAJJ2WY2LFOR2CAXZAIFWGMYJAK5UGS43LMV4SAUDBOBQSAVDBNZTW6==='
    flag_morze = '0111 010 001 011 00111 1011 0111 01 00 10 001 110 1010 00001 1 11 10 0010 000 000 01 0001 1 0111 11 10 00111 110 10000 00001 010 01 101 10 001 011 101 00001 1 000 11 0 1101 0010 10000 00 1010 11 10 0010 011 011 1010 00 1010 0001 10 1100 001 011 11 00011 00011 000 10 001 1101 0010 11 00111 0100 100 111 010 1001 1001 0 00 1010 11000 0 1000 11 011 1010 00011 1 0100 11 0001 000 000 01 000 100 0110 111 010 000 011 1011 00 1010 00111 111 0001 011 0000 101 00 1010 11 10 0010 011 011 1010 00 1010 00 10 00000 00111 110 101 00011 1000 01 0111 0111 00111 011 1011 00111 0100 0010 111 010 00111 1010 01 1001 1100 01 0111 0001 001 011 011 1100 0111 01 00 0010 011 110 11 1011 0111 01 0111 0111 00111 011 1011 00111 0100 0010 111 010 00111 1010 01 1001 1100 01 00 0010 011 110 11 1011 0111 01 101 00000 001 110 000 00001 00011 0100 11 0001 00001 000 01 001 100 1000 111 1000 1101 000 01 0001 100 1000 10 1100 1 011 10000 10001 10001 10001'
    file = open('caesar_text.txt', 'r')
    # 0 - space
    # 1 - tab
    # space - \n
    data = file.readline()
    file.close()
    data = data.split()
    output_file = open('caesar_encoded.txt', 'w+')
    ids = 0
    for k in flag_morze:
        if k == '0':
            output_file.write(data[ids] + ' ')
            ids += 1
        elif k == '1':
            output_file.write(data[ids] + '\t')
            ids += 1
        elif k == ' ':
            output_file.write('\n')

    output_file.close()


def check():
    # file = open('caesar_encoded.txt', 'r')
    file = open('ch.txt', 'r')
    ig = ''
    data = file.readlines()
    for i in data:
        for j in i:
            if j == ' ':
                ig += '0'
            elif j == '\t':
                ig += '1'
        ig += ' '
    ig = ig[:-1]
    ig = ig[1:-1]
    print(ig)
    flag_morze = '0111 010 001 011 00111 1011 0111 01 00 10 001 110 1010 00001 1 11 10 0010 000 000 01 0001 1 0111 11 10 00111 110 10000 00001 010 01 101 10 001 011 101 00001 1 000 11 0 1101 0010 10000 00 1010 11 10 0010 011 011 1010 00 1010 0001 10 1100 001 011 11 00011 00011 000 10 001 1101 0010 11 00111 0100 100 111 010 1001 1001 0 00 1010 11000 0 1000 11 011 1010 00011 1 0100 11 0001 000 000 01 000 100 0110 111 010 000 011 1011 00 1010 00111 111 0001 011 0000 101 00 1010 11 10 0010 011 011 1010 00 1010 00 10 00000 00111 110 101 00011 1000 01 0111 0111 00111 011 1011 00111 0100 0010 111 010 00111 1010 01 1001 1100 01 0111 0001 001 011 011 1100 0111 01 00 0010 011 110 11 1011 0111 01 0111 0111 00111 011 1011 00111 0100 0010 111 010 00111 1010 01 1001 1100 01 00 0010 011 110 11 1011 0111 01 101 00000 001 110 000 00001 00011 0100 11 0001 00001 000 01 001 100 1000 111 1000 1101 000 01 0001 100 1000 10 1100 1 011 10000 10001 10001 10001'
    print(ig == flag_morze)


if __name__ == '__main__':
    # process()
    check()
