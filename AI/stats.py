'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''

from collections import namedtuple
from ways import load_map_from_csv


def give_me_stats(roads):
    min_dis = 0
    avg_dis = 0
    max_dis = 0

    min_out_branch = 0
    max_out_branch = 0
    map_roads_num_links = {}
    counts_branches = 0
    count = 0
    for k, v in roads.items():
        counts_branches = 0
        for vl in v[3]:
            if vl[3] not in map_roads_num_links:
                map_roads_num_links[vl[3]] = 1
            else:
                map_roads_num_links[vl[3]] += 1
            counts_branches += 1
            count += 1
            current_val = vl[2]
            avg_dis += current_val
            if (min_dis == 0) or (current_val < min_dis):
                min_dis = current_val
            max_dis = max(max_dis, current_val)
        if min_out_branch == 0:
            min_out_branch = counts_branches
        min_out_branch = min(counts_branches, min_out_branch)
        max_out_branch = max(counts_branches, max_out_branch)
    num_links = count
    avg_dis = avg_dis / count
    avg_out_branch = count / len(roads)
    return min_dis, avg_dis, max_dis, min_out_branch, avg_out_branch, max_out_branch, map_roads_num_links, num_links


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    min_dis, avg_dis, max_dis, min_out_branch, avg_out_branch, max_out_branch, map_roads_num_links, num_links = give_me_stats(
        roads)
    return {
        'Number of junctions': len(roads),
        'Number of links': num_links,
        'Outgoing branching factor': Stat(max=max_out_branch, min=min_out_branch, avg=avg_out_branch),
        'Link distance': Stat(max=max_dis, min=min_dis, avg=avg_dis),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': map_roads_num_links,  # tip: use collections.Counter
    }


# def euclidean_distance(p1, p2):
#   return np.linalg.norm(p1 - p2)

def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print_stats()
