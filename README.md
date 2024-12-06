# SpeechSign3D
This academic project implements an application to convert speech to American Sign Language (ASL) as images or 3D models

## Installation
1. Clone the GitHub repository:
```
git clone git@github.com:hgky95/SpeechSign3D.git
```

2. Open your command line and run below command to create virtual environment:
```
cd SpeechSign3D
python -m venv .venv
```

3. Activate the virtual environment

- On windows:
```
.venv/Scripts/activate
```

- On Unix/Mac:
```
source .venv/bin/activate
```

4. Install library dependencies:
```
pip install -r requirements.txt
```

5. Convert Speech to ASL:
```
cd SpeechToASL
python main.py
```

6. Convert Speech to 3D ASL:
```
cd SignLanguage3D
python main.py
```

Result: converting Speech to ASL image:
![output](https://github.com/user-attachments/assets/973a1375-7a67-40b6-aaa1-8d63ba1e89cb)

Result: converting Speech to 3D model:
![1](https://github.com/user-attachments/assets/a8546ed5-1343-444e-93ec-f01def2250a2)


## Acknowledgement
This project uses [InstantMesh](https://huggingface.co/spaces/TencentARC/InstantMesh) to create 3D models
