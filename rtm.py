import subprocess
import argparse



#python rtmscore.py -p ./1qkt_p.pdb -l ./1qkt_decoys.sdf -rl ./1qkt_l.sdf -gen_pocket -c 10.0 -m ../trained_models/rtmscore_model1.pth



parser = argparse.ArgumentParser(description='rtm')
parser.add_argument('--protein', '-p', default='')
parser.add_argument('--ligand', '-l', default='')  #ligand files, 匹配~/VINA_screening/10gs/output/testxxx下所有ligand.pdb
#首先要把ligand.pdb全部转换成sdf



