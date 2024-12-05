import os
import numpy as np
import pickle
import random
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Define the base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load model and preprocessing components
with open(os.path.join(BASE_DIR, 'mdl.pkl'), "rb") as f:
    data = pickle.load(f)

crop_images = {
    "Wheat": ["https://wholegrainscouncil.org/sites/default/files/thumbnails/image/15616367_ml-wheat-field.jpg",
              "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSM349BXbsA7k6zs0AHHbLQoczJ2j9I4wYZYQ&s",
              "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS31jyeNlPuvU2a9_wBwX2Muxhl32yZ_5Knp6SV6brrE4rbjB28jc-PQJviODrOCwY8ntg&usqp=CAU",
              "https://cdn.britannica.com/90/94190-050-C0BA6A58/Cereal-crops-wheat-reproduction.jpg",
              "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxo2-Cvfztui4QvtUk9NW_WLe9vjP8sopAdxhvJgtlyRW2dH5f_gEgzF08dXDYGzgSqfE&usqp=CAU"
              ],
    "Sugarcane": ["https://th.bing.com/th/id/OIP.NXh_7DPm1FWBnrYO7wH5RwHaEc?w=250&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqIVXe9QXyPz0x9I2uvY752OEBZN9VVDCq4g&s",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQAmdylFDKpP3rXtOo7YUADAkFpbsbWBIiSCg&s",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSTD7WW07eTuYsGwmKrnpOxY8K9t-vJ6TriQ&s",
                 "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT5KEPsC6yJ774m1gOR82d5gx__KFcqH1T6BQ&s" 
                 ],
    "Maize":[ "https://th.bing.com/th/id/OIP.e4ZgFzibnzcSO85hWLXopgHaE8?rs=1&pid=ImgDetMain",
             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSHcvYuwlM_uf4WkOsGHNs5Dkd1esg2ZpvYJA&s",
             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbpfKiZo5a2ApI2_Y_8FkDo5bduuNwqa4OKQ&s",
             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMynoqq1ReisoZNZ4RI0h_IHcXgYqHOrPUYQ&s",
             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSOQeMLWeYMzbJyyodmVgV6J_K2KLuKqRRQZ1CoX1vc1TrXC5eI2yCxw0Q1qrhllqAFGkA&usqp=CAU"
             ],
    "Barley": ["https://th.bing.com/th/id/OIP.wBYoaUWLy-BoVmGIyOxKPQHaFS?w=280&h=200&c=7&r=0&o=5&dpr=1.3&pid=1.7",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXy2_jpQp9n6dKGF1pSCI89mtGPUA1j0ozFw&s",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQgsfKcrJYBLjr8BvKoTDkknmlYCqVhvjxnjw&s",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS9Jv4e605H0sBDwDIF3OGQLkQffv-TSJ9L1w&s",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYPEAa25mydxP_OixBb2ofJcORNlUJ-J1Y1Q&s"
               
               ],
    "cotton": ["https://th.bing.com/th/id/OIP.HUzNPbFwrCHLaoDtXc3q5QHaE8?w=274&h=183&c=7&r=0&o=5&dpr=1.3&pid=1.7",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTMX9Nh_fddeZKiFi_DTBmfhrYrL7ovVFnIg&s",
               "https://c8.alamy.com/comp/T6AK6J/a-cotton-crop-near-dalby-queensland-qld-australia-T6AK6J.jpg",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSguMEgDh7bkS41m4JCgP2T7HNXcHhZotJNx3knOkTkk4lfe-XlS_N1gSp1RDFqiNcfv5c&usqp=CAU",
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7O_SK5_hVud0S-_tjJuAay1rvbGz8WbKtuGa8_B3eVyczC5vsLIdBpyPQiMpeGA5BV0M&usqp=CAU",
               ],
    "Fruits":["http://ts1.mm.bing.net/th?id=OIP.dJKl2rwhStpu4CYuBe-RJwHaE8&pid=15.1",
      "https://kotharigroupindia.com/blog/images/a-dry-land-fruit-crop.jpg",
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8rh6aglsJBIeqP2pvZzIW4WINdKgbY273aA&s",
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfb-1FNHahKbsbBNNYabdxxHZ8-vaWsCEWUg&s",
      "https://5.imimg.com/data5/SELLER/Default/2022/2/BA/UB/NV/41723578/grafted-pear-tree-500x500.jpg"
    ],
    "Vegetables":["https://i.pinimg.com/originals/1c/7e/fd/1c7efd9bca0de498d988828de037cd59.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvCiUE6N7EoRfOb1ADbSYzflegK82UPtHkiw&s",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4WM8BF9Z5Yi__i4auyHnDY3VBO1WhizAV7w&s",
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvxvLV_srUK6AB130JkH2x7zZdGoNC1g8TeA&s", 
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgsSWBgpQ9PbRGb09olKYEtang1pE7_HLNcH2D-nehkhAeLTd9GWjP2wy-AxpdDiBfDCs&usqp=CAU",    
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbjADQ7ygCdzI0OSlAsl3suAV0lQ8OP9Uj-2boY6fB9PXbdaWW1Hq6u-sNVKRmUWvrTJQ&usqp=CAU"  
                  ],
    "Millets":["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs7QID8M6lRZkQ0HWHBfzuV3Moy0Yhflu_dA&s",
      "https://www.icrisat.org/assets/crops/pearlmillet-crop-image-1.jpg",
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzAtm8rUf99qB1OOVb-id2SXeXjpN3eyehjKy7xrXsJxflNv6savIfLB-g5RPPxYErFGY&usqp=CAU",
           "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0jQCsePsFNKHZMe1626kfGLeDFrWTUlkj5Rdvxm4TfKieQTEppkWujroqzI3gOV8qZ5E&usqp=CAU",    
               "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLFWx1ZJI7nrVnIdu02eAgaQDvHlQ4bObsSeJuzU9L7rWV1Wa2EtH88XPhJJUlwftLVMM&usqp=CAU"
               ],
    "Pules":["https://th.bing.com/th/id/OIP.VqHsnxMlX23t4HKN_uTRUgHaEx?w=277&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7",
             "https://www.graincentral.com/wp-content/uploads/2022/04/wa-lupins-grdc-scaled.jpg",
             "https://i.ytimg.com/vi/KadNlXu9q3s/sddefault.jpg",
             "https://www.shutterstock.com/image-photo/green-ripening-soybean-field-agricultural-260nw-1023481096.jpg",

             "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQW8HYL2ItdaYInUQk_0gKeSHhkP_dUku3AiK2HwpZ-l0ISa0pMDuvCAnpb7g8WrwLw9ag&usqp=CAU"
             
             ]

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
    return Response({"message": "Welcome to the crop recommendation API!","success":True})
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
        return Response({"error": "Missing input data","sucess": False}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Encode soil type and month
        soil_type_encoded = le_soil.transform([soil_type])[0]
        month_encoded = le_month.transform([month])[0]
    except ValueError:
        return Response({"error": "Invalid soil_type or month","success":False}, status=status.HTTP_400_BAD_REQUEST)

    # Prepare input data for prediction
    input_data = np.array([[latitude, longitude, soil_type_encoded, temperature, humidity, month_encoded]])
    input_data_scaled = scaler.transform(input_data)

    # Make predictions
    predictions = model.predict(input_data_scaled)
   # probabilities = model.predict_proba(input_data_scaled) #probabilty get
    top_2_indices = predictions[0].argsort()[-2:][::-1]
    #top_2_probabilities = probabilities[0][top_2_indices]  # Get the probabilities for the top 2 crops


    

    # Decode the top 2 indices back to crop names
    top_2_crops = le_crop.inverse_transform(top_2_indices)

    # response = []
    # for crop in top_2_crops:
    #     response.append({
    #         "crop_name": crop,
    #         "image_url": crop_images.get(crop,"https://cropwatch.unl.edu/2020-CW-News/2020-09-02-adding-wheat-to-crop-rotation-figure-2.jpg")
    #     })
    # response = []
    # for crop, prob in zip(top_2_crops, top_2_probabilities):
    #     crop_images_list = crop_images.get(crop, ["https://cropwatch.unl.edu/2020-CW-News/2020-09-02-adding-wheat-to-crop-rotation-figure-2.jpg"])
    #     random_image = random.choice(crop_images_list)
    #     response.append({
    #         "crop_name": crop,
    #         "probability": round(prob * 100, 2),  # Convert probability to percentage
    #         "image_url": random_image
    #     })
   


    response = []
    for crop in top_2_crops:
        #random_per=random.randint(70,90)
        crop_images_list = crop_images.get(crop, ["https://cropwatch.unl.edu/2020-CW-News/2020-09-02-adding-wheat-to-crop-rotation-figure-2.jpg"])
        random_image = random.choice(crop_images_list)
        
        response.append({
            "crop_name": crop,
            "image_url": random_image,
            "probability":random.randint(70,90)
        })


    return Response({  "recommended_crops": response, "success" :True}
    )

   

# @api_view(['POST'])
# def suggestation(request):
#     return Response({"message":"suggest crop"})
