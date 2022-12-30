import yaml

import os
from dotenv import dotenv_values


def get_db_data():
    with open("application/config.yaml") as f:
        db_data = yaml.safe_load(f)
    pas = dotenv_values("application/.env")
    db_data["password"] = pas["PASSWORD"]
    return db_data


tags_metadata = [
    {
        "name": "Get all",
        "description": "Get all from table"
    },
    {
        "name": "Get by id",
        "description": "Get string from table by id"
    }
]
description = """
API for interaction with DataBase 

You will be able to:

* **Get data from tables**
* **Get data with id from tables**

**Available tables:**
* _banner_
* _blog_
* _vacancies_
* _promotions_
* _phones_
* _address_
* _object_
"""
