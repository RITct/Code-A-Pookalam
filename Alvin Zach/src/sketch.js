function setup() {
  // Create the canvas
  createCanvas(900,600);

  fill(255,87,34);
  translate(450,270);
  noStroke(); 
  //outer red ellipses
  for(i=0;i<6;i++){
        ellipse(0, 0, 270, 470);
        rotate(PI/6);
    }
  // yellow ellipses
  fill(255,193,7);
  for(i=0;i<6;i++){
        ellipse(0, 0, 270, 470);
        rotate(PI/3);
  }
  //lighter yellow inner ellipse
  fill(255,235,40);
  for(i=0;i<6;i++){
        ellipse(0, 0, 230, 430);
        rotate(PI/3);
  }
  fill(191,54,12);
  for(i=0;i<6;i++){
        ellipse(0, 0, 100, 400);
        rotate(PI/3);
  }
  fill(255,160,0);
  ellipse(0,0,300,300);
  fill(255,193,7);
  ellipse(0,0,260,260);
  fill(255,87,34,150);
  for (var i = 0; i < 10; i ++) {
    ellipse(0, 0, 50, 260);
    rotate(PI/10);
  }
  fill(255,87,34);
  ellipse(0,0,150,150);
  fill(255,235,40);
  ellipse(0,0,100,100);
  
  fill(255,87,34,120);
  ellipse(0,0,20,50);
  ellipse(0,0,15,40);
  ellipse(0,0,10,40);
  ellipse(0,0,5,40);

  fill(191,54,12);
  arc(0,0, 60, 60, 0, PI);
  
}