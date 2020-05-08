
userinput=input('\n[For morse->text press: 1 and for text->morse press: 2]\n\nselect mode: ')

list=[]
word=""
mcode=''
b=''
space=0
sentence=''

dic1 = {
    "A" : ".- ",
    "B" : "-... ",
    "C" : '-.-. ',
    "D" : '-.. ',
    "E" : '. ',
    "F" : '..-. ',
    "G" : '--. ',
    "H" : '.... ',
    "I" : '.. ',
    "J" : '.--- ',
    "K" : '-.- ',
    "L" : '.-.. ',
    "M" : '-- ',
    "N" : '-. ',
    "O" : '--- ',
    "P" : '.--. ',
    "Q" : '--.- ',
    "R" : ".-. ",
    "S" : "... ",
    "T" : "- ",
    "U" : "..- ",
    "V" : "...- ",
    "W" : ".-- ",
    "X" : "-..- ",
    "Y" : "-.-- ",
    "Z" : "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "...._ ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- ",
    " ": '  '
}
dic2={
    ".-" :"A",
    "-..." : "B",
    '-.-.' : "C",
    '-..' : "D",
    '.' : "E",
    '..-.' : "F",
    '--.' : "G",
    '....' : "H",
    '..' : "I",
    '.---' : "J",
    '-.-' : "K",
    '.-..' : "L",
    '--' : "M",
    '-.' : "N",
    '---' : "O",
    '.--.' : "P",
    '--.-' : "Q",
    ".-." : "R",
    "..." : "S",
    "-" : "T",
    "..-" : "U",
    "...-" : "V",
    ".--" : "W",
    "-..-" : "X",
    "-.--" : "Y",
    "--.." : "Z",
    ".----" : "1",
    "..---" : "2",
    "...--" : "3",
    "...._" : "4",
    "....." : "5",
    "-...." : "6",
    "--..." : "7",
    "---.." : "8",
    "----." : "9",
    "-----" : "0",
    ''      : " "
}


if userinput=='1':
    morse=input('\nafter finishing a letter give a space and after finishing a word give two space \n[ exanple abcd efgh= .- -... -.-. -..  . .-.. --. ....]\n\nEnter your morse code: ')
    for i in morse:
        if i!=" ":
            mcode=mcode+i
            space=0
            #print(mcode)
        elif i==" ":
            list.append(mcode)
            space=space+1
            mcode = ''

    list.append(mcode)
    print(list)
    for code in list:
        b=dic2[code]
        sentence=sentence+b
    print("Text>" +sentence)


elif userinput=='2':
    text = input('Enter your text: ')
    text=text.upper()
    for i in text:
        a=dic1[i]
        word=word+a
    print('morse code> '+word)







