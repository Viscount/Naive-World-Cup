#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv


def parse_data(path):
    lst = []
    # 1. 获取数据路径
    match_file_path = path

    # 2. 读入数据
    with open(match_file_path, "r+", encoding='utf-8') as file:
        lines = csv.DictReader(file)
        for line in lines:
            # 3.整理成字典
            # 4.加入到列表
            lst.append(dict(line))

    return lst


def main():
    matches = parse_data("sc_data/wc_group_matches.csv")
    teams = parse_data("sc_data/team_info.csv")
    history_matches = parse_data("sc_data/history_matches.csv")
    squads = parse_data("sc_data/squads.csv")


if __name__ == "__main__":
    main()
