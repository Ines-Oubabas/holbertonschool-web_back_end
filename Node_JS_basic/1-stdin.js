process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.setEncoding('utf8');  // S'assurer que les données sont en UTF-8

process.stdin.on('data', (input) => {
  const name = input.trim();  // Supprimer les espaces et les retours à la ligne

  if (name) {  // Si un nom a été entré
    process.stdout.write(`Your name is: ${name}\n`);
    process.stdout.write('This important software is now closing\n');
    process.exit();  // Fermer le programme proprement après l'affichage
  }
});
