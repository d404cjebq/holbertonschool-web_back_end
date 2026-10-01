import fs from 'fs';

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data
        .toString('utf-8')
        .split('\n')
        .map((line) => line.trim())
        .filter((line) => line.length > 0);
      const students = {};
      for (let i = 1; i < lines.length; i += 1) {
        const [firstname, , , field] = lines[i].split(',');
        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      }
      resolve(students);
    });
  });
}

export default readDatabase;
