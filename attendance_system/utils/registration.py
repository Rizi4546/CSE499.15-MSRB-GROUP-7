import cv2
import face_recognition
import numpy as np
from database.db_manager import add_student

def register_student(student_id, name, num_samples=10):
    """Capture face samples and store averaged embedding"""
    cap = cv2.VideoCapture(0)
    embeddings = []
    samples_collected = 0
    
    print(f"Registering {name} ({student_id})...")
    print("Look at the camera. Press 'c' to capture, 'q' to quit")
    
    while samples_collected < num_samples:
        ret, frame = cap.read()
        if not ret:
            continue
            
        # Detect faces
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        
        # Draw rectangle
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, f"Samples: {samples_collected}/{num_samples}", 
                       (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow("Registration", frame)
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('c') and len(face_locations) == 1:
            # Extract embedding
            encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
            embeddings.append(encoding)
            samples_collected += 1
            print(f"  Sample {samples_collected} captured")
            
        elif key == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    if len(embeddings) > 0:
        # Average all embeddings
        avg_embedding = np.mean(embeddings, axis=0)
        add_student(student_id, name, avg_embedding)
        print(f"✓ {name} registered successfully with {len(embeddings)} samples!")
        return True
    else:
        print("✗ No samples captured")
        return False

if __name__ == "__main__":
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    register_student(sid, name, num_samples=10)