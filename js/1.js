var dark = 'background-color:black; color:white;';
var day  = 'background-color:white; color:black;';

var button = document.querySelector('.nav');
var web = document.querySelector('body');

function lightSwitch(){
  if (web.style.cssText == dark) {
    web.style.cssText = day;
    alert('Day Mode');
  } else {
    web.style.cssText = dark;
    alert('Night Mode');
  }
}

button.onclick = lightSwitch
