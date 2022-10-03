def make_results(results):
    result_data = []
    for result in results:
        result_dict = {'date': result.date, 'open': result.open, 'high': result.high,
                       'low': result.low, 'close': result.close, 'adj_close': result.adj_close,
                       'volume': result.volume}
        result_data.append(result_dict)
        del result_dict
    return result_data


def file_to_json(file):
    with open(file, 'r', encoding='utf-8-sig') as f:
        lines = f.readlines()[1:]
    new_lines = []
    for line in lines:
        line = line.strip().split(',')
        line_dict = {'date': line[0], 'open': line[1], 'high': line[2], 'low': line[3],
                     'close': line[4], 'adj_close': line[5], 'volume': line[6]}
        new_lines.append(line_dict)
        del line_dict
    return new_lines