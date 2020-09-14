[![Discord](https://img.shields.io/discord/630805507782868992.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/GghbTQA)

# Abysser
A tool to parse Eve Online screenshots for Abyssal details


Todo: 
 - Everything... lol.
 
 
Flow:

- get images from current directory
- parse with open cv
- if loot can, record loot info and can info
- if no loot can, record overview info
- save to csv
- end

Stack:

- Python 3+
- [opencv-python](https://pypi.org/project/opencv-python/)
- [Tesseract](https://github.com/tesseract-ocr/tesseract/wiki)
