##########################################################################
# FILE : ex11.py
# WRITER : Oren Motiei , oren503, 321174591
# EXERCISE : intro2cs2 ex11 2020
# DESCRIPTION: Practice decision tree.
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED: None.
# NOTES: None.
##########################################################################

import copy
import itertools


class Node:
    """
    Represents nodes in a decision tree.
    """
    def __init__(self, data, positive_child=None, negative_child=None):
        """
        A constructor for an object of type Node.
        :param data: A string. If the node is a leaf, it represents
                     a decision. Otherwise, It represents a question.
        :param positive_child: A string. A leaf that represents a decision.
        :param negative_child: A string. A child that represents a question.
        """
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child

    def get_data(self):
        """
        :return: Node's data.
        """
        return self.data

    def get_positive(self):
        """
        :return: Positive child's value.
        """
        return self.positive_child

    def get_negative(self):
        """
        :return: Negative child's value.
        """
        return self.negative_child

    def set_positive(self, node):
        """
        Sets the value of positive child to node.
        :param node: An object of type Node.
        """
        self.positive_child = node

    def set_negative(self, node):
        """
        Sets the value of negative child to node.
        :param node: An object of type Node.
        """
        self.negative_child = node

    def __repr__(self):
        """
        :return: A string that represents the data.
        """
        return str(self.data)


class Record:
    """
    Represents records of illnesses and their symptoms.
    """
    def __init__(self, illness, symptoms):
        """
        A constructor for an object of type Record.
        :param illness: A string with a name of an illness.
        :param symptoms: A list of strings. Each string represents a symptom.
        """
        self.illness = illness
        self.symptoms = symptoms

    def get_illness(self):
        """
        :return: A string with a name of an illness.
        """
        return self.illness

    def get_symptoms(self):
        """
        :return: A list of strings. Each string represents a symptom.
        """
        return self.symptoms


def parse_data(filepath):
    """
    :param filepath: A string that represents the path to a file.
    :return: A list of objects of type Record.
    """
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        """
        A constructor for an object of type Diagnoser.
        :param root: An object of type Node. Represents the root of
                     a decision Tree.
        """
        self.root = root

    def get_root(self):
        """
        :return: An object of type Node. Represents the root of
                 a decision Tree.
        """
        return self.root

    def diagnose(self, symptoms):
        """
        Diagnoses the symptoms and returns the name of the correct illness.
        :param symptoms: A list of strings. Each string represents a symptom.
        :return: The name of the illness.
        """
        cur_child = self.root
        leaf_data = []
        self.diagnose_helper(cur_child, leaf_data, symptoms)
        print(leaf_data)
        return leaf_data[0]

    def diagnose_helper(self, cur_child, leaf_data, symptoms):
        """
        :param cur_child: The current child in each recursive call.
        :param leaf_data: A list that contains the correct illness.
        :param symptoms: A list of strings. Each string represents a symptom.
        """
        if cur_child is None:
            leaf_data.append(None)
            return
        if cur_child.get_positive() is None and \
                cur_child.get_negative() is None:
            leaf_data.append(cur_child.get_data())
            return
        if cur_child.get_data() in symptoms:
            cur_child = cur_child.get_positive()
            self.diagnose_helper(cur_child, leaf_data, symptoms)
        else:
            cur_child = cur_child.get_negative()
            self.diagnose_helper(cur_child, leaf_data, symptoms)

    def calculate_success_rate(self, records):
        """
        :param records: A list of objects of type Record.
        :return: The ratio of the number of times there is a correct illness,
                 to the number of total records.
        """
        counter = 0
        for record in records:
            result = self.diagnose(record.get_symptoms())
            if result == record.get_illness():
                counter += 1
        return counter / len(records)

    def all_illnesses(self):
        """
        :return: A list of all the illnesses kept on the tree's leafs.
        """
        cur_child = self.root
        leaf_illnesses = list()
        self.all_illnesses_helper(leaf_illnesses, cur_child)
        leaf_illnesses = sorted(leaf_illnesses, key=leaf_illnesses.count,
                                reverse=True)
        result = list()
        for idx in range(len(leaf_illnesses)):
            if leaf_illnesses[idx] == leaf_illnesses[idx - 1]:
                pass
            else:
                result.append(leaf_illnesses[idx])
        return result

    def all_illnesses_helper(self, lst, cur_child):
        """
        :param lst: Contains all the illnesses kept on the tree's leafs.
        :param cur_child: The current child in each recursive call.
        """
        if cur_child.get_positive() is None \
                and cur_child.get_negative() is None:
            lst.append(cur_child.get_data())
            return
        temp = cur_child
        if cur_child.get_positive() is not None:
            cur_child = cur_child.get_positive()
            self.all_illnesses_helper(lst, cur_child)
        cur_child = temp
        if cur_child.get_negative() is not None:
            cur_child = cur_child.get_negative()
            self.all_illnesses_helper(lst, cur_child)

    def paths_to_illness(self, illness):
        """
        :param illness: A string with the name of the illness.
        :return: A list of lists. Each list represents a path to the illness.
        """
        all_paths = list()
        if self.root.get_positive() is None \
                and self.root.get_negative() is None:
            return all_paths
        cur_child = self.root
        path = list()
        self.paths_to_illness_helper(path, all_paths, cur_child, illness)
        return all_paths

    def paths_to_illness_helper(self, path, all_paths, cur_child, illness):
        """
        :param path: A list that contains a path to the illness.
        :param all_paths: A list that contains all the possible paths.
        :param cur_child: The current child in each recursive call.
        :param illness: A string with the name of the illness.
        """
        if cur_child.get_positive() is None \
                and cur_child.get_negative() is None:
            if cur_child.get_data() == illness:
                all_paths.append(path)
            return
        temp_child, temp_path = cur_child, path[:]
        if cur_child.get_positive() is not None:
            path.append(True)
            cur_child = cur_child.get_positive()
            self.paths_to_illness_helper(path, all_paths, cur_child, illness)
        cur_child, path = temp_child, temp_path
        if cur_child.get_negative() is not None:
            path.append(False)
            cur_child = cur_child.get_negative()
            self.paths_to_illness_helper(path, all_paths, cur_child, illness)


def build_tree(records, symptoms):
    """
    Builds a single tree according to the records and symptoms.
    :param records: A list of objects of type Record.
    :param symptoms: A list of strings that represent the symptoms.
    :return: The root of the tree that was built.
    """
    if len(symptoms) == 0:
        root = Node(None)
    else:
        root = build_symptoms_tree(symptoms)
        answered_symptoms = list()
        symptoms_path = list()
        get_symptoms_answers(root, answered_symptoms, symptoms_path)
        match_illnesses(records, answered_symptoms)
    return root


def build_symptoms_tree(symptoms):
    """
    Builds a tree according to the symptoms.
    :param symptoms: A list of strings that represent the symptoms.
    :return: An object of type Node that represents the tree's root.
    """
    if len(symptoms) == 1:
        empty_leaf1 = Node(None)
        empty_leaf2 = Node(None)
        return Node(symptoms[0], empty_leaf1, empty_leaf2)
    node = build_symptoms_tree(symptoms[1:])
    node_copy = copy.deepcopy(node)
    return Node(symptoms[0], node, node_copy)


def get_symptoms_answers(root, answered_symptoms, symptoms_path):
    """
    :param root: An object of type Node that represents the tree's root.
    :param answered_symptoms: A list of lists. Each list represents a path
                              and it's possible answers.
    :param symptoms_path: A list of tuples. Each tuple contains a child
                          and an answer - True or False.
    """
    if root.get_positive() is None and root.get_negative() is None:
        answered_symptoms.append(symptoms_path)
        return
    temp_root, temp_symptoms_path = root, symptoms_path[:]
    if root.get_positive() is not None:
        symptoms_path.append((root, "True"))
        root = root.get_positive()
        get_symptoms_answers(root, answered_symptoms, symptoms_path)
    root, symptoms_path = temp_root, temp_symptoms_path
    if root.get_negative() is not None:
        symptoms_path.append((root, "False"))
        root = root.get_negative()
        get_symptoms_answers(root, answered_symptoms, symptoms_path)


def match_illnesses(records, answered_symptoms):
    """
    Matches illnesses to the leafs.
    :param records: A list of objects of type Record.
    :param answered_symptoms: A list of lists. Each list represents a path
                              and it's possible answers.
    """
    for symptoms_path in answered_symptoms:
        possible_illnesses = list()
        for record in records:
            counter = 0
            for item in symptoms_path:
                if item[1] == "True":
                    if item[0].get_data() in record.get_symptoms():
                        counter += 1
                        pass
                    else:
                        break
                elif item[1] == "False":
                    if item[0].get_data() in record.get_symptoms():
                        break
                    else:
                        counter += 1
                        pass
            if counter == len(symptoms_path):
                possible_illnesses.append(record.get_illness())
        match_illness_to_leaf(symptoms_path, possible_illnesses)


def match_illness_to_leaf(symptoms_path, possible_illnesses):
    """
    :param symptoms_path: A list of tuples. Each tuple contains a child
                          and an answer - True or False.
    :param possible_illnesses: A list that contains all the possible illnesses.
    """
    if possible_illnesses == list():
        return
    else:
        possible_illnesses = sorted(possible_illnesses,
                                    key=possible_illnesses.count)
        leaf = Node(possible_illnesses[-1])
        if symptoms_path[-1][1] == "True":
            symptoms_path[-1][0].set_positive(leaf)
        elif symptoms_path[-1][1] == "False":
            symptoms_path[-1][0].set_negative(leaf)


def optimal_tree(records, symptoms, depth):
    """
    :param records: A list of objects of type Record.
    :param symptoms: A list of strings that represent the symptoms.
    :param depth: A non-negative int that represents the tree's depth.
    :return: An object of type Node that represents a tree's root
             with the highest success rate.
    """
    optimal_root = [None, 0]
    for sub_group in itertools.combinations(symptoms, depth):
        root = build_tree(records, sub_group)
        diagnoser = Diagnoser(root)
        success_rate = diagnoser.calculate_success_rate(records)
        if success_rate >= optimal_root[1]:
            optimal_root[0] = root
            optimal_root[1] = success_rate
    return optimal_root[0]
