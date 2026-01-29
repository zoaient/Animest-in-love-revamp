from pydantic import BaseModel, Field
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import core_schema
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: any, _handler: any
    ) -> core_schema.CoreSchema:
        def validate(value: str) -> ObjectId:
            if not ObjectId.is_valid(value):
                raise ValueError("Invalid ObjectId")
            return ObjectId(value)

        return core_schema.json_or_python_schema(
            json_schema=core_schema.str_schema(),
            python_schema=core_schema.union_schema(
                [
                    core_schema.is_instance_schema(ObjectId),
                    core_schema.chain_schema(
                        [
                            core_schema.str_schema(),
                            core_schema.no_info_plain_validator_function(validate),
                        ]
                    ),
                ]
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda v: str(v)
            ),
        )

class Character(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    name: str
    color: str
    picture: str
    class Config:
        populate_by_name = True
        json_encoders = {ObjectId: str}

class Answer(BaseModel):
    id: int
    text: str
        
class Message(BaseModel):
    character: str
    content: str | None = None 
    channel: str | None = None
    choices: list[Answer] | None = None



