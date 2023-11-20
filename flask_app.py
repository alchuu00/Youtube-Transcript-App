from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

def get_youtube_transcription(url):
    video_id = url.replace("https://www.youtube.com/watch?v=", "")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        output = ' '.join([sentence['text'] for sentence in transcript])
        return output, None  # Return transcription and no error
    except Exception as e:
        print(f"Error retrieving transcript: {e}")
        return None, "Error retrieving transcription. Please try again."

@app.route('/', methods=['GET', 'POST'])
def index():
    transcription, error = None, None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            transcription, error = get_youtube_transcription(url)
        else:
            error = "No URL provided."
    
    return render_template('index.html', transcription=transcription, error=error)

if __name__ == '__main__':
    app.run(debug=True)
