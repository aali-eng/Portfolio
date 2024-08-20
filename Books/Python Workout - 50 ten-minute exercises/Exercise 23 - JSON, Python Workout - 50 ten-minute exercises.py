# In this exercise, you’re analyzing test data in a high school.
# There’s a scores directory on the filesystem containing a number
# of files in JSON format. Each file represents the scores for one
# class. Write a function, print_scores, that takes a directory
# name as an argument and prints a summary of the student scores
# it finds.

# Book solution:

import json
import glob


def print_scores(dirname):
    scores = {}

    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = {}

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject,
                                                [])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) /
                             len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')


print_scores('scores/9a.json')
