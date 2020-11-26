import glob
import io
from contextlib import redirect_stdout
import code

inputFilenamesList = sorted(glob.glob('tests/input*.txt'))
outputFilenamesList = sorted(glob.glob('tests/output*.txt'))

# check we have some tests
if(len(inputFilenamesList) == 0):
    exit()

if(len(inputFilenamesList) != len(outputFilenamesList)):
    print('Nombre de fichiers Input/Output différent')
    exit()

currentTest = 1

for filename in inputFilenamesList:
    print('=======[ Test {} ]======='.format(currentTest))
    lines = []
    with open(filename, "r") as file: 
        for line in file:
            lines.append(line.rstrip('\n'))
    # response from output.txt
    fileResponse = open(outputFilenamesList[currentTest-1])
    responseExcepted = fileResponse.read()

    # get user response from stdout
    f = io.StringIO()
    with redirect_stdout(f):
        code.response(lines)
    userResponse = str.rstrip((f.getvalue()))
    f.close()

    if len(userResponse) == 0:
        print('❌ ERREUR: Aucune sortie reçue.')
    elif (userResponse != responseExcepted):
        print('Résultat obtenue : \n {}'.format(userResponse))
        print('❌ ERREUR : {} != {}'.format(userResponse, responseExcepted))
        print(''.format(currentTest))
    else:
        print('✅ Test {} réussi'.format(currentTest))

    # post test task
    currentTest += 1
