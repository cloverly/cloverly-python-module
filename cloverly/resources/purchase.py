"""
    Author: Zain Lakhani
    Date: 08/06/2021

    Title: Cloverly Purchase Offset Model
    Description: Relates to /purchases endpoint. For creating
    and paying for purchases
"""


from ..base import CloverlyResource


class Purchase(CloverlyResource):
    """Relates to /purchases endpoint. For creating
    and paying for purchases
    """
    resource_url = 'purchases'

    @classmethod
    def Estimate(cls, **kwargs: iter) -> object:
        """The endpoint extension for creating purchases from an estimated

        For creating estimate based purchases

        Args:
            kwargs (iter): Any custom parameters to post to the given endpoint
                - estimate_slug (str): The estimate to create the purchase based off of

        """
        return cls.extend_endpoint("", **kwargs)
