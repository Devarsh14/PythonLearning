from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# To run python main.py
# uvicorn main:app --reload
# pip list | grep fastapi
# pip freeze > requirements.txt
