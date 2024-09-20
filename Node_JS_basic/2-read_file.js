const fs = require('fs');

function countStudents(path) {
    try {
        if (!fs.existsSync(path)) {
            throw new Error('Cannot load the database');
        }
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.split('\n');

        const students = lines.filter(line => line.trim() !== '' && !line.startsWith('firstname'));

        console.log(`Number of students: ${students.length}`);

        const fields = {};

        students.forEach(student => {
            const [firstname, , , field] = student.split(',');
            if (!fields[field]) fields[field] = [];
            fields[field].push(firstname);
        });

        for (const [field, names] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }
    } catch (error) {
        console.error('Error reading file at path: ${path}');
        throw new Error('Cannot load the database');
    }
}

module.exports = countStudents;
