import glob
import subprocess

inputFiles = sorted(glob.glob('tests/input*.txt'))
outputFiles = sorted(glob.glob('tests/output*.txt'))

if len(inputFiles) == 0:
    print("== Ajouter des jeux de tests dans /tests == ")
    exit()

if len(inputFiles) != len(outputFiles):
    print("== Nombre de fichiers input/output différent ==")
    exit()

success = 0
resMessage = ""

for filename in inputFiles:
    n = int(filename[len("tests/input"):-4])
    output = subprocess.check_output(
        f"python solution.py < {filename}", shell=True)
    userResponse = str.rstrip(output.decode("utf-8"))
    fileResponse = open(f"tests/output{n}.txt")
    responseExcepted = fileResponse.read()

    if len(userResponse) == 0:
        print(f"==== Test {n} ❌ ====")
        print("ERREUR: Aucune sortie reçue.")
        resMessage += " ❌"
    elif userResponse != responseExcepted:
        print(f"==== Test {n} ❌ ====")
        print("--- Result ---")
        print(userResponse)
        print("--- Excepted ---")
        print(responseExcepted)
        print("----")
        resMessage += " ❌ "
    else:
        success += 1
        print(f"==== Test {n} ✅ ====")
        resMessage += " ✅ "

percentage = round(success/len(inputFiles), 2)*100
print(f"\n ==== TOTAL {resMessage} -- {percentage}% ====")
