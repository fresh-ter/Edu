#!/bin/bash
source env/bin/activate
pyuic5 UI/SuperApp.ui -o UI/SuperAppUI.py
pyuic5 UI/SuperAppExtension.ui -o UI/SuperAppExtensionUI.py
