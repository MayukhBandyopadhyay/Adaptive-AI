import React from "react";
import { Container, Row, Col, Button } from "react-bootstrap";

const Home = () => {
  return (
    <div className="home-page">
      {/* Hero Section */}
      <div className="hero-section text-center text-dark">
        <Container>
          <h1 className="display-3 fw-bold mt-5">🚀 Welcome to Adaptive AI</h1>
          <p className="lead">
            "AdaptiveLearn: AI-Powered Learning, Tailored for You!" 📚✨
          </p>
          <Button variant="primary" size="lg" href="/dashboard">
            Get Started
          </Button>
        </Container>
      </div>

      {/* About Section */}
      <Container className="text-center mt-5">
       <h2 className="fw-bold">🌟 Our Vision</h2>
       <p className="mx-auto" style={{ maxWidth: "700px" }}>
       At AdaptiveLearn, our vision is to revolutionize education by leveraging the power of AI-driven personalization. We aim to create an intelligent learning ecosystem that adapts to individual needs, helping learners of all backgrounds achieve their full potential.
       </p>
      </Container>

      {/* Features Section */}
      <Container className="features-section text-center mt-5 p-5 bg-light rounded">
        <h2>✨ Why Choose Adaptive AI?</h2>
        <Row className="mt-4">
          <Col md={4}>
            <i className="bi bi-chat-dots display-4 text-primary"></i>
            <h4 className="mt-3">Gamification</h4>
            <p>We utilize leaderboards, achievement badges, progress tracking, and reward points to create an interactive and competitive learning experience.</p>
          </Col>
          <Col md={4}>
            <i className="bi bi-brain display-4 text-danger"></i>
            <h4 className="mt-3">Smart AI Models</h4>
            <p>Our AI uses collaborative filtering and deep learning-based recommendation systems to analyze user progress, learning behavior, and preferences.</p>
          </Col>
          <Col md={4}>
            <i className="bi bi-globe display-4 text-success"></i>
            <h4 className="mt-3">Accessible Anywhere</h4>
            <p>Available on mobile & web.</p>
          </Col>
        </Row>
      </Container>

      {/* Business Model */}
      <Container className="text-center mt-5">
        <h2>📈 Business Model</h2>
        <p>AdaptiveLearn operates on a subscription-based SaaS model, offering AI-driven personalized learning for students, professionals, and institutions.</p>
      </Container>

      {/* Call to Action */}
      <div className="cta-section text-center text-dark mt-5 p-5">
        <Container>
          <h2>🔹 Join Us in Revolutionizing Education!</h2>
          <Button variant="success" size="lg" href="/dashboard">
            Start Now
          </Button>
        </Container>
      </div>
    </div>
  );
};

export default Home;
