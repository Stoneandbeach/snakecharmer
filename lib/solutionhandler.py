import random
import sys
import os
import numpy as np

import_template = """
from lib.template_solutions.{} import solution as reference_func
global reference_func
"""

references = {
    "1" : "template1_n_largest_numbers",
    "2" : "template2_clamp_values",
    "3" : "template3_snakespeare",
    "4" : "template4_normalization",
    "5" : "template5_bothon",
    "6" : "template6_find_mass",
    "7" : "template7_count_instances"
}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class SolutionHandler:
    def __init__(self, id, use_numpy=False, **kwargs):
        setup, self.get_args, self.check, self.post_process = {
            "1" : (self.setup_n_largest, self.get_generic, self.check_n_largest, self.post_generic),
            "2" : (self.setup_clamp, self.get_clamp, self.check_clamp, self.post_generic),
            "3" : (self.setup_snakespeare, self.get_generic, self.check_snakespeare, self.post_snakespeare),
            "4" : (self.setup_normalization, self.get_generic, self.check_normalization, self.post_generic),
            "5" : (self.setup_bothon, self.get_generic, self.check_bothon, self.post_generic),
            "6" : (self.setup_mass, self.get_generic, self.check_mass, self.post_generic),
            "7" : (self.setup_count, self.get_count, self.check_count, self.post_generic),
            "999" : (self.setup_dummy, self.get_generic, self.check_dummy, self.post_dummy)
        }[id]
        self.id = id
        self.use_numpy = use_numpy
        self.args = setup(**kwargs)
        self.shuffle_func = {
            False : random.shuffle,
            True : np.random.shuffle
        }[use_numpy]
        if use_numpy:
            print(f"{bcolors.WARNING}Found numpy import. Assuming you want the input data as a numpy.ndarray. \
To prevent this, add '--skip-numpy' when you run this script.{bcolors.ENDC}")
    
    
    # General methods
    def get_generic(self, **kwargs):
        if self.shuffle:
            self.shuffle_func(self.args[0])
        return tuple(arg.copy() if hasattr(arg, 'copy') else arg for arg in self.args)
    
    def post_generic(self, results):
        return None
    
    def get_reference(self):
        template = import_template.format(references[self.id])
        # Execute import to access reference function
        try:
            exec(template)
        except ImportError as e:
            sys.exit(f"Could not import reference function. Broken import: '{template}'. Error: {e}")
        
        # Temporarily disable shuffling and get reference results
        _shuffle = self.shuffle
        self.shuffle = False
        reference_result = reference_func(*self.get_args())
        self.shuffle = _shuffle
        return reference_result
    
    def conclude(self, match, message):
        if match:
            return True, "".join([bcolors.OKGREEN, "Results evaluate correctly!", bcolors.ENDC]), message
        else:
            return False, "".join([bcolors.FAIL, "Results do not match the expected!", bcolors.ENDC]), message
        
        
    # 1 - N largest numbers
    def setup_n_largest(self, length=10000, n=50):
        self.shuffle = True
        if self.use_numpy:
            lst = np.arange(length)
        else:
            lst = list(range(length))
        return (lst, n)
    
    def check_n_largest(self, result):
        reference_result = self.get_reference()
        match = True
        for a, b in zip(result, reference_result):
            if a != b:
                match = False
                break
        if len(result) != len(reference_result):
            match = False
        message = f"Your result: {result}\nExpected result: {reference_result}"
        return self.conclude(match, message)
            
        
    # 2 - Clamp values
    def setup_clamp(self, size=200):
        self.shuffle = False
        if self.use_numpy:
            matrix = np.random.randint(low=-200, high=500, size=(size, size))
        else:
            matrix = [[random.randint(-200, 500) for _ in range(size)] for _ in range(size)]
        return (matrix,)
    
    def get_clamp(self, **kwargs):
        if self.use_numpy:
            return (self.args[0].copy(),)
        else:
            _matrix = self.args[0]
            return ([row.copy() for row in _matrix],)
        
    def check_clamp(self, results):
        reference_result = self.get_reference()
        result_sum = sum([sum(row) for row in results])
        reference_sum = sum([sum(row) for row in reference_result])
        match = result_sum == reference_sum
        if match:
            message = ""
        else:
            message = f"The sum of your matrix ({result_sum}) does not match the reference value ({reference_sum}).\n"
        
        contains = False
        if self.use_numpy:
            contains = (results > 255).any() or (results < 0).any()
        else:
            class ClampChecker:
                def __init__(self, lower, upper):
                    self.upper = upper
                    self.lower = lower
                def __eq__(self, value):
                    return (value > self.upper) or (value < self.lower)
            clamp_checker = ClampChecker(0, 255)
            for row in results:
                if row.count(clamp_checker):
                    contains = True
                    break
        if contains:
            C_TEXT = bcolors.FAIL
        else:
            C_TEXT = bcolors.OKGREEN
        string = "{}Matrix does {}contain numbers < 0 or > 255.{}".format(
            C_TEXT,
            {True : "still ", False : "not "}[contains],
            bcolors.ENDC
        )
        
        return self.conclude(match, message + string)
    
    
    # 3 - Snakespeare
    def setup_snakespeare(self):
        self.shuffle = False
        with open("./data/sonnets.txt", "r") as fp:
            sonnets = fp.read()
        if self.use_numpy:
            sonnets = np.array(sonnets)
        return (sonnets,)

    def check_snakespeare(self, result):
        reference_result = self.get_reference()
        match = True
        message = ""
        for key in reference_result.keys():
            if not key in result.keys():
                match = False
                message += f"Missing key: word pair {key}\n"
            elif not len(result[key]) == len(reference_result[key]):
                match = False
                for word in result[key]:
                    if word not in reference_result[key]:
                        message += f"List of words following word pair {key} is missing word {word}.\n"
        return self.conclude(match, message)

    def post_snakespeare(self, word_dict):
        w1, w2 = random.choice([word_pair for word_pair in list(word_dict.keys()) if word_pair[0][0].isupper()])
        num_words = 2
        words = [w1, w2]
        while num_words < 10 or w2[-1] != ".":
            try:
                if (w1, w2) in word_dict.keys():
                    w1, w2 = w2, random.choice(word_dict[(w1, w2)])
                else:
                    w1, w2 = random.choice(list(word_dict.keys()))
            except IndexError as e:
                print()
                print()
                print(f"Error! {e}")
                print(w1, w2, word_dict[(w1, w2)])
                break
            words.append(w2)
            num_words += 1
        return "\n".join(["Snakespeare writes:", " ".join(words)])
    
    
    # 4 - Normalization
    def setup_normalization(self, length=10000):
        self.shuffle = True
        if self.use_numpy:
            lst = np.arange(length)
        else:
            lst = list(range(length))
        return(lst,)

    def check_normalization(self, result):
        reference_result = self.get_reference()
        match = True
        for a, b in zip(result, reference_result):
            if a != b:
                match = False
                break
        if len(result) != len(reference_result):
            match = False
            
        message = f"Sum of your result: {sum(result)}\nExpected sum: {sum(reference_result)}"
        return self.conclude(match, message)
    
    
    # 5 - Bothon
    def setup_bothon(self, E_split=12, E_mass=3, stop_threshold=60):
        self.shuffle = False
        if self.use_numpy:
            initial_state = np.array([8])
        else:
            initial_state = [8]
        return (initial_state, E_split, E_mass, stop_threshold)
    
    def check_bothon(self, result):
        reference_result = self.get_reference()
        match = result == reference_result
        message = f"Number of bothons; your result: {result}\nExpected result: {reference_result}"
        return self.conclude(match, message)
    
    
    #6 - Find mass
    def setup_mass(self):
        self.shuffle = False
        return (os.sep.join(["data", "collision_data.csv"]),)
    
    def check_mass(self, result):
        reference_result = self.get_reference()
        match = result[0] == reference_result[0] and result[1] == reference_result[1]
        message = f"your results; mass: {result[0]}, standard deviation: {result[1]}\nExpected result; mass: {reference_result[0]}, standard deviation: {reference_result[1]}"
        return self.conclude(match, message)
    
    
    #7 - Count instances
    def setup_count(self, length=100000, number=1):
        self.shuffle = False
        self.arg_count = 0
        lists = [[random.randint(-5, 5) for _ in range(length)] for _ in range(5)]
        return (lists, number)
    
    def get_count(self, check=False, **kwargs):
        lst = self.args[0][self.arg_count]
        if not check:
            self.arg_count = (self.arg_count + 1) % len(self.args[0])
        if self.use_numpy:
            lst = np.array(lst)
        return (lst, self.args[1])
    
    def check_count(self, result):
        reference_result = self.get_reference()
        match = result == reference_result
        message = f"your results: {result} counts\nExpected result: {reference_result} counts"
        return self.conclude(match, message)
    
    
    # 999 - Dummy exercise
    def setup_dummy(self):
        self.shuffle = True
        if self.use_numpy:
            lst = np.arange(10000)
        else:
            lst = list(range(10000))
        n = 100
        return (lst, n)
    
    def check_dummy(self, results):
        pass
    
    def post_dummy(self, results):
        pass


class TestRunHandler(SolutionHandler):
    # General methods
    def post_generic(self, results):
        return f"Your results:\n{results}"
    
    
    # 1 N largest numbers
    def setup_n_largest(self):
        return super().setup_n_largest(length=10, n=3)
    
    
    # 2 - Clamp values
    def setup_clamp(self):
        return super().setup_clamp(size=4)
    
    
    # 3 - Snakespeare
    def setup_snakespeare(self):
        self.shuffle = False
        sample = 'This text is an example text. This text will hopefully help. For an example is an aid.'
        if self.use_numpy:
            return (np.array(sample),)
        else:
            return (sample,)
    
    def post_snakespeare(self, word_dict):
        print("Word dictionary:")
        for key in word_dict:
            print(key, word_dict[key])
        print()
        return super().post_snakespeare(word_dict)
    
    
    # 4 - Normalization
    def setup_normalization(self):
        return super().setup_normalization(length=10)
    
    
    # 5 - Bothon
    def setup_bothon(self):
        return super().setup_bothon(stop_threshold = 10)
    
    
    # 6 - Find mass
    def setup_bothon(self):
        self.shuffle = False
        return (os.sep.join(["data", "collision_data_test.csv"]),)
    
    
    #7 - Count instances
    def setup_count(self, length=100, number=1):
        return super().setup_count(length, number)
    
    def get_count(self):
        return (self.args[0][0], self.args[1])