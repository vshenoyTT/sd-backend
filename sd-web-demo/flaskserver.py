from flask import Flask, request, jsonify, send_from_directory, send_file, send_from_directory
import json
import os
import atexit

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    prompt = data.get('prompt')
    print(prompt)

    json_file_path = 'models/demos/wormhole/stable_diffusion/demo/web_demo/input_prompts.json'

    if not os.path.isfile(json_file_path):
        with open(json_file_path, 'w') as f:
            json.dump({"prompts": []}, f)

    with open(json_file_path, 'r') as f:
        prompts_data = json.load(f)

    prompts_data['prompts'].append({"prompt": prompt, "status": "not generated"})

    with open(json_file_path, 'w') as f:
        json.dump(prompts_data, f, indent=4)

    return jsonify({"message": "Prompt received and added to queue."})

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.get_json()
    prompt = data.get('prompt')

    json_file_path = 'models/demos/wormhole/stable_diffusion/demo/web_demo/input_prompts.json'

    with open(json_file_path, 'r') as f:
        prompts_data = json.load(f)

    for p in prompts_data['prompts']:
        if p['prompt'] == prompt:
            p['status'] = "generated"
            break

    with open(json_file_path, 'w') as f:
        json.dump(prompts_data, f, indent=4)

    return jsonify({"message": "Prompt status updated to generated."})

@app.route('/get_image', methods=['GET'])
def get_image():
    image_name = 'interactive_512x512_ttnn.png'
    directory = os.getcwd()  # Get the current working directory
    return send_from_directory(directory, image_name)

@app.route('/image_exists', methods=['GET'])
def image_exists():
    image_path = 'interactive_512x512_ttnn.png'
    if os.path.isfile(image_path):
        return jsonify({"exists": True}), 200
    else:
        return jsonify({"exists": False}), 200

@app.route('/clean_up', methods=['POST'])
def clean_up():
    json_file_path = 'models/demos/wormhole/stable_diffusion/demo/web_demo/input_prompts.json'

    with open(json_file_path, 'r') as f:
        prompts_data = json.load(f)

    prompts_data['prompts'] = [p for p in prompts_data['prompts'] if p['status'] != 'done']

    with open(json_file_path, 'w') as f:
        json.dump(prompts_data, f, indent=4)

    return jsonify({"message": "Cleaned up done prompts."})

def cleanup():
    if os.path.isfile("models/demos/wormhole/stable_diffusion/demo/web_demo/input_prompts.json"):
        os.remove("models/demos/wormhole/stable_diffusion/demo/web_demo/input_prompts.json")
        print(f"Deleted json")

    if os.path.isfile("interactive_512x512_ttnn.png"):
        os.remove("interactive_512x512_ttnn.png")
        print(f"Deleted image")

atexit.register(cleanup)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
