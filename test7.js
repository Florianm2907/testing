const string = "SQNLPZWYVNYLZZ"
const steps = 100000

let step = -steps
let value = string

function forward() {
  const i = (((step + 1) % string.length) + string.length) % string.length
  const chars = value.split('')
  chars[i] = String.fromCharCode(65 + ((chars[i].charCodeAt(0) - 65 + 1) % 26))
  value = chars.join('')
  step++
  //console.log('forward to', value)
  return value
}

function work(noTimeout) {
  if (step >= 0) {
    // bar.style.width = '100%'
  } else {
     // do nothing
    if (!noTimeout) {
      setTimeout(work, 0)
    }
  }
}
setTimeout(work, 0)
for(let i = 0; i < steps; i++){
    console.log(forward())
}