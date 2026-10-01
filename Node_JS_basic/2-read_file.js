const fs = require('fs');

function countStudents(path) {
  if (!fs.existsSync(path)) {
    throw new Error('Cannot load the database');
  }

  let content;
  try {
    content = fs.readFileSync(path, 'utf-8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  const lines = content.trim().split('\n').filter((line) => line.trim().length > 0);

  if (lines.length <= 1) {
    console.log('Number of students: 0');
    return;
  }

  const students = lines.slice(1);
  console.log(`Number of students: ${students.length}`);

  const fields = {};

  students.forEach((student) => {
    const parts = student.split(',');
    if (parts.length >= 4) {
      const firstname = parts[0].trim();
      const field = parts[3].trim();

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    }
  });

  for (const [field, names] of Object.entries(fields)) {
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  }
}

module.exports = countStudents;
