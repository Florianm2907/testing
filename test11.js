const robot = require('robotjs');
const ioHook = require('iohook');
const sleep = (milliseconds) => new Promise(resolve => setTimeout(resolve, milliseconds));

// Wartezeit, um genügend Zeit zum Wechseln des Fokus auf das Zielprogramm zu haben
const delay = 5000;

// Flag zum Stoppen des Programms
let stopFlag = false;

// Wartezeit am Ende des Programms
const endDelay = 5000;

// Funktion zum Stoppen des Programms
function stopProgram() {
  console.log("Programm gestoppt.");
  stopFlag = true;
  ioHook.stop();
}

// Abfangen des Tastendrucks auf "A"
ioHook.on('keydown', event => {
  if (String.fromCharCode(event.keychar) === 'A') {
    stopProgram();
  }
});

// Wartezeit, bevor das Programm startet
async function run() {
  await sleep(delay);

  // Bildschirmauflösung abrufen
  const screen = robot.getScreenSize();
  const screenWidth = screen.width;
  const screenHeight = screen.height;

  // Schleife durch jeden Pixel und klicke darauf
  for (let x = 0; x < screenWidth && !stopFlag; x++) {
    for (let y = 0; y < screenHeight && !stopFlag; y++) {
      robot.moveMouse(x, y);
      robot.mouseClick();
    }
  }

  // Optional: Wartezeit am Ende, um den Abschluss zu sehen (kann entfernt werden)
  await sleep(endDelay);
}

// Starte das Programm
run();

// Starte den ioHook
ioHook.start();

// Wartezeit für das Programmende, bevor das ioHook gestoppt wird
setTimeout(() => {
  ioHook.stop();
}, endDelay);
