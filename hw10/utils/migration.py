import os
import django
from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw10.settings")
django.setup()

from quotes.models import Quote, Tag, Author

client = MongoClient("mongodb://localhost")

db = client.hw

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname= author["fullname"],
        born_date= author["date_born"],
        location_born= author["location_born"],
        bio= author["bio"]
    )

quotes= db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote["tags"]:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
        
        
    quote_exist = bool(len(Quote.objects.filter(quote=quote["quote"])))
    if not quote_exist:
        author= db.authors.find_one({"_id": quote["author"]})
        author_ = Author.objects.get(fullname=author["fullname"])
        quote_= Quote.objects.create(
            quote=quote["quote"],
            author= author_
        )
        for tag in tags:
            quote_.tags.add(tag)


