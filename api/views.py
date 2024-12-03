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
    "Wheat": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fcommon-wheat&psig=AOvVaw135Pk3K4zKPOkrHDy37lLi&ust=1733259413660000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCIC_29D8iYoDFQAAAAAdAAAAABAR",
    "Rice": "https://www.google.com/imgres?q=rice%20crop%20images&imgurl=https%3A%2F%2Fst.depositphotos.com%2F1469828%2F1559%2Fi%2F450%2Fdepositphotos_15595841-stock-photo-hand-with-rice-field.jpg&imgrefurl=https%3A%2F%2Fdepositphotos.com%2Fphotos%2Frice-crop.html&docid=dNQiz3qCR1dqzM&tbnid=DDVPT631OkPVzM&vet=12ahUKEwiT0NPu_YmKAxV4d2wGHYhCHigQM3oECEgQAA..i&w=600&h=397&hcb=2&ved=2ahUKEwiT0NPu_YmKAxV4d2wGHYhCHigQM3oECEgQAA",
    "Sugarcane": "https://www.google.com/imgres?q=rice%20crop%20images&imgurl=https%3A%2F%2Fst.depositphotos.com%2F1469828%2F1559%2Fi%2F450%2Fdepositphotos_15595841-stock-photo-hand-with-rice-field.jpg&imgrefurl=https%3A%2F%2Fdepositphotos.com%2Fphotos%2Frice-crop.html&docid=dNQiz3qCR1dqzM&tbnid=DDVPT631OkPVzM&vet=12ahUKEwiT0NPu_YmKAxV4d2wGHYhCHigQM3oECEgQAA..i&w=600&h=397&hcb=2&ved=2ahUKEwiT0NPu_YmKAxV4d2wGHYhCHigQM3oECEgQAA",
    "Maize": "https://www.google.com/imgres?q=rice%20crop%20images&imgurl=https%3A%2F%2Fst.depositphotos.com%2F1469828%2F1559%2Fi%2F450%2Fdepositphotos_15595841-stock-photo-hand-with-rice-field.jpg&imgrefurl=https%3A%2F%2Fdepositphotos.com%2Fphotos%2Frice-crop.html&docid=dNQiz3qCR1dqzM&tbnid=DDVPT631OkPVzM&vet=12ahUKEwiT0NPu_YmKAxV4d2wGHYhCHigQM3oECEgQAA..i&w=600&h=397&hcb=2&ved=2ahUKEwiT0NPu_YmKAxV4d2wGHYhCHigQM3oECEgQAA",
    "Barley": "https://www.google.com/imgres?q=barley%20crop%20image&imgurl=https%3A%2F%2Fblog.agribazaar.com%2Fwp-content%2Fuploads%2F2022%2F01%2Fphoto-1437252611977-07f74518abd7.jpg&imgrefurl=https%3A%2F%2Fblog.agribazaar.com%2Fbarley-health-overview%2F&docid=Nc2g2XWkMnHTwM&tbnid=sluZAOXMfaayMM&vet=12ahUKEwiAudPN_omKAxWfd2wGHS3jBqIQM3oECBcQAA..i&w=1000&h=750&hcb=2&ved=2ahUKEwiAudPN_omKAxWfd2wGHS3jBqIQM3oECBcQAA",
    "Millets": "https://www.google.com/imgres?q=Millets%20crop%20image&imgurl=https%3A%2F%2Fwww.croptrust.org%2Ffileadmin%2F_processed_%2Fb%2F2%2Fcsm_Small_foxtail_millet_4ea404745c.jpeg&imgrefurl=https%3A%2F%2Fwww.croptrust.org%2Fknowledge-hub%2Fcrops-countries-and-genebanks%2Fcrops%2Fsmall-millets%2F&docid=TIcL42_xauhDfM&tbnid=njpCsyoh4bUWHM&vet=12ahUKEwiPh6GcgYqKAxWySWwGHf2jC0sQM3oECB0QAA..i&w=900&h=600&hcb=2&itg=1&ved=2ahUKEwiPh6GcgYqKAxWySWwGHf2jC0sQM3oECB0QAA",
    "cotton": "https://www.google.com/imgres?q=cotton%20crop%20images&imgurl=https%3A%2F%2Fcdn.pixabay.com%2Fphoto%2F2019%2F11%2F24%2F17%2F08%2Fcotton-4649804_640.jpg&imgrefurl=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fcotton%2520crop%2F&docid=Qbj2qnJOOin-dM&tbnid=eK184QZmS5xItM&vet=12ahUKEwjQi6CAhYqKAxW8xTgGHSH2M8gQM3oECHEQAA..i&w=640&h=424&hcb=2&ved=2ahUKEwjQi6CAhYqKAxW8xTgGHSH2M8gQM3oECHEQAA",
    "Fruits":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Ffarmers-crop-large-variety-of-fresh-fruit-and-vegetables-water-droplets-visib-ad-fresh-fruit-vegetables-v--760967668269523282%2F&psig=AOvVaw2bq4gC8bZiS5sOdFd6KYbn&ust=1733261700788000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCMCI5ZWFiooDFQAAAAAdAAAAABAE",
    "Vegetables":"https://www.google.com/imgres?q=Vegetables%20crop%20images&imgurl=https%3A%2F%2Fwww.shutterstock.com%2Fimage-photo%2Fharvest-garden-organic-vegetables-selective-260nw-1691372296.jpg&imgrefurl=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fvegetable-crops&docid=TmKRrdPRNzM6LM&tbnid=7rH_KkARdvEmeM&vet=12ahUKEwiPz7CjhYqKAxWC4DgGHXJVAGcQM3oECBwQAA..i&w=515&h=280&hcb=2&ved=2ahUKEwiPz7CjhYqKAxWC4DgGHXJVAGcQM3oECBwQAA",
    "Pules":"https://www.google.com/imgres?q=Pules%20crop%20images&imgurl=https%3A%2F%2Feng.ruralvoice.in%2Fuploads%2Fimages%2F2023%2F12%2Fimage_750x_658fc09b22ef1.jpg&imgrefurl=https%3A%2F%2Feng.ruralvoice.in%2Fnational%2Fpulse-crops-in-rabi-season-decreased-by-about-11-lakh-hect.html&docid=h1meTGk_C4h6oM&tbnid=V78LTyqKFMFjuM&vet=12ahUKEwjuzpi5hYqKAxUs3jgGHWrACy4QM3oECGcQAA..i&w=750&h=500&hcb=2&ved=2ahUKEwjuzpi5hYqKAxUs3jgGHWrACy4QM3oECGcQAA"

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
    top_2_indices = predictions[0].argsort()[-3:][::-1]

    # Decode the top 2 indices back to crop names
    top_2_crops = le_crop.inverse_transform(top_2_indices)

    response = []
    for crop in top_2_crops:
        response.append({
            "crop_name": crop,
            "image_url": crop_images.get(crop,"https://www.google.com/imgres?q=soil%20image%20at%20far%20with%20crop&imgurl=https%3A%2F%2Fc8.alamy.com%2Fcomp%2FD4J407%2Ffield-with-rows-of-crops-kubatsirana-far-manica-district-mozambique-D4J407.jpg&imgrefurl=https%3A%2F%2Fwww.alamy.com%2Fstock-photo%2Fcrops-dry-land-africa.html&docid=aKdMhiOEi1ON9M&tbnid=WujtpODiGbBPHM&vet=12ahUKEwj-uIn0gIqKAxW3S2wGHZT8KA8QM3oECFMQAA..i&w=1300&h=956&hcb=2&ved=2ahUKEwj-uIn0gIqKAxW3S2wGHZT8KA8QM3oECFMQAA")
        })

    
    return Response({  "recommended_crops": response}
    )
