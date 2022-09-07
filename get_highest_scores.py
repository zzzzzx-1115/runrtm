import argparse
import pandas as pd
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', required=True, help='input csv')
#in example: /home/ubuntu/asdxvsadwe/10gs.csv
parser.add_argument('--output', '-o', help='prefix of output', default='./')
#out example: /home/ubuntu/new/
parser.add_argument('--num', '-n', help='top n results', default=1, type=int)

args = parser.parse_args()


name = os.path.splitext(os.path.basename(args.input))[0]  #10gs

df = pd.read_csv(os.path.join(args.input), header=None)

sorted_df = df.sort_values(by=1, ascending=False)

res = sorted_df[:args.num]

res.to_csv(os.path.join(args.output, name+'_topn.csv'), header=0, index=0)