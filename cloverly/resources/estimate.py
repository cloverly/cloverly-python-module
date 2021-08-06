"""
    Author: Zain Lakhani
    Date: 08/06/2021

    Title: Cloverly Resource Estimate Model
    Description: Relates to /estimates endpoint. For creating and
    viewing estimates
"""

from ..base import CloverlyResource


class Estimate(CloverlyResource):
    """Relates to /estimates endpoint. For creating and
    viewing estimates
    """
    resource_url = 'estimates'
