try:
    import uvicorn
    
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    
    from utility import*

except Exception as e:
   print('Error loading module in model_pred.py: ', e)


app = FastAPI(title='Assentify')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict_cervF")
async def predict_cervF(image_file: UploadFile =File(...)):
    try: 
        prediction = await model_pred_utility(model_cervF, image_file)
        return prediction
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict_boneF")
async def predict_boneF(image_file: UploadFile =File(...)):
    try: 
        prediction = await model_pred_utility(model_boneF, image_file)
        return prediction
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @app.post("/predict_pneumo")
# async def predict_pneumo(image_file: UploadFile =File(...)):
#     try: 
#         prediction = await model_pred_utility(model_pneumo, image_file)
#         return prediction
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)