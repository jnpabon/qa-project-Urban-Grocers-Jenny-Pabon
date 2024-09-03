import sender_stand_request
import data


# Get the token and put it into the headers and return it
def get_authorization():
    # copy the headers
    current_headers = data.headers.copy()
    # add the token to the headers
    current_headers['Authorization'] = ("Bearer " +
                                        sender_stand_request.post_new_user(data.user_body).json()['authToken'])
    return current_headers


# get the kit body to replace the value of name param and return it
def get_kit_body(name):
    # copy the kit body and create a new body
    current_body = data.kit_body.copy()
    # replace the value of name param
    current_body['name'] = name
    return current_body


# assertion section
def positive_assert(name):
    # get the body and replace de name param
    kit_body = get_kit_body(name)
    # get the header with the authorization (token)
    headers = get_authorization()
    # Creating the client kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers)
    # Verify if the status code is 201
    assert kit_response.status_code == 201
    # Verify if the request name is the same as response name
    assert kit_response.json()['name'] == kit_body['name']


def negative_assert_code_400(name):
    # get the body and replace de name param
    kit_body = get_kit_body(name)
    # get the header with the authorization (token)
    headers = get_authorization()
    # Creating the client kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers)
    # Verify if the status code is 400
    assert kit_response.status_code == 400
    # Verify if the response code is 400
    assert kit_response.json()['code'] == 400


def negative_assert_no_name(kit_body):
    # get the header with the authorization (token)
    headers = get_authorization()
    # Creating the client kit
    kit_response = sender_stand_request.post_new_client_kit(kit_body, headers)
    # Verify if the status code is 400
    assert kit_response.status_code == 400
    # Verify if the response code is 400
    assert kit_response.json()['code'] == 400


# test cases......

# Test case 1. Creating a new client kit
# the "name" param contain 1 character
def test_create_client_kit_1_letter_in_name_get_success_response():
    positive_assert(data.one_letter_name)


# Test case 2. Creating a new client kit
# the "name" param contain less than 511 characters
def test_create_client_kit_in_511_letter_in_name_get_success_response():
    positive_assert(data.in_511_letter)


# Test case 3. Creating a new client kit
# the "name" param is empty
def test_create_client_kit_empty_name_get_error_response():
    kit_body = get_kit_body(data.empty_name)
    negative_assert_no_name(kit_body)


# Test case 4. Creating a new client kit
# the "name" param contain more than 512 characters
def test_create_client_kit_more_than_512_letter_in_name_get_error_response():
    negative_assert_code_400(data.more_than_512_letter)


# Test case 5. Creating a new client kit
# the "name" param contain specials characters
def test_create_client_kit_specials_symbols_in_name_get_success_response():
    positive_assert(data.specials_symbols_in_name)


# Test case 6. Creating a new client kit
# the "name" param contain spaces
def test_create_client_kit_space_in_name_get_success_response():
    positive_assert(data.space_in_name)


# Test case 7. Creating a new client kit
# the "name" param contain numbers type string ("123")
def test_create_client_kit_string_numbers_in_name_get_success_response():
    positive_assert(data.string_numbers_in_name)


# Test case 8. Creating a new client kit
# the "name" param is not send
def test_create_client_kit_no_name_get_success_response():
    kit_body = data.kit_body.copy()
    kit_body.pop('name')
    negative_assert_no_name(kit_body)


# Test case 9. Creating a new client kit
# the "name" param contain specials characters
def test_create_client_kit_number_type_in_name_get_success_response():
    negative_assert_code_400(data.number_type_in_name)
