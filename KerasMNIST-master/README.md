# Deploying Your Keras Model To Production - Part I

This implementation is inspired by Siraj Raval's You Tube video about deploying your Keras model to production. 
https://github.com/llSourcell/how_to_deploy_a_keras_model_to_production

https://www.youtube.com/watch?v=f6Bf3gl4hWY

# How this is different from Siraj's Code?

[1] Initially has faced some challenges in cloning and running the code as is. 
The code would generally break for me around:
`imgstr = re.search(b'base64,(.*)', imgData).group(1)`
After some basic Google-ing, just importing the `base64` library in the `app_file.py` did the trick.

[2] This implementation has been trained on scenarios for user to draw numbers not just at the canvas center / or maintain a specific size, i.e. the implementation should ideally recognize digits drawn also on the sides with varing sizes

# Quick Bits

This exercise made me realize that there is no proportional relation between the depth of the network and prediction accuracy, my inital setup had much more layers but struggled to improve accuracy beyond 85%, but then trimming the layers pushed the accuracy to 98%+

# To use your Keras model driven MNIST recoginition app on your local computer simply clone the directory:

`git clone https://github.com/AnuragHalder/KerasMNIST.git`

This will create a new directory for you `KerasMNIST`, please go into this directory and run the following command:

`python app_file.py` 

[Click Here For A Quick Video Demo On YouTube](https://www.youtube.com/watch?v=LFzcnRVCUYQ&feature=youtu.be)

![Example](https://github.com/AnuragHalder/KerasMNIST/blob/master/two.png)

