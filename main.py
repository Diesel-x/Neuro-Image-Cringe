import io
from typing import Union

import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse, RedirectResponse
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("Model\keras_model.h5", compile=False)

# Load the labels
class_names = open("Model\labels.txt", "r").readlines()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return FileResponse("index.html")
    
@app.post("/predict")
async def predict(image: UploadFile):
    try:
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open(io.BytesIO(await image.read())).convert("RGB")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data[0] = normalized_image_array
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index].encode("windows-1251").decode("utf-8")
        confidence_score = prediction[0][index] 
        return { 
            "Class": class_name[2:-1],
            "Score": str(confidence_score)
        }
    except Exception as e:
        return "Не удалось, выполнить запрос: " + str(e)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)