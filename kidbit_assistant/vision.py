import requests
import hashlib

__img_hash_to_id = {}

def set_secrets(key, secret):
    global api_key, api_secret
    api_key = key
    api_secret = secret

def check_success(resp):
    if resp['status']['type'] != 'success':
        raise Exception("Failed to get output from Imagga, status: " + resp['status']['type'] + ", reason: " + resp['status']['text'])

def __upload_image_and_get_id__(image_path, debug=False):
    global __img_hash_to_id
    img_hash = hashlib.md5(open(image_path,'rb').read()).hexdigest()
    
    if debug:
        print("[__upload_image_and_get_id__] hash:", img_hash, "image_path:", image_path)
    
    if img_hash not in __img_hash_to_id:
        response = requests.post(
            'https://api.imagga.com/v2/uploads',
            auth=(api_key, api_secret),
            files={'image': open(image_path, 'rb')})
        resp = response.json()
        
        if debug:
            print("[__upload_image_and_get_id__] Not Present, Response:", resp)
        check_success(resp)
        
        __img_hash_to_id[img_hash] = resp['result']['upload_id']
    
    return __img_hash_to_id[img_hash]

def get_objects(image_path, confidence=50, debug=False):
    upload_id = __upload_image_and_get_id__(image_path, debug)
    
    response = requests.get(
        'https://api.imagga.com/v2/tags?image_upload_id=%s' % upload_id,
        auth=(api_key, api_secret))
    resp = response.json()
    
    if debug:
        print("[get_objects] Response: ", resp)
    check_success(resp)
    
    class_list = []
    
    if debug:
        print("[get_objects] Printing Class, Confidence")
    
    tags = resp['result']['tags']
    for x in tags:
        if x['confidence'] >= confidence:
            class_list.append(x['tag']['en'])
        if debug:
            print("[get_objects] %s %.2f" % (x['tag']['en'], x['confidence']))
    
    return class_list

def get_number_of_faces(image_path, confidence=50, debug=False):
    upload_id = __upload_image_and_get_id__(image_path)
    response = requests.get(
        'https://api.imagga.com/v2/faces/detections?image_upload_id=%s' % (upload_id),
        auth=(api_key, api_secret))

    resp = response.json()

    if debug:
        print("[get_number_of_faces] Response: ", resp)
    check_success(resp)

    num_faces = 0
    faces = resp['result']['faces']
    for face in faces:
        if debug:
            print(f"[get_number_of_faces] Confidence: {face['confidence']}, Co-ordinates: {face['coordinates']}, Face Id: {face['face_id']}")
        if face['confidence'] >= confidence:
            num_faces += 1  

    return num_faces

def get_text(image_path, debug=False):
    response = requests.post(
        'https://api.imagga.com/v2/text',
        auth=(api_key, api_secret),
        files={'image': open(image_path, 'rb')})

    resp = response.json()

    if debug:
        print("[get_text] Response: ", resp)
    check_success(resp)
    
    words = []
    for word in resp['result']['text']:
        words.append(word['data'])

    return words