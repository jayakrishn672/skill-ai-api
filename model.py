
from supabase_client import supabase

def detect_skill(video_url):
    # Dummy example logic for now
    return "Java" if "java" in video_url.lower() else "Video Editing"

def match_skills(offered, wanted):
    response = supabase.table("users").select("*").execute()
    users = response.data or []
    matches = [
        user for user in users
        if user.get("teaches", "").lower() == wanted.lower() and user.get("learns", "").lower() == offered.lower()
    ]
    return matches
