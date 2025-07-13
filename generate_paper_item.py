import time

papers = [
    {
        'paper_name': 'GTA1: GUI Test-time Scaling Agent',
        'paper_url': 'https://www.arxiv.org/abs/2507.05791',
        'github_url': 'https://github.com/Yan98/GTA1',
        'author_name': 'Yan Yang, Dongxu Li, Yutong Dai, Yuhao Yang, Ziyang Luo, Zirui Zhao, Zhiyuan Hu, Junzhe Huang, Amrita Saha, Zeyuan Chen, Ran Xu, Liyuan Pan, Caiming Xiong, Junnan Li',
        'image_path': 'https://arxiv.org/html/2507.05791v3/x2.png',
        'conference': '',
    },
    {
        'paper_name': 'ShowUI: One Vision-Language-Action Model for GUI Visual Agent',
        'paper_url': 'https://arxiv.org/abs/2411.17465',
        'github_url': 'https://github.com/showlab/ShowUI',
        'author_name': 'Kevin Qinghong Lin, Linjie Li, Difei Gao, Zhengyuan Yang, Shiwei Wu, Zechen Bai, Weixian Lei, Lijuan Wang, Mike Zheng Shou',
        'image_path': 'https://arxiv.org/html/2411.17465v1/x4.png',
        'conference': 'CVPR_2025',
    },
    {
        'paper_name': 'AppAgent: Multimodal Agents as Smartphone Users',
        'paper_url': 'https://arxiv.org/abs/2312.13771',
        'github_url': 'https://github.com/TencentQQGYLab/AppAgent',
        'author_name': 'Chi Zhang, Zhao Yang, Jiaxuan Liu, Yucheng Han, Xin Chen, Zebiao Huang, Bin Fu, Gang Yu',
        'image_path': 'https://arxiv.org/html/2312.13771v2/x2.png',
        'conference': 'CHI_2025',
    },
    {
        'paper_name': 'Mirage-1: Augmenting and Updating GUI Agent with Hierarchical Multimodal Skills',
        'paper_url': 'https://arxiv.org/abs/2506.10387',
        'github_url': 'https://github.com/JiuTian-VL/Mirage-1',
        'author_name': 'Yuquan Xie, Zaijing Li, Rui Shao, Gongwei Chen, Kaiwen Zhou, Yinchuan Li, Dongmei Jiang, Liqiang Nie',
        'image_path': 'https://arxiv.org/html/2506.10387v1/x2.png',
        'conference': '',
    },
    {
        'paper_name': 'AgentSynth: Scalable Task Generation for Generalist Computer-Use Agents',
        'paper_url': 'https://arxiv.org/abs/2506.14205',
        'github_url': 'https://github.com/sunblaze-ucb/AgentSynth',
        'author_name': 'Jingxu Xie, Dylan Xu, Xuandong Zhao, Dawn Song',
        'image_path': 'figures/AgentSynth.png',
        'conference': '',
    },
    {
        'paper_name': 'Look Before You Leap: A GUI-Critic-R1 Model for Pre-Operative Error Diagnosis in GUI Automation',
        'paper_url': 'https://arxiv.org/abs/2506.04614',
        'github_url': 'https://github.com/X-PLUG/MobileAgent',
        'author_name': 'Yuyang Wanyan, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Jiabo Ye, Yutong Kou, Ming Yan, Fei Huang, Xiaoshan Yang, Weiming Dong, Changsheng Xu',
        'image_path': 'https://arxiv.org/html/2506.04614v1/x2.png',
        'conference': '',
    },
    {
        'paper_name': 'GUI-Reflection: Empowering Multimodal GUI Models with Self-Reflection Behavior',
        'paper_url': 'https://arxiv.org/abs/2506.08012',
        'github_url': 'https://github.com/penghao-wu/GUI_Reflection',
        'author_name': 'Penghao Wu, Shengnan Ma, Bo Wang, Jiaheng Yu, Lewei Lu, Ziwei Liu',
        'image_path': 'https://arxiv.org/html/2506.08012v1/x2.png',
        'conference': '',
    }
]

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
