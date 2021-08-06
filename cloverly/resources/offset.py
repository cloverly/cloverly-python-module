"""
    Author: Zain Lakhani
    Date: 08/06/2021

    Title: Cloverly Resource Offset Model
    Description: Relates to /offsets endpoint. For getting
    information about offsets
"""

from ..base import CloverlyResource


class Offset(CloverlyResource):
    """Relates to /purchases endpoint. For creating
    and paying for purchases
    """
    resource_url = 'offsets'
