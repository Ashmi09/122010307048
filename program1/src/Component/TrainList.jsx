import React, { useState, useEffect } from 'react';

const TrainList = () => {
  const [trains, setTrains] = useState([]);

  useEffect(() => {
    
    fetch('http://20.244.56.144:80/train/trains')
      .then(response => response.json())
      .then(data => setTrains(data))
      .catch(error => console.error('Error fetching trains:', error));
  }, []);

  return (
    <div>
      <h2>Available Trains</h2>
      <ul>
        {trains.map(train => (
          <li key={train.id}>
            Train Name: {train.trainName}, Train Number : {train.trainNumber}, Departure Time : {train.DepartureTime}, seats Available : {train.seatsAvailable}, Price : {train.price}, Delayed By : {train.delayedBy}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TrainList;