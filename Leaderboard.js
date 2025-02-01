import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

function Leaderboard() {
  const leaderboardData = [
    { rank: 1, name: "Alice Johnson", score: 980 },
    { rank: 2, name: "Bob Smith", score: 920 },
    { rank: 3, name: "Charlie Brown", score: 890 },
  ];

  return (
    <div className="container mt-5">
      <h2 className="text-center text-primary">🏆 Leaderboard</h2>
      <table className="table table-striped table-hover mt-3">
        <thead className="table-dark">
          <tr>
            <th>Rank</th>
            <th>Name</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {leaderboardData.map((user, index) => (
            <tr key={index}>
              <td>{user.rank}</td>
              <td>{user.name}</td>
              <td>{user.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;
