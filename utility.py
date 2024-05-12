try:
    import os
    import tensorflow as tf
    import PIL
    from PIL import Image
    import numpy as np
    from tensorflow.keras.preprocessing import image
    from fastapi import UploadFile, File, HTTPException
    from io import BytesIO
    import tensorflow.keras as keras
    
except Exception as e:
   print('Error loading module in utilites.py: ', e)

model_cervF = keras.models.load_model('cervical_fractured_model.h5')
model_boneF = keras.models.load_model('bone_fractured_model.h5')
# model_pneumo = keras.models.load_model('pneumonia_model.h5')

async def model_pred_utility(model, image_file: UploadFile=File(...)):
    try:
        image = np.array(Image.open(BytesIO(await image_file.read())))
        
        image = Image.fromarray(image).resize((256, 256))
        image = np.array(image)

        img_batch = np.expand_dims(image, 0)

        predictions = model.predict(img_batch)
        predicted_classes = predictions.tolist()
        
        return {"predicted_class": predicted_classes}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        