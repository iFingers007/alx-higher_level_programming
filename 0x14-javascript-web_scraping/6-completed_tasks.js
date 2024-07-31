#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

if (!url) {
  console.error('Error: Provide url and file path');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }
  if (response.statuscode !== 200) {
    console.log('Failed to fecth data:', response.statuscode);
    return;
  }
  try {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (!completedTasks[task.userId]) {
          completedTasks[task.userId] = 0;
        }
        completedTasks[task.userId]++;
      }
    });

    console.log(completedTasks);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
