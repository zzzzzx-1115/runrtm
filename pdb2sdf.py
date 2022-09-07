from openbabel import openbabel
import argparse
import os
import glob
from tqdm import tqdm

parser = argparse.ArgumentParser(description='converter')
parser.add_argument('--file', '-f', required=True)
parser.add_argument('--output', '-o', default='/home/ubuntu')

args = parser.parse_args()


if __name__ == '__main__':
    #匹配file名下所有的pdb id文件夹
    conv = openbabel.OBConversion()
    pdb_files = glob.glob(os.path.join(args.file, '[a-z,0-9][a-z,0-9][a-z,0-9][a-z,0-9]'))
    for pdb_file in pdb_files:
        count = 0
        all_test = glob.glob(os.path.join(pdb_file, 'output', '*'))
        for path in tqdm(all_test):
            files = glob.glob(os.path.join(path, '????_ligand_out*.pdb'))
            for file in files:
                name = os.path.basename(file)
                outfile = os.path.join(args.output, name[:4])
                if not os.path.exists(outfile):
                    os.makedirs(outfile)
                conv.OpenInAndOutFiles(file, os.path.join(outfile, name[:4]+'_{}.sdf'.format(count)))
                conv.SetInAndOutFormats("pdb", "sdf")
                conv.Convert()
                conv.CloseOutFile()
                count += 1