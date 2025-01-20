import json, csv
import pandas as pd


def load_data(path):
    return pd.read_csv(path)


def save_data(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)


def make_data(data):
    out = {}
    for item in data['item']:
        words = item.split()
        if 'and' in words:
            and_index = words.index('and')
            following = ' '.join(words[1:and_index + 2])
            prefix = '_'.join(words[1:and_index + 2])
            next = words[and_index + 2]
            dict = {
                    "templates": [
                        "{noun1} {verb1} {gap} {noun2} "+following
                    ],
                    "label": "gap",
                    "result_prepend_space": False,
                    "labels": {
                        "what": ["."],
                        "that": [f" {next}"]
                    },
                    "variables": {
                        "noun1": ["the mother", "the security guard", "the man", "the delivery boy",
                            "the judge", "the reporter", "the accountant", "the secretary"
                            ],
                        "noun2": [
                            "the investigator", "the businessman", "the friend", "the painter",
                            "the neighbor", "the woman", "the politician", "the old man"
                            ],
                        "verb1": ["said", "believed", "knew", "remarked", "heard", "thought", "stated", 
                                "thought", "reported"],
                        "gap": {
                            "what": ["."],
                            "that": [f" {next}"]
                        }
                    }
                }
            out["filler_gap_" + prefix] = dict
    save_data(out, 'data/templates/filler_gap.json')


def main():
    data = load_data('filler_gap/means_all_studies_LSA.csv')
    make_data(data)


if __name__ == '__main__':
    main()