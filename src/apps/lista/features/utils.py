# -*- coding: utf-8 -*-
from lettuce import world


def is_step_items_present(step):
    """
    Assert if all items inside the step hashes are present in the current page
    """
    for item in step.hashes:  # step.hashes eh uma lista de dicionarios
        assert world.browser.is_text_present(item['nome'])
    return True
