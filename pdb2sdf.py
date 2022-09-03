import openbabel
import argparse
import os
import glob

parser = argparse.ArgumentParser(description='converter')
parser.add_argument('--file', '-f', required=True)
parser.add_argument('--output', '-o', default='/home/ubuntu')

args = parser.parse_args()


if __name__ == '__main__':
    conv = openbabel.OBConversion()
    for i in range(1, 11):
        path = os.path.join(args.file, 'output', 'test_{}'.format(i))
        files = glob.glob(os.path.join(path, '????_ligand_out*.pdb'))
        for file in files:
            name = os.path.basename(file)
            print(name)
            outfile = os.path.join(args.output, 'output', name[:4])
            if not os.path.exists(outfile):
                os.makedirs(outfile)
            conv.OpenInAndOutFiles(file, os.path.join(outfile, name[:-3]+'sdf'))
            conv.SetInAndOutFormats("pdb", "sdf")
            conv.Convert()
            conv.CloseOutFile()