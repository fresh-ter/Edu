#!/bin/bash
source env/bin/activate
pyinstaller -F SuperApp.py
pyinstaller -F SuperAppExtension.py

cp dist/SuperApp SuperApp/System/
cp dist/SuperAppExtension SuperApp/System/
