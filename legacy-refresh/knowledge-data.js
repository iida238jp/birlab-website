window.BIRL_KNOWLEDGE = {
  questions: [
    {id:'emergence', en:'How does intelligence emerge from physical interaction?', ja:'知能は、身体と環境の相互作用からどのように生まれるのか。', themes:['embodied-intelligence','physical-interaction','adaptation']}
  ],
  themes: [
    {id:'embodied-intelligence', projects:['body-dynamics-sensing','physical-robot-evolution','roboscientist-falling-paper']},
    {id:'soft-robotics', projects:['thermoplastic-robotics','anthropomorphic-robot-hand','multi-layer-tactile-skins']},
    {id:'embodied-sensing', projects:['body-dynamics-sensing','multi-layer-tactile-skins','eit-tactile-sensing']},
    {id:'adaptive-manipulation', projects:['cambridge-arm','agri-food-robotics','food-handling-humanoid']}
  ],
  robots: [
    {id:'robotic-hand', image:'robotic-hand-1200.jpg', projects:['anthropomorphic-robot-hand'], themes:['adaptive-manipulation']},
    {id:'soft-fingers', image:'soft-fingers.jpg', projects:['thermoplastic-robotics'], themes:['soft-robotics']},
    {id:'vegebot', image:'vegebot-1200.jpg', projects:['agri-food-robotics'], themes:['adaptive-manipulation']},
    {id:'foodly', image:'foodly-1200.jpg', projects:['food-handling-humanoid'], themes:['adaptive-manipulation']},
    {id:'roboscientist', image:'falling-paper-1200.jpg', projects:['roboscientist-falling-paper'], themes:['embodied-intelligence']},
    {id:'cambridge-arm', image:'cambridge-arm-1200.jpg', projects:['cambridge-arm'], themes:['adaptive-manipulation']},
    {id:'cargo', image:'cargo-robot-1200.jpg', projects:['energy-efficient-locomotion'], themes:['embodied-intelligence']},
    {id:'climbing-robot', image:'climbing-robot.png', projects:['climbing-robots'], themes:['soft-robotics']},
    {id:'robot-evolution', image:'robot-evolution-1200.jpg', projects:['physical-robot-evolution'], themes:['embodied-intelligence']},
    {id:'eit-sensing', image:'soft-sensor.jpg', projects:['eit-tactile-sensing','multi-layer-tactile-skins'], themes:['embodied-sensing']}
  ],
  programmes: [
    {id:'digital-roads', period:'current', themes:['embodied-intelligence'], impact:['manufacturing-infrastructure'], source:'https://drf.eng.cam.ac.uk/research/automation-and-robotics'},
    {id:'agriforwards', period:'current', themes:['adaptive-manipulation'], impact:['food-agriculture'], source:'https://agriforwards.eng.cam.ac.uk/'},
    {id:'aigreenbots', period:'2024-2028', themes:['adaptive-manipulation','embodied-sensing'], impact:['food-agriculture'], source:'https://gtr.ukri.org/search/project?term=AIGreenBots&type='},
    {id:'robopatient', period:'2019-2023', themes:['embodied-sensing'], impact:['healthcare-human-support'], source:'https://gtr.ukri.org/search/project?term=RoboPatient&type='}
  ]
};
