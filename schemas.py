from datetime import datetime, date
from typing import Optional, List
from pydantic import BaseModel
from pydantic.color import Color
import enum

class Theme(enum.Enum):
    light = 'light'
    dark = 'dark'

class Bool(enum.Enum):
    light = 'light'
    dark = 'dark'

class Type(enum.Enum):
    Integer = 'Integer'
    String = 'String'
    Float = 'Float'
    Boolean = 'Boolean'

class Field(BaseModel):
    name: str
    type: Type
    nullable: bool
    default: str

class Model(BaseModel):
    title: str
    relations: list
    fields: List[Field]

class AppCreatingRequestData(BaseModel):
    title: str
    theme: Theme
    mainColor: Color
    contrastColor: Color
    secondaryColor: Color
    secondaryContrastColor: Color
    componentNames: List[str]
    models: List[Model]