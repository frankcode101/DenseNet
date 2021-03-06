import streamlit as st
import tensorflow as tf
import streamlit as st

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('final_model.hdf5')
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()
st.write("""
         # Fashion MNIST Classification
         """
         )
file = st.file_uploader("Please upload an image", type=["jpg", "png"])
import cv2
from PIL import Image, ImageOps
import numpy as np
st.set_option('deprecation.showfileUploaderEncoding', False)
def import_and_predict(image_data, model):
        size = (28,28)
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img_resize = (cv2.resize(img, dsize=(28, 28),interpolation=cv2.INTER_CUBIC))/255.
        img_reshape = img_resize[np.newaxis,...]
        prediction = model.predict(img_reshape)
        return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag',
                   'Ankle boot']
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    score = 100*np.max(predictions[0])
    st.write(
    "This image most likely belongs to {} with a {:.2f} percent."
    .format(class_names[np.argmax(predictions[0])], (score))
)
    print(
    "This image most likely belongs to {} with a {:.2f} percent."
    .format(class_names[np.argmax(predictions[0])], (score))
)


