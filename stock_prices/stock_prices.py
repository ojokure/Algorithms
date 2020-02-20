#!/usr/bin/python

import argparse


def find_max_profit(prices):

    for i in range(0, len(prices)):
        current_max_price_so_far = prices[len(prices) - 1]
        current_min_price_so_far = prices[0]
        max_profit_so_far = current_max_price_so_far - current_min_price_so_far

        for j in range(i, len(prices)):
            if prices[j] < current_min_price_so_far:
                current_min_price_so_far, prices[j] = prices[j], current_min_price_so_far

                j += 1
            elif prices[j] > current_max_price_so_far:
                current_max_price_so_far, prices[j] = prices[j], current_max_price_so_far

                j += 1
    return max_profit_so_far


print(find_max_profit([200, 60, 30, 45, 60, 20, 90]))


# if __name__ == '__main__':
#     # This is just some code to accept inputs from the command line
#     parser = argparse.ArgumentParser(
#         description='Find max profit from prices.')
#     parser.add_argument('integers', metavar='N', type=int,
#                         nargs='+', help='an integer price')
#     args = parser.parse_args()

#     print("A profit of ${profit} can be made from the stock prices {prices}.".format(
#         profit=find_max_profit(args.integers), prices=args.integers))
