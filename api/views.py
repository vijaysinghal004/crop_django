import os
import numpy as np
import pickle
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and preprocessing components
with open(os.path.join(BASE_DIR, 'mdl.pkl'), "rb") as f:
    data = pickle.load(f)

crop_images = {
    "Wheat": "https://wholegrainscouncil.org/sites/default/files/thumbnails/image/15616367_ml-wheat-field.jpg",
    "Sugarcane": "https://th.bing.com/th/id/OIP.NXh_7DPm1FWBnrYO7wH5RwHaEc?w=250&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Maize": "https://th.bing.com/th/id/OIP.e4ZgFzibnzcSO85hWLXopgHaE8?rs=1&pid=ImgDetMain",
    "Barley": "https://th.bing.com/th/id/OIP.wBYoaUWLy-BoVmGIyOxKPQHaFS?w=280&h=200&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "cotton": "https://th.bing.com/th/id/OIP.HUzNPbFwrCHLaoDtXc3q5QHaE8?w=274&h=183&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Fruits":"http://ts1.mm.bing.net/th?id=OIP.dJKl2rwhStpu4CYuBe-RJwHaE8&pid=15.1",
    "Vegetables":"https://th.bing.com/th/id/OIP.-2QdepLpzF3_krchZtFKpQHaE8?w=288&h=192&c=7&r=0&o=5&dpr=1.3&pid=1.7",
    "Pules":"https://th.bing.com/th/id/OIP.VqHsnxMlX23t4HKN_uTRUgHaEx?w=277&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7"

    # Add mappings for all crops in your dataset
} 

# Extract components from the model data
le_soil = data["label_encoder_soil"]
le_month = data["label_encoder_month"]
le_crop = data["label_encoder_crop"]
scaler = data["scaler"]
model = data["model"]

# Home route
@api_view(['GET'])
def home(request):
    return Response({"message": "Welcome to the crop recommendation API!"})

# Prediction route
@api_view(['POST'])
def predict(request):
    data = request.data
    
    # Extract input data
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    soil_type = data.get("soil_type")
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    month = data.get("month")

    # Check for missing inputs
    if None in [latitude, longitude, soil_type, temperature, humidity, month]:
        return Response({"error": "Missing input data"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Encode soil type and month
        soil_type_encoded = le_soil.transform([soil_type])[0]
        month_encoded = le_month.transform([month])[0]
    except ValueError:
        return Response({"error": "Invalid soil_type or month"}, status=status.HTTP_400_BAD_REQUEST)

    # Prepare input data for prediction
    input_data = np.array([[latitude, longitude, soil_type_encoded, temperature, humidity, month_encoded]])
    input_data_scaled = scaler.transform(input_data)

    # Make predictions
    predictions = model.predict(input_data_scaled)
    top_2_indices = predictions[0].argsort()[-2:][::-1]

    # Decode the top 2 indices back to crop names
    top_2_crops = le_crop.inverse_transform(top_2_indices)

    response = []
    for crop in top_2_crops:
        response.append({
            "crop_name": crop,
            "image_url": crop_images.get(crop,"https://cropwatch.unl.edu/2020-CW-News/2020-09-02-adding-wheat-to-crop-rotation-figure-2.jpg")
        })

    
    return Response({  "recommended_crops": response}
    )
