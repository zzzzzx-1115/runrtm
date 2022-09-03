import openbabel
import argparse
import os
import glob

parser = argparse.ArgumentParser(description='converter')
parser.add_argument('--file', '-f', required=True)
parser.add_argument('--output', '-o', default='/home')

args = parser.parse_args()


if __name__ == '__main__':
    conv = openbabel.OBConversion()
    for i in range(1, 11):
        path = os.path.join(args.file, 'output', 'test_{}'.format(i))
        files = glob.glob(os.path.join(path, '????_ligand_out*.pdb'))
        for file in files:
            print(args.output)
            kkk = os.path.join(args.output, 'output', file[:4], file[:-3] + 'sdf')
            print('kkk', kkk)
            conv.OpenInAndOutFiles(file, kkk)
            conv.SetInAndOutFormats("pdb", "sdf")
            conv.Convert()
            conv.CloseOutFile()