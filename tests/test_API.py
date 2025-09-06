import allure
import requests
import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject

@allure.feature('Create object')
@allure.story('POST')
def test_create_object():
    with allure.step('Create new object'):
        new_object_endpoint = CreateObject()
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    new_object_endpoint.new_object(payload=payload)
    with allure.step('check response'):
        new_object_endpoint.check_response_200()
        new_object_endpoint.check_name(payload['name'])

@allure.feature('GET_object')
@allure.story('GET')
def test_get_object(obj_id):
    with allure.step('Send GET request'):
        get_obj_endpoint = GetObject()
        get_obj_endpoint.get_by_id(obj_id)
    with allure.step('Validate response'):
        get_obj_endpoint.check_response_200()
        get_obj_endpoint.check_response_id(obj_id)



    payload = {
    "name": "Apple MacBook Pro 10",
    "data": {
      "year": 2025,
      "price": 1849.99,
      "CPU model": "Intel Core i19",
      "Hard disk size": "2 TB"
   }
}
@allure.feature('update_object')
@allure.story('PUT')
def test_update_object(obj_id):
    with allure.step('Send PUT request'):
        update_obj_endpoint = UpdateObject()
        payload = {
            "name": "Apple MacBook Pro 10",
            "data": {
            "year": 2025,
            "price": 1849.99,
            "CPU model": "Intel Core i19",
            "Hard disk size": "2 TB"
        }
    }

    update_obj_endpoint.update_by_id(obj_id, payload)
    with allure.step('Validate response'):
        update_obj_endpoint.check_response_200()
        update_obj_endpoint.check_response_name(payload['name'])


@allure.feature('delete_object')
@allure.story('DELETE')
def test_delete_object(obj_id):
    with allure.step('send delete request'):
        delete_obj_endpoint = DeleteObject()
        delete_obj_endpoint.delete_by_id(obj_id)
    with allure.step('Validate response'):
        delete_obj_endpoint.check_response_200()
    with allure.step('Check that object was deleted'):
        get_obj_endpoint = GetObject()
        get_obj_endpoint.get_by_id(obj_id)
        get_obj_endpoint.check_response_404()




