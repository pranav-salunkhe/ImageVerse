import time
from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import subprocess
import shutil
import requests

app = Flask(__name__, static_folder='static')

UPLOAD_FOLDER_CONTENT = 'content_dir'
UPLOAD_FOLDER_STYLE = 'style_dir'
STYLIZED_FOLDER = 'test_results/comm/stylized_results'


app.config['UPLOAD_FOLDER_CONTENT'] = UPLOAD_FOLDER_CONTENT
app.config['UPLOAD_FOLDER_STYLE'] = UPLOAD_FOLDER_STYLE
app.config['STYLIZED_FOLDER'] = STYLIZED_FOLDER


def save_image(file, folder, filename):
    file_path = os.path.join(app.config[folder], filename)
    file.save(file_path)
# 
def run_style_transfer(content_dir, style_dir):
    command = [
        'python3', 'main.py',
        '--type', 'test',
        '--batch_size', '1',
        '--comment', 'comm',
        '--content_dir', content_dir,
        '--style_dir', style_dir,
        '--num_workers', '1'
    ]
    subprocess.run(command)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        content_image = request.files['content_image']
        style_image = request.files['style_image']

        if content_image and style_image:
            save_image(content_image, 'UPLOAD_FOLDER_CONTENT', 'ci.jpg')
            save_image(style_image, 'UPLOAD_FOLDER_STYLE', 'si.jpg')

            run_style_transfer(UPLOAD_FOLDER_CONTENT, UPLOAD_FOLDER_STYLE)
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

    return jsonify({'status': 'success', 'message': 'Images uploaded successfully'})

@app.route('/text-submit', methods=['POST'])
def text_submit():
    try:
        # Get input prompts from the request
        content_image_text = request.form.get('input1')
        style_image_text = request.form.get('input2')
        print("CIT: ",content_image_text)
        if not content_image_text or not style_image_text:
            return jsonify({'status': 'error', 'message': 'Both prompts are required.'}), 400

        # Define the Prodia API URL and headers
        prodia_url = "https://api.prodia.com/v1/sd/generate"
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "X-Prodia-Key": "86854128-348f-4cb4-b03f-819dd08862fe"  # Replace with your Prodia API key
        }

        # Helper function to generate and download image
        def generate_and_download_image(prompt, save_path):
            payload = {
                "model": "elldreths-vivid-mix.safetensors [342d9d26]",
                "prompt": prompt
                }
            response = requests.post(prodia_url, json=payload, headers=headers)
            response_data = response.json()

            # Check for job creation success
            if 'job' not in response_data:
                raise Exception("Failed to create Prodia generation job.")

            job_id = response_data['job']
            job_url = f"https://api.prodia.com/v1/job/{job_id}"

            # Poll for the job result
            while True:
                job_response = requests.get(job_url, headers=headers).json()
                print("in")
                if job_response.get('status') == 'succeeded':
                    image_url = job_response.get('imageUrl')
                    if not image_url:
                        raise Exception("Image URL not found in job response.")

                    # Download the image
                    image_response = requests.get(image_url)
                    if image_response.status_code == 200:
                        with open(save_path, 'wb') as file:
                            file.write(image_response.content)
                        return
                    else:
                        raise Exception("Failed to download the generated image.")
                elif job_response.get('status') == 'failed':
                    raise Exception("Prodia generation job failed.")
                # Add a short delay to prevent rapid polling
                time.sleep(1)

        # Generate and save the content and style images
        generate_and_download_image(content_image_text, UPLOAD_FOLDER_CONTENT+'/ci.jpg')
        print("between")
        generate_and_download_image(style_image_text, UPLOAD_FOLDER_STYLE+'/si.jpg')

        # Run the style transfer
        run_style_transfer(UPLOAD_FOLDER_CONTENT, UPLOAD_FOLDER_STYLE)

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

    return jsonify({'status': 'success', 'message': 'Images generated and style transfer completed successfully'})


@app.route('/stylized')
def stylized():
    stylized_image_path = os.path.join(app.config['STYLIZED_FOLDER'], 'single_art_stylized.png')
    static_image_path = os.path.join(app.root_path, 'static', 'single_art_stylized.png')  # Construct path within static folder

    try:
        shutil.copyfile(stylized_image_path, static_image_path)  # Copy the image
    except Exception as e:
        print(f"Error copying image: {e}")
    print(static_image_path)
    return render_template('stylized.html', static_image_path=static_image_path)
    # print(stylized_image_path)
    # print("\n")
    # print(os.path.dirname(stylized_image_path))
    # print("\n")
    # print(os.path.basename(stylized_image_path))
    # send_from_directory(os.path.dirname(stylized_image_path), os.path.basename(stylized_image_path))
    return render_template('stylized.html', stylized_image_path=stylized_image_path)

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/text')
def text():
    return render_template('text.html')


if __name__ == '__main__':
    app.run(debug=True)
