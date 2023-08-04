# apitesting_fastapi
Current project is based on FastAPI Swagger User Interface application and its deployment on azure.
Runs on ASGI server, for production such as Uvicorn.
Model is implemented on prompt generation for recipe by help of Google Generative PaLM api.
You can test the url on postman as api.on http request "POST"  
body/raw as json format
{
"recipe":"recipe name"
}
#url
https://apitestingrecipe.azurewebsites.net/gen_recipe/
