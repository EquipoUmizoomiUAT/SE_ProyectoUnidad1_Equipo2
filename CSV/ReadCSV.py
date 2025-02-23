def ReturnDataSet(mode):
    # Check which problem is being treated
    if mode == 1 or mode == 3:
        filename = 'AnalogValues.csv'
    elif mode == 2:
        filename = 'DigitalValues.csv'
    else:
        # In case of an invalid problem
        exit("CSV/ReadCSV.py: Modo Invalido, Mode={0}".format(mode))

    # Get the dataset
    with open(file=filename, mode='r') as file:
        dataset = []
        for line in file:
            line = line.strip().split(',')
            dataset.append(line)

    return dataset
