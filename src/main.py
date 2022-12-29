from fastapi import FastAPI,status, Depends, HTTPException
from src.database import engine, get_db
from src.models import Base, User, BlogPost
from src.schemas import UserCreate, BlogCreate
from sqlalchemy.orm import Session
from src.linked_list import LinkedList
from fastapi.encoders import jsonable_encoder
from src.hash_table import HashTable
from datetime import datetime

app = FastAPI()
Base.metadata.create_all(bind=engine)



@app.get("/",status_code=status.HTTP_200_OK)
def root():
    return {
        "message": "Datastructure in a Backend system"
    }


@app.post("/user/", status_code=status.HTTP_201_CREATED)
def create_user(new_user: UserCreate,db:Session= Depends(get_db)):

    new_user = User(**new_user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User Created successfully",
        "data": new_user,
        "status":status.HTTP_201_CREATED
    }
    pass

@app.get("/user/descending_id/", status_code=status.HTTP_200_OK)
def get_users_descending(db:Session= Depends(get_db)):
    users = db.query(User).all()
    all_user_ll = LinkedList()

    for user in jsonable_encoder(users):

        all_user_ll.insert_beginning(user)

    ll_response = all_user_ll.to_array()    
    return {
        "message": "Users Linked List in descending order",
        "data":ll_response,
        "status": status.HTTP_200_OK
    }



@app.get("/user/ascending_id/", status_code= status.HTTP_200_OK)
def get_users_ascending(db:Session= Depends(get_db)):

    users = db.query(User).all()
    all_user_ll = LinkedList()

    for user in jsonable_encoder(users):

        all_user_ll.insert_at_end(user)
    ll_response = all_user_ll.to_array()    


    return {
        "message": "Users returned in a Linked List",
        "data": ll_response,
        "status": status.HTTP_200_OK
    }
    


@app.get("/user/{user_id}/")
def get_user_by_id(user_id:int, db:Session = Depends(get_db)):
    users = db.query(User).all()
    all_user_ll = LinkedList()

    for user in jsonable_encoder(users):
        all_user_ll.insert_at_end(user)

    user = all_user_ll.get_user_by_id(user_id)



    return {
        "message": "Returned Use from a Linked List",
        "data": user,
        "status": status.HTTP_200_OK
    }


@app.delete("/user/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id:int, db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)

    return {
        "status": status.HTTP_204_NO_CONTENT
    }


@app.post("/blog/{user_id}",status_code= status.HTTP_201_CREATED)
def create_blog_post(user_id:int,blog_create:BlogCreate, db:Session= Depends(get_db)):

    user_check = db.query(User).filter(User.id == user_id).first()
    if not user_check:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail= "User does not exist"
        )

    ht  = HashTable(10)
    ht.add_key_value("title", blog_create.title)
    ht.add_key_value("body", blog_create.body)
    ht.add_key_value("date", datetime.now().date())
    ht.add_key_value("user_id", user_check.id)

    # ht.print_table()


    new_blog = BlogPost(title= ht.get_value("title"), body= ht.get_value("body"),
                        date= ht.get_value("date"), user_id = ht.get_value("user_id"))



    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        "message": "New blog post created",
        "data": new_blog,
        "status": status.HTTP_201_CREATED
    }



@app.get("/blog/")
def get_blog_posts():
    pass



@app.get("/blog/{blog_id}")
def get_blog_post():
    pass


@app.delete("/blog/{blog_id}")
def delete_blog_post():
    pass