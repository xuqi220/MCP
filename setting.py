charge_desc = {"掩饰、隐瞒犯罪所得罪":"明知是犯罪所得，而予以窝藏、转移、收购、代为销售或者以其他方法掩饰、隐瞒的行为",
                "窝藏、包庇罪":"明知是犯罪的人而为其提供隐藏处所、财物，帮助其逃匿或者以作假证明的方式掩盖其罪行的行为",
                "非法拘禁罪":"故意非法拘禁他人或者以其他方法非法剥夺他人人身自由的行为",
                "寻衅滋事罪":"肆意挑衅，随意殴打、骚扰他人或任意损毁、占用公私财物等行为，或者在公共场所起哄闹事，造成了严重破坏社会秩序的损害结果的行为",
                "聚众斗殴罪":"聚集多人攻击对方身体或者相互攻击对方身体，扰乱公共秩序的行为",
                "抢劫罪":"以非法占有为目的, 使用暴力、胁迫或者其他方法, 迫使被害人当场交出财物或者强行将公私财物当场抢走的行为",
                "故意伤害罪":"故意非法损害他人身体健康的行为",
                "故意杀人罪":"故意非法剥夺他人生命的行为",
                "诈骗罪":"以非法占有为目的, 用虚构事实或者隐瞒真相的方法, 骗取数额较大的公私财物的行为",
                "合同诈骗罪":"以非法占有为目的，在签订、履行合同过程中，实施虚构事实或者隐瞒真相等欺骗手段，骗取对方当事人的财物，数额较大的行为",
                "敲诈勒索罪":"以非法占有为目的, 对财物的所有人、管理人实施恐吓、威胁或者要挟的方法, 强行索取数额较大的公私财物的行为",
                "非法持有枪支罪":"违反枪支管理规定, 未经许可, 非法持有枪支的行为",
                "非法制造枪支罪":"行为人违反国家有关枪支管理的法规，非法制造枪支、危害公共安全的行为",
                "非法买卖枪支罪":"行为人违反国家有关枪支管理的法规，非法买卖枪支、危害公共安全的行为",
                "假冒注册商标罪":"违反国家商标管理法规，未经注册商标所有人许可，在同一种商品、服务上使用与其注册商标相同的商标，情节严重的行为",
                "销售假冒注册商标的商品罪":"销售明知是假冒注册商标的商品, 销售金额较大的行为",
                "非法经营罪":"违反国家规定, 非法从事经营活动, 扰乱市场秩序, 情节严重的行为",
                "组织卖淫罪":"以招募、雇佣、引诱、容留等手段，纠集、控制多人从事卖淫的行为",
                "协助组织卖淫罪":"为他人实施组织卖淫的犯罪活动提供方便、创造条件、排除障碍的行为",
                "容留卖淫罪":"为他人卖淫提供场所的行为",
                "介绍卖淫罪":"为卖淫的人与嫖客牵线搭桥的行为",
                "招摇撞骗罪":"为谋取非法利益，假冒国家机关工作人员的身份或职称，进行诈骗，损害国家机关的威信及其正常活动的行为"}

cate2charge = {
               "社会公共安全":["非法制造枪支罪", "非法买卖枪支罪", "非法持有枪支罪"],
               "国家对知识产权的管理秩序":['假冒注册商标罪', "销售假冒注册商标的商品罪"],
               "市场秩序":["合同诈骗罪", "非法经营罪"],
               "公民的人身、民主权利":["故意杀人罪", "故意伤害罪", "非法拘禁罪"],
               "财产权利":["抢劫罪", "诈骗罪", '敲诈勒索罪'],
               "社会公共秩序":['招摇撞骗罪', "聚众斗殴罪", "寻衅滋事罪"],
               "国家司法秩序":["窝藏、包庇罪", "掩饰、隐瞒犯罪所得罪"],
               "社会道德风尚和社会治安管理秩序":["组织卖淫罪", "协助组织卖淫罪", "容留卖淫罪", "介绍卖淫罪"]
               }

simG = {
'财产权利': ['国家司法秩序', '公民的人身、民主权利'],
 '国家司法秩序': ['财产权利', '公民的人身、民主权利', '社会公共安全'],
 '公民的人身、民主权利': ['国家司法秩序', '财产权利', '社会公共秩序'],
 '社会公共秩序': ['公民的人身、民主权利'],
 '市场秩序': ['社会道德风尚和社会治安管理秩序', '国家对知识产权的管理秩序'],
 '社会道德风尚和社会治安管理秩序': ['市场秩序'],
 '国家对知识产权的管理秩序': ['市场秩序'],
 '社会公共安全': ['国家司法秩序']
 }

index2charge = ["非法制造枪支罪", "非法买卖枪支罪", "非法持有枪支罪",
                "假冒注册商标罪", "销售假冒注册商标的商品罪",
                "合同诈骗罪", "非法经营罪",
                "故意杀人罪", "故意伤害罪", "非法拘禁罪",
                "抢劫罪", "诈骗罪", "敲诈勒索罪",
                "窝藏、包庇罪", "掩饰、隐瞒犯罪所得罪",
                "组织卖淫罪", "协助组织卖淫罪", "容留卖淫罪", "介绍卖淫罪",
                "聚众斗殴罪", "寻衅滋事罪", "招摇撞骗罪"]


enc = "./pretrained_files/roberta_wwm"

params = {"epoch":20,
          "batch_size":12,
          "lr":0.00005,
          "pattern":"ext",# anno:直接使用标注结果；ext:使用模型抽取结果
          "data_path":["hard","easy", "all"], # , "all""hard",
          "topk":[2,3],
          "alpha":[0.001,0.005, 0.01, 0.02, 0.05, 0.08, 0.1, 0.2, 0.5, 1], # 控制charge prediction的分布 dist/alpha
          "beta":[0.001,0.005, 0.01, 0.05, 0.1, 0.5, 1, 10, 100], # 控制group prediction 的分布dist*beta
          "threhold":0.0,
          "seeds":[80,19, 23, 94, 13, 0, 7, 47, 21, 81]
          }

if __name__=="__main__":
    pass