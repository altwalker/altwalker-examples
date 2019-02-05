from pypom import Page


class Base(Page):
    def __init__(self, selenium, base_url=None, timeout=10, **url_kwargs):
        return super().__init__(selenium, base_url=base_url, timeout=timeout, **url_kwargs)


class HomePage(Base):
    pass