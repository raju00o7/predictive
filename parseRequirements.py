# Purpose: Parse the requirements.txt file and change all the versions like pandas==1.0.0 to pandas.
with open('requirements.txt') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].split('==')[0] + '\n'
with open('requirements.txt', 'w') as f:
    f.writelines(lines)