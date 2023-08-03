import os
import google.generativeai as palm
from fastapi import FastAPI, HTTPException, Body, Request

API_KEY = os.environ.get('api_key')
palm.configure(api_key=API_KEY)
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]

app = FastAPI()


def generate_recipe(recipe_name):
    prompt = f"I want you to act as a Recipe Developer. You will create a recipe for a dish called \"{recipe_name}\"."
    response = palm.generate_text(
        prompt=prompt
    )
    return {"recipe": response.result}


@app.get("/")
async def read_root():
    return {"message": "Welcome to the recipe generator API."}

@app.post("/gen_recipe/")
async def gen_recipe_api(
    recipe_data: dict = Body(
        ...,
        example={"recipe": "Pasta Carbonara"})):
    if not recipe_data or not recipe_data.get("recipe"):
        raise HTTPException(status_code=400, detail="recipe_name is a required field in the input JSON.")

    recipe_name = recipe_data.get("recipe")

    recipe_text = generate_recipe(recipe_name)
    return {"recipe": recipe_text}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
