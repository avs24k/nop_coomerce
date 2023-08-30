import pytest



@pytest.mark.usefixtures("setup")
class Base_class():
    pass

    def select_genders(self, locator, text):
        Genders = locator
        for G in Genders:
            if G.text == text:
                G.click()