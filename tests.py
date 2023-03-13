from extract import get_input
from transform import remove_duplicate_UID,remove_empty_lines,Capitalize_Array,Validate_Q3

def test_input_is_list():
    # Arrange
    filename = "results.csv"
    expected_output = list

    # Act
    output = get_input(filename)

    # Assert
    assert type(output) == expected_output

def test_output_is_list():
    # Arrange
    filename = "clean_results.csv"
    expected_output = list

    # Act
    output = get_input(filename)

    # Assert
    assert type(output) == expected_output

def test_input_columns_correct():
    # Arrange
    filename = "results.csv"
    expected_columns = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    # Act
    output = get_input(filename)
    actual_columns = output[0]

    # Assert
    assert actual_columns == expected_columns

def test_output_columns_correct():
    # Arrange
    filename = "clean_results.csv"
    expected_columns = ["user_id","first_name","last_name","answer_1","answer_2","answer_3"]
    # Act
    output = get_input(filename)
    actual_columns = output[0]

    # Assert
    assert actual_columns == expected_columns

def test_output_columns_Caps():
    # Arrange
    filename = "results.csv"
    expected_lowerletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Act
    output = Capitalize_Array(remove_empty_lines(get_input(filename)))
    actual_string_position0 = []
    for i in range(1,len(output)): 
        string_loop_firstname = str(output[i][1])[0]
        string_loop_lastname = str(output[i][2])[0]
        #string_loop = string_loop[0]
        #print(string_loop)
        actual_string_position0.append(string_loop_firstname)
        actual_string_position0.append(string_loop_lastname)

    # Assert
    assert any(item not in actual_string_position0 for item in expected_lowerletters) 

def test_duplicates():
    # Arrange
    expected = [['1', 'A'], ['2', 'D'], ['3', 'G']]

    #act
    output = remove_duplicate_UID([["1","A"],["1","B"],["1","C"],["2","D"],["2","E"],["2","F"],["3","G"]])

    #assert
    assert expected == output

def test_empty_lines():
    # Arrange
    expected = [['1', 'A'], ['2', 'D'], ['3', 'G']]

    #act
    output = remove_empty_lines([["1","A"],["",""],["",""],["2","D"],["",""],["",""],["3","G"]])

    #assert
    assert expected == output

def test_Q3_Validation():
    # Arrange
    expected = [["user_id","first_name","last_name","answer_1","answer_2","answer_3"]]

    #act
    output = Validate_Q3([["user_id","first_name","last_name","answer_1","answer_2","answer_3"],\
                          ['1', 'Alan','Duncan', '2', '1', '-6'],\
                          ['1', 'Alan','Duncan', '2', '1', '50'],\
                          ['1', 'Alan','Duncan', '2', '1', '0'],\
                          ['1', 'Alan','Duncan', '2', '1', '11']\
                            ])

    #assert
    assert expected == output


# print(test_input_columns_correct())
# print(test_output_columns_correct())
# print(test_input_is_list())
# print(test_output_is_list())
# print(test_output_columns_Caps())
# print(test_duplicates())
# # print(test_Q3_Validation())
# print(test_empty_lines())

# NOTE when making the output tests I realized that my code capitalized the column headers for firstname and last name... changed code to for i in range(1,len(array)): from for i in range(len(array)): Howeve this is testing data as opposed to testing the function itself!
# Note when Testing whether or not the columns were in capitals - very convoluted - basically tsting whther or not capitalise is doing its job so not really sure of the value of incorporating this into my programming? Basically feels like a lot of work to re-writ ethe function in another way which is pretty pointless?
# note but for ensuring that duplicates weer removed - made the test much simpler and ensured that just the core function of the function was being tested
# note when writing the test for checking for integers I got teh following error message ValueError: invalid literal for int() with base 10: '10.1'. This led down a new path which was testing to ensure that the inputs are integers and not decimals. i didnt write this test but it shows how useful TDD can be as it can ensure a higher quality of coding

# print(Validate_Q3([["user_id","first_name","last_name","answer_1","answer_2","answer_3"],['1', 'Alan','Duncan', '2', '1', '11']]))
