#Lawrence Byun
#ID: 94998893
def validWord(word):
    #Check if word is in Hawaiian characters
    letters = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'p', 'P', 'k', 'K', 'h', 'H', 'l', 'L', 'm', 'M', 'n', 'N', 'w', 'W', '\'', ' ']
    count = 0
    for i in word:
        if i not in letters:
            count += 1
    if count == 0:
        return True
    else:
        return False

def pronunciate(phrase):
    pron = ""
    pro = {'a': 'ah', 'e': 'eh', 'i': 'ee', 'o': 'oh', 'u': 'oo', 'ai': 'eye', 'ae': 'eye', 'ao': 'ow', 'au': 'ow', 'ei': 'ay', 'eu': 'eh-oo', 'iu': 'ew', 'oi': 'oy', 'ou': 'ow', 'ui': 'ooey'}
    phrase = phrase.replace('iw', 'iv')
    phrase = phrase.replace('ew', 'ev')
    i = 0

    while i < len(phrase) - 1:
        letter = phrase[i]
        letter = letter.lower()
        if letter == 'a':
            letter2 = phrase[i + 1]
            letter2 = letter2.lower()
            if letter2 == 'o' or letter2 == 'u':
                pron += pro['ao'] + '-'
                i += 1
            elif letter2 == 'e' or letter2 == 'i':
                pron += pro['ae'] + '-'
                i += 1
            else:
                pron += pro['a'] + '-'
        elif letter == 'e':
            letter2 = phrase[i + 1]
            letter2 = letter2.lower()
            if letter2 == 'i':
                pron += pro['ei'] + '-'
                i += 1
            elif letter2 == 'u':
                pron += pro['eu'] + '-'
                i += 1
            else:
                pron += pro['e'] + '-'
        elif letter == 'i':
            letter2 = phrase[i + 1]
            letter2 = letter2.lower()
            if letter2 == 'u':
                pron += pro['iu'] + '-'
                i += 1
            else:
                pron += pro['i'] + '-'
        elif letter == 'o':
            letter2 = phrase[i + 1]
            letter2 = letter2.lower()
            if letter2 == 'u':
                pron += pro['ou'] + '-'
                i += 1
            elif letter2 == 'i':
                pron += pro['oi'] + '-'
                i += 1
            else:
                pron += pro['o'] + '-'
        elif letter == 'u':
            letter2 = phrase[i + 1]
            letter2 = letter2.lower()
            if letter2 == 'i':
                pron += pro['ui'] + '-'
                i += 1
            else:
                pron += pro['u'] + '-'
        elif letter == ' ' and pron[len(pron) - 1] == '-':
            pron = pron[0:len(pron) - 1] + ' '
        elif letter == '\'' and pron[len(pron) - 1] == '-':
            pron = pron[0:len(pron) - 1] + "'"
        else:
            pron += letter
        i += 1
    if i < len(phrase):
        letter = phrase[len(phrase) - 1]
        letter = letter.lower()
        if letter == 'a' or letter == 'e' or letter == 'o':
            pron += letter + 'h'
        elif letter == 'i':
            pron += 'ee'
        elif letter == 'u':
            pron += 'oo'
        else:
            pron += letter
    if pron[len(pron) - 1] == '-':
        pron = pron[0: len(pron) - 1]
    words = pron.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    
    return (' '.join(words))
            
        
        

def createGuide(inputFile, outFile):
  try:
    file_obj = open(inputFile, 'r')
  except:
    print('The input file does not exist')
    return
  outfile = open(outFile, 'w')

  line = file_obj.readline()
  lst = line.split()
  for i in range(len(lst) - 1):
    if ',' in lst[i]:
      if validWord(lst[i][:-1]) == True:
        lst[i] = pronunciate(lst[i][:-1]) + ','
    elif '.' in lst[i]:
      if validWord(lst[i][:-1]) == True:
        lst[i] = pronunciate(lst[i][:-1]) + '.'
    else:
      if validWord(lst[i]) == True:
        lst[i] = pronunciate(lst[i])
      else:
        lst[i] = "\"" + lst[i] + "\""
    outfile.write(lst[i])
    outfile.write(" ")
  if ',' in lst[-1]:
    if validWord(lst[-1][:-1]) == True:
      lst[-1] = pronunciate(lst[-1][:-1]) + ','
  elif '.' in lst[-1]:
    if validWord(lst[-1][:-1]) == True:
      lst[-1] = pronunciate(lst[-1][:-1]) + '.'
  else:
    if validWord(lst[-1]) == True:
      lst[-1] = pronunciate(lst[-1])
    else:
      lst[-1] = "\"" + lst[-1] + "\""
  outfile.write(lst[-1])



  for line in file_obj:
    outfile.write("\n")
    lst = line.split()
    for i in range(len(lst) - 1):
      if ',' in lst[i]:
        if validWord(lst[i][:-1]) == True:
          lst[i] = pronunciate(lst[i][:-1]) + ','
      elif '.' in lst[i]:
        if validWord(lst[i][:-1]) == True:
          lst[i] = pronunciate(lst[i][:-1]) + '.'
      else:
        if validWord(lst[i]) == True:
          lst[i] = pronunciate(lst[i])
        else:
          lst[i] = "\"" + lst[i] + "\""
      outfile.write(lst[i])
      outfile.write(" ")
    if ',' in lst[-1]:
      if validWord(lst[-1][:-1]) == True:
        lst[-1] = pronunciate(lst[-1][:-1]) + ','
    elif '.' in lst[-1]:
      if validWord(lst[-1][:-1]) == True:
        lst[-1] = pronunciate(lst[-1][:-1]) + '.'
    else:
      if validWord(lst[-1]) == True:
        lst[-1] = pronunciate(lst[-1])
      else:
        lst[-1] = "\"" + lst[-1] + "\""
    outfile.write(lst[-1])
  file_obj.close()
  outfile.close()
