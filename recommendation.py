import os
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import LabelEncoder
from dashboard.models import Course, Progress, UserProfile
from django.contrib.auth.models import User

# Collaborative Filtering Model
class CourseRecommender(nn.Module):
    def __init__(self, num_users, num_courses, embed_size=50):
        super(CourseRecommender, self).__init__()
        self.user_embed = nn.Embedding(num_users, embed_size)
        self.course_embed = nn.Embedding(num_courses, embed_size)
        self.fc = nn.Linear(embed_size, 1)

    def forward(self, user, course):
        user_embedding = self.user_embed(user)
        course_embedding = self.course_embed(course)
        interaction = user_embedding * course_embedding
        output = self.fc(interaction)
        return output

# Train the Model
def train_model():
    progress_data = list(Progress.objects.values('user', 'course', 'progress'))

    if not progress_data:
        print("❌ No data available for training!")
        return None

    # Ensure 'ml/' directory exists
    if not os.path.exists('ml'):
        os.makedirs('ml')

    df = pd.DataFrame(progress_data)

    # Remap IDs to start from 0
    user_encoder = LabelEncoder()
    df['user'] = user_encoder.fit_transform(df['user'])

    course_encoder = LabelEncoder()
    df['course'] = course_encoder.fit_transform(df['course'])

    num_users = df['user'].nunique()
    num_courses = df['course'].nunique()

    print(f"🔄 Training model with {num_users} users and {num_courses} courses")

    model = CourseRecommender(num_users, num_courses)
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.MSELoss()

    # Prepare training data
    user_tensor = torch.tensor(df['user'].values, dtype=torch.long)
    course_tensor = torch.tensor(df['course'].values, dtype=torch.long)
    progress_tensor = torch.tensor(df['progress'].values, dtype=torch.float32)

    # Training loop
    for epoch in range(100):
        optimizer.zero_grad()
        predictions = model(user_tensor, course_tensor).squeeze()
        loss = criterion(predictions, progress_tensor)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            print(f"✅ Epoch {epoch}: Loss = {loss.item()}")

    # 🗑️ Remove old model if it exists
    model_path = 'ml/course_recommender.pth'
    if os.path.exists(model_path):
        os.remove(model_path)
        print("🗑️ Removed old model file.")

    # 🎉 Save new model
    torch.save(model.state_dict(), model_path)
    print(f"🎉 New model saved successfully at {model_path}!")

    return model