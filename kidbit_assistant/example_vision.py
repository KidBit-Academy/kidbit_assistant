from vision import *

API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'
IMAGE = 'PATH_TO_IMAGE'

set_secrets(API_KEY, API_SECRET)

print("Objects Detected: ", get_objects(IMAGE))
print("\nNumber of Faces: ", get_number_of_faces(IMAGE))
print("\nText: ", get_text(IMAGE))