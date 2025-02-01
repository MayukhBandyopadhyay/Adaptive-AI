from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Progress
from .serializers import CourseSerializer, ProgressSerializer
from .services import get_recommendations

class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch user progress
        progress_data = Progress.objects.filter(user=request.user)
        progress_serializer = ProgressSerializer(progress_data, many=True)

        # Get AI-based recommendations
        recommended_courses = get_recommendations(request.user)
        course_serializer = CourseSerializer(recommended_courses, many=True)

        return Response({
            "progress": progress_serializer.data,
            "recommended_courses": course_serializer.data
        })
