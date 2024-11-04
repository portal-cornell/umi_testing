import cv2

# print("Available camera devices:")
for i in range(20):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        # print(f"Camera device {i} is available")
        # Attempt to read a frame to check if it's the Elgato HD60x
        ret, frame = cap.read()
        if ret:
            print("i", i)
            print(f"Successfully read from camera device")
            # Display the frame (optional)
            cv2.imshow(f"Camera device", frame)
            cv2.waitKey(5000)  # Display the frame for 1 second
            cv2.destroyAllWindows()
        cap.release()
# breakpoint()
# import cv2

# cap = cv2.VideoCapture(1)
# if cap.isOpened():
#     print("success")
# else:
#     print("failed")
# cap.release()

import cv2

# Change this to the index of your camera (2 or 3 based on your previous output)
camera_index = 3

# Open the camera
cap = cv2.VideoCapture(camera_index)
# breakpoint()
if not cap.isOpened():
    print(f"Error: Camera {camera_index} could not be opened.")
else:
    print(f"Camera {camera_index} is opened successfully.")

# cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# # Search for a connected camera
# camera_index = find_camera_index()

# if camera_index is not None:
#     print(f"Using camera device {camera_index}")
# else:
#     print("No camera device found")

while True:
    ret, frame = cap.read()
    if not ret:
        # print("Error: Frame not captured.")
        continue

    # Display the frame
    cv2.imshow(f'Camera {camera_index}', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()


# import cv2

# def find_camera_index(max_index=10):
#     for i in range(max_index):
#         cap = cv2.VideoCapture(i)
#         if cap.isOpened():
#             ret, frame = cap.read()
#             if ret:
#                 print(f"Camera device {i} is available and working")
#                 cap.release()
#                 return i
#             cap.release()
#     print("No working camera device found")
#     return None

# # Search for a connected camera
# camera_index = find_camera_index()

# if camera_index is not None:
#     print(f"Using camera device {camera_index}")
# else:
#     print("No camera device found")