import os
import torch
import pandas as pd
import numpy as np
from dashboard.models import Course, Progress, UserProfile
from django.contrib.auth.models import User
from .recommendation import CourseRecommender  # Import ML model

# Load trained model
def load_model():
    model_path = 'ml/course_recommender.pth'

    if not os.path.exists(model_path):
        print("❌ Model file not found! Train the model first.")
        return None  # Prevent loading if model does not exist

    # Get updated number of users and courses
    num_users = Progress.objects.values('user').distinct().count()
    num_courses = Progress.objects.values('course').distinct().count()

    print(f"🔄 Loading model with {num_users} users and {num_courses} courses")

    # Create a model with updated dimensions
    model = CourseRecommender(num_users, num_courses)

    # Load state dictionary with strict=False (Prevents errors if sizes change)
    try:
        model.load_state_dict(torch.load(model_path), strict=False)
        print("✅ Model loaded successfully!")
    except RuntimeError as e:
        print(f"❌ Model loading failed: {e}")
        return None  # Prevent crashing if loading fails

    return model

def get_recommendations(user):
    model = load_model()
    if model is None:
        print("❌ Model could not be loaded!")
        return []

    # Get user ID and clip it to valid range
    user_id = User.objects.filter(username=user.username).first().id
    max_users = Progress.objects.values('user').distinct().count()
    user_id = min(user_id, max_users - 1)  # Prevent out-of-range index

    # Get available courses
    courses = list(Course.objects.all())  # Convert QuerySet to list
    course_ids = np.array([course.id for course in courses])

    max_courses = Progress.objects.values('course').distinct().count()
    course_ids = np.clip(course_ids, 0, max_courses - 1)  # Prevent out-of-range index

    # Convert to tensors
    user_tensor = torch.tensor([user_id], dtype=torch.long)
    course_tensor = torch.tensor(course_ids, dtype=torch.long)

    # Ensure valid tensor shape
    user_tensor = user_tensor.expand(len(course_tensor))

    # Make predictions
    with torch.no_grad():
        predictions = model(user_tensor, course_tensor).squeeze().numpy()

    # Rank courses by predicted score
    sorted_indices = np.argsort(predictions)[::-1]  # Sort in descending order

    # ✅ Convert indices to Python `int` before accessing Django QuerySet
    sorted_courses = [courses[int(i)] for i in sorted_indices]

    return sorted_courses[:5]  # Return top 5 recommendations