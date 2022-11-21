from fastapi import APIRouter, Request, Form
from rjson import *
import pprint
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory = "templates")

router = APIRouter(
    tags = ['restaurant'],
    responses = {404: {"message": "Not found"}}
)

rest_db = Data()

#all restaurant
@router.get("/", response_class = HTMLResponse)
def get_res(request: Request):
    cnt = 0
    context = {}
    for i in rest_db:
        context["rest_id" + str(cnt)] = i["rest_id"]
        context["Name" + str(cnt)] = i["Name"]
        context["Location" + str(cnt)] = i["Location"]
        context["Type_of_food" + str(cnt)] = i["Type_of_food"]
        context["Recommend_menu" + str(cnt)] = i["Recommend_menu"]
        context["O_C_time" + str(cnt)] = i["Opening-Closing_time"]
        context["Contact_number" + str(cnt)] = i["Contact_number"]
        cnt = cnt + 1
    context ['request'] = request
    return templates.TemplateResponse("index.html", context)

#search restaurant location
@router.get("/{rest_location}")
def get_rest_location(rest_location : str):
    print()
    print("console rest_location is " + rest_location)
    count = -1
    data = []
    for i in rest_db:
        count = count + 1
        if i.get("Location") == rest_location:
            data.append(rest_db[count])
    pprint.pprint(data)
    return {"response": data}

@router.post("/", response_class = HTMLResponse)
def post_form(request: Request, loc: str = Form(...)):
    print(loc)
    return templates.TemplateResponse("test.html", {'request': request})