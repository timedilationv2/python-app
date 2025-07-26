from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from task_manager import load_tasks, save_tasks

app = FastAPI()

# Allow browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

class Task(BaseModel):
    name: str

@app.get("/tasks")
def get_tasks():
    return load_tasks()

@app.post("/tasks")
def add_task(task: Task):
    tasks = load_tasks()
    tasks.append({"name": task.name, "done": False})
    save_tasks(tasks)
    return {"message": "Task added"}

@app.post("/tasks/{task_id}/done")
def mark_done(task_id: int):
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks[task_id]["done"] = True
        save_tasks(tasks)
        return {"message": "Marked as done"}
    return {"error": "Invalid task ID"}
