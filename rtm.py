import os
import argparse
import glob


#python rtmscore.py -p ./1qkt_p.pdb -l ./1qkt_decoys.sdf -rl ./1qkt_l.sdf -gen_pocket -c 10.0 -m ../trained_models/rtmscore_model1.pth



parser = argparse.ArgumentParser(description='rtm')
parser.add_argument('--protein', '-p', default='/home/ubuntu/VINA_creening/example/', help='prefix of protein')
#protein path: ~/VINA_creening/example/{name}_protein.pdb
parser.add_argument('--ligand', '-l', default='/home/ubuntu/output/', help='prefix of ligands')
#ligand path: ~/output/{name}/{name}_ligand_out_{i}.sdf
parser.add_argument('--name', '-n', required=True, help='name of complex')
parser.add_argument('--rtm_loc', default='/home/ubuntu/RTMScore/example/rtmscore.py')
parser.add_argument('--out', '-o', default='/home/ubuntu/output_rtm/', help='prefix of output')


args = parser.parse_args()


if __name__ == '__main__':
    ligands = glob.glob(os.path.join(args.ligand, args.name, '*.sdf'))
    if not os.path.exists(args.out):
        os.makedirs(args.out)
    outpath = os.path.join(args.out, args.name + '.csv')
    for ligand in ligands:
        print(' python ' + args.rtm_loc + ' -p ' + os.path.join(args.protein, '{}_protein.pdb'.format(args.name))
              + ' -l ' + ligand + ' -o ' + outpath)
        os.system(' python ' + args.rtm_loc + ' -p ' + os.path.join(args.protein, '{}_protein.pdb'.format(args.name))
              + ' -l ' + ligand + ' -o ' + outpath)