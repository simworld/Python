# Created by Simone Susino - D18124815

# Income predictor
#
# Using a dataset ( the "Adult Data Set") from the UCI Machine-Learning Repository we can predict based
# on a number of factors whether o not someone's income will be greater than $50,000.

# Process overview
#
#     Create training set from data
#     Create classifier using training dataset to determine separator values for each attribute
#     Create test dataset
#     Use classifier to classify data in test set while maintaining accuracy score
#
# Data is available from http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data.

import string, httplib2, numpy

adult_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

dict_above = {'AGE': [], 'WORKCLASS': [], 'EDUCATION_NUMBER': [], 'MARITAL_STATUS': [], 'OCCUPATION': [],
              'RELATIONSHIP': [], 'RACE': [], 'SEX': [], 'CAPITAL_GAIN': [], 'CAPITAL_LOSS': [], 'HOURS_PER_WEEK': [],
              'OUTCOME_FOR_THIS_RECORD': []}

dict_below = {'AGE': [], 'WORKCLASS': [], 'EDUCATION_NUMBER': [], 'MARITAL_STATUS': [], 'OCCUPATION': [],
              'RELATIONSHIP': [], 'RACE': [], 'SEX': [], 'CAPITAL_GAIN': [], 'CAPITAL_LOSS': [], 'HOURS_PER_WEEK': [],
              'OUTCOME_FOR_THIS_RECORD': []}

above50k = []

below50k = []

final_data = []

def get_data():
    '''
    Get the data form the HTTP link
    :return:
    '''
    try:
        h = httplib2.Http(".cache")
        header, data = h.request(adult_data, "GET")
        data = data.decode().split("\n")
        return data
    except httplib2.HttpLib2Error as e:
        print(e)
        quit()


def process_data(data):
    '''
    Process the data to remove spaces and the commas
    :param data:
    :return: training data and test data
    '''
    for i in range(len(data)):
        new_data = []
        datasplit = data[i].split(',')  # remove the comma from the file data set

        for x in range(len(datasplit)):
            datastrip = datasplit[x].strip()  # remove the space from the file data set
            if datastrip.isnumeric():  # check if there is a digit in the file data set
                datastrip = int(datastrip)  # if a digit has been found, declare the value as int
                new_data.append(datastrip)  # append the value to the new data list
            else:
                new_data.append(datastrip)
        final_data.append(new_data)

    try:
        to_delete = [2, 3, 13]  # delete the rows 2, 3 and 13 not needed for the study
        for i in final_data:
            for x in sorted(to_delete, reverse=True):
                del i[x]
    except Exception:
        pass
    # Two for loop to remove the last 2 blank lines in the file
    for line in final_data:
        if len(line) < 11:
            final_data.remove(line)
            for line in final_data:
                if len(line) < 11:
                    final_data.remove(line)

    len_data = int(len(data) * 0.7)

    training_data = final_data[:len_data]

    test_data = final_data[len_data:]

    return training_data, test_data  # return two list, the training data and the test data


def creat_dict(training_data):
    '''
    Get the training data, split the data in two different list and create two dict for below and above 50K
    :param training_data:
    :return:
    '''

    # split the training data in two list <=50K and >50K
    for i in training_data:

        if i[-1] == '<=50K':

            below50k.append(i)

        else:

            above50k.append(i)

    # Fill the two dict below and above 50K with the values of the training data
    for x in range(len(below50k)):
        dict_below['AGE'].append(below50k[x][0])
        dict_below['WORKCLASS'].append(below50k[x][1])
        dict_below['EDUCATION_NUMBER'].append(below50k[x][2])
        dict_below['MARITAL_STATUS'].append(below50k[x][3])
        dict_below['OCCUPATION'].append(below50k[x][4])
        dict_below['RELATIONSHIP'].append(below50k[x][5])
        dict_below['RACE'].append(below50k[x][6])
        dict_below['SEX'].append(below50k[x][7])
        dict_below['CAPITAL_GAIN'].append(below50k[x][8])
        dict_below['CAPITAL_LOSS'].append(below50k[x][9])
        dict_below['HOURS_PER_WEEK'].append(below50k[x][10])
        dict_below['OUTCOME_FOR_THIS_RECORD'].append(below50k[x][11])

    for x in range(len(above50k)):
        dict_above['AGE'].append(above50k[x][0])
        dict_above['WORKCLASS'].append(above50k[x][1])
        dict_above['EDUCATION_NUMBER'].append(above50k[x][2])
        dict_above['MARITAL_STATUS'].append(above50k[x][3])
        dict_above['OCCUPATION'].append(above50k[x][4])
        dict_above['RELATIONSHIP'].append(above50k[x][5])
        dict_above['RACE'].append(above50k[x][6])
        dict_above['SEX'].append(above50k[x][7])
        dict_above['CAPITAL_GAIN'].append(above50k[x][8])
        dict_above['CAPITAL_LOSS'].append(above50k[x][9])
        dict_above['HOURS_PER_WEEK'].append(above50k[x][10])
        dict_above['OUTCOME_FOR_THIS_RECORD'].append(above50k[x][11])


def classifier(discrete_attributes):
    '''
    Calculate the average for each key
    :param discrete_attributes:
    :return: weight
    '''

    counts = {}
    weight = {}

    # For loop to calculate the average for each key.
    # If the value is a number, it will calculate the average with numpy
    # and the value will be added to the weight dictionary at the current key
    for x, y in discrete_attributes.items():
        if x == 'AGE':
            age = numpy.average(y)
            weight[x] = age
            continue
        elif x == 'EDUCATION_NUMBER':
            edunum = int(numpy.average(y))
            weight[x] = edunum
            continue
        elif x == 'CAPITAL_GAIN':
            capgain = round(numpy.average(y), 4)
            weight[x] = capgain
            continue
        elif x == 'CAPITAL_LOSS':
            caploss = round(numpy.average(y), 4)
            weight[x] = caploss
            continue
        elif x == 'HOURS_PER_WEEK':
            hrsweek = round(numpy.average(y), 4)
            weight[x] = hrsweek
            continue
        # If the value is a string, the for loop will count how many time the word occurs
        for word in y:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        # Loop for the dict counts to calculate the average for each value in the corresponding attribute
        for key, value in counts.items():
            if key == '<=50K':  # Break the for for the last attribute <=50K
                break
            else:
                weight[key] = round(value / len(y), 4)
    return weight


def avg(attributes1, attributes2):
    '''
    Calculate the average of the averages
    :param attributes1:
    :param attributes2:
    :return: dict avg
    '''
    # Function to calculate the average of the averages for the dict below and above 50K
    dict_avg = {}
    for key, value in attributes1.items():
        average = 0
        for key1, value1 in attributes2.items():
            if key == key1:
                average = (value + value1) / 2
                dict_avg[key] = average
    return dict_avg


def test(average_data, data_test):
    '''
    Compare the value of each attribute in the data test with the average data
    and it will return below prediction and the accuracy of the correct values
    :param average_data:
    :param data_test:
    :return:
    '''
    # The test function will take the average data, the test data
    over_50k = 0
    below_50k = 0
    temp_above = 0
    temp_below = 0
    str_data_test = []
    final_data_test = []
    acc_below = 0
    acc_over = 0
    wrong = 0

    # The for below will be convert all the values in data_test into below string,
    # so then we can use the .isnumeric method to check if the value is numeric or not
    for line in data_test:
        for value in line:
            value = str(value)
            str_data_test.append(value)
        final_data_test.append(str_data_test)
        str_data_test = []

    # Loop in the final_data_test for each line and then for the index of each line check if the value is numeric or not
    # it will compare the value of the data_test with the value in the average data and after it will add <=50K or >50K
    # in the variable temp_result_list
    for line in final_data_test:
        temp_result_list = [''] * 11

        for index in range(len(line)):
            value = line[index]
            if value.isnumeric() and index == 0:
                temp_value = int(value) >= average_data['AGE']
                if temp_value == True:
                    temp_result_list[index] = '>50K'
                else:
                    temp_result_list[index] = '<=50K'

            elif value.isnumeric() and index == 2:
                temp_value = int(value) >= average_data['EDUCATION_NUMBER']
                if temp_value == True:
                    temp_result_list[index] = '>50K'
                else:
                    temp_result_list[index] = '<=50K'

            elif value.isnumeric() and index == 8:
                temp_value = int(value) >= average_data['CAPITAL_GAIN']
                if temp_value == True:
                    temp_result_list[index] = '>50K'
                else:
                    temp_result_list[index] = '<=50K'

            elif value.isnumeric() and index == 9:
                temp_value = int(value) >= average_data['CAPITAL_LOSS']
                if temp_value == True:
                    temp_result_list[index] = '>50K'
                else:
                    temp_result_list[index] = '<=50K'

            elif value.isnumeric() and index == 10:
                temp_value = int(value) >= average_data['HOURS_PER_WEEK']
                if temp_value == True:
                    temp_result_list[index] = '>50K'
                else:
                    temp_result_list[index] = '<=50K'
            # when it will get below string it will check the corresponding value of the string
            elif value in average_data:
                temp_value = average_data[value]  # save in temp_value the value of the key in average data
                if temp_value >= weights_below[value]:  # if the value is >= of the value in the dict below
                    temp_result_list[index] = '>50K'
                else:
                    temp_result_list[index] = '<=50K'
            # Count how many record over and below 50K exist in the test data
            elif value == '>50K':
                over_50k += 1
            elif value == '<=50K':
                below_50k += 1
        below = []
        above = []
        # Count and compare to predict if the record is below or above 50K
        if temp_result_list.count('<=50K') >= temp_result_list.count('>50K'):
            temp_below += 1
            below = '<=50K'
            # When the value is below, if the last value in the line is <=50K
            # increment acc_below to check the accuracy
            if line[-1] == below:
                acc_below += 1
            # Can uncomment to print all the not correct lines
            else:
                wrong += 1
                # print(line, '--> NOT CORRECT','-','PREDICTION WAS:', below)
        else:
            above = '>50K'
            temp_above += 1
            # When the value is above, if the last value in the line is >50K
            # increment acc_over to check the accuracy
            if line[-1] == above:
                acc_over += 1
            # Can uncomment to print all the not correct lines
            else:
                wrong += 1
                # print(line, '--> NOT CORRECT','-','PREDICTION WAS:', above)

    accuracy = round((acc_over * 100) / over_50k, 2)
    accuracy2 = round((acc_below * 100) / below_50k, 2)

    print()
    print('----------------------------------')
    print('Test data over 50k: ', over_50k)
    print('Test data below 50k: ', below_50k, '\n')
    print('Prediction above 50k:', acc_over)
    print('Prediction below 50k:', acc_below, '\n')

    print('Not correct:', wrong)
    print('Accuracy >50K: ', accuracy, '%')
    print('Accuracy <=50K: ', accuracy2, '%', '\n')
    print('Total accuracy: ', (accuracy + accuracy2) / 2, '%')
    print('----------------------------------', '\n')


get_adultdata = get_data()
training, data = process_data(get_adultdata)
creat_dict(training)
weights_below = classifier(dict_below)
weights_above = classifier(dict_above)
tot_avg = avg(weights_below, weights_above)
test(tot_avg, data)

# Uncomment to print all the dict with the below average, above average, and the total average
# print()
# print('Average training data <=50K: ', weights_below)
# print('Average of the training data >50K: ', weights_above)
# print('Average of averages: ', tot_avg)
