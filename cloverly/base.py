import requests
from .exceptions import CloverlyError

class CloverlyResource:
    base_url = 'https://api.cloverly.com'
    resource_url = ''
    _version = ''
    _headers = {}

    def __init__(self, **kwargs: iter):
        for attr in kwargs:
            self.__setattr__(attr, kwargs[attr])

    @classmethod
    def request(cls, url: str, method: str, data: dict) -> requests.request:
        r = requests.request(method, url, json=data, headers=cls._headers)
        json = r.json()
        if json['error']:
            raise CloverlyError(json['error'])
        return r

    @classmethod
    def list(cls, **kwargs):
        r = cls.request(f"{cls.base_url}/{cls._version}/{cls.resource_url}", 'GET', kwargs)
        results = r.json()
        if type(results) == list:
            object_list = []
            for result in results:
                new = cls(**result)
                object_list.append(new)
            return object_list

    @classmethod
    def activate_session(cls, api_key, version):
        cls._version = version
        cls._headers["Authorization"] = f"Bearer {api_key}"
        cls._headers["Content-type"] = "application/json"

    @classmethod
    def extend_endpoint(cls, endpoint: str, **kwargs):
        e = cls(**kwargs)
        e.save(endpoint)
        return e

    @classmethod
    def Fixed(cls, **kwargs):
        return cls.extend_endpoint("/currency", **kwargs)

    @classmethod
    def Carbon(cls, **kwargs):
        return cls.extend_endpoint("/carbon", **kwargs)

    @classmethod
    def Shipping(cls, **kwargs):
        return cls.extend_endpoint("/shipping", **kwargs)

    @classmethod
    def Ground(cls, **kwargs):
        return cls.extend_endpoint("/vehicle", **kwargs)

    @classmethod
    def Flight(cls, **kwargs):
        return cls.extend_endpoint("/flights", **kwargs)

    @classmethod
    def Electricity(cls, **kwargs):
        return cls.extend_endpoint("/electricity", **kwargs)

    def delete(self):
        url = f"{self.base_url}/{self._version}/{self.resource_url}/{self.__getattribute__('slug')}"
        self.request(url, "DELETE", {})

    def save(self, slug: str = None):
        url = f"{self.base_url}/{self._version}/{self.resource_url}"

        if slug is not None:
            url += slug

        r = self.request(url, "POST", self.__dict__)
        result = r.json()

        for attr in result:
            self.__setattr__(attr, result[attr])
