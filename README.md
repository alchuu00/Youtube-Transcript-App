# Youtube Transcript App
This is a simple Flask application that extracts transcripts from YouTube videos using the youtube_transcript_api.

## Functionality
The application defines a single route (/) that responds to both GET and POST requests.

For GET requests, it simply renders the index page.
For POST requests, it expects a form field named ‘url’ containing the URL of a YouTube video. It then attempts to fetch the transcript of the video using the youtube_transcript_api and displays it on the page.

## Error Handling
If an error occurs while fetching the transcript (for example, if the video does not have a transcript), the application will catch the exception and display an error message.

## API used
youtube-transcript-api: https://github.com/jdepoix/youtube-transcript-api
