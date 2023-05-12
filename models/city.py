#!/usr/bin/python3

"""
The module that creates City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    This class has 'state id' and 'name' public class attributes
    """

    state_id = ""
    name = ""
