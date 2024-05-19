#!/usr/bin/python3
""" Initialises the storage engine on console start """
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
