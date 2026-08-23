window.BIRL_PROJECTS = [
  ['eit-tactile-sensing','2026','sensing','Sensing','センシング','EIT-based tactile sensing','EIT触覚センシング','Task-driven information selection for tactile perception.','タスクに応じて触覚情報を選択する知覚技術。'],
  ['food-handling-humanoid','2025','manipulation','Manipulation','操作','Food-handling humanoid robot','食品ハンドリング・ヒューマノイド','Adaptive robotic handling in challenging food environments.','難しい食品環境に適応するロボットハンドリング。'],
  ['multi-layer-tactile-skins','2024','sensing','Sensing','センシング','Multi-layer soft tactile skins','多層ソフト触覚スキン','High-density contact sensing with flexible electrode placement.','電極配置の自由度を高めた高密度接触センシング。'],
  ['ei-conference','2023','embodied','Embodied Intelligence','身体知能','EI Conference','EI Conference','An international forum for embodied intelligence research.','身体知能研究のための国際フォーラム。'],
  ['anthropomorphic-robot-hand','2021','manipulation','Manipulation','操作','Anthropomorphic robot hand','人型ロボットハンド','Musculoskeletal design for dexterous, human-like manipulation.','器用で人らしい操作を目指す筋骨格デザイン。'],
  ['roboscientist-falling-paper','2020','experiments','Robot Experiments','ロボット実験','RoboScientist: Falling Paper','RoboScientist：落下する紙','Large-scale automated physical experimentation.','大規模な物理実験を自動で繰り返すシステム。'],
  ['agri-food-robotics','2019','manipulation','Manipulation','操作','Agri-food robotics','アグリフード・ロボティクス','Robotics for delicate and demanding agricultural work.','繊細で負荷の高い農作業のためのロボティクス。'],
  ['physical-robot-evolution','2018','evolution','Evolution / Design','進化・設計','Physical robot evolution','ロボットの物理的進化','Autonomous design and fabrication for adaptable machines.','適応する機械のための自律的な設計と製造。'],
  ['cambridge-arm','2016','manipulation','Manipulation','操作','CambridgeARM','CambridgeARM','Robust vision, gripping, and warehouse manipulation.','ロバストな視覚、把持、倉庫内マニピュレーション。'],
  ['thermoplastic-robotics','2014','soft','Soft Robotics','ソフトロボティクス','Thermoplastic adhesives for robots','ロボット用熱可塑性接着剤','Mechanisms for robotic growth and morphological change.','ロボットの成長と形態変化を実現する機構。'],
  ['energy-efficient-locomotion','2013','locomotion','Locomotion','移動','Energy-efficient legged locomotion','高効率な脚移動','Elastic mechanisms for hopping, walking, and running.','跳躍、歩行、走行のための弾性メカニズム。'],
  ['climbing-robots','2012','locomotion','Locomotion','移動','Large-payload climbing robots','大荷重壁面移動ロボット','Adhesive locomotion across complex vertical environments.','複雑な垂直環境を移動する接着技術。'],
  ['clutch-actuators','Legacy','locomotion','Actuation','駆動','Unconventional clutch-based actuators','非従来型クラッチ式アクチュエータ','Variable stiffness and damping for versatile movement.','多様な動きのための可変剛性・減衰機構。'],
  ['posture-support','Legacy','systems','Wearable','ウェアラブル','Assistive mechatronic posture support','メカトロニクス姿勢支援','Low-energy body support for standing and industrial assistance.','立位や産業作業を支える低エネルギー装置。'],
  ['compass-gait','Legacy','locomotion','Locomotion','移動','Compass gait in rough terrain','不整地でのコンパス歩行','Underactuated walking through steps and uneven ground.','段差や荒れた地面を進む劣駆動歩行。'],
  ['underactuated-locomotion','Legacy','locomotion','Locomotion','移動','Underactuated legged locomotion','劣駆動脚ロボット移動','Mechanical design for efficient rough-terrain traversal.','不整地を効率よく進むための機械設計。'],
  ['biped-locomotion','Legacy','locomotion','Locomotion','移動','Human-like biped locomotion','人間らしい二足歩行','Compliant bipeds as physical models of human walking.','人の歩行を理解するための柔軟な二足ロボット。'],
  ['body-dynamics-sensing','Legacy','embodied','Embodied Intelligence','身体知能','Sensing through body dynamics','身体ダイナミクスによる知覚','How perception, control, and physical dynamics shape one another.','知覚、制御、身体の動きが形づくる相互関係。'],
  ['underwater-locomotion','Legacy','locomotion','Locomotion','移動','Minimal underwater locomotion','最小構成の水中移動','Behavioural diversity from material properties and simple actuation.','材料特性と簡単な駆動から多様な動きを生む研究。'],
  ['puppy','Legacy','locomotion','Locomotion','移動','Puppy: rapid legged locomotion','Puppy：高速脚移動','Musculoskeletal design for fast four-legged movement.','素早い四足移動のための筋骨格デザイン。'],
  ['stumpy','Legacy','locomotion','Locomotion','移動','Stumpy: pendulum-driven hopping','Stumpy：振り子式跳躍','Behavioural diversity through morphology and minimal control.','形態と最小限の制御から生まれる多様な振る舞い。'],
  ['bio-inspired-navigation','Legacy','sensing','Navigation','ナビゲーション','Biologically inspired 3D navigation','生物規範型3D視覚ナビゲーション','Animal-inspired omnidirectional vision for learning and navigation.','動物に学ぶ全方位視覚を使った学習と移動。'],
  ['non-verbal-face-robot','Legacy','interaction','Human–Robot Interaction','人間–ロボット相互作用','Active non-verbal face robot','非言語対話フェイスロボット','Artificial muscles and expression for human–robot communication.','人工筋肉と表情による人とロボットのコミュニケーション。']
];

(() => {
  const list = document.querySelector('[data-project-list]');
  if (!list) return;
  const ja = document.documentElement.lang === 'ja';
  list.innerHTML = window.BIRL_PROJECTS.map((p) => `<article class="archive-item" id="${p[0]}" data-category="${p[2]}" data-search="${p.join(' ')}"><time>${ja && p[1] === 'Legacy' ? '初期' : p[1]}</time><div><span>${p[ja ? 4 : 3]}</span><h3>${p[ja ? 6 : 5]}</h3><p>${p[ja ? 8 : 7]}</p></div><b aria-hidden="true">#</b></article>`).join('');
  if (window.location.hash) requestAnimationFrame(() => document.querySelector(window.location.hash)?.scrollIntoView());
})();
