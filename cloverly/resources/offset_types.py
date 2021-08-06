"""
    Author: Zain Lakhani
    Date: 08/06/2021

    Title: Cloverly Resource Offset Types Model
    Description: Relates to /offset-types endpoint. For getting
    information about available offset types
"""

from ..base import CloverlyResource


class OffsetTypes(CloverlyResource):
    """Relates to /purchases endpoint. For creating
    and paying for purchases
    """
    resource_url = 'offset-types'
