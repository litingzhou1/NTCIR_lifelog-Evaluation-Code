import argparse
import numpy as np
from eval_results import EvaluationResult

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def process(files, outfile):
    result_list = [EvaluationResult(f) for f in files]

    names = [r.runid for r in result_list]
    iprec = [[r.results['iprec_at_recall_0.00'],
              r.results['iprec_at_recall_0.10'],
              r.results['iprec_at_recall_0.20'],
              r.results['iprec_at_recall_0.30'],
              r.results['iprec_at_recall_0.40'],
              r.results['iprec_at_recall_0.50'],
              r.results['iprec_at_recall_0.60'],
              r.results['iprec_at_recall_0.70'],
              r.results['iprec_at_recall_0.80'],
              r.results['iprec_at_recall_0.90'],
              r.results['iprec_at_recall_1.00']] for r in result_list]

    recall = np.arange(0, 1.1, 0.1)

    plt.xlabel('Recall')
    plt.ylabel('Interpolated Precision')

    for p in iprec:
        plt.plot(recall, p)

    plt.legend(names)
    plt.savefig(outfile, bbox_inches='tight')


if __name__ == '__main__':
    argparser = argparse.ArgumentParser('Plot precision-recall curves.')
    argparser.add_argument('-f', '--output', help='Save the figure to specified file.',
                           default='pr_curve.pdf', required=False)
    argparser.add_argument('files',
                           help='Pass multiple files to plot all the runs in the same plot.',
                           type=str, nargs='+')
    args = argparser.parse_args()

    process(args.files, args.output)
