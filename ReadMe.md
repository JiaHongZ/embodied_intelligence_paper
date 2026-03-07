# Embodied Intelligence Paper Index

Automatically updated daily from arXiv for embodied intelligence research.

## What This Project Does

- Fetches recent papers from arXiv (`cs.AI`, `cs.RO`, `cs.CV`, `cs.LG`, `cs.CL`, `stat.ML`)
- Filters by embodied intelligence keywords
- Categorizes papers into major subfields
- Extracts potential code links from abstracts
- Updates this README and `data/latest_papers.json`
- Runs daily via GitHub Actions

## Local Usage

```bash
python -m pip install -e .
python -m ei_paper_index --days 1 --max-results 300 --readme-path ReadMe.md --json-output data/latest_papers.json
```

## GitHub Actions

The workflow file is located at `.github/workflows/daily_update.yml`.

It runs once per day at `01:00 UTC` and can also be triggered manually using `workflow_dispatch`.

<!-- PAPER_INDEX_START -->

## Daily Embodied Intelligence Paper Index (2026-03-07 UTC)

Total papers: **40**

### Embodied AI

- [Observing and Controlling Features in Vision-Language-Action Models](https://arxiv.org/abs/2603.05487v1)
  - Authors: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05487v1)
- [On the Strengths and Weaknesses of Data for Open-set Embodied Assistance](https://arxiv.org/abs/2603.04819v1)
  - Authors: Pradyumna Tambwekar, Andrew Silva, Deepak Gopinath, Jonathan DeCastro, Xiongyi Cui, et al.
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04819v1)

### Foundation Models for Robotics

- [On the Strengths and Weaknesses of Data for Open-set Embodied Assistance](https://arxiv.org/abs/2603.04819v1)
  - Authors: Pradyumna Tambwekar, Andrew Silva, Deepak Gopinath, Jonathan DeCastro, Xiongyi Cui, et al.
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04819v1)

### Human-Robot Interaction

- [Rethinking the Role of Collaborative Robots in Rehabilitation](https://arxiv.org/abs/2603.05252v1)
  - Authors: Vivek Gupte, Shalutha Rajapakshe, Emmanuel Senft
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05252v1)
- [Direct Contact-Tolerant Motion Planning With Vision Language Models](https://arxiv.org/abs/2603.05017v1)
  - Authors: He Li, Jian Sun, Chengyang Li, Guoliang Li, Qiyu Ruan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05017v1)
  - Code Links: [code](https://github.com/ChrisLeeUM/DCT)
- [U-OBCA: Uncertainty-Aware Optimization-Based Collision Avoidance via Wasserstein Distributionally Robust Chance Constraints](https://arxiv.org/abs/2603.04914v1)
  - Authors: Zehao Wang, Yuxuan Tang, Han Zhang, Jingchuan Wang, Weidong Chen
  - Published: 2026-03-05
  - Categories: cs.RO, eess.SY, math.OC
  - PDF: [link](https://arxiv.org/pdf/2603.04914v1)

### Multimodal Robotics

- [Observing and Controlling Features in Vision-Language-Action Models](https://arxiv.org/abs/2603.05487v1)
  - Authors: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05487v1)
- [PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410v1)
  - Authors: Weikai Qin, Sichen Wu, Ci Chen, Mengfan Liu, Linxi Feng, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05410v1)
- [Iterative On-Policy Refinement of Hierarchical Diffusion Policies for Language-Conditioned Manipulation](https://arxiv.org/abs/2603.05291v1)
  - Authors: Clemence Grislain, Olivier Sigaud, Mohamed Chetouani
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05291v1)
- [Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation](https://arxiv.org/abs/2603.05185v1)
  - Authors: Pengfei Yi, Yingjie Ma, Wenjiang Xu, Yanan Hao, Shuai Gan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05185v1)
- [Lifelong Language-Conditioned Robotic Manipulation Learning](https://arxiv.org/abs/2603.05160v1)
  - Authors: Xudong Wang, Zebin Han, Zhiyu Liu, Gan Li, Jiahua Dong, et al.
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI
  - PDF: [link](https://arxiv.org/pdf/2603.05160v1)
- [Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models](https://arxiv.org/abs/2603.05147v1)
  - Authors: Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci
  - Published: 2026-03-05
  - Categories: cs.CV, cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05147v1)
- [SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation](https://arxiv.org/abs/2603.05117v1)
  - Authors: Youqiang Gui, Yuxuan Zhou, Shen Cheng, Xinyang Yuan, Haoqiang Fan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05117v1)
  - Code Links: [code](https://github.com/Youqiang-Gui/SeedPolicy)
- [Direct Contact-Tolerant Motion Planning With Vision Language Models](https://arxiv.org/abs/2603.05017v1)
  - Authors: He Li, Jian Sun, Chengyang Li, Guoliang Li, Qiyu Ruan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05017v1)
  - Code Links: [code](https://github.com/ChrisLeeUM/DCT)
- [VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory](https://arxiv.org/abs/2603.04910v1)
  - Authors: Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04910v1)
  - Code Links: [code](https://github.com/HarryLui98/code_vpwem)
- [On the Strengths and Weaknesses of Data for Open-set Embodied Assistance](https://arxiv.org/abs/2603.04819v1)
  - Authors: Pradyumna Tambwekar, Andrew Silva, Deepak Gopinath, Jonathan DeCastro, Xiongyi Cui, et al.
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04819v1)

### Other Embodied Intelligence

- [CT-Enabled Patient-Specific Simulation and Contact-Aware Robotic Planning for Cochlear Implantation](https://arxiv.org/abs/2603.05333v1)
  - Authors: Lingxiao Xun, Gang Zheng, Alexandre Kruszewski, Renato Torres
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05333v1)
- [Constraint-Free Static Modeling of Continuum Parallel Robot](https://arxiv.org/abs/2603.05309v1)
  - Authors: Lingxiao Xun, Matyas Diezinger, Azad Artinian, Guillaume Laurent, Brahim Tamadazte
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05309v1)
- [Curve-Induced Dynamical Systems on Riemannian Manifolds and Lie Groups](https://arxiv.org/abs/2603.05268v1)
  - Authors: Saray Bakker, Martin Schonger, Tobias Löw, Javier Alonso-Mora, Sylvain Calinon
  - Published: 2026-03-05
  - Categories: cs.RO, eess.SY
  - PDF: [link](https://arxiv.org/pdf/2603.05268v1)
- [VinePT-Map: Pole-Trunk Semantic Mapping for Resilient Autonomous Robotics in Vineyards](https://arxiv.org/abs/2603.05070v1)
  - Authors: Giorgio Audrito, Mauro Martini, Alessandro Navone, Giorgia Galluzzo, Marcello Chiaberge
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05070v1)
- [CoIn3D: Revisiting Configuration-Invariant Multi-Camera 3D Object Detection](https://arxiv.org/abs/2603.05042v1)
  - Authors: Zhaonian Kuang, Rui Ding, Haotian Wang, Xinhu Zheng, Meng Yang, et al.
  - Published: 2026-03-05
  - Categories: cs.CV, cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05042v1)
- [Observer Design for Augmented Reality-based Teleoperation of Soft Robots](https://arxiv.org/abs/2603.05015v1)
  - Authors: Jorge Francisco García-Samartín, Iago López Pérez, Emirhan Yolcu, Jaime del Cerro, Antonio Barrientos
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05015v1)
- [SURE: Semi-dense Uncertainty-REfined Feature Matching](https://arxiv.org/abs/2603.04869v1)
  - Authors: Sicheng Li, Zaiwang Gu, Jie Zhang, Qing Guo, Xudong Jiang, et al.
  - Published: 2026-03-05
  - Categories: cs.CV
  - PDF: [link](https://arxiv.org/pdf/2603.04869v1)
  - Code Links: [code](https://github.com/LSC-ALAN/SURE)

### Reinforcement Learning for Robotics

- [RoboPocket: Improve Robot Policies Instantly with Your Phone](https://arxiv.org/abs/2603.05504v1)
  - Authors: Junjie Fang, Wendi Chen, Han Xue, Fangyuan Zhou, Tian Le, et al.
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.05504v1)
  - Code Links: [code](https://robo-pocket.github.io)
- [Observing and Controlling Features in Vision-Language-Action Models](https://arxiv.org/abs/2603.05487v1)
  - Authors: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05487v1)
- [Residual RL--MPC for Robust Microrobotic Cell Pushing Under Time-Varying Flow](https://arxiv.org/abs/2603.05448v1)
  - Authors: Yanda Yang, Sambeeta Das
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI
  - PDF: [link](https://arxiv.org/pdf/2603.05448v1)
- [PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410v1)
  - Authors: Weikai Qin, Sichen Wu, Ci Chen, Mengfan Liu, Linxi Feng, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05410v1)
- [OpenFrontier: General Navigation with Visual-Language Grounded Frontiers](https://arxiv.org/abs/2603.05377v1)
  - Authors: Esteban Padilla, Boyang Sun, Marc Pollefeys, Hermann Blum
  - Published: 2026-03-05
  - Categories: cs.RO, cs.CV
  - PDF: [link](https://arxiv.org/pdf/2603.05377v1)
- [Omni-Manip: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception](https://arxiv.org/abs/2603.05355v1)
  - Authors: Pei Qu, Zheng Li, Yufei Jia, Ziyun Liu, Liang Zhu, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05355v1)
- [UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data](https://arxiv.org/abs/2603.05312v1)
  - Authors: Sizhe Yang, Yiman Xie, Zhixuan Liang, Yang Tian, Jia Zeng, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05312v1)
  - Code Links: [code](https://github.com/InternRobotics/UltraDexGrasp)
- [Latent Policy Steering through One-Step Flow Policies](https://arxiv.org/abs/2603.05296v1)
  - Authors: Hokyun Im, Andrey Kolobov, Jianlong Fu, Youngwoon Lee
  - Published: 2026-03-05
  - Categories: cs.RO, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.05296v1)
- [Digital Twin Driven Textile Classification and Foreign Object Recognition in Automated Sorting Systems](https://arxiv.org/abs/2603.05230v1)
  - Authors: Serkan Ergun, Tobias Mitterer, Hubert Zangl
  - Published: 2026-03-05
  - Categories: cs.CV, cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05230v1)
- [Decoupling Task and Behavior: A Two-Stage Reward Curriculum in Reinforcement Learning for Robotics](https://arxiv.org/abs/2603.05113v1)
  - Authors: Kilian Freitag, Knut Åkesson, Morteza Haghir Chehreghani
  - Published: 2026-03-05
  - Categories: cs.LG, cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05113v1)
- [GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108v1)
  - Authors: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05108v1)
- [Integrated cooperative localization of heterogeneous measurement swarm: A unified data-driven method](https://arxiv.org/abs/2603.04932v1)
  - Authors: Kunrui Ze, Wei Wang, Guibin Sun, Jiaqi Yan, Kexin Liu, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.04932v1)
- [U-OBCA: Uncertainty-Aware Optimization-Based Collision Avoidance via Wasserstein Distributionally Robust Chance Constraints](https://arxiv.org/abs/2603.04914v1)
  - Authors: Zehao Wang, Yuxuan Tang, Han Zhang, Jingchuan Wang, Weidong Chen
  - Published: 2026-03-05
  - Categories: cs.RO, eess.SY, math.OC
  - PDF: [link](https://arxiv.org/pdf/2603.04914v1)
- [Beyond the Patch: Exploring Vulnerabilities of Visuomotor Policies via Viewpoint-Consistent 3D Adversarial Object](https://arxiv.org/abs/2603.04913v1)
  - Authors: Chanmi Lee, Minsung Yoon, Woojae Kim, Sebin Lee, Sung-eui Yoon
  - Published: 2026-03-05
  - Categories: cs.RO, cs.CV
  - PDF: [link](https://arxiv.org/pdf/2603.04913v1)
- [VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory](https://arxiv.org/abs/2603.04910v1)
  - Authors: Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04910v1)
  - Code Links: [code](https://github.com/HarryLui98/code_vpwem)
- [Hyperbolic Multiview Pretraining for Robotic Manipulation](https://arxiv.org/abs/2603.04848v1)
  - Authors: Jin Yang, Ping Wei, Yixin Chen
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.04848v1)
- [On the Strengths and Weaknesses of Data for Open-set Embodied Assistance](https://arxiv.org/abs/2603.04819v1)
  - Authors: Pradyumna Tambwekar, Andrew Silva, Deepak Gopinath, Jonathan DeCastro, Xiongyi Cui, et al.
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04819v1)

### Robot Manipulation

- [cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots](https://arxiv.org/abs/2603.05493v1)
  - Authors: Balakumar Sundaralingam, Adithyavairavan Murali, Stan Birchfield
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05493v1)
- [RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)
  - Authors: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, et al.
  - Published: 2026-03-05
  - Categories: cs.CV, cs.AI, cs.GR
  - PDF: [link](https://arxiv.org/pdf/2603.05449v1)
  - Code Links: [code](https://liuwei283.github.io/RealWonder/)
- [Residual RL--MPC for Robust Microrobotic Cell Pushing Under Time-Varying Flow](https://arxiv.org/abs/2603.05448v1)
  - Authors: Yanda Yang, Sambeeta Das
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI
  - PDF: [link](https://arxiv.org/pdf/2603.05448v1)
- [Omni-Manip: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception](https://arxiv.org/abs/2603.05355v1)
  - Authors: Pei Qu, Zheng Li, Yufei Jia, Ziyun Liu, Liang Zhu, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05355v1)
- [UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data](https://arxiv.org/abs/2603.05312v1)
  - Authors: Sizhe Yang, Yiman Xie, Zhixuan Liang, Yang Tian, Jia Zeng, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05312v1)
  - Code Links: [code](https://github.com/InternRobotics/UltraDexGrasp)
- [Iterative On-Policy Refinement of Hierarchical Diffusion Policies for Language-Conditioned Manipulation](https://arxiv.org/abs/2603.05291v1)
  - Authors: Clemence Grislain, Olivier Sigaud, Mohamed Chetouani
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05291v1)
- [Digital Twin Driven Textile Classification and Foreign Object Recognition in Automated Sorting Systems](https://arxiv.org/abs/2603.05230v1)
  - Authors: Serkan Ergun, Tobias Mitterer, Hubert Zangl
  - Published: 2026-03-05
  - Categories: cs.CV, cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05230v1)
- [Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation](https://arxiv.org/abs/2603.05185v1)
  - Authors: Pengfei Yi, Yingjie Ma, Wenjiang Xu, Yanan Hao, Shuai Gan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05185v1)
- [Lifelong Language-Conditioned Robotic Manipulation Learning](https://arxiv.org/abs/2603.05160v1)
  - Authors: Xudong Wang, Zebin Han, Zhiyu Liu, Gan Li, Jiahua Dong, et al.
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI
  - PDF: [link](https://arxiv.org/pdf/2603.05160v1)
- [SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation](https://arxiv.org/abs/2603.05117v1)
  - Authors: Youqiang Gui, Yuxuan Zhou, Shen Cheng, Xinyang Yuan, Haoqiang Fan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05117v1)
  - Code Links: [code](https://github.com/Youqiang-Gui/SeedPolicy)
- [SPIRIT: Perceptive Shared Autonomy for Robust Robotic Manipulation under Deep Learning Uncertainty](https://arxiv.org/abs/2603.05111v1)
  - Authors: Jongseok Lee, Ribin Balachandran, Harsimran Singh, Jianxiang Feng, Hrishik Mishra, et al.
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI
  - PDF: [link](https://arxiv.org/pdf/2603.05111v1)
- [GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins](https://arxiv.org/abs/2603.05108v1)
  - Authors: Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05108v1)
- [Beyond the Patch: Exploring Vulnerabilities of Visuomotor Policies via Viewpoint-Consistent 3D Adversarial Object](https://arxiv.org/abs/2603.04913v1)
  - Authors: Chanmi Lee, Minsung Yoon, Woojae Kim, Sebin Lee, Sung-eui Yoon
  - Published: 2026-03-05
  - Categories: cs.RO, cs.CV
  - PDF: [link](https://arxiv.org/pdf/2603.04913v1)
- [VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory](https://arxiv.org/abs/2603.04910v1)
  - Authors: Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04910v1)
  - Code Links: [code](https://github.com/HarryLui98/code_vpwem)
- [Hyperbolic Multiview Pretraining for Robotic Manipulation](https://arxiv.org/abs/2603.04848v1)
  - Authors: Jin Yang, Ping Wei, Yixin Chen
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.04848v1)
- [Task-Relevant and Irrelevant Region-Aware Augmentation for Generalizable Vision-Based Imitation Learning in Agricultural Manipulation](https://arxiv.org/abs/2603.04845v1)
  - Authors: Shun Hattori, Hikaru Sasaki, Takumi Hachimine, Yusuke Mizutani, Takamitsu Matsubara
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.04845v1)
- [EchoGuard: An Agentic Framework with Knowledge-Graph Memory for Detecting Manipulative Communication in Longitudinal Dialogue](https://arxiv.org/abs/2603.04815v1)
  - Authors: Ratna Kandala, Niva Manchanda, Akshata Kishore Moharir, Ananth Kandala
  - Published: 2026-03-05
  - Categories: cs.AI
  - PDF: [link](https://arxiv.org/pdf/2603.04815v1)

### Robot Navigation

- [Safe-SAGE: Social-Semantic Adaptive Guidance for Safe Engagement through Laplace-Modulated Poisson Safety Functions](https://arxiv.org/abs/2603.05497v1)
  - Authors: Lizhi Yang, Ryan M. Bena, Meg Wilkinson, Gilbert Bahati, Andy Navarro Brenes, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05497v1)
- [cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots](https://arxiv.org/abs/2603.05493v1)
  - Authors: Balakumar Sundaralingam, Adithyavairavan Murali, Stan Birchfield
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05493v1)
- [Accelerating Sampling-Based Control via Learned Linear Koopman Dynamics](https://arxiv.org/abs/2603.05385v1)
  - Authors: Wenjian Hao, Yuxuan Fang, Zehui Lu, Shaoshuai Mou
  - Published: 2026-03-05
  - Categories: cs.RO, eess.SY
  - PDF: [link](https://arxiv.org/pdf/2603.05385v1)
- [OpenFrontier: General Navigation with Visual-Language Grounded Frontiers](https://arxiv.org/abs/2603.05377v1)
  - Authors: Esteban Padilla, Boyang Sun, Marc Pollefeys, Hermann Blum
  - Published: 2026-03-05
  - Categories: cs.RO, cs.CV
  - PDF: [link](https://arxiv.org/pdf/2603.05377v1)
- [Digital Twin Driven Textile Classification and Foreign Object Recognition in Automated Sorting Systems](https://arxiv.org/abs/2603.05230v1)
  - Authors: Serkan Ergun, Tobias Mitterer, Hubert Zangl
  - Published: 2026-03-05
  - Categories: cs.CV, cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05230v1)
- [Direct Contact-Tolerant Motion Planning With Vision Language Models](https://arxiv.org/abs/2603.05017v1)
  - Authors: He Li, Jian Sun, Chengyang Li, Guoliang Li, Qiyu Ruan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05017v1)
  - Code Links: [code](https://github.com/ChrisLeeUM/DCT)
- [Replaying pre-training data improves fine-tuning](https://arxiv.org/abs/2603.04964v1)
  - Authors: Suhas Kotha, Percy Liang
  - Published: 2026-03-05
  - Categories: cs.CL, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04964v1)
- [TimeWarp: Evaluating Web Agents by Revisiting the Past](https://arxiv.org/abs/2603.04949v1)
  - Authors: Md Farhan Ishmam, Kenneth Marino
  - Published: 2026-03-05
  - Categories: cs.AI, cs.CL, cs.CV, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04949v1)
- [U-OBCA: Uncertainty-Aware Optimization-Based Collision Avoidance via Wasserstein Distributionally Robust Chance Constraints](https://arxiv.org/abs/2603.04914v1)
  - Authors: Zehao Wang, Yuxuan Tang, Han Zhang, Jingchuan Wang, Weidong Chen
  - Published: 2026-03-05
  - Categories: cs.RO, eess.SY, math.OC
  - PDF: [link](https://arxiv.org/pdf/2603.04914v1)

### Robotics Learning

- [RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)
  - Authors: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, et al.
  - Published: 2026-03-05
  - Categories: cs.CV, cs.AI, cs.GR
  - PDF: [link](https://arxiv.org/pdf/2603.05449v1)
  - Code Links: [code](https://liuwei283.github.io/RealWonder/)
- [Omni-Manip: Beyond-FOV Large-Workspace Humanoid Manipulation with Omnidirectional 3D Perception](https://arxiv.org/abs/2603.05355v1)
  - Authors: Pei Qu, Zheng Li, Yufei Jia, Ziyun Liu, Liang Zhu, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05355v1)
- [Decoupling Task and Behavior: A Two-Stage Reward Curriculum in Reinforcement Learning for Robotics](https://arxiv.org/abs/2603.05113v1)
  - Authors: Kilian Freitag, Knut Åkesson, Morteza Haghir Chehreghani
  - Published: 2026-03-05
  - Categories: cs.LG, cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05113v1)

### Simulation-to-Real Transfer

- [UltraDexGrasp: Learning Universal Dexterous Grasping for Bimanual Robots with Synthetic Data](https://arxiv.org/abs/2603.05312v1)
  - Authors: Sizhe Yang, Yiman Xie, Zhixuan Liang, Yang Tian, Jia Zeng, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05312v1)
  - Code Links: [code](https://github.com/InternRobotics/UltraDexGrasp)

### Vision-Language-Action

- [Observing and Controlling Features in Vision-Language-Action Models](https://arxiv.org/abs/2603.05487v1)
  - Authors: Hugo Buurmeijer, Carmen Amo Alonso, Aiden Swann, Marco Pavone
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05487v1)
- [PhysiFlow: Physics-Aware Humanoid Whole-Body VLA via Multi-Brain Latent Flow Matching and Robust Tracking](https://arxiv.org/abs/2603.05410v1)
  - Authors: Weikai Qin, Sichen Wu, Ci Chen, Mengfan Liu, Linxi Feng, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05410v1)
- [OpenFrontier: General Navigation with Visual-Language Grounded Frontiers](https://arxiv.org/abs/2603.05377v1)
  - Authors: Esteban Padilla, Boyang Sun, Marc Pollefeys, Hermann Blum
  - Published: 2026-03-05
  - Categories: cs.RO, cs.CV
  - PDF: [link](https://arxiv.org/pdf/2603.05377v1)
- [Digital Twin Driven Textile Classification and Foreign Object Recognition in Automated Sorting Systems](https://arxiv.org/abs/2603.05230v1)
  - Authors: Serkan Ergun, Tobias Mitterer, Hubert Zangl
  - Published: 2026-03-05
  - Categories: cs.CV, cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05230v1)
- [Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation](https://arxiv.org/abs/2603.05185v1)
  - Authors: Pengfei Yi, Yingjie Ma, Wenjiang Xu, Yanan Hao, Shuai Gan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05185v1)
- [Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models](https://arxiv.org/abs/2603.05147v1)
  - Authors: Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci
  - Published: 2026-03-05
  - Categories: cs.CV, cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05147v1)
- [SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation](https://arxiv.org/abs/2603.05117v1)
  - Authors: Youqiang Gui, Yuxuan Zhou, Shen Cheng, Xinyang Yuan, Haoqiang Fan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05117v1)
  - Code Links: [code](https://github.com/Youqiang-Gui/SeedPolicy)
- [Direct Contact-Tolerant Motion Planning With Vision Language Models](https://arxiv.org/abs/2603.05017v1)
  - Authors: He Li, Jian Sun, Chengyang Li, Guoliang Li, Qiyu Ruan, et al.
  - Published: 2026-03-05
  - Categories: cs.RO
  - PDF: [link](https://arxiv.org/pdf/2603.05017v1)
  - Code Links: [code](https://github.com/ChrisLeeUM/DCT)
- [VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory](https://arxiv.org/abs/2603.04910v1)
  - Authors: Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo
  - Published: 2026-03-05
  - Categories: cs.RO, cs.AI, cs.LG
  - PDF: [link](https://arxiv.org/pdf/2603.04910v1)
  - Code Links: [code](https://github.com/HarryLui98/code_vpwem)

<!-- PAPER_INDEX_END -->
