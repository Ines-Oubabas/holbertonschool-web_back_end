const http = require('http');
const fs = require('fs');
const path = require('path');

// Function to count students from CSV
function countStudents(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                reject(new Error('Cannot load the database'));
                return;
            }

            const lines = data.split('\n').filter(line => line.trim() !== ''); // Filter empty lines
            if (lines.length <= 1) {
                reject(new Error('Database file has no valid data'));
                return;
            }

            const header = lines[0].split(',');
            const students = lines.slice(1).map(line => line.split(',')).filter(student => student.length === header.length);

            const fields = {};
            students.forEach(student => {
                const firstName = student[0];
                const field = student[student.length - 1];
                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstName);
            });

            let result = `Number of students: ${students.length}\n`;

            for (const [field, studentsList] of Object.entries(fields)) {
                result += `Number of students in ${field}: ${studentsList.length}. List: ${studentsList.join(', ')}\n`;
            }

            resolve(result.trim());
        });
    });
}

// Create the server
const app = http.createServer((req, res) => {
    if (req.url === '/') {
        res.statusCode = 200;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Hello Holberton School!\n');
    } else if (req.url === '/students') {
        const databaseFile = process.argv[2]; // Take database file path from command line arguments
        countStudents(databaseFile)
            .then((message) => {
                res.statusCode = 200;
                res.setHeader('Content-Type', 'text/plain');
                res.end(`This is the list of our students\n${message}`);
            })
            .catch((error) => {
                res.statusCode = 500;
                res.setHeader('Content-Type', 'text/plain');
                res.end(error.message);
            });
    } else {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Not Found\n');
    }
});

// Listen on port 1245
app.listen(1245, () => {
    console.log('Server listening on port 1245');
});

module.exports = app;
