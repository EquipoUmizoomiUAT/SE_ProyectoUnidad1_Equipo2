def SaveCSV(data, filename):
    with open(file=filename, mode='w') as file:
        for instance in data:
            file.write(",".join(map(str, instance)) + '\n')