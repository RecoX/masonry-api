import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from instagrapi import Client

load_dotenv()
app = Flask(__name__)

cl = Client()
cl.login(os.environ.get('EMAIL'), os.environ.get('EMAIL_PASSWORD'))

@app.route('/getInstagramMediaByUsername/<username>/<quantity>', methods=['GET'])
def get_instagram_media(username, quantity):
    # try:
        user_id = cl.user_id_from_username(username)
        medias = cl.user_medias(user_id, quantity)
        images_urls = []
        # Convert each Media object into a dictionary
        for item in medias:
            if item.thumbnail_url:
                images_urls.append(item.thumbnail_url)
        
        return jsonify(images_urls)
        
    # except:
        # print("Exception thrown. x does not exist.")
        # return "Error Nene"

if __name__ == '__main__':
    app.run()
