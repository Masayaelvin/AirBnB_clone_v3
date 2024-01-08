#!/usr/bin/python3
#comment

""" Test .get() and .count() methods
"""
from models import storage
from models.state import State
from models.user import User

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

print("All objects: {}".format(storage.count()))
print("User objects: {}".format(storage.count(User)))

#first_user_id = list(storage.all(User).values())[0].id
#print("First state: {}".format(storage.get(User, first_user_id)))

first_state_id = list(storage.all(State).values())[0].id
print("First state: {}".format(storage.get(State, first_state_id)))
