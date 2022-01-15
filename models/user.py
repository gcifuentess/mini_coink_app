#!/usr/bin/python3
"""Defines class User"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Representation of a user"""
    __tablename__ = 'users'
    full_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    city = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
