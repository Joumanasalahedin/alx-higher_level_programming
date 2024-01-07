#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, todos) {
  if (error == null) {
    const data = JSON.parse(todos);
    const completedTasks = {};

    data.forEach(todo => {
      if (todo.completed) {
        if (!completedTasks[todo.userId]) {
          completedTasks[todo.userId] = 0;
        }
        completedTasks[todo.userId]++;
      }
    });

    console.log(completedTasks);
  }
});
