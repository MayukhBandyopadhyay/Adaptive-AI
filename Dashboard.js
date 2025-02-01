import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';
import { Container, Card, Spinner, Table, ListGroup } from 'react-bootstrap';

function Dashboard() {
    const [progress, setProgress] = useState([]);
    const [recommendedCourses, setRecommendedCourses] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/dashboard/', {
            headers: { 'Authorization': 'Token 0708531540cb46290b1e54cecdb56425dd2a3806' }
        })
        .then(response => {
            console.log("API Response:", response.data);
            setProgress(response.data.progress);
            setRecommendedCourses(response.data.recommended_courses);
            setLoading(false);
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            setLoading(false);
        });
    }, []);

    if (loading) {
        return (
            <Container className="text-center mt-5">
                <Spinner animation="border" variant="primary" />
                <h2>Loading...</h2>
            </Container>
        );
    }

    if (!progress.length && !recommendedCourses.length) {
        return (
            <Container className="text-center mt-5">
                <h2 className="text-danger">❌ No data available. Check API or login again.</h2>
            </Container>
        );
    }

    const progressData = progress.map(p => ({
        name: p.course.title,
        progress: p.progress
    }));

    return (
        <Container className="mt-4">
            <Card className="p-4 shadow">
                <h1 className="text-center mb-4">📊 Student Dashboard</h1>

                {/* Progress Overview */}
                <h2 className="mt-4 text-primary">Progress Overview</h2>
                {progress.length > 0 ? (
                    <ResponsiveContainer width="100%" height={300}>
                        <BarChart data={progressData}>
                            <XAxis dataKey="name" />
                            <YAxis />
                            <Tooltip />
                            <Bar dataKey="progress" fill="#007bff" />
                        </BarChart>
                    </ResponsiveContainer>
                ) : (
                    <p className="text-muted">No progress data available.</p>
                )}

                {/* Recommended Courses */}
                <h2 className="mt-4 text-success">Recommended Courses</h2>
                {recommendedCourses.length > 0 ? (
                    <ListGroup>
                        {recommendedCourses.map((course, index) => (
                            <ListGroup.Item key={index}>
                                {course.title} - <span className="text-warning">{course.difficulty}</span>
                            </ListGroup.Item>
                        ))}
                    </ListGroup>
                ) : (
                    <p className="text-muted">No recommended courses available.</p>
                )}
            </Card>
        </Container>
    );
}

export default Dashboard;
