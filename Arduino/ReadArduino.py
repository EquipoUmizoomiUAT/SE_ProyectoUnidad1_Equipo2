import serial
from CSV import WriteCSV


def ReadArduino():
    # Open connection
    arduino = serial.Serial('com3', baudrate=9600, timeout=1)

    # Vector to store the data
    analogData = []
    digitalData = []
    totalReadings = 0

    # 10k readings to test with different population sizes
    while totalReadings <= 10000:
        try:
            if arduino.in_waiting > 0:
                # Read, decode and split the reading into a vector
                line = arduino.readline().decode('utf-8').strip().split(",")

                # Parse the vector to integers to create a digital version
                analogVector = [int(value) for value in line]

                # Create digital values vector with odd/even numbers
                digitalVector = [0 if value % 2 == 0 else 1 for value in analogVector]

                # Collect the data
                analogData.append(analogVector)
                digitalData.append(digitalVector)

                print(totalReadings)
                totalReadings += 1
        except:
            print("Bad Reading")

    # Close the serial connection
    arduino.close()

    # Save the data using the CSV writer module
    WriteCSV.SaveCSV(analogData, '../AnalogValues.csv')
    WriteCSV.SaveCSV(digitalData, '../DigitalValues.csv')


if __name__ == "__main__":
    ReadArduino()
