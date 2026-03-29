import React, { useState, useEffect } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const codespace_name = process.env.REACT_APP_CODESPACE_NAME;
    const base_url = codespace_name
      ? `https://${codespace_name}-8000.app.github.dev`
      : 'http://localhost:8000';

    fetch(`${base_url}/api/activities/`)
      .then(response => response.json())
      .then(data => {
        console.log('Activities data:', data);
        setActivities(Array.isArray(data) ? data : data.results || []);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching activities:', err);
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="text-center"><div className="spinner-border" role="status"></div></div>;
  if (error) return <div className="alert alert-danger">Error: {error}</div>;

  return (
    <div>
      <h2 className="mb-4">Activities</h2>
      <table className="table table-striped table-hover">
        <thead className="table-dark">
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Duration (minutes)</th>
            <th>Schedule</th>
            <th>Max Attendance</th>
          </tr>
        </thead>
        <tbody>
          {activities.map((activity, index) => (
            <tr key={activity._id || index}>
              <td><strong>{activity.name}</strong></td>
              <td>{activity.description}</td>
              <td>{activity.duration_minutes}</td>
              <td>{activity.schedule}</td>
              <td>{activity.max_attendance}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Activities;
