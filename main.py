# from typing import Union
# from fastapi import FastAPI, Path
# from pydantic import BaseModel
# from typing import Optional
# import uvicorn
# app = FastAPI()

# # @app.get('/')
# # def read_root():
# #     return{"Hello": "World"}

# # #http://127.0.0.1:8000//items/%7B1%7D

# # class Item(BaseModel):
# #     name: str
# #     price: float
# #     is_offer: Union[bool, None] = None

# # @app.get("/items/{item_id}")
# # def read_item(item_id: int, q:Union[str, None] = None):
# #     return {"item_id": item_id, "q": q}

# # @app.put("/items/{item_id}")
# # def update_item(item_id: int, item: Item):
# #     return {"item_name": item.name, "item_id": item_id}


# class Student(BaseModel):
#     name: str
#     age: int
#     year: str


# class UpdateStudent(BaseModel):
#     name: Optional[str] = None
#     age: Optional[int] = None
#     year: Optional[str] = None

# students = {
#     1: {
#         "name": "John",
#         "age": 23,
#         "class": "ss3"
#     },
#     2: {
#         "name": "Paul",
#         "age": 22,
#         "class": "ss3"
#     }
# }

# #Below is example of PATH parameter
# @app.get("/get-student/{student_id}")
# #def get_student(student_id: int): gt means greater than and lt means lesser than
# def get_student(student_id: int = Path(..., description='The Id of the student you want to view', gt=0, lt=7)):
# #def get_student(student_id: int = Path(None, description='The Id of the student you want to view')): This will not work path cannot be NONE
#     return students[student_id]

# #Below is example of Query parameter
# @app.get("/get-by-name")
# #def get_student(name: str = None): for not required option=> name not required as input
# # def get_student(name: str): for name is required
# # best practice below
# # def get_student(name: Optional[str]= None):
# #def get_student(name: Optional[str]= None, test: int): it will not work to can a true request and after option request except you put a star/asterik
# def get_student(*,name: Optional[str]= None, test: int):
#     for student_id in students:
#         if students[student_id]['name'] == name:
#             return students[student_id]
#         # else:
#         #     return {"Data": "error!"}
#     return {"Data": "Not found"}

# #Below is example of PATH parameter
# @app.get("/get-by-name/{student_id}")
# def get_student(*,student_id: int,name: Optional[str]= None, test: int):
#     for student_id in students:
#         if students[student_id]['name'] == name:
#             return students[student_id]
#         # else:
#         #     return {"Data": "error!"}
#     return {"Data": "Not found"}

# @app.post("/create-student/{student_id}")
# def create_student(student_id: int, student: Student):
#     if student_id in students:
#         return {"Error": "Student exist"}
    
#     students[student_id] = student
#     return students[student_id]


# @app.put("/update-student/{student_id}")
# def update_student(student_id: int, student: UpdateStudent):
#     if student_id not in students:
#         return {"Error": "Student does not exist"}
#     if student.name != None:
#         students[student_id].name = student.name
#     if student.age != None:
#         students[student_id].age = student.age
#     if student.year != None:
#         students[student_id].year = student.year
    
#     return students[student_id]

# @app.delete("/delete-student/{student_id}")
# def delete_student(student_id: int):
#     if student_id not in students:
#         return {"Error": "Student does not exist"}
    
#     del students[student_id]
#     return {"message": 'student deleted successfully'}

# #@app.get('/blog?limit=10&published=true')
# @app.get('/blog')
# def index(limit, published: bool =True, sort: Optional[str] = None):
    
#     if published:
#         return{"data": f"{limit} published blogs from the db"}
#     else:
#         return {'data': f"{limit} blogs from the db"}
# @app.get('/blog/unpublished')
# def unpublished():
#     return{'data': 'all unpublished blogs'}

# @app.get('/blog/{id}')
# def show(id: int):
#     return {'data': id}

# @app.get('/blog/{id}/comments')
# def comments(id, limit= 50):
#     return{'data': ['1', '2']}


# class Blog(BaseModel):
#     title: str
#     body: str
#     published : Optional[bool]


# @app.post('/blog')
# def create_blog(blog: Blog):
#     return {'data': f"Blog is created with title as {blog.title}"}
# #http://127.0.0.1:8000/get-student/1


# # if __name__ == "__main__":
# #     uvicorn.run(app, host='127.0.0.1', port= 9000)