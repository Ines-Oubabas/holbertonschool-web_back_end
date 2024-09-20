const fs = require('fs');

function countStudents(path) {
  try {
    // Vérifier si le fichier existe
    if (!fs.existsSync(path)) {
      throw new Error('Cannot load the database');
    }

    // Lire le fichier de manière synchrone
    const data = fs.readFileSync(path, 'utf8').trim();

    if (!data) {
      throw new Error('Cannot load the database');
    }

    // Diviser les lignes du fichier
    const lines = data.split('\n').filter(line => line.trim() !== ''); // Ignorer les lignes vides
    const students = lines.slice(1); // Enlever l'en-tête

    if (students.length === 0) {
      throw new Error('Cannot load the database');
    }

    console.log(`Number of students: ${students.length}`);

    // Organiser les étudiants par domaine
    const fields = {};

    students.forEach((line) => {
      const [firstname, lastname, age, field] = line.split(',');

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    // Afficher les résultats par domaine
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (err) {
    console.error(err.message); // Afficher le message d'erreur exact
  }
}

module.exports = countStudents;

