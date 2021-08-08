"""
    Author: Zain Lakhani
    Date: 08/05/2021

    Title: Cloverly Resource Base Model
    Description: The base cloverly resource model that interacts
    with the Cloverly API
"""

import requests
from .exceptions import CloverlyError


class CloverlyResource:
    """The Base Cloverly Resource Object
    Handles creating, deleting and updating resources via the cloverly API,
    as well as activating an API session

    Attributes:
        base_url (str): The base url of the cloverly API (ex. https://api.cloverly.com)

        resource_url (str): The specifc resource endpoint to interact with (ex. estimates, purchases, etc...)

        _version (str): The API version to use (ex. 2019-03-beta)

        _headers (dict): The headers to be sent with every request. Includes the API key
    """
    base_url = 'https://api.cloverly.com'
    resource_url = ''
    _version = ''
    _headers = {}

    def __init__(self, **kwargs: iter):
        # Initializes all passed in attributes as instance attributes
        for attr in kwargs:
            self.__setattr__(attr, kwargs[attr])

    @classmethod
    def request(cls, url: str, method: str, data: dict) -> requests.request:
        """The request function, a wrapper around the request module

        Used for making requests to the Cloverly API with JSON bodies

        Args:
            url (int): The url to request
            method (str): The method to request (ex. POST)
            data (dict): The data (in the form of json) to send in the body

        Returns:
            requests.request: If the status code is 201, 200 or 300

        Raises:
            CloverlyError: If any errors are included in the payload response

        """
        r = requests.request(method, url, json=data, headers=cls._headers)
        json = r.json()
        if type(json) is dict and json.get('error'):
            raise CloverlyError(json['error'])
        return r

    @classmethod
    def list(cls, **kwargs: iter) -> object:
        """The list function, lists all known instances of the given resource url

        Used for listing resources (ex. a list of available offsets, a list of estimates created)

        Args:
            **kwargs (iter): Custom filters to pass in to the search endpoint

        Returns:
            list: A list of object resources for the given resource_url.
            For example a list of Estimate objects

        """
        r = cls.request(f"{cls.base_url}/{cls._version}/{cls.resource_url}", 'GET', kwargs)
        results = r.json()
        if type(results) == list:
            object_list = []
            for result in results:
                new = cls(**result)
                object_list.append(new)
            return object_list

    @classmethod
    def activate_session(cls, api_key: str, version: str):
        """The session activation function, activates and authenticates a cloverly api session

        Used for initializing the Cloverly module and conencting to the API

        Args:
            api_key (str): API Key for use with the Cloverly API
            version (str): Cloverly API version to interact with

        """
        cls._version = version
        cls._headers["Authorization"] = f"Bearer {api_key}"
        cls._headers["Content-type"] = "application/json"

    @classmethod
    def clear_session(cls):
        """The clear session function, clears the current cloverly session

        Used for ending or clearing a session with the Cloverly API
        """
        cls._version = ''
        cls._headers = {}

    @classmethod
    def extend_endpoint(cls, endpoint: str, **kwargs: iter) -> object:
        """The endpoint extension function, extends the current resource url

        Used for accessing sub endpoints for a resource url (ex. estimates/shipping, estimates/currency)

        Args:
            endpoint (str): The endpoint to extend
            kwargs (iter): Any custom parameters to post to the given endpoint

        """
        e = cls(**kwargs)
        e.save(endpoint)
        return e

    @classmethod
    def Fixed(cls, **kwargs: iter) -> object:
        """The endpoint extension for /currency

        For creating fixed price resources

        Args:
            kwargs (iter): Any custom parameters to post to the given endpoint

        """
        return cls.extend_endpoint("/currency", **kwargs)

    @classmethod
    def Carbon(cls, **kwargs: iter) -> object:
        """The endpoint extension for /carbon

        For creating carbon emission resources

        Args:
            kwargs (iter): Any custom parameters to post to the given endpoint

        """
        return cls.extend_endpoint("/carbon", **kwargs)

    @classmethod
    def Shipping(cls, **kwargs: iter) -> object:
        """The endpoint extension for /shipping

        For creating shipping distance and weight resources

        Args:
            kwargs (iter): Any custom parameters to post to the given endpoint

        """
        return cls.extend_endpoint("/shipping", **kwargs)

    @classmethod
    def Ground(cls, **kwargs: iter) -> object:
        """The endpoint extension for /vehicle

        For creating ground related resources (driving a car, shipping via truck, etc...)

        Args:
            kwargs (iter): Any custom parameters to post to the given endpoint

        """
        return cls.extend_endpoint("/vehicle", **kwargs)

    @classmethod
    def Flight(cls, **kwargs: iter) -> object:
        """The endpoint extension for /flights

        For creating flight related resources

        Args:
            kwargs (iter): Any custom parameters to post to the given endpoint

        """
        return cls.extend_endpoint("/flights", **kwargs)

    @classmethod
    def Electricity(cls, **kwargs: iter) -> object:
        """The endpoint extension for /electricity

        For creating electricity related resources

        Args:
            kwargs (iter): Any custom parameters to post to the given endpoint

        """
        return cls.extend_endpoint("/electricity", **kwargs)

    def delete(self) -> None:
        """The deletion function, for deleting resources

        Deletes the resource that's calling the function

        """
        url = f"{self.base_url}/{self._version}/{self.resource_url}/{self.__getattribute__('slug')}"
        self.request(url, "DELETE", {})

    def save(self, slug: str = None) -> None:
        """The save function, creates and saves a resource

        Args:
            slug (str): An extension slug to add to the resource url

        """
        url = f"{self.base_url}/{self._version}/{self.resource_url}"

        if slug is not None:
            url += slug

        r = self.request(url, "POST", self.__dict__)
        result = r.json()

        for attr in result:
            self.__setattr__(attr, result[attr])
