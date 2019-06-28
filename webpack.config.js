const path = require('path');

module.exports = {
  entry: {
    chatroom: './src/chatroom.js',
    homepage: './src/homepage.js'
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'static/js/')
  },
  watch: true,
  watchOptions: {
    ignored: ['../main.py', 'node_modules']
  }
};