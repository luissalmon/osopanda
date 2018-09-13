var initial = 0;
var interval;
var sectionLeft,
    sectionRight,
    bgSectionL,
    bgSectionR;

var running = false,
    runningBg = false;

var animSpeed = 400,
    bgSpeed = 250;

var initialY, 
    initialBgY;
    
resize();
window.addEventListener("resize", resize);

function alerta() {
  counter = 0;
  console.log('entro');
  
  var inter = setInterval(displayAlert, 200);
  function displayAlert() {
    if(c === 3) {
      clearInterval(inter)
      alert('hola');
    } else {
      counter++;
    }
  }
}

function resize() {
  var data = document.getElementById('imgLS').getBoundingClientRect();
  adjustHeight('bgSectL');
  adjustHeight('bgSectR');
  adjustHeight('areaL');
  adjustHeight('areaR');
  adjustFontSize('bgPL');
  adjustFontSize('bgPR');

  function adjustHeight(id) {
    document.getElementById(id).style.height = `${data.height}px`;
  }

  function adjustFontSize(id) {
    var fontsize = data.width * 0.03;
    document.getElementById(id).style.fontSize = `${fontsize}px`;
  }
}

function actionArea(id, action) {
  var el = document.getElementById(id);
  this.counter = new countDown(el);
  if (action === 'start') {
    counter.startTimer();
  } else {
    counter.stopTimer();
  }
};

function countDown(el) {
  var anim = new animation(el);
  this.startTimer = function() {
    initial = 0;
    interval = setInterval(start, 200);
    function start() {
      if (initial === 1) {
        clearInterval(interval);
        if (!running) {
          anim.start();
        }
      } else {
        initial ++;
      }
    }
  }

  this.stopTimer = function() {
    clearInterval(interval);
    if (running) {
      anim.stop();
    }
  };
}

function animation(el) {
  var bgAnim = new bgAnimation(el);
  var id = el.id;
  this.start = function() {
    running = true;
    var frame = [
    { transform: 'rotate(0) translateY(0px)', opacity: 1, },
    { transform: 'rotate(0) translateY(50%)', opacity: 1, }];
    var options = {
      duration: animSpeed,
      fill: 'forwards',
      iterations: 1,
    };
    initialY = el.getBoundingClientRect().top;
    if (id === 'imgL') {
      sectionLeft = el.animate(frame, options);
      sectionLeft.onfinish = function() {
        bgAnim.start('bgSectL');
      }
      
    } else {
      sectionRight = el.animate(frame, options);
      sectionRight.onfinish = function() {
        bgAnim.start('bgSectR');
      }
    } 
  }

  this.stop = function() {
    var axisY = changedPos(el, initialY);
    
    running = false;
    var frame = [
    { transform: `rotate(0) translateY(${axisY}px)`, opacity: 1, },
    { transform: 'rotate(0) translateY(0px)', opacity: 1, }];
    var options = {
      duration: backSpeed(axisY, animSpeed),
      fill: 'forwards',
      iterations: 1,
    }
    if (id === 'imgL') {
      if (runningBg) {
        bgAnim.stop('bgSectL',() => {
          sectionLeft = el.animate(frame, options);
        });
      } else {
        sectionLeft.pause();
        sectionLeft = el.animate(frame, options);
      }
    } else {
      if (runningBg) {
        bgAnim.stop('bgSectR',() => {
          sectionRight = el.animate(frame, options);
        });
      } else {
        sectionRight.pause();
        sectionRight = el.animate(frame, options);
      }
    }
  }
}

function bgAnimation() {

  this.start = function(id) {
    var el = document.getElementById(id);
    runningBg = true;

    var frame = [
    { transform: 'rotate(0) translateY(30%)', opacity: 0 },
    { transform: 'rotate(0) translateY(0px)', opacity: 1 },
    ];
    var options = {
      duration: bgSpeed,
      fill: 'forwards',
      iterations: 1,
    };
    initialBgY = el.getBoundingClientRect().top;
    if (id === 'bgSectL') {
      bgSectionL = el.animate(frame, options);
      bgSectionL.onfinish = function() {
        console.log('entro');
        
        this.alerta();
      }
    } else {
      bgSectionR = el.animate(frame, options);
      bgSectionR.onfinish = function() {
        console.log('entro');
        
        this.alerta();
      }
    }
  }

  this.stop = function(id, a) {
    runningBg = false;
    var el = document.getElementById(id);
    var axisY = changedPos(el, initialBgY);
    var speed = backSpeed(axisY, bgSpeed);

    var frame = [
    { transform: 'rotate(0) translateY(0px)', opacity: 1, },
    { transform: `rotate(0) translateY(${axisY === 0 ? '30%' : `${axisY}px`})`, opacity: 0, },
    { transform: 'rotate(0) translateY(0px)', opacity: 0, },
    ];
    var options = {
      duration: speed === 0 ? bgSpeed : speed,
      fill: 'forwards',
      iterations: 1,
    };

    if (id === 'bgSectL') {
      bgSectionL = el.animate(frame, options);
      bgSectionL.onfinish = function() {
        a();
      };
    } else {
      bgSectionR = el.animate(frame, options);
      bgSectionR.onfinish = function() {
        a();
      };
    }
  }
}

function changedPos(e, i) {
  var currentY = e.getBoundingClientRect().top;
  return currentY - i;
}

function backSpeed(currentY, duration) {
  if(currentY === 0) return 0;

  return currentY * (duration/currentY);
}

function showBtn(el) {
  console.log('entro');
  
  var show = document.getElementById('showSection');
  this.hideShow(show);

  var to = el.getAttribute("to"),
      page = document.getElementById(to);
  var showEl = this.hideShow(page);
  if (showEl === 'show') {
    var elY = page.getBoundingClientRect().top;
    this.doScrolling(elY, 400);
  }
}


function hideShow(el) {
  var id = el.getAttribute('id');
  var len = el.classList.length;
  var added = false;

  for (let index = 0; index < len; index++) {
    if (el.classList[index] === 'd-none') {
      added = true;
      if (id === 'info') {
        el.classList.replace('d-none', 'd-flex');
      } else {
        el.classList.replace('d-none', 'd-block');
      }
      return 'show';
    } else if (el.classList[index] === 'd-block') {
      added = true;
      el.classList.replace('d-block', 'd-none');
      return 'hide';
    } else {
      added = false;
    }
  }
  if (!added) el.classList.add('d-none');
  return 'hide';
}

function doScrolling(elementY, duration) {
  var startingY = window.pageXOffset;
  var diff = elementY;
  var start;
  window.requestAnimationFrame(function step(timestamp) {
    if (!start) start = timestamp;
    var time = timestamp - start;
    var percent = Math.min(time / duration, 1);

    window.scrollTo(0, startingY + diff * percent);
    if (time < duration) {
      window.requestAnimationFrame(step);
    }
  });
};