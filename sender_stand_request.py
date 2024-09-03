import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # insert complete URL
                         json=body,  # insert body request
                         headers=data.headers)  # insert headers request


def post_new_client_kit(kit_body, current_headers):
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_headers)

