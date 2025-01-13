try:
    from googleapiclient.discovery import build
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
except ModuleNotFoundError as e:
    print("Required modules are missing. Please install them using:\n\n    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client\n")
    exit(1)

import pickle
import os

# Define scopes for YouTube Data API
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def authenticate_youtube():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build("youtube", "v3", credentials=creds)

def get_uploaded_videos(youtube):
    request = youtube.channels().list(part="contentDetails", mine=True)
    response = request.execute()
    uploads_playlist_id = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    
    videos = []
    next_page_token = None
    while True:
        playlist_request = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        playlist_response = playlist_request.execute()
        
        for item in playlist_response["items"]:
            video_id = item["snippet"]["resourceId"]["videoId"]
            videos.append(video_id)
        
        next_page_token = playlist_response.get("nextPageToken")
        if not next_page_token:
            break
    return videos

def update_video_description(youtube, video_id, old_text, new_text):
    video_request = youtube.videos().list(part="snippet", id=video_id)
    video_response = video_request.execute()
    
    if video_response["items"]:
        video = video_response["items"][0]
        description = video["snippet"].get("description", "")
        
        if old_text in description:
            updated_description = description.replace(old_text, new_text)
            video["snippet"]["description"] = updated_description
            
            update_request = youtube.videos().update(
                part="snippet",
                body={
                    "id": video_id,
                    "snippet": video["snippet"]
                }
            )
            update_request.execute()
            print(f"Updated video ID {video_id}")
        else:
            print(f"No matching text found in video ID {video_id}")

def main():
    old_text = "some_text"
    new_text = "replace_with_new_text"
    
    youtube = authenticate_youtube()
    videos = get_uploaded_videos(youtube)
    
    for video_id in videos:
        update_video_description(youtube, video_id, old_text, new_text)

if __name__ == "__main__":
    main()