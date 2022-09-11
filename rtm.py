import os
import argparse
import glob

# python rtmscore.py -p ./1qkt_p.pdb -l ./1qkt_decoys.sdf -rl ./1qkt_l.sdf -gen_pocket -c 10.0 -m ../trained_models/rtmscore_model1.pth


parser = argparse.ArgumentParser(description = 'rtm')
parser.add_argument('--protein', '-p', default = '/home/ubuntu/VINA_screening/example/', help = 'prefix of protein')
# protein path: ~/VINA_creening/example/{name}/{name}_protein.pdb
parser.add_argument('--ligand', '-l', default = '/home/ubuntu/output/', help = 'prefix of ligands')
# ligand path: ~/output/{name}/{name}_ligand_out_{i}.sdf
parser.add_argument('--name', '-n', required = True, help = 'name of complex')
parser.add_argument('--rtm_loc', default = '/home/ubuntu/RTMScore/example/rtmscore.py')
parser.add_argument('--out', '-o', default = '/home/ubuntu/output_rtm/', help = 'prefix of output')
parser.add_argument('-gen_pocket', '--gen_pocket', action = "store_true", default = False,
                    help = 'whether to generate the pocket')
parser.add_argument('-c', '--cutoff', default = 10.0, type = float,
                    help = 'the cutoff the define the pocket and interactions within the pocket (default: 10.0)')
parser.add_argument('-rl', '--reflig', default = None,
                    help = 'the reference ligand to determine the pocket(.sdf/.mol2)')

args = parser.parse_args()

if __name__ == '__main__':
    ligands = glob.glob(os.path.join(args.ligand, args.name, '*.sdf'))
    if not os.path.exists(args.out):
        os.makedirs(args.out)
    outpath = os.path.join(args.out, args.name)
    if args.gen_pocket:
        for ligand in ligands:
            print(' python ' + args.rtm_loc + ' -p ' + os.path.join(args.protein, args.name, '{}_protein.pdb'.format(args.name))
                  + ' -l ' + ligand + ' -o ' + outpath)
            os.system(' python ' + args.rtm_loc + ' -p ' + os.path.join(args.protein, args.name,
                                                                        '{}_protein.pdb'.format(args.name))
                      + ' -l ' + ligand + ' -o ' + outpath + ' -c ' + args.cutoff + ' --gen_pocket ')
    else:
        for ligand in ligands:
            # print(' python ' + args.rtm_loc + ' -p ' + os.path.join(args.protein, args.name, '{}_protein.pdb'.format(args.name))
            #       + ' -l ' + ligand + ' -o ' + outpath)
            os.system(' python ' + args.rtm_loc + ' -p ' + os.path.join(args.protein, args.name,
                                                                        '{}_protein.pdb'.format(args.name))
                      + ' -l ' + ligand + ' -o ' + outpath + ' -c ' + args.cutoff + ' -rl ' + args.reflig)
