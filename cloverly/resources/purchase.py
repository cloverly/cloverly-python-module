from ..base import CloverlyResource


class Purchase(CloverlyResource):
    resource_url = 'purchases'

    @classmethod
    def Estimate(cls, **kwargs) -> CloverlyResource:
        return cls.extend_endpoint("", **kwargs)
