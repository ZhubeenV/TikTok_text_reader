import cv2
from pytesseract import pytesseract 

video_url = "https://www.tiktok.com/@whatliameats/video/7458728631934782762?_d=secCgYIASAHKAESPgo8G9nmq7ZyEFkn0Ql5Tql2ouiWhDSCMYjQIm17jzzDQfjUaydFBGGDddvHhH%2BTihIvzlrsA8Rhj879KZUfGgA%3D&_r=1&checksum=e03bc339b30d3d1b3de6e59e08bc1acd6a27f2ba1e5450646f20580d93cd86a4&language=en&sec_user_id=MS4wLjABAAAA9t812yzu4c8k0-o9H11uj6X4ftXu-Ey6HrV88hpg1UeQvM1bchOzyMP7OEEmnux6&share_app_id=1233&share_link_id=9C42D23B-5FD8-4172-8E9E-469CF1932ABC&social_share_type=24&timestamp=1737316190&tt_from=sms&u_code=d772jliihiakd9&ug_btm=b0%2Cb0&user_id=6712663528023393286&utm_campaign=client_share&utm_medium=ios&utm_source=sms"  # Could be a local file or a stream URL
cap = cv2.VideoCapture(video_url)

frame_interval = 30  # Process every 30th frame (adjust as needed)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    text = pytesseract.image_to_string(frame)
    print("Detected text:", text)
    # Process frame (e.g., pass it to an OCR model)
    # For example, save or analyze every nth frame
    if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) % frame_interval == 0:
        # Do something with the frame, like feed to ML model
        print("Processing frame...")

cap.release()
cv2.destroyAllWindows()
