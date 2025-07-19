import time

papers = [
    # {
    #     'paper_url': '',
    #     'paper_name': '',
    #     'author_name': '',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': '',
    # },
    # {
    #     'paper_name': 'GTA1: GUI Test-time Scaling Agent',
    #     'paper_url': 'https://www.arxiv.org/abs/2507.05791',
    #     'github_url': 'https://github.com/Yan98/GTA1',
    #     'author_name': 'Yan Yang, Dongxu Li, Yutong Dai, Yuhao Yang, Ziyang Luo, Zirui Zhao, Zhiyuan Hu, Junzhe Huang, Amrita Saha, Zeyuan Chen, Ran Xu, Liyuan Pan, Caiming Xiong, Junnan Li',
    #     'image_path': 'https://arxiv.org/html/2507.05791v3/x2.png',
    #     'conference': '',
    # },
    # {
    #     'paper_name': 'ShowUI: One Vision-Language-Action Model for GUI Visual Agent',
    #     'paper_url': 'https://arxiv.org/abs/2411.17465',
    #     'github_url': 'https://github.com/showlab/ShowUI',
    #     'author_name': 'Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou',
    #     'image_path': 'https://arxiv.org/html/2411.17465v1/x4.png',
    #     'conference': 'CVPR_2025',
    # },
    # {
    #     'paper_name': 'AppAgent: Multimodal Agents as Smartphone Users',
    #     'paper_url': 'https://arxiv.org/abs/2312.13771',
    #     'github_url': 'https://github.com/TencentQQGYLab/AppAgent',
    #     'author_name': 'Chi Zhang, Zhao Yang, Jiaxuan Liu, Yucheng Han, Xin Chen, Zebiao Huang, Bin Fu, Gang Yu',
    #     'image_path': 'https://arxiv.org/html/2312.13771v2/x2.png',
    #     'conference': 'CHI_2025',
    # },
    # {
    #     'paper_name': 'Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills',
    #     'paper_url': 'https://arxiv.org/abs/2506.10387',
    #     'github_url': 'https://github.com/JiuTian-VL/Mirage-1',
    #     'author_name': 'Yuquan Xie, Zaijing Li, Rui Shao, Gongwei Chen, Kaiwen Zhou, Yinchuan Li, Dongmei Jiang, Liqiang Nie',
    #     'image_path': 'https://arxiv.org/html/2506.10387v1/x2.png',
    #     'conference': '',
    # },
    # {
    #     'paper_name': 'AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents',
    #     'paper_url': 'https://arxiv.org/abs/2506.14205',
    #     'github_url': 'https://github.com/sunblaze-ucb/AgentSynth',
    #     'author_name': 'Jingxu Xie, Dylan Xu, Xuandong Zhao, Dawn Song',
    #     'image_path': 'figures/AgentSynth.png',
    #     'conference': '',
    # },
    # {
    #     'paper_name': 'Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation',
    #     'paper_url': 'https://arxiv.org/abs/2506.04614',
    #     'github_url': 'https://github.com/X-PLUG/MobileAgent',
    #     'author_name': 'Yuyang Wanyan, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Jiabo Ye, Yutong Kou, Ming Yan, Fei Huang, Xiaoshan Yang, Weiming Dong, Changsheng Xu',
    #     'image_path': 'https://arxiv.org/html/2506.04614v1/x2.png',
    #     'conference': '',
    # },
    # {
    #     'paper_name': 'GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior',
    #     'paper_url': 'https://arxiv.org/abs/2506.08012',
    #     'github_url': 'https://github.com/penghao-wu/GUI_Reflection',
    #     'author_name': 'Penghao Wu, Shengnan Ma, Bo Wang, Jiaheng Yu, Lewei Lu, Ziwei Liu',
    #     'image_path': 'https://arxiv.org/html/2506.08012v1/x2.png',
    #     'conference': '',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2505.14246v1',
    #     'paper_name': 'Visual Agentic Reinforcement Fine-Tuning',
    #     'author_name': 'Ziyu Liu, Yuhang Zang, Yushan Zou, Zijian Liang, Xiaoyi Dong, Yuhang Cao, Haodong Duan, Dahua Lin, Jiaqi Wang',
    #     'github_url': 'https://github.com/Liuziyu77/Visual-RFT',
    #     'conference': 'ICCV_2025',
    #     'image_path': 'https://arxiv.org/html/2505.14246v1/x2.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2505.08617v2',
    #     'paper_name': 'OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning',
    #     'author_name': 'Zhaochen Su, Linjie Li, Mingyang Song, Yunzhuo Hao, Zhengyuan Yang, Jun Zhang, Guanjie Chen, Jiawei Gu, Juntao Li, Xiaoye Qu, Yu Cheng',
    #     'github_url': 'https://github.com/zhaochen0110/OpenThinkIMG',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2505.08617v2/x1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2504.21776',
    #     'paper_name': 'WebThinker: Empowering Large Reasoning Models with Deep Research Capability',
    #     'author_name': 'Xiaoxi Li, Jiajie Jin, Guanting Dong, Hongjin Qian, Yutao Zhu, Yongkang Wu, Ji-Rong Wen, Zhicheng Dou',
    #     'github_url': 'https://github.com/RUC-NLPIR/WebThinker',
    #     'conference': '',
    #     'image_path': 'https://github.com/RUC-NLPIR/WebThinker/raw/main/figures/framework.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2507.07998',
    #     'paper_name': 'PyVision: Agentic Vision with Dynamic Tooling',
    #     'author_name': 'Shitian Zhao, Haoquan Zhang, Shaoheng Lin, Ming Li, Qilong Wu, Kaipeng Zhang, Chen Wei',
    #     'github_url': 'https://github.com/agents-x-project/PyVision',
    #     'conference': '',
    #     'image_path': 'figures/PyVision.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2507.02592',
    #     'paper_name': 'WebSailor: Navigating Super-human Reasoning for Web Agent',
    #     'author_name': 'Kuan Li, Zhongwang Zhang, Huifeng Yin, Liwen Zhang, Litu Ou, Jialong Wu, Wenbiao Yin, Baixuan Li, Zhengwei Tao, Xinyu Wang, Weizhou Shen, Junkai Zhang, Dingchu Zhang, Xixi Wu, Yong Jiang, Ming Yan, Pengjun Xie, Fei Huang, Jingren Zhou',
    #     'github_url': 'https://github.com/Alibaba-NLP/WebAgent',
    #     'conference': '',
    #     'image_path': 'figures/WebSailor.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2501.05366',
    #     'paper_name': 'Search-o1: Agentic Search-Enhanced Large Reasoning Models',
    #     'author_name': 'Xiaoxi Li, Guanting Dong, Jiajie Jin, Yuyao Zhang, Yujia Zhou, Yutao Zhu, Peitian Zhang, Zhicheng Dou',
    #     'github_url': 'https://github.com/sunnynexus/Search-o1',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2501.05366v1/x2.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2506.20670',
    #     'paper_name': 'MMSearch-R1: Incentivizing LMMs to Search',
    #     'author_name': 'Jinming Wu, Zihao Deng, Wei Li, Yiding Liu, Bo You, Bo Li, Zejun Ma, Ziwei Liu',
    #     'github_url': 'https://github.com/EvolvingLMMs-Lab/multimodal-search-r1',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2506.20670v1/x1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2506.10821',
    #     'paper_name': 'VideoDeepResearch: Long Video Understanding With Agentic Tool Using',
    #     'author_name': 'Huaying Yuan, Zheng Liu, Junjie Zhou, Hongjin Qian, Ji-Rong Wen, Zhicheng Dou',
    #     'github_url': 'https://github.com/yhy-2000/VideoDeepResearch',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2506.10821v2/x2.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2409.12959v2',
    #     'paper_name': 'MMSearch: Benchmarking the Potential of Large Models as Multi-modal Search Engines',
    #     'author_name': 'Dongzhi Jiang, Renrui Zhang, Ziyu Guo, Yanmin Wu, Jiayi Lei, Pengshuo Qiu, Pan Lu, Zehui Chen, Chaoyou Fu, Guanglu Song, Peng Gao, Yu Liu, Chunyuan Li, Hongsheng Li',
    #     'github_url': 'https://github.com/CaraJ7/MMSearch',
    #     'conference': 'ICLR_2025',
    #     'image_path': 'https://arxiv.org/html/2409.12959v2/x1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2506.21506',
    #     'paper_name': 'Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge',
    #     'author_name': 'Boyu Gou, Zanming Huang, Yuting Ning, Yu Gu, Michael Lin, Weijian Qi, Andrei Kopanev, Botao Yu, Bernal Jiménez Gutiérrez, Yiheng Shu, Chan Hee Song, Jiaman Wu, Shijie Chen, Hanane Nour Moussa, Tianshu Zhang, Jian Xie, Yifei Li, Tianci Xue, Zeyi Liao, Kai Zhang, Boyuan Zheng, Zhaowei Cai, Viktor Rozgic, Morteza Ziyadi, Huan Sun, Yu Su',
    #     'github_url': 'https://github.com/osu-nlp-group/mind2web2',
    #     'conference': '',
    #     'image_path': 'https://github.com/OSU-NLP-Group/Mind2Web-2/raw/main/assets/mind2web2_overview.jpg',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2411.04890',
    #     'paper_name': 'GUI Agents with Foundation Models: A Comprehensive Survey',
    #     'author_name': 'Shuai Wang, Weiwen Liu, Jingxuan Chen, Yuqi Zhou, Weinan Gan, Xingshan Zeng, Yuhan Che, Shuai Yu, Xinlong Hao, Kun Shao, Bin Wang, Chuhan Wu, Yasheng Wang, Ruiming Tang, Jianye Hao',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2411.04890v2/x2.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2304.00685',
    #     'paper_name': 'Vision-Language Models for Vision Tasks: A Survey',
    #     'author_name': 'Jingyi Zhang, Jiaxing Huang, Sheng Jin, Shijian Lu',
    #     'github_url': 'https://github.com/jingyi0000/VLM_survey',
    #     'conference': 'TPAMI_2024',
    #     'image_path': 'https://arxiv.org/html/2304.00685v2/x4.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2405.17935v1',
    #     'paper_name': 'Tool Learning with Large Language Models: A Survey',
    #     'author_name': 'Changle Qu, Sunhao Dai, Xiaochi Wei, Hengyi Cai, Shuaiqiang Wang, Dawei Yin, Jun Xu, Ji-Rong Wen',
    #     'github_url': 'https://github.com/quchangle1/LLM-Tool-Survey',
    #     'conference': 'FCS_2025',
    #     'image_path': 'https://arxiv.org/html/2405.17935v1/x2.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2403.15452',
    #     'paper_name': 'What Are Tools Anyway? A Survey from the Language Model Perspective',
    #     'author_name': 'Zhiruo Wang, Zhoujun Cheng, Hao Zhu, Daniel Fried, Graham Neubig',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2403.15452v1/x1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2410.10934',
    #     'paper_name': 'Agent-as-a-Judge: Evaluate Agents with Agents',
    #     'author_name': 'Mingchen Zhuge, Changsheng Zhao, Dylan Ashley, Wenyi Wang, Dmitrii Khizbullin, Yunyang Xiong, Zechun Liu, Ernie Chang, Raghuraman Krishnamoorthi, Yuandong Tian, Yangyang Shi, Vikas Chandra, Jürgen Schmidhuber',
    #     'github_url': 'https://github.com/metauto-ai/agent-as-a-judge',
    #     'conference': 'ICML_2025',
    #     'image_path': 'https://arxiv.org/html/2410.10934v2/x1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2507.06229',
    #     'paper_name': 'Agent KB: Leveraging Cross-Domain Experience for Agentic Problem Solving',
    #     'author_name': 'Xiangru Tang, Tianrui Qin, Tianhao Peng, Ziyang Zhou, Daniel Shao, Tingting Du, Xinming Wei, Peng Xia, Fang Wu, He Zhu, Ge Zhang, Jiaheng Liu, Xingyao Wang, Sirui Hong, Chenglin Wu, Hao Cheng, Chi Wang, Wangchunshu Zhou',
    #     'github_url': 'https://github.com/OPPO-PersonalAI/Agent-KB',
    #     'conference': '',
    #     'image_path': 'https://github.com/OPPO-PersonalAI/Agent-KB/raw/master/assets/agent_kb.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2506.07675',
    #     'paper_name': 'QUITE: A Query Rewrite System Beyond Rules with LLM Agents',
    #     'author_name': 'Yuyang Song, Hanxu Yan, Jiale Lao, Yibo Wang, Yufei Li, Yuanchun Zhou, Jianguo Wang, Mingjie Tang',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2506.07675v2/x3.png',
    # },
    # {
    #     'paper_url': 'https://www.arxiv.org/abs/2507.04036',
    #     'paper_name': 'PresentAgent: Multimodal Agent for Presentation Video Generation',
    #     'author_name': 'Jingwei Shi, Zeyu Zhang, Biao Wu, Yanjie Liang, Meng Fang, Ling Chen, Yang Zhao',
    #     'github_url': 'https://github.com/AIGeeksGroup/PresentAgent',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2507.04036v1/x3.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2506.10974',
    #     'paper_name': 'AutoMind: Adaptive Knowledgeable Agent for Automated Data Science',
    #     'author_name': 'Yixin Ou, Yujie Luo, Jingsheng Zheng, Lanning Wei, Shuofei Qiao, Jintian Zhang, Da Zheng, Huajun Chen, Ningyu Zhang',
    #     'github_url': 'https://github.com/innovatingAI/AutoMind',
    #     'conference': '',
    #     'image_path': 'https://github.com/InnovatingAI/AutoMind/raw/main/assets/framework.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2506.10055',
    #     'paper_name': 'TaskCraft: Automated Generation of Agentic Tasks',
    #     'author_name': 'Dingfeng Shi, Jingyi Cao, Qianben Chen, Weichen Sun, Weizhen Li, Hongxuan Lu, Fangchen Dong, Tianrui Qin, King Zhu, Minghao Liu, Jian Yang, Ge Zhang, Jiaheng Liu, Changwang Zhang, Jun Wang, Yuchen Eleanor Jiang, Wangchunshu Zhou',
    #     'github_url': 'https://github.com/OPPO-PersonalAI/TaskCraft',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2506.10055v2/x3.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2507.05241v2',
    #     'paper_name': "SciMaster: Towards General-Purpose Scientific AI Agents, Part I. X-Master as Foundation: Can We Lead on Humanity's Last Exam?",
    #     'author_name': 'Jingyi Chai, Shuo Tang, Rui Ye, Yuwen Du, Xinyu Zhu, Mengcheng Zhou, Yanfeng Wang, Weinan E, Yuzhi Zhang, Linfeng Zhang, Siheng Chen',
    #     'github_url': 'https://github.com/sjtu-sai-agents/X-Master',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2507.05241v2/x1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2504.14870v1',
    #     'paper_name': 'OTC: Optimal Tool Calls via Reinforcement Learning',
    #     'author_name': 'Hongru Wang, Cheng Qian, Wanjun Zhong, Xiusi Chen, Jiahao Qiu, Shijue Huang, Bowen Jin, Mengdi Wang, Kam-Fai Wong, Heng Ji',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2504.14870v1/x1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2504.21561',
    #     'paper_name': 'Iterative Tool Usage Exploration for Multimodal Agents via Step-wise Preference Tuning',
    #     'author_name': 'Pengxiang Li, Zhi Gao, Bofei Zhang, Yapeng Mi, Xiaojian Ma, Chenrui Shi, Tao Yuan, Yuwei Wu, Yunde Jia, Song-Chun Zhu, Qing Li',
    #     'github_url': 'https://github.com/SPORT-Agents/SPORT-Agents',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2504.21561v3/x1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2505.00024',
    #     'paper_name': 'Nemotron-Research-Tool-N1: Exploring Tool-Using Language Models with Reinforced Reasoning',
    #     'author_name': 'Shaokun Zhang, Yi Dong, Jieyu Zhang, Jan Kautz, Bryan Catanzaro, Andrew Tao, Qingyun Wu, Zhiding Yu, Guilin Liu',
    #     'github_url': 'https://github.com/NVlabs/Tool-N1',
    #     'conference': '',
    #     'image_path': 'https://github.com/NVlabs/Tool-N1/raw/master/assets/overview.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2410.07745',
    #     'paper_name': 'StepTool: Enhancing Multi-Step Tool Usage in LLMs through Step-Grained Reinforcement Learning',
    #     'author_name': 'Yuanqing Yu, Zhefan Wang, Weizhi Ma, Shuai Wang, Chuhan Wu, Zhiqiang Guo, Min Zhang',
    #     'github_url': '',
    #     'conference': 'ICLR_2025',
    #     'image_path': 'figures/StepTool.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2308.11432',
    #     'paper_name': 'A Survey on Large Language Model based Autonomous Agents',
    #     'author_name': 'Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, Ji-Rong Wen',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2308.11432v7/x2.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2506.01056',
    #     'paper_name': 'MCP-Zero: Active Tool Discovery for Autonomous LLM Agents',
    #     'author_name': 'Xiang Fei, Xiawu Zheng, Hao Feng',
    #     'github_url': 'https://github.com/xfey/MCP-Zero',
    #     'conference': '',
    #     'image_path': 'https://github.com/xfey/MCP-Zero/raw/master/assets/fig1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2403.00839',
    #     'paper_name': 'ToolNet: Connecting Large Language Models with Massive Tools via Tool Graph',
    #     'author_name': 'Xukun Liu, Zhiyuan Peng, Xiaoyuan Yi, Xing Xie, Lirong Xiang, Yuchen Liu, Dongkuan Xu',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': 'figures/ToolNet.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2410.08328',
    #     'paper_name': 'Agents Thinking Fast and Slow: A Talker-Reasoner Architecture',
    #     'author_name': 'Konstantina Christakopoulou, Shibl Mourad, Maja Matarić',
    #     'github_url': '',
    #     'conference': 'NeurIPS_2024_Workshop',
    #     'image_path': 'https://arxiv.org/html/2410.08328v1/extracted/5914711/images/agents-talk-extract-react-3.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2406.12045',
    #     'paper_name': 'τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains',
    #     'author_name': 'Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan',
    #     'github_url': 'https://github.com/sierra-research/tau-bench',
    #     'conference': '',
    #     'image_path': 'figures/tau_bench.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2407.08713',
    #     'paper_name': 'GTA: A Benchmark for General Tool Agents',
    #     'author_name': 'Jize Wang, Zerun Ma, Yining Li, Songyang Zhang, Cailian Chen, Kai Chen, Xinyi Le',
    #     'github_url': 'https://github.com/open-compass/GTA',
    #     'conference': 'NeurIPS_2024',
    #     'image_path': 'https://arxiv.org/html/2407.08713v2/x2.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2501.12851',
    #     'paper_name': 'ACEBench: Who Wins the Match Point in Tool Usage?',
    #     'author_name': 'Chen Chen, Xinlong Hao, Weiwen Liu, Xu Huang, Xingshan Zeng, Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan, Yuefeng Huang, Wulong Liu, Xinzhi Wang, Defu Lian, Baoqun Yin, Yasheng Wang, Wu Liu',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2501.12851v5/x1.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2506.03143',
    #     'paper_name': 'GUI-Actor: Coordinate-Free Visual Grounding for GUI Agents',
    #     'author_name': 'Qianhui Wu, Kanzhi Cheng, Rui Yang, Chaoyun Zhang, Jianwei Yang, Huiqiang Jiang, Jian Mu, Baolin Peng, Bo Qiao, Reuben Tan, Si Qin, Lars Liden, Qingwei Lin, Huan Zhang, Tong Zhang, Jianbing Zhang, Dongmei Zhang, Jianfeng Gao',
    #     'github_url': 'https://github.com/microsoft/GUI-Actor',
    #     'conference': '',
    #     'image_path': 'https://microsoft.github.io/GUI-Actor/static/images/actor_model_illustration.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2506.05334',
    #     'paper_name': 'Search Arena: Analyzing Search-Augmented LLMs',
    #     'author_name': 'Mihran Miroyan, Tsung-Han Wu, Logan King, Tianle Li, Jiayi Pan, Xinyan Hu, Wei-Lin Chiang, Anastasios N. Angelopoulos, Trevor Darrell, Narges Norouzi, Joseph E. Gonzalez',
    #     'github_url': 'https://github.com/lmarena/search-arena',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2506.05334v1/extracted/6514317/figure/example.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2411.18279',
    #     'paper_name': 'Large Language Model-Brained GUI Agents: A Survey',
    #     'author_name': 'Chaoyun Zhang, Shilin He, Jiaxu Qian, Bowen Li, Liqun Li, Si Qin, Yu Kang, Minghua Ma, Guyue Liu, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang',
    #     'github_url': 'https://github.com/vyokky/LLM-Brained-GUI-Agents-Survey',
    #     'conference': '',
    #     'image_path': 'https://arxiv.org/html/2411.18279v12/x2.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2412.13501',
    #     'paper_name': 'GUI Agents: A Survey',
    #     'author_name': 'Dang Nguyen, Jian Chen, Yu Wang, Gang Wu, Namyong Park, Zhengmian Hu, Hanjia Lyu, Junda Wu, Ryan Aponte, Yu Xia, Xintong Li, Jing Shi, Hongjie Chen, Viet Dac Lai, Zhouhang Xie, Sungchul Kim, Ruiyi Zhang, Tong Yu, Mehrab Tanjim, Nesreen K. Ahmed, Puneet Mathur, Seunghyun Yoon, Lina Yao, Branislav Kveton, Thien Huu Nguyen, Trung Bui, Tianyi Zhou, Ryan A. Rossi, Franck Dernoncourt',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': '',
    # },
    {
        'paper_url': 'https://arxiv.org/abs/2504.13865',
        'paper_name': 'A Survey on (M)LLM-Based GUI Agents',
        'author_name': 'Fei Tang, Haolei Xu, Hang Zhang, Siqi Chen, Xingyu Wu, Yongliang Shen, Wenqi Zhang, Guiyang Hou, Zeqi Tan, Yuchen Yan, Kaitao Song, Jian Shao, Weiming Lu, Jun Xiao, Yueting Zhuang',
        'github_url': 'https://github.com/zju-real/Awesome-GUI-Agents',
        'conference': '',
        'image_path': 'https://arxiv.org/html/2504.13865v2/x3.png',
    },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2307.13854',
    #     'paper_name': 'WebArena: A Realistic Web Environment for Building Autonomous Agents',
    #     'author_name': 'Shuyan Zhou, Frank F. Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried, Uri Alon, Graham Neubig',
    #     'github_url': 'https://github.com/web-arena-x/webarena',
    #     'conference': '',
    #     'image_path': 'https://github.com/web-arena-x/webarena/raw/main/media/overview.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2504.12516',
    #     'paper_name': 'BrowseComp: A Simple Yet Challenging Benchmark for Browsing Agents',
    #     'author_name': 'Jason Wei, Zhiqing Sun, Spencer Papay, Scott McKinney, Jeffrey Han, Isa Fulford, Hyung Won Chung, Alex Tachard Passos, William Fedus, Amelia Glaese',
    #     'github_url': 'https://github.com/openai/simple-evals',
    #     'conference': '',
    #     'image_path': 'figures/BrowseComp.png',
    # },
    # {
    #     'paper_url': 'https://arxiv.org/abs/2406.14991',
    #     'paper_name': 'SpreadsheetBench: Towards Challenging Real World Spreadsheet Manipulation',
    #     'author_name': 'Zeyao Ma, Bohan Zhang, Jing Zhang, Jifan Yu, Xiaokang Zhang, Xiaohan Zhang, Sijia Luo, Xi Wang, Jie Tang',
    #     'github_url': 'https://github.com/RUCKBReasoning/SpreadsheetBench',
    #     'conference': 'NeurIPS_2024',
    #     'image_path': 'https://arxiv.org/html/2406.14991v2/x2.png',
    # },
]
# {
    #     'paper_url': '',
    #     'paper_name': '',
    #     'author_name': '',
    #     'github_url': '',
    #     'conference': '',
    #     'image_path': '',
    # },
star_format = '[![Star](https://img.shields.io/github/stars/{}.svg?style=social&label=Star)](https://github.com/{})'
conference_format = " [![Publish](https://img.shields.io/badge/Conference-{}-blue)]()"
main_item_format = '[{}]({}) <br> {} |'
image_format = '<img width="1002" alt="image" src="{}"> |'
github_format = '[Github]({}) <br> '
paper_format = '[Paper]({})'

month = time.strftime("%m", time.localtime())
day = time.strftime("%d", time.localtime())
timestamp = f"[//]: #{month}/{day}"

# print("### ✅ Simple Format Output\n")
# for paper in papers:
#     final_str = "* "
#     if paper['conference']:
#         final_str += conference_format.format(paper['conference']) + " "
#     if paper['github_url']:
#         github_item = '/'.join(paper['github_url'].split('/')[-2:])
#         final_str += star_format.format(github_item, github_item) + " "
#     final_str += "[{}]({}). {}. [[Paper]]({})".format(
#         paper['paper_name'], paper['paper_url'], paper['author_name'], paper['paper_url'])
#     if paper['github_url']:
#         final_str += "[[Github]]({})".format(paper['github_url'])
#     print(final_str)

print("\n### ✅ Complex Format Output\n")
for paper in papers:
    final_str = "|"
    flag = False
    if paper['github_url']:
        github_item = '/'.join(paper['github_url'].split('/')[-2:])
        final_str += star_format.format(github_item, github_item)
        flag = True
    if paper['conference']:
        final_str += conference_format.format(paper['conference'])
        flag = True
    if flag:
        final_str += '<br>'
    final_str += main_item_format.format(paper['paper_name'], paper['paper_url'], paper['author_name'])
    final_str += image_format.format(paper['image_path'])
    if paper['github_url']:
        final_str += github_format.format(paper['github_url'])
    final_str += paper_format.format(paper['paper_url'])
    final_str += '| ' + timestamp
    print(final_str)
