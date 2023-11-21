import requests

api_cep_url = "https://brasilapi.com.br/api/cep/v2"


def validate_cep(field):
    cep = "".join(field.replace("-", " ").split())
    if cep.isdigit() and len(cep) == 8:
        return cep
    raise Exception('CEP "{field}" Format Invalid'.format(field=field))


def findcep(cep):
    cep = validate_cep(cep)
    response = requests.get(api_cep_url + "/" + cep)
    if response.status_code == 404:
        return {"city": "", "state": "", "neighborhood": ""}
    return response.json()


if __name__ == "__main__":
    print(findcep("01234000"))
    print(findcep("11680000"))
