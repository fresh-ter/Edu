#!/bin/bash
source env/bin/activate
pyinstaller -F SuperApp.py
pyinstaller -F SuperAppExtension.py
