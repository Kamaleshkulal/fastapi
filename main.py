from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}

todos = []

@app.get("/todos")
async def get_todos():
    return {"todos": todos}


# create todos
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return {"message" : "todos has been added"}

# create single todos
@app.get("/todos/{todos_id}")
async def get_todos_single(todos_id:int):
    for todo in todos:
        if todo.id == todos_id:
            return {"todos":todo}
    return {"message":"not found"}

#delete todos
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id :int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message":" todos id has been removed"}
        
        
        
# create single todos
@app.get("/todos/{todos_id}")
async def get_todos_single(todos_id:int):
    for todo in todos:
        if todo.id == todos_id:
            return {"todos":todo}
    return {"message":"not found"}    
            
        
# Update todos
@app.put("/todos/{todo_id}")
async def update_todo(todo_id:int , todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todos" : todo}
    return {"message": "not valid"}    