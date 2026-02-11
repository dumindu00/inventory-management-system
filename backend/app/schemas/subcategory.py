from pydantic import BaseModel

class SubCategoryBase(BaseModel):
    name: str
    category_id: int
    
class SubCategoryCreate(SubCategoryBase):
    pass

class SubCategoryRead(SubCategoryBase):
    id: int
    
    class Config:
        from_attributes = True
