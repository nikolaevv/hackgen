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
    Text = 'Text'
    Float = 'Float'
    Boolean = 'Boolean'
    DateTime = 'DateTime'
    enum = 'enum'
    Date = 'Date'
    Relation = 'Relation'

class Field(BaseModel):
    name: str
    type: Type
    nullable: bool
    default: str
    choices: list

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