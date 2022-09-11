# One line for VINA&RTM!

一个脚本，完成VINA screeing和RTM score并获取top k结果

# Preliminaries
VINA_screening

RTMScore
    
需将`rtmscore.py`中187行处df.to_csv()的存储模式改为append


# 使用
直接运行`all_in_one.sh`
### 各变量含义
`VINA`, `VINA_GPU`, `OBABEL`: 同VINA_screening

`CONVERTER`: 此repo中`pdb2sdf.py`的位置

`RTM_PY`: 此repo中`rtm.py`的位置

`RTM_ORIGIN`: `rtmscore.py`的位置 (RTMScore)

`SORTER`: 此repo中`get_highest_scores.py`的位置

`NUMBER`: 获取评分最高的若干个结果

`INPUT_PREFIX`: `xxxx/VINA_screening/example`, 将xxxx替换为VINA_screening所在位置，自动匹配其中的所有pdb id

`OUTPUT_PREFIX`: 存放VINA_screening的结果

`SDF_PREFIX`: 将VINA_screening生成的pdb文件转换为sdf格式时的输出位置

`RTM_PREFIX`: 存储所有RTM scores

`RESULT_PREFIX`: 获取`RTM_PREFIX`下top k结果的存储位置