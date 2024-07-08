# Face_Mask

# ABOUT THE PROJECT  
The current pandemic situation of COVID-19 has led us to wear mask to safeguard us from others and the other way around too,
yet there are very few people who refused to wear masks and we have come up with a solution to identify people not wearing the masks.
Our project uses deep learning algorithms to detect whether a person has worn a mask or not.
We are using a pretrained resnet50 to train the dataset which helps us to get significant accuracy. 
The significance of the model is it has residual connections that helps to solve the vanishing gradient problem to an extent which has a major impact on accuracy of the test set. 
The images are then measured for a cosine distance with the face of people present in the database to find the person not wearing the mask. This can be used in institutions where there are enormous people.  
# The modules which are defined in this project are   
* Dataset preparation and loading  
* Model definition  
* Model training  
* Face mask detection  
* Face verification  

#  Dataset preparation and loading:
This module is used to prepare the dataset such as scaling, applying filter    and adding the annotations as the prediction to the data loader.  
#  Model Definition:
          This module initializes the model class and the parameters required for the model.  
#  Model Training:
          This module is used to train the model with certain number of epochs.  
#  Facemask detection:
          This module uses the trained model and tests the images whether the person has worn a mask or not    
#  Face verification:
          In case where the person has not won a mask, this module finds the name of the person that is already present in the database   

# CONCLUSION  
In today’s world it is inevitable to go out without a mask. This application helps an organization or an institute to manage their employees and people who often visit them.
The discovery of deep learning algorithms has led to a big leap in the development of difficult problems such as detection, segmentation etc.
We used a pretrained resnet50 to train the dataset which helped us to get significant accuracy.
The significance of the model is it has residual connections that helps to solve the vanishing gradient problem to an extent which has a major impact on accuracy of the test set.  

# License
Apache-2.0 license
