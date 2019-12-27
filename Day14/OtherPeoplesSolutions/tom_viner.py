#See https://gist.github.com/tomviner/5aa9449ee7742f70747fd46bdaab8031
import math
from collections import Counter

from funcy import post_processing
from parse import parse
from scipy.optimize import minimize_scalar


@post_processing(dict)
def parse_input(input_str):
    quantity_pattern = '{num:d} {unit:w}'
    for line in input_str.strip().splitlines():
        left_str, right = line.split(' => ')
        lefts = [parse(quantity_pattern, input) for input in left_str.split(', ')]
        lefts = {input['unit']: input['num'] for input in lefts}
        right = parse(quantity_pattern, right)
        yield right['unit'], {'right_num': right['num'], 'lefts': lefts}


def calc_ore(eqs, fuel):
    chemicals = Counter()
    chemicals['FUEL'] = fuel

    last_chemicals = None

    while last_chemicals != chemicals:
        last_chemicals = chemicals.copy()

        for right, eq_data in eqs.items():
            for got_unit, got_num in list(chemicals.items()):

                if got_unit == right and got_num > 0:
                    mult = math.ceil(got_num / eq_data['right_num'])
                    chemicals[got_unit] -= mult * eq_data['right_num']

                    for left_unit, left_num in eq_data['lefts'].items():
                        chemicals[left_unit] += mult * left_num

    return chemicals['ORE']


def part_one(input_str):
    eqs = parse_input(input_str)
    return calc_ore(eqs, fuel=1)


def part_two(input_str):
    eqs = parse_input(input_str)
    max_ore = 1e12

    def fuel_error(fuel_quota):
        ore = calc_ore(eqs, int(fuel_quota))
        print(fuel_quota, ore)

        ore_left = max_ore - ore
        if ore_left < 0:
            # Penalise using more than the quota
            return abs(ore_left) * 100
        return ore_left

    ore_per_fuel = calc_ore(eqs, fuel=1)
    fuel_estimate = max_ore / ore_per_fuel

    fuel = minimize_scalar(
        fuel_error,
        bracket=(fuel_estimate, 2 * fuel_estimate)
    ).x
    return int(fuel)

input = """
4 QBQB, 2 NTLZ => 2 DPJP
5 SCSDX, 3 WBLBS => 5 GVPG
128 ORE => 1 WCQS
14 LHMZ => 2 SWBFV
5 NZJV, 1 MCLXC => 2 BSRT
1 WJHZ => 6 HRZV
5 SPNML, 1 QTVZL => 6 HBGD
1 BSRT, 1 JRBM, 1 GVPG => 2 XVDQT
10 CBQSB => 6 NRXGX
6 TBFQ => 7 QPXS
1 LKSVN => 1 FBFC
39 CBQSB => 7 PSLXZ
3 HBGD, 4 RCZF => 4 ZCTS
2 BMDV, 6 DPJP => 1 RCZF
1 GPBXP, 11 SWBFV, 12 XSBGR, 7 ZCLVG, 9 VQLN, 12 HRZV, 3 VLDVB, 3 QTVZL, 12 DVSD, 62 PSLXZ => 1 FUEL
10 CFPG, 1 TBFQ => 3 NHKZB
24 QLMJ => 1 SCSDX
2 VKHZC => 1 SMLPV
3 SMLPV, 11 NZJV, 1 HTSXK => 2 GPBXP
1 SCKB => 3 TBFQ
3 VKHZC, 2 XVDQT => 6 PHJH
3 QBQB => 3 XHWH
19 NHKZB, 3 MBQVK, 10 HTSXK, 2 GXVQG, 8 VKHZC, 1 XHWH, 1 RCZF => 5 ZCLVG
1 GVPG => 4 QTVZL
4 TMHMV => 7 LHMZ
5 NRXGX, 9 NTLZ, 3 PSLXZ => 1 BMDV
10 MCLXC => 3 VKHZC
1 KTLR => 1 VLDVB
5 HTSXK => 6 TMHMV
5 LKSVN, 1 CGQHF, 11 WJHZ => 1 HGZC
15 XHWH, 1 WBLBS => 4 NZJV
3 MCLXC => 9 KTLR
1 CBQSB => 1 SCKB
140 ORE => 4 LKSVN
2 NZJV, 8 XVDQT, 1 PHJH => 8 GXVQG
21 NJXV, 1 XHWH, 12 TMHMV, 1 QPXS, 10 ZCTS, 3 TBFQ, 1 VLDVB => 7 DVSD
4 QLMJ, 2 LKSVN => 1 NTLZ
1 LKSVN => 4 QBQB
1 SPNML, 3 CPBQ => 4 BKLPC
2 CFPG => 5 MCLXC
147 ORE => 7 CGQHF
7 HGZC, 5 QLMJ => 3 CFPG
3 LCLQV, 3 MLXGB, 1 NTLZ => 8 JRBM
4 NHWG => 5 GPQN
2 XHWH => 7 WBLBS
7 CGFN, 2 RCZF, 13 NHWG, 1 VLDVB, 3 PHJH, 9 CBQSB => 9 XSBGR
181 ORE => 7 WJHZ
8 WJHZ => 9 CBQSB
3 BTQWK, 8 BKLPC => 2 CGFN
3 SCSDX => 3 NJXV
6 JTBM, 23 GPQN => 1 VQLN
23 MCLXC, 1 NTLZ => 7 SPNML
1 SPNML => 2 JTBM
1 BMDV => 7 HTSXK
1 WBLBS => 9 NHWG
4 FBFC, 1 LKSVN, 4 VKHZC => 7 CPBQ
1 WCQS => 7 QLMJ
1 BMDV, 2 DPJP => 6 MBQVK
3 XHWH, 5 QLMJ => 4 LCLQV
1 CBQSB, 2 PSLXZ => 2 MLXGB
3 NHWG => 9 BTQWK
""".strip()

print(part_one(input))
print(part_two(input))